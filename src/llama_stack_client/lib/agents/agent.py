# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import json
import logging
from typing import Any, AsyncIterator, Callable, Dict, Iterator, List, Optional, Tuple, Union, TypedDict
from uuid import uuid4

from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
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
    AgentResponseFailed,
    iter_agent_events,
)
from .turn_events import (
    AgentStreamChunk,
    StepCompleted,
    StepStarted,
    TurnFailed,
    ToolExecutionStepResult,
)
from .event_synthesizer import TurnEventSynthesizer


class ToolResponsePayload(TypedDict):
    call_id: str
    tool_name: str
    content: Any


logger = logging.getLogger(__name__)


class ToolUtils:
    @staticmethod
    def coerce_tool_content(content: Any) -> str:
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
    def parse_tool_arguments(arguments: Any) -> Dict[str, Any]:
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
    def normalize_tool_response(tool_response: Any) -> ToolResponsePayload:
        if isinstance(tool_response, ToolResponse):
            payload: ToolResponsePayload = {
                "call_id": tool_response.call_id,
                "tool_name": str(tool_response.tool_name),
                "content": ToolUtils.coerce_tool_content(tool_response.content),
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
                "content": ToolUtils.coerce_tool_content(tool_response.get("content")),
            }
            return payload

        raise TypeError(f"Unsupported tool response type: {type(tool_response)!r}")


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
        self._session_last_response_id: Dict[str, str] = {}

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
        return conversation.id

    def _run_tool_calls(self, tool_calls: List[ToolCall]) -> List[ToolResponsePayload]:
        responses: List[ToolResponsePayload] = []
        for tool_call in tool_calls:
            raw_result = self._run_single_tool(tool_call)
            responses.append(ToolUtils.normalize_tool_response(raw_result))
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
            tool_args = ToolUtils.parse_tool_arguments(tool_call.arguments)
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
                "content": ToolUtils.coerce_tool_content(tool_result.content),
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

        # Generate turn_id
        turn_id = f"turn_{uuid4().hex[:12]}"

        # Create synthesizer
        synthesizer = TurnEventSynthesizer(session_id=session_id, turn_id=turn_id)

        request_headers = extra_headers or self.extra_headers

        # Main turn loop
        while True:
            # Create response stream
            raw_stream = self.client.responses.create(
                model=self._model,
                instructions=self._instructions,
                conversation=session_id,
                input=messages,
                stream=True,
                extra_headers=request_headers,
            )

            # Process events
            function_calls_to_execute: List[ToolCall] = []  # Only client-side!

            for low_level_event in iter_agent_events(raw_stream):
                # Handle failures
                if isinstance(low_level_event, AgentResponseFailed):
                    yield AgentStreamChunk(
                        event=TurnFailed(
                            turn_id=turn_id, session_id=session_id, error_message=low_level_event.error_message
                        )
                    )
                    return

                # Feed to synthesizer
                for high_level_event in synthesizer.process_low_level_event(low_level_event):
                    # Track function calls that need client execution
                    if isinstance(high_level_event, StepCompleted):
                        if high_level_event.step_type == "inference":
                            result = high_level_event.result
                            if result.function_calls:  # Only client-side function calls
                                function_calls_to_execute = result.function_calls

                    yield AgentStreamChunk(event=high_level_event)

            # Enrich server-side tool executions with results from ResponseObject
            response = self.client.responses.retrieve(
                synthesizer.current_response_id or "", extra_headers=request_headers
            )
            synthesizer.enrich_with_response(response)

            # If no client-side function calls, turn is done
            if not function_calls_to_execute:
                # Emit TurnCompleted
                for event in synthesizer.finish_turn(response):
                    yield AgentStreamChunk(event=event, response=response)
                self._last_response_id = response.id
                self._session_last_response_id[session_id] = response.id
                break

            # Execute client-side tools (emit tool execution step events)
            tool_step_id = f"{turn_id}_step_{synthesizer.step_counter}"
            synthesizer.step_counter += 1

            yield AgentStreamChunk(
                event=StepStarted(
                    step_id=tool_step_id,
                    step_type="tool_execution",
                    turn_id=turn_id,
                    metadata={"server_side": False},
                )
            )

            tool_responses = self._run_tool_calls(function_calls_to_execute)

            yield AgentStreamChunk(
                event=StepCompleted(
                    step_id=tool_step_id,
                    step_type="tool_execution",
                    turn_id=turn_id,
                    result=ToolExecutionStepResult(
                        step_id=tool_step_id, tool_calls=function_calls_to_execute, tool_responses=tool_responses
                    ),
                )
            )

            # Continue loop with tool outputs as input
            messages = [
                response_create_params.InputUnionMember1OpenAIResponseInputFunctionToolCallOutput(
                    type="function_call_output", call_id=payload["call_id"], output=payload["content"]
                )
                for payload in tool_responses
            ]


