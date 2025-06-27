# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import logging
from typing import Any, AsyncIterator, Callable, Iterator, List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient
from llama_stack_client.types import ToolResponseMessage, ToolResponseParam, UserMessage
from llama_stack_client.types.agent_create_params import AgentConfig
from llama_stack_client.types.agents.agent_turn_response_stream_chunk import (
    AgentTurnResponseStreamChunk,
)
from llama_stack_client.types.agents.turn import CompletionMessage, Turn
from llama_stack_client.types.agents.turn_create_params import Document, Toolgroup
from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types.shared_params.agent_config import ToolConfig
from llama_stack_client.types.shared_params.response_format import ResponseFormat
from llama_stack_client.types.shared_params.sampling_params import SamplingParams

from ..._types import Headers
from .client_tool import ClientTool, client_tool
from .tool_parser import ToolParser

DEFAULT_MAX_ITER = 10

logger = logging.getLogger(__name__)


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
    def get_tool_calls(chunk: AgentTurnResponseStreamChunk, tool_parser: Optional[ToolParser] = None) -> List[ToolCall]:
        if chunk.event.payload.event_type not in {
            "turn_complete",
            "turn_awaiting_input",
        }:
            return []

        message = chunk.event.payload.turn.output_message
        if message.stop_reason == "out_of_tokens":
            return []

        if tool_parser:
            return tool_parser.get_tool_calls(message)

        return message.tool_calls

    @staticmethod
    def get_turn_id(chunk: AgentTurnResponseStreamChunk) -> Optional[str]:
        if chunk.event.payload.event_type not in [
            "turn_complete",
            "turn_awaiting_input",
        ]:
            return None

        return chunk.event.payload.turn.turn_id

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
            )
            client_tools = AgentUtils.get_client_tools(tools)

        self.agent_config = agent_config
        self.client_tools = {t.get_name(): t for t in client_tools}
        self.sessions = []
        self.tool_parser = tool_parser
        self.builtin_tools = {}
        self.extra_headers = extra_headers
        self.initialize()

    def initialize(self) -> None:
        agentic_system_create_response = self.client.agents.create(
            agent_config=self.agent_config,
            extra_headers=self.extra_headers,
        )
        self.agent_id = agentic_system_create_response.agent_id
        for tg in self.agent_config["toolgroups"]:
            toolgroup_id = tg if isinstance(tg, str) else tg.get("name")
            for tool in self.client.tools.list(toolgroup_id=toolgroup_id, extra_headers=self.extra_headers):
                self.builtin_tools[tool.identifier] = tg.get("args", {}) if isinstance(tg, dict) else {}

    def create_session(self, session_name: str) -> str:
        agentic_system_create_session_response = self.client.agents.session.create(
            agent_id=self.agent_id,
            session_name=session_name,
            extra_headers=self.extra_headers,
        )
        self.session_id = agentic_system_create_session_response.session_id
        self.sessions.append(self.session_id)
        return self.session_id

    def _run_tool_calls(self, tool_calls: List[ToolCall]) -> List[ToolResponseParam]:
        responses = []
        for tool_call in tool_calls:
            responses.append(self._run_single_tool(tool_call))
        return responses

    def _run_single_tool(self, tool_call: ToolCall) -> ToolResponseParam:
        # custom client tools
        if tool_call.tool_name in self.client_tools:
            tool = self.client_tools[tool_call.tool_name]
            # NOTE: tool.run() expects a list of messages, we only pass in last message here
            # but we could pass in the entire message history
            result_message = tool.run(
                [
                    CompletionMessage(
                        role="assistant",
                        content=tool_call.tool_name,
                        tool_calls=[tool_call],
                        stop_reason="end_of_turn",
                    )
                ]
            )
            return result_message

        # builtin tools executed by tool_runtime
        if tool_call.tool_name in self.builtin_tools:
            tool_result = self.client.tool_runtime.invoke_tool(
                tool_name=tool_call.tool_name,
                kwargs={
                    **tool_call.arguments,
                    **self.builtin_tools[tool_call.tool_name],
                },
                extra_headers=self.extra_headers,
            )
            return ToolResponseParam(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=tool_result.content,
            )

        # cannot find tools
        return ToolResponseParam(
            call_id=tool_call.call_id,
            tool_name=tool_call.tool_name,
            content=f"Unknown tool `{tool_call.tool_name}` was called.",
        )

    def create_turn(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
        # TODO: deprecate this
        extra_headers: Headers | None = None,
    ) -> Iterator[AgentTurnResponseStreamChunk] | Turn:
        if stream:
            return self._create_turn_streaming(
                messages, session_id, toolgroups, documents, extra_headers=extra_headers or self.extra_headers
            )
        else:
            chunks = [
                x
                for x in self._create_turn_streaming(
                    messages,
                    session_id,
                    toolgroups,
                    documents,
                    extra_headers=extra_headers or self.extra_headers,
                )
            ]
            if not chunks:
                raise Exception("Turn did not complete")

            last_chunk = chunks[-1]
            if hasattr(last_chunk, "error"):
                if "message" in last_chunk.error:
                    error_msg = last_chunk.error["message"]
                else:
                    error_msg = str(last_chunk.error)
                raise RuntimeError(f"Turn did not complete. Error: {error_msg}")
            try:
                return last_chunk.event.payload.turn
            except AttributeError:
                raise RuntimeError(f"Turn did not complete. Output: {last_chunk}") from None

    def _create_turn_streaming(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        # TODO: deprecate this
        extra_headers: Headers | None = None,
    ) -> Iterator[AgentTurnResponseStreamChunk]:
        n_iter = 0

        # 1. create an agent turn
        turn_response = self.client.agents.turn.create(
            agent_id=self.agent_id,
            # use specified session_id or last session created
            session_id=session_id or self.session_id[-1],
            messages=messages,
            stream=True,
            documents=documents,
            toolgroups=toolgroups,
            extra_headers=extra_headers or self.extra_headers,
        )

        # 2. process turn and resume if there's a tool call
        is_turn_complete = False
        while not is_turn_complete:
            is_turn_complete = True
            for chunk in turn_response:
                if hasattr(chunk, "error"):
                    yield chunk
                    return
                tool_calls = AgentUtils.get_tool_calls(chunk, self.tool_parser)
                if not tool_calls:
                    yield chunk
                else:
                    is_turn_complete = False
                    # End of turn is reached, do not resume even if there's a tool call
                    # We only check for this if tool_parser is not set, because otherwise
                    # tool call will be parsed on client side, and server will always return "end_of_turn"
                    if not self.tool_parser and chunk.event.payload.turn.output_message.stop_reason in {"end_of_turn"}:
                        yield chunk
                        break

                    turn_id = AgentUtils.get_turn_id(chunk)
                    if n_iter == 0:
                        yield chunk

                    # run the tools
                    tool_responses = self._run_tool_calls(tool_calls)

                    # pass it to next iteration
                    turn_response = self.client.agents.turn.resume(
                        agent_id=self.agent_id,
                        session_id=session_id or self.session_id[-1],
                        turn_id=turn_id,
                        tool_responses=tool_responses,
                        stream=True,
                        extra_headers=extra_headers or self.extra_headers,
                    )
                    n_iter += 1

            if self.tool_parser and n_iter > self.agent_config.get("max_infer_iters", DEFAULT_MAX_ITER):
                raise Exception("Max inference iterations reached")


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
            )
            client_tools = AgentUtils.get_client_tools(tools)

        self.agent_config = agent_config
        self.client_tools = {t.get_name(): t for t in client_tools}
        self.sessions = []
        self.tool_parser = tool_parser
        self.builtin_tools = {}
        self.extra_headers = extra_headers
        self._agent_id = None

        if isinstance(client, LlamaStackClient):
            raise ValueError("AsyncAgent must be initialized with an AsyncLlamaStackClient")

    @property
    def agent_id(self) -> str:
        if not self._agent_id:
            raise RuntimeError("Agent ID not initialized. Call initialize() first.")
        return self._agent_id

    async def initialize(self) -> None:
        if self._agent_id:
            return

        agentic_system_create_response = await self.client.agents.create(
            agent_config=self.agent_config,
        )
        self._agent_id = agentic_system_create_response.agent_id
        for tg in self.agent_config["toolgroups"]:
            for tool in await self.client.tools.list(toolgroup_id=tg, extra_headers=self.extra_headers):
                self.builtin_tools[tool.identifier] = tg.get("args", {}) if isinstance(tg, dict) else {}

    async def create_session(self, session_name: str) -> str:
        await self.initialize()
        agentic_system_create_session_response = await self.client.agents.session.create(
            agent_id=self.agent_id,
            session_name=session_name,
            extra_headers=self.extra_headers,
        )
        self.session_id = agentic_system_create_session_response.session_id
        self.sessions.append(self.session_id)
        return self.session_id

    async def create_turn(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
    ) -> AsyncIterator[AgentTurnResponseStreamChunk] | Turn:
        if stream:
            return self._create_turn_streaming(messages, session_id, toolgroups, documents)
        else:
            chunks = [x async for x in self._create_turn_streaming(messages, session_id, toolgroups, documents)]
            if not chunks:
                raise Exception("Turn did not complete")
            return chunks[-1].event.payload.turn

    async def _run_tool_calls(self, tool_calls: List[ToolCall]) -> List[ToolResponseParam]:
        responses = []
        for tool_call in tool_calls:
            responses.append(await self._run_single_tool(tool_call))
        return responses

    async def _run_single_tool(self, tool_call: ToolCall) -> ToolResponseParam:
        # custom client tools
        if tool_call.tool_name in self.client_tools:
            tool = self.client_tools[tool_call.tool_name]
            result_message = await tool.async_run(
                [
                    CompletionMessage(
                        role="assistant",
                        content=tool_call.tool_name,
                        tool_calls=[tool_call],
                        stop_reason="end_of_turn",
                    )
                ]
            )
            return result_message

        # builtin tools executed by tool_runtime
        if tool_call.tool_name in self.builtin_tools:
            tool_result = await self.client.tool_runtime.invoke_tool(
                tool_name=tool_call.tool_name,
                kwargs={
                    **tool_call.arguments,
                    **self.builtin_tools[tool_call.tool_name],
                },
                extra_headers=self.extra_headers,
            )
            return ToolResponseParam(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=tool_result.content,
            )

        # cannot find tools
        return ToolResponseParam(
            call_id=tool_call.call_id,
            tool_name=tool_call.tool_name,
            content=f"Unknown tool `{tool_call.tool_name}` was called.",
        )

    async def _create_turn_streaming(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
    ) -> AsyncIterator[AgentTurnResponseStreamChunk]:
        n_iter = 0

        # 1. create an agent turn
        turn_response = await self.client.agents.turn.create(
            agent_id=self.agent_id,
            # use specified session_id or last session created
            session_id=session_id or self.session_id[-1],
            messages=messages,
            stream=True,
            documents=documents,
            toolgroups=toolgroups,
            extra_headers=self.extra_headers,
        )

        # 2. process turn and resume if there's a tool call
        is_turn_complete = False
        while not is_turn_complete:
            is_turn_complete = True
            async for chunk in turn_response:
                if hasattr(chunk, "error"):
                    yield chunk
                    return

                tool_calls = AgentUtils.get_tool_calls(chunk, self.tool_parser)
                if not tool_calls:
                    yield chunk
                else:
                    is_turn_complete = False
                    # End of turn is reached, do not resume even if there's a tool call
                    if not self.tool_parser and chunk.event.payload.turn.output_message.stop_reason in {"end_of_turn"}:
                        yield chunk
                        break

                    turn_id = AgentUtils.get_turn_id(chunk)
                    if n_iter == 0:
                        yield chunk

                    # run the tools
                    tool_responses = await self._run_tool_calls(tool_calls)

                    # pass it to next iteration
                    turn_response = await self.client.agents.turn.resume(
                        agent_id=self.agent_id,
                        session_id=session_id or self.session_id[-1],
                        turn_id=turn_id,
                        tool_responses=tool_responses,
                        stream=True,
                        extra_headers=self.extra_headers,
                    )
                    n_iter += 1

            if self.tool_parser and n_iter > self.agent_config.get("max_infer_iters", DEFAULT_MAX_ITER):
                raise Exception("Max inference iterations reached")
