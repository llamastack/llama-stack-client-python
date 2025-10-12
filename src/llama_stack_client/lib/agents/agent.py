# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import json
import logging
from dataclasses import dataclass
from typing import Any, AsyncIterator, Callable, Dict, Iterator, List, Optional, Tuple, Union, TypedDict

from llama_stack_client import LlamaStackClient
from llama_stack_client.types import ResponseObject
from llama_stack_client.types import response_create_params
from llama_stack_client.types.alpha.tool_response import ToolResponse
from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types.shared.agent_config import Toolgroup
from llama_stack_client.types.shared_params.document import Document
from llama_stack_client.types.shared.completion_message import CompletionMessage

from ..._types import Headers
from .client_tool import ClientTool, client_tool
from .tool_parser import ToolParser
from .stream_events import (
    AgentResponseCompleted,
    AgentResponseFailed,
    AgentStreamEvent,
    AgentToolCallCompleted,
    AgentToolCallDelta,
    AgentToolCallIssued,
    iter_agent_events,
)


class ToolResponsePayload(TypedDict):
    call_id: str
    tool_name: str
    content: Any


logger = logging.getLogger(__name__)


@dataclass
class AgentStreamChunk:
    event: AgentStreamEvent
    response: Optional[ResponseObject]


class AgentUtils:
    @staticmethod
    def get_client_tools(
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]],
    ) -> List[ClientTool]:
        if not tools:
            return []

        # Wrap any function in client_tool decorator
        tools = [client_tool(tool) if (callable(tool) and not isinstance(tool, ClientTool)) else tool for tool in tools]
        return [tool for tool in tools if isinstance(tool, ClientTool)]

    @staticmethod
    def get_tool_calls(chunk: AgentStreamChunk, tool_parser: Optional[ToolParser] = None) -> List[ToolCall]:
        if not isinstance(chunk.event, AgentToolCallIssued):
            return []

        tool_call = ToolCall(
            call_id=chunk.event.call_id,
            tool_name=chunk.event.name,
            arguments=chunk.event.arguments_json,
        )

        if tool_parser:
            completion = CompletionMessage(
                role="assistant",
                content="",
                tool_calls=[tool_call],
                stop_reason="end_of_turn",
            )
            return tool_parser.get_tool_calls(completion)

        return [tool_call]

    @staticmethod
    def get_turn_id(chunk: AgentStreamChunk) -> Optional[str]:
        return chunk.response.turn.turn_id if chunk.response else None

    @staticmethod
    def normalize_tools(
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]],
    ) -> Tuple[List[Union[Toolgroup, str, Dict[str, Any]]], List[ClientTool]]:
        if not tools:
            return [], []

        normalized: List[Union[Toolgroup, ClientTool, Callable[..., Any], str, Dict[str, Any]]] = [
            client_tool(tool) if (callable(tool) and not isinstance(tool, ClientTool)) else tool for tool in tools
        ]
        client_tool_instances = [tool for tool in normalized if isinstance(tool, ClientTool)]

        toolgroups: List[Union[Toolgroup, str, Dict[str, Any]]] = []
        for tool in normalized:
            if isinstance(tool, ClientTool):
                continue
            if isinstance(tool, (str, dict, Toolgroup)):
                toolgroups.append(tool)
                continue
            raise TypeError(f"Unsupported tool type: {type(tool)!r}")

        return toolgroups, client_tool_instances