class AsyncAgent:
    def __init__(
        self,
        client: AsyncLlamaStackClient,
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
        self._session_last_response_id: Dict[str, str] = {}

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
            responses.append(ToolUtils.normalize_tool_response(raw_result))
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
            tool_args = ToolUtils.parse_tool_arguments(tool_call.arguments)
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
                "content": ToolUtils.coerce_tool_content(tool_result.content),
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

        # Generate turn_id
        turn_id = f"turn_{uuid4().hex[:12]}"

        # Create synthesizer
        synthesizer = TurnEventSynthesizer(session_id=session_id, turn_id=turn_id)

        request_headers = self.extra_headers

        # Main turn loop
        while True:
            # Create response stream
            raw_stream = await self.client.responses.create(
                model=self._model,
                instructions=self._instructions,
                conversation=session_id,
                input=messages,
                stream=True,
                extra_headers=request_headers,
            )

            # Process events
            function_calls_to_execute: List[ToolCall] = []  # Only client-side!

            async for low_level_event in iter_agent_events(raw_stream):
                # Handle failures
                if isinstance(low_level_event, AgentResponseFailed):
                    yield AgentStreamChunk(
                        event=TurnFailed(
                            turn_id=turn_id, session_id=session_id, error_message=low_level_event.error_message
                        )
                    )
                    return

                # Feed to synthesizer
                for high_level_event in synthesizer.process_low_level_event(low_level_event):
                    # Track function calls that need client execution
                    if isinstance(high_level_event, StepCompleted):
                        if high_level_event.step_type == "inference":
                            result = high_level_event.result
                            if result.function_calls:  # Only client-side function calls
                                function_calls_to_execute = result.function_calls

                    yield AgentStreamChunk(event=high_level_event)

            # Enrich server-side tool executions with results from ResponseObject
            response = await self.client.responses.retrieve(
                synthesizer.current_response_id or "", extra_headers=request_headers
            )
            synthesizer.enrich_with_response(response)

            # If no client-side function calls, turn is done
            if not function_calls_to_execute:
                # Emit TurnCompleted
                for event in synthesizer.finish_turn(response):
                    yield AgentStreamChunk(event=event, response=response)
                self._last_response_id = response.id
                self._session_last_response_id[session_id] = response.id
                break

            # Execute client-side tools (emit tool execution step events)
            tool_step_id = f"{turn_id}_step_{synthesizer.step_counter}"
            synthesizer.step_counter += 1

            yield AgentStreamChunk(
                event=StepStarted(
                    step_id=tool_step_id,
                    step_type="tool_execution",
                    turn_id=turn_id,
                    metadata={"server_side": False},
                )
            )

            tool_responses = await self._run_tool_calls(function_calls_to_execute)

            yield AgentStreamChunk(
                event=StepCompleted(
                    step_id=tool_step_id,
                    step_type="tool_execution",
                    turn_id=turn_id,
                    result=ToolExecutionStepResult(
                        step_id=tool_step_id, tool_calls=function_calls_to_execute, tool_responses=tool_responses
                    ),
                )
            )

            # Continue loop with tool outputs as input
            messages = [
                response_create_params.InputUnionMember1OpenAIResponseInputFunctionToolCallOutput(
                    type="function_call_output", call_id=payload["call_id"], output=payload["content"]
                )
                for payload in tool_responses
            ]


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
