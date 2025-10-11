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
from llama_stack_client.types import AgentConfig, ResponseObject
from llama_stack_client.types import response_create_params
from llama_stack_client.types.alpha.tool_response import ToolResponse
from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types.shared.agent_config import ToolConfig, Toolgroup
from llama_stack_client.types.shared_params.document import Document
from llama_stack_client.types.shared.completion_message import CompletionMessage
from llama_stack_client.types.shared.response_format import ResponseFormat
from llama_stack_client.types.shared.sampling_params import SamplingParams

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

DEFAULT_MAX_ITER = 10


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
    def get_agent_config(
        model: Optional[str] = None,
        instructions: Optional[str] = None,
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]] = None,
        tool_config: Optional[ToolConfig] = None,
        sampling_params: Optional[SamplingParams] = None,
        max_infer_iters: Optional[int] = None,
        input_shields: Optional[List[str]] = None,
        output_shields: Optional[List[str]] = None,
        response_format: Optional[ResponseFormat] = None,
        enable_session_persistence: Optional[bool] = None,
        name: str | None = None,
    ) -> AgentConfig:
        # Create a minimal valid AgentConfig with required fields
        if model is None or instructions is None:
            raise ValueError("Both 'model' and 'instructions' are required when agent_config is not provided")

        agent_config = {
            "model": model,
            "instructions": instructions,
            "toolgroups": [],
            "client_tools": [],
        }

        # Add optional parameters if provided
        if enable_session_persistence is not None:
            agent_config["enable_session_persistence"] = enable_session_persistence
        if max_infer_iters is not None:
            agent_config["max_infer_iters"] = max_infer_iters
        if input_shields is not None:
            agent_config["input_shields"] = input_shields
        if output_shields is not None:
            agent_config["output_shields"] = output_shields
        if response_format is not None:
            agent_config["response_format"] = response_format
        if sampling_params is not None:
            agent_config["sampling_params"] = sampling_params
        if tool_config is not None:
            agent_config["tool_config"] = tool_config
        if name is not None:
            agent_config["name"] = name
        if tools is not None:
            toolgroups: List[Toolgroup] = []
            for tool in tools:
                if isinstance(tool, str) or isinstance(tool, dict):
                    toolgroups.append(tool)

            agent_config["toolgroups"] = toolgroups
            agent_config["client_tools"] = [tool.get_tool_definition() for tool in AgentUtils.get_client_tools(tools)]

        agent_config = AgentConfig(**agent_config)
        return agent_config