class Agent:
    def __init__(
        self,
        client: LlamaStackClient,
        *,
        model: str,
        instructions: str,
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]] = None,
        tool_parser: Optional[ToolParser] = None,
        extra_headers: Headers | None = None,
    ):
        """Construct an Agent backed by the responses + conversations APIs."""
        self.client = client
        self.tool_parser = tool_parser
        self.extra_headers = extra_headers
        self._model = model
        self._instructions = instructions

        toolgroups, client_tools = AgentUtils.normalize_tools(tools)
        self._toolgroups: List[Union[Toolgroup, str, Dict[str, Any]]] = toolgroups
        self.client_tools = {tool.get_name(): tool for tool in client_tools}

        self.sessions: List[str] = []
        self.builtin_tools: Dict[str, Dict[str, Any]] = {}
        self._last_response_id: Optional[str] = None
        self._session_last_response_id: Dict[str, Optional[str]] = {}

    def initialize(self) -> None:
        # Ensure builtin tools cache is ready
        if not self.builtin_tools and self._toolgroups:
            for tg in self._toolgroups:
                toolgroup_id = tg if isinstance(tg, str) else tg.name
                args = {} if isinstance(tg, str) else tg.args
                for tool in self.client.tools.list(toolgroup_id=toolgroup_id, extra_headers=self.extra_headers):
                    self.builtin_tools[tool.name] = args

    def create_session(self, session_name: str) -> str:
        conversation = self.client.conversations.create(
            extra_headers=self.extra_headers,
            metadata={"name": session_name},
        )
        self.sessions.append(conversation.id)
        self._session_last_response_id[conversation.id] = None
        return conversation.id

    @staticmethod
    def _coerce_tool_content(content: Any) -> str:
        if isinstance(content, str):
            return content
        if content is None:
            return ""
        if isinstance(content, (dict, list)):
            try:
                return json.dumps(content)
            except TypeError:
                return str(content)
        return str(content)

    @staticmethod
    def _parse_tool_arguments(arguments: Any) -> Dict[str, Any]:
        if isinstance(arguments, dict):
            return arguments
        if not arguments:
            return {}
        if isinstance(arguments, str):
            try:
                parsed = json.loads(arguments)
            except json.JSONDecodeError:
                logger.warning("Failed to decode tool arguments JSON", exc_info=True)
                return {}
            if isinstance(parsed, dict):
                return parsed
            logger.warning("Tool arguments JSON did not decode into a dict: %s", type(parsed))
            return {}
        logger.warning("Unsupported tool arguments type: %s", type(arguments))
        return {}

    @staticmethod
    def _normalize_tool_response(tool_response: Any) -> ToolResponsePayload:
        if isinstance(tool_response, ToolResponse):
            payload: ToolResponsePayload = {
                "call_id": tool_response.call_id,
                "tool_name": str(tool_response.tool_name),
                "content": Agent._coerce_tool_content(tool_response.content),
            }
            return payload

        if isinstance(tool_response, dict):
            call_id = tool_response.get("call_id")
            tool_name = tool_response.get("tool_name")
            if call_id is None or tool_name is None:
                raise KeyError("Tool response missing required keys 'call_id' or 'tool_name'")
            payload: ToolResponsePayload = {
                "call_id": str(call_id),
                "tool_name": str(tool_name),
                "content": Agent._coerce_tool_content(tool_response.get("content")),
            }
            return payload

        raise TypeError(f"Unsupported tool response type: {type(tool_response)!r}")

    def _run_tool_calls(self, tool_calls: List[ToolCall]) -> List[ToolResponsePayload]:
        responses: List[ToolResponsePayload] = []
        for tool_call in tool_calls:
            raw_result = self._run_single_tool(tool_call)
            responses.append(self._normalize_tool_response(raw_result))
        return responses

    def _run_single_tool(self, tool_call: ToolCall) -> Any:
        # custom client tools
        if tool_call.tool_name in self.client_tools:
            tool = self.client_tools[tool_call.tool_name]
            result_message = tool.run(
                [
                    CompletionMessage(
                        role="assistant",
                        content=tool_call.arguments,
                        tool_calls=[tool_call],
                        stop_reason="end_of_turn",
                    )
                ]
            )
            return result_message

        # builtin tools executed by tool_runtime
        if tool_call.tool_name in self.builtin_tools:
            tool_args = self._parse_tool_arguments(tool_call.arguments)
            tool_result = self.client.tool_runtime.invoke_tool(
                tool_name=tool_call.tool_name,
                kwargs={
                    **tool_args,
                    **self.builtin_tools[tool_call.tool_name],
                },
                extra_headers=self.extra_headers,
            )
            return {
                "call_id": tool_call.call_id,
                "tool_name": tool_call.tool_name,
                "content": self._coerce_tool_content(tool_result.content),
            }

        # cannot find tools
        return {
            "call_id": tool_call.call_id,
            "tool_name": tool_call.tool_name,
            "content": f"Unknown tool `{tool_call.tool_name}` was called.",
        }

    def create_turn(
        self,
        messages: List[response_create_params.InputUnionMember1],
        session_id: str,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
        # TODO: deprecate this
        extra_headers: Headers | None = None,
    ) -> Iterator[AgentStreamChunk] | ResponseObject:
        if stream:
            return self._create_turn_streaming(
                messages, session_id, toolgroups, documents, extra_headers=extra_headers or self.extra_headers
            )
        else:
            _ = toolgroups
            _ = documents
            last_chunk: Optional[AgentStreamChunk] = None
            for chunk in self._create_turn_streaming(
                messages,
                session_id,
                toolgroups,
                documents,
                extra_headers=extra_headers or self.extra_headers,
            ):
                last_chunk = chunk

            if not last_chunk or not last_chunk.response:
                raise Exception("Turn did not complete")

            return last_chunk.response

    def _create_turn_streaming(
        self,
        messages: List[response_create_params.InputUnionMember1],
        session_id: str,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        # TODO: deprecate this
        extra_headers: Headers | None = None,
    ) -> Iterator[AgentStreamChunk]:
        _ = toolgroups
        _ = documents
        self.initialize()
        conversation_id = session_id
        self._session_last_response_id.setdefault(conversation_id, None)

        request_headers = extra_headers or self.extra_headers
        stream = self.client.responses.create(
            model=self._model,
            instructions=self._instructions,
            conversation=conversation_id,
            input=messages,
            stream=True,
            previous_response_id=self._session_last_response_id.get(conversation_id),
            extra_headers=request_headers,
        )

        last_response: Optional[ResponseObject] = None
        pending_tools: Dict[str, Dict[str, Any]] = {}

        while True:
            restart_stream = False
            for event in iter_agent_events(stream):
                if isinstance(event, AgentResponseCompleted):
                    last_response = self.client.responses.retrieve(
                        event.response_id,
                        extra_headers=request_headers,
                    )
                    self._last_response_id = event.response_id
                    self._session_last_response_id[conversation_id] = event.response_id
                    yield AgentStreamChunk(event=event, response=last_response)
                    continue

                if isinstance(event, AgentResponseFailed):
                    raise RuntimeError(event.error_message)

                if isinstance(event, AgentToolCallIssued):
                    tool_call = ToolCall(
                        call_id=event.call_id,
                        tool_name=event.name,
                        arguments=event.arguments_json,
                    )
                    pending_tools[event.call_id] = {
                        "tool_call": tool_call,
                        "response_id": event.response_id,
                        "arguments": event.arguments_json or "",
                    }
                    yield AgentStreamChunk(event=event, response=None)
                    continue

                if isinstance(event, AgentToolCallDelta):
                    builder = pending_tools.get(event.call_id)
                    if builder and event.arguments_delta:
                        builder["arguments"] = builder.get("arguments", "") + event.arguments_delta
                        builder["tool_call"].arguments = builder["arguments"]
                    yield AgentStreamChunk(event=event, response=None)
                    continue

                if isinstance(event, AgentToolCallCompleted):
                    builder = pending_tools.get(event.call_id)
                    if builder:
                        arguments = event.arguments_json or builder.get("arguments") or ""
                        builder["tool_call"].arguments = arguments
                        tool_responses = self._run_tool_calls([builder["tool_call"]])
                        followup_messages: List[response_create_params.InputUnionMember1] = [
                            response_create_params.InputUnionMember1OpenAIResponseInputFunctionToolCallOutput(
                                type="function_call_output",
                                call_id=payload["call_id"],
                                output=payload["content"],
                            )
                            for payload in tool_responses
                        ]
                        stream = self.client.responses.create(
                            model=self._model,
                            instructions=self._instructions,
                            conversation=conversation_id,
                            input=followup_messages,
                            stream=True,
                            previous_response_id=builder.get("response_id", event.response_id),
                            extra_headers=request_headers,
                        )
                        pending_tools.pop(event.call_id, None)
                        restart_stream = True
                        yield AgentStreamChunk(event=event, response=None)
                        if restart_stream:
                            break
                        continue

                yield AgentStreamChunk(event=event, response=None)

            if not restart_stream:
                break


