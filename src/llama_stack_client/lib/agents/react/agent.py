# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import logging
from typing import Any, Callable, List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient
from llama_stack_client.types.agent_create_params import AgentConfig
from llama_stack_client.types.agents.turn_create_params import Toolgroup
from llama_stack_client.types.shared_params.agent_config import ToolConfig
from llama_stack_client.types.shared_params.response_format import ResponseFormat
from llama_stack_client.types.shared_params.sampling_params import SamplingParams

from ..agent import Agent, AgentUtils
from ..client_tool import ClientTool
from ..tool_parser import ToolParser
from .prompts import DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE
from .tool_parser import ReActOutput, ReActToolParser

logger = logging.getLogger(__name__)


def get_tool_defs(
    client: LlamaStackClient, builtin_toolgroups: Tuple[Toolgroup] = (), client_tools: Tuple[ClientTool] = ()
):
    tool_defs = []
    for x in builtin_toolgroups:
        if isinstance(x, str):
            toolgroup_id = x
        else:
            toolgroup_id = x["name"]
        tool_defs.extend(
            [
                {
                    "name": tool.identifier,
                    "description": tool.description,
                    "parameters": tool.parameters,
                }
                for tool in client.tools.list(toolgroup_id=toolgroup_id)
            ]
        )

    tool_defs.extend(
        [
            {
                "name": tool.get_name(),
                "description": tool.get_description(),
                "parameters": tool.get_params_definition(),
            }
            for tool in client_tools
        ]
    )
    return tool_defs


def get_default_react_instructions(
    client: LlamaStackClient, builtin_toolgroups: Tuple[str] = (), client_tools: Tuple[ClientTool] = ()
):
    tool_defs = get_tool_defs(client, builtin_toolgroups, client_tools)
    tool_names = ", ".join([x["name"] for x in tool_defs])
    tool_descriptions = "\n".join([f"- {x['name']}: {x}" for x in tool_defs])
    instruction = DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE.replace("<<tool_names>>", tool_names).replace(
        "<<tool_descriptions>>", tool_descriptions
    )
    return instruction


def get_agent_config_DEPRECATED(
    client: LlamaStackClient,
    model: str,
    builtin_toolgroups: Tuple[str] = (),
    client_tools: Tuple[ClientTool] = (),
    json_response_format: bool = False,
    custom_agent_config: Optional[AgentConfig] = None,
) -> AgentConfig:
    if custom_agent_config is None:
        instruction = get_default_react_instructions(client, builtin_toolgroups, client_tools)

        # user default toolgroups
        agent_config = AgentConfig(
            model=model,
            instructions=instruction,
            toolgroups=builtin_toolgroups,
            client_tools=[client_tool.get_tool_definition() for client_tool in client_tools],
            tool_config={
                "tool_choice": "auto",
                "system_message_behavior": "replace",
            },
            input_shields=[],
            output_shields=[],
            enable_session_persistence=False,
        )
    else:
        agent_config = custom_agent_config

    if json_response_format:
        agent_config["response_format"] = {
            "type": "json_schema",
            "json_schema": ReActOutput.model_json_schema(),
        }

    return agent_config


class ReActAgent(Agent):
    """ReAct agent.

    Simple wrapper around Agent to add prepare prompts for creating a ReAct agent from a list of tools.
    """

    def __init__(
        self,
        client: LlamaStackClient,
        model: str,
        tool_parser: ToolParser = ReActToolParser(),
        instructions: Optional[str] = None,
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]] = None,
        tool_config: Optional[ToolConfig] = None,
        sampling_params: Optional[SamplingParams] = None,
        max_infer_iters: Optional[int] = None,
        input_shields: Optional[List[str]] = None,
        output_shields: Optional[List[str]] = None,
        response_format: Optional[ResponseFormat] = None,
        enable_session_persistence: Optional[bool] = None,
        json_response_format: bool = False,
        builtin_toolgroups: Tuple[str] = (),  # DEPRECATED
        client_tools: Tuple[ClientTool] = (),  # DEPRECATED
        custom_agent_config: Optional[AgentConfig] = None,  # DEPRECATED
    ):
        """Construct an Agent with the given parameters.

        :param client: The LlamaStackClient instance.
        :param custom_agent_config: The AgentConfig instance.
            ::deprecated: use other parameters instead
        :param client_tools: A tuple of ClientTool instances.
            ::deprecated: use tools instead
        :param builtin_toolgroups: A tuple of Toolgroup instances.
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
        :param json_response_format: Whether to use the json response format with default ReAct output schema.
            ::deprecated: use response_format instead
        """
        use_deprecated_params = False
        if custom_agent_config is not None:
            logger.warning("`custom_agent_config` is deprecated. Use inlined parameters instead.")
            use_deprecated_params = True
        if client_tools != ():
            logger.warning("`client_tools` is deprecated. Use `tools` instead.")
            use_deprecated_params = True
        if builtin_toolgroups != ():
            logger.warning("`builtin_toolgroups` is deprecated. Use `tools` instead.")
            use_deprecated_params = True

        if use_deprecated_params:
            agent_config = get_agent_config_DEPRECATED(
                client=client,
                model=model,
                builtin_toolgroups=builtin_toolgroups,
                client_tools=client_tools,
                json_response_format=json_response_format,
            )
            super().__init__(
                client=client,
                agent_config=agent_config,
                client_tools=client_tools,
                tool_parser=tool_parser,
            )

        else:
            if not tool_config:
                tool_config = {
                    "tool_choice": "auto",
                    "system_message_behavior": "replace",
                }

            if json_response_format:
                if instructions is not None:
                    logger.warning(
                        "Using a custom instructions, but json_response_format is set. Please make sure instructions are"
                        "compatible with the default ReAct output format."
                    )
                response_format = {
                    "type": "json_schema",
                    "json_schema": ReActOutput.model_json_schema(),
                }

            # build REACT instructions
            client_tools = AgentUtils.get_client_tools(tools)
            builtin_toolgroups = [x for x in tools if isinstance(x, str) or isinstance(x, dict)]
            if not instructions:
                instructions = get_default_react_instructions(client, builtin_toolgroups, client_tools)

            super().__init__(
                client=client,
                model=model,
                tool_parser=tool_parser,
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