class Agent:
    def __init__(
        self,
        client: LlamaStackClient,
        # begin deprecated
        agent_config: Optional[AgentConfig] = None,
        client_tools: Tuple[ClientTool, ...] = (),
        # end deprecated
        tool_parser: Optional[ToolParser] = None,
        model: Optional[str] = None,
        instructions: Optional[str] = None,
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]] = None,
        tool_config: Optional[ToolConfig] = None,
        sampling_params: Optional[SamplingParams] = None,
        max_infer_iters: Optional[int] = None,
        input_shields: Optional[List[str]] = None,
        output_shields: Optional[List[str]] = None,
        response_format: Optional[ResponseFormat] = None,
        enable_session_persistence: Optional[bool] = None,
        extra_headers: Headers | None = None,
        name: str | None = None,
    ):
        """Construct an Agent with the given parameters.

        :param client: The LlamaStackClient instance.
        :param agent_config: The AgentConfig instance.
            ::deprecated: use other parameters instead
        :param client_tools: A tuple of ClientTool instances.
            ::deprecated: use tools instead
        :param tool_parser: Custom logic that parses tool calls from a message.
        :param model: The model to use for the agent.
        :param instructions: The instructions for the agent.
        :param tools: A list of tools for the agent. Values can be one of the following:
            - dict representing a toolgroup/tool with arguments: e.g. {"name": "builtin::rag/knowledge_search", "args": {"vector_db_ids": [123]}}
            - a python function with a docstring. See @client_tool for more details.
            - str representing a tool within a toolgroup: e.g. "builtin::rag/knowledge_search"
            - str representing a toolgroup_id: e.g. "builtin::rag", "builtin::code_interpreter", where all tools in the toolgroup will be added to the agent
            - an instance of ClientTool: A client tool object.
        :param tool_config: The tool configuration for the agent.
        :param sampling_params: The sampling parameters for the agent.
        :param max_infer_iters: The maximum number of inference iterations.
        :param input_shields: The input shields for the agent.
        :param output_shields: The output shields for the agent.
        :param response_format: The response format for the agent.
        :param enable_session_persistence: Whether to enable session persistence.
        :param extra_headers: Extra headers to add to all requests sent by the agent.
        :param name: Optional name for the agent, used in telemetry and identification.
        """
        self.client = client

        if agent_config is not None:
            logger.warning("`agent_config` is deprecated. Use inlined parameters instead.")
        if client_tools != ():
            logger.warning("`client_tools` is deprecated. Use `tools` instead.")

        # Construct agent_config from parameters if not provided
        if agent_config is None:
            agent_config = AgentUtils.get_agent_config(
                model=model,
                instructions=instructions,
                tools=tools,
                tool_config=tool_config,
                sampling_params=sampling_params,
                max_infer_iters=max_infer_iters,
                input_shields=input_shields,
                output_shields=output_shields,
                response_format=response_format,
                enable_session_persistence=enable_session_persistence,
                name=name,
            )
            client_tools = AgentUtils.get_client_tools(tools)

        self.agent_config = agent_config
        self.client_tools = {t.get_name(): t for t in client_tools}
        self.sessions: List[str] = []
        self.tool_parser = tool_parser
        self.builtin_tools = {}
        self.extra_headers = extra_headers
        self._conversation_id: Optional[str] = None
        self._last_response_id: Optional[str] = None
        self._model = self.agent_config.model
        self._instructions = self.agent_config.instructions

    def initialize(self) -> None:
        # Ensure builtin tools cache is ready
        if not self.builtin_tools and self.agent_config.toolgroups:
            for tg in self.agent_config.toolgroups:
                toolgroup_id = tg if isinstance(tg, str) else tg.name
                args = {} if isinstance(tg, str) else tg.args
                for tool in self.client.tools.list(toolgroup_id=toolgroup_id, extra_headers=self.extra_headers):
                    self.builtin_tools[tool.name] = args

    def create_session(self, session_name: str) -> str:
        conversation = self.client.conversations.create(
            extra_headers=self.extra_headers,
            metadata={"name": session_name},
        )
        self._conversation_id = conversation.id
        self.sessions.append(conversation.id)
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
        session_id: Optional[str] = None,
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
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        # TODO: deprecate this
        extra_headers: Headers | None = None,
    ) -> Iterator[AgentStreamChunk]:
        _ = toolgroups
        _ = documents
        self.initialize()
        conversation_id = session_id or self._conversation_id
        if not conversation_id:
            conversation_id = self.create_session(session_name="default")

        request_headers = extra_headers or self.extra_headers
        stream = self.client.responses.create(
            model=self._model,
            instructions=self._instructions,
            conversation=conversation_id,
            input=messages,
            stream=True,
            previous_response_id=self._last_response_id,
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
                            previous_response_id=event.response_id,
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
        # begin deprecated
        agent_config: Optional[AgentConfig] = None,
        client_tools: Tuple[ClientTool, ...] = (),
        # end deprecated
        tool_parser: Optional[ToolParser] = None,
        model: Optional[str] = None,
        instructions: Optional[str] = None,
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]] = None,
        tool_config: Optional[ToolConfig] = None,
        sampling_params: Optional[SamplingParams] = None,
        max_infer_iters: Optional[int] = None,
        input_shields: Optional[List[str]] = None,
        output_shields: Optional[List[str]] = None,
        response_format: Optional[ResponseFormat] = None,
        enable_session_persistence: Optional[bool] = None,
        extra_headers: Headers | None = None,
        name: str | None = None,
    ):
        """Construct an Agent with the given parameters.

        :param client: The LlamaStackClient instance.
        :param agent_config: The AgentConfig instance.
            ::deprecated: use other parameters instead
        :param client_tools: A tuple of ClientTool instances.
            ::deprecated: use tools instead
        :param tool_parser: Custom logic that parses tool calls from a message.
        :param model: The model to use for the agent.
        :param instructions: The instructions for the agent.
        :param tools: A list of tools for the agent. Values can be one of the following:
            - dict representing a toolgroup/tool with arguments: e.g. {"name": "builtin::rag/knowledge_search", "args": {"vector_db_ids": [123]}}
            - a python function with a docstring. See @client_tool for more details.
            - str representing a tool within a toolgroup: e.g. "builtin::rag/knowledge_search"
            - str representing a toolgroup_id: e.g. "builtin::rag", "builtin::code_interpreter", where all tools in the toolgroup will be added to the agent
            - an instance of ClientTool: A client tool object.
        :param tool_config: The tool configuration for the agent.
        :param sampling_params: The sampling parameters for the agent.
        :param max_infer_iters: The maximum number of inference iterations.
        :param input_shields: The input shields for the agent.
        :param output_shields: The output shields for the agent.
        :param response_format: The response format for the agent.
        :param enable_session_persistence: Whether to enable session persistence.
        :param extra_headers: Extra headers to add to all requests sent by the agent.
        :param name: Optional name for the agent, used in telemetry and identification.
        """
        self.client = client

        if agent_config is not None:
            logger.warning("`agent_config` is deprecated. Use inlined parameters instead.")
        if client_tools != ():
            logger.warning("`client_tools` is deprecated. Use `tools` instead.")

        # Construct agent_config from parameters if not provided
        if agent_config is None:
            agent_config = AgentUtils.get_agent_config(
                model=model,
                instructions=instructions,
                tools=tools,
                tool_config=tool_config,
                sampling_params=sampling_params,
                max_infer_iters=max_infer_iters,
                input_shields=input_shields,
                output_shields=output_shields,
                response_format=response_format,
                enable_session_persistence=enable_session_persistence,
                name=name,
            )
            client_tools = AgentUtils.get_client_tools(tools)

        self.agent_config = agent_config
        self.client_tools = {t.get_name(): t for t in client_tools}
        self.sessions = []
        self.tool_parser = tool_parser
        self.builtin_tools = {}
        self.extra_headers = extra_headers
        self._conversation_id: Optional[str] = None
        self._last_response_id: Optional[str] = None

        if isinstance(client, LlamaStackClient):
            raise ValueError("AsyncAgent must be initialized with an AsyncLlamaStackClient")

        self._model = self.agent_config.model
        self._instructions = self.agent_config.instructions

    @property
    def agent_id(self) -> str:
        raise RuntimeError("Agent ID is deprecated in the responses-backed agent")

    async def initialize(self) -> None:
        if not self.builtin_tools and self.agent_config.toolgroups:
            for tg in self.agent_config.toolgroups:
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
        self._conversation_id = conversation.id
        self.sessions.append(conversation.id)
        return conversation.id

    async def create_turn(
        self,
        messages: List[response_create_params.InputUnionMember1],
        session_id: Optional[str] = None,
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
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
    ) -> AsyncIterator[AgentStreamChunk]:
        _ = toolgroups
        _ = documents
        await self.initialize()
        conversation_id = session_id or self._conversation_id
        if not conversation_id:
            conversation_id = await self.create_session(session_name="default")

        request_headers = self.extra_headers
        stream = await self.client.responses.create(
            model=self._model,
            instructions=self._instructions,
            conversation=conversation_id,
            input=messages,
            stream=True,
            previous_response_id=self._last_response_id,
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
                            previous_response_id=event.response_id,
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