class AsyncAgent:
    def __init__(
        self,
        client: LlamaStackClient,
        *,
        model: str,
        instructions: str,
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]] = None,
        tool_parser: Optional[ToolParser] = None,
        extra_headers: Headers | None = None,
    ):
        """Construct an async Agent backed by the responses + conversations APIs."""
        self.client = client

        if isinstance(client, LlamaStackClient):
            raise ValueError("AsyncAgent must be initialized with an AsyncLlamaStackClient")

        self.tool_parser = tool_parser
        self.extra_headers = extra_headers
        self._model = model
        self._instructions = instructions

        toolgroups, client_tools = AgentUtils.normalize_tools(tools)
        self._toolgroups: List[Union[Toolgroup, str, Dict[str, Any]]] = toolgroups
        self.client_tools = {tool.get_name(): tool for tool in client_tools}

        self.sessions: List[str] = []
        self.builtin_tools: Dict[str, Dict[str, Any]] = {}
        self._last_response_id: Optional[str] = None
        self._session_last_response_id: Dict[str, Optional[str]] = {}

    async def initialize(self) -> None:
        if not self.builtin_tools and self._toolgroups:
            for tg in self._toolgroups:
                toolgroup_id = tg if isinstance(tg, str) else tg.name
                args = {} if isinstance(tg, str) else tg.args
                tools = await self.client.tools.list(toolgroup_id=toolgroup_id, extra_headers=self.extra_headers)
                for tool in tools:
                    self.builtin_tools[tool.name] = args

    async def create_session(self, session_name: str) -> str:
        await self.initialize()
        conversation = await self.client.conversations.create(  # type: ignore[union-attr]
            extra_headers=self.extra_headers,
            metadata={"name": session_name},
        )
        self.sessions.append(conversation.id)
        self._session_last_response_id[conversation.id] = None
        return conversation.id

    async def create_turn(
        self,
        messages: List[response_create_params.InputUnionMember1],
        session_id: str,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
    ) -> AsyncIterator[AgentStreamChunk] | ResponseObject:
        if stream:
            return self._create_turn_streaming(messages, session_id, toolgroups, documents)
        else:
            _ = toolgroups
            _ = documents
            last_chunk: Optional[AgentStreamChunk] = None
            async for chunk in self._create_turn_streaming(messages, session_id, toolgroups, documents):
                last_chunk = chunk
            if not last_chunk or not last_chunk.response:
                raise Exception("Turn did not complete")
            return last_chunk.response

    async def _run_tool_calls(self, tool_calls: List[ToolCall]) -> List[ToolResponsePayload]:
        responses: List[ToolResponsePayload] = []
        for tool_call in tool_calls:
            raw_result = await self._run_single_tool(tool_call)
            responses.append(Agent._normalize_tool_response(raw_result))
        return responses

    async def _run_single_tool(self, tool_call: ToolCall) -> Any:
        # custom client tools
        if tool_call.tool_name in self.client_tools:
            tool = self.client_tools[tool_call.tool_name]
            result_message = await tool.async_run(
                [
                    CompletionMessage(
                        role="assistant",
                        content=tool_call.arguments,
                        tool_calls=[tool_call],
                        stop_reason="end_of_turn",
                    )
                ]
            )
            return result_message

        # builtin tools executed by tool_runtime
        if tool_call.tool_name in self.builtin_tools:
            tool_args = Agent._parse_tool_arguments(tool_call.arguments)
            tool_result = await self.client.tool_runtime.invoke_tool(
                tool_name=tool_call.tool_name,
                kwargs={
                    **tool_args,
                    **self.builtin_tools[tool_call.tool_name],
                },
                extra_headers=self.extra_headers,
            )
            return {
                "call_id": tool_call.call_id,
                "tool_name": tool_call.tool_name,
                "content": Agent._coerce_tool_content(tool_result.content),
            }

        # cannot find tools
        return {
            "call_id": tool_call.call_id,
            "tool_name": tool_call.tool_name,
            "content": f"Unknown tool `{tool_call.tool_name}` was called.",
        }

    async def _create_turn_streaming(
        self,
        messages: List[response_create_params.InputUnionMember1],
        session_id: str,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
    ) -> AsyncIterator[AgentStreamChunk]:
        _ = toolgroups
        _ = documents
        await self.initialize()
        conversation_id = session_id
        self._session_last_response_id.setdefault(conversation_id, None)

        request_headers = self.extra_headers
        stream = await self.client.responses.create(
            model=self._model,
            instructions=self._instructions,
            conversation=conversation_id,
            input=messages,
            stream=True,
            previous_response_id=self._session_last_response_id.get(conversation_id),
            extra_headers=request_headers,
        )

        last_response: Optional[ResponseObject] = None
        pending_tools: Dict[str, Dict[str, Any]] = {}

        while True:
            restart_stream = False
            async for event in iter_agent_events(stream):
                if isinstance(event, AgentResponseCompleted):
                    last_response = await self.client.responses.retrieve(
                        event.response_id,
                        extra_headers=request_headers,
                    )
                    self._last_response_id = event.response_id
                    self._session_last_response_id[conversation_id] = event.response_id
                    yield AgentStreamChunk(event=event, response=last_response)
                    continue

                if isinstance(event, AgentResponseFailed):
                    raise RuntimeError(event.error_message)

                if isinstance(event, AgentToolCallIssued):
                    tool_call = ToolCall(
                        call_id=event.call_id,
                        tool_name=event.name,
                        arguments=event.arguments_json,
                    )
                    pending_tools[event.call_id] = {
                        "tool_call": tool_call,
                        "response_id": event.response_id,
                        "arguments": event.arguments_json or "",
                    }
                    yield AgentStreamChunk(event=event, response=None)
                    continue

                if isinstance(event, AgentToolCallDelta):
                    builder = pending_tools.get(event.call_id)
                    if builder and event.arguments_delta:
                        builder["arguments"] = builder.get("arguments", "") + event.arguments_delta
                        builder["tool_call"].arguments = builder["arguments"]
                    yield AgentStreamChunk(event=event, response=None)
                    continue

                if isinstance(event, AgentToolCallCompleted):
                    builder = pending_tools.get(event.call_id)
                    if builder:
                        arguments = event.arguments_json or builder.get("arguments") or ""
                        builder["tool_call"].arguments = arguments
                        tool_responses = await self._run_tool_calls([builder["tool_call"]])
                        followup_messages: List[response_create_params.InputUnionMember1] = [
                            response_create_params.InputUnionMember1OpenAIResponseInputFunctionToolCallOutput(
                                type="function_call_output",
                                call_id=payload["call_id"],
                                output=payload["content"],
                            )
                            for payload in tool_responses
                        ]
                        stream = await self.client.responses.create(
                            model=self._model,
                            instructions=self._instructions,
                            conversation=conversation_id,
                            input=followup_messages,
                            stream=True,
                            previous_response_id=builder.get("response_id", event.response_id),
                            extra_headers=request_headers,
                        )
                        pending_tools.pop(event.call_id, None)
                        restart_stream = True
                        yield AgentStreamChunk(event=event, response=None)
                        if restart_stream:
                            break
                        continue

                yield AgentStreamChunk(event=event, response=None)

            if not restart_stream:
                break
