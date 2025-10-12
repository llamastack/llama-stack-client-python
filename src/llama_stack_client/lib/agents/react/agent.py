# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import logging
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient
from llama_stack_client.types.agents.turn_create_params import Toolgroup

from ...._types import Headers
from ..agent import Agent, AgentUtils
from ..client_tool import ClientTool
from ..tool_parser import ToolParser
from .prompts import DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE
from .tool_parser import ReActToolParser

logger = logging.getLogger(__name__)


def get_tool_defs(
    client: LlamaStackClient,
    builtin_toolgroups: Tuple[Union[str, Dict[str, Any], Toolgroup], ...] = (),
    client_tools: Tuple[ClientTool, ...] = (),
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
                    "input_schema": tool.input_schema,
                }
                for tool in client.tools.list(toolgroup_id=toolgroup_id)
            ]
        )

    tool_defs.extend(
        [
            {
                "name": tool.get_name(),
                "description": tool.get_description(),
                "input_schema": tool.get_input_schema(),
            }
            for tool in client_tools
        ]
    )
    return tool_defs


def get_default_react_instructions(
    client: LlamaStackClient,
    builtin_toolgroups: Tuple[Union[str, Dict[str, Any], Toolgroup], ...] = (),
    client_tools: Tuple[ClientTool, ...] = (),
):
    tool_defs = get_tool_defs(client, builtin_toolgroups, client_tools)
    tool_names = ", ".join([x["name"] for x in tool_defs])
    tool_descriptions = "\n".join([f"- {x['name']}: {x}" for x in tool_defs])
    instruction = DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE.replace("<<tool_names>>", tool_names).replace(
        "<<tool_descriptions>>", tool_descriptions
    )
    return instruction


class ReActAgent(Agent):
    def __init__(
        self,
        client: LlamaStackClient,
        *,
        model: str,
        tools: Optional[List[Union[Toolgroup, ClientTool, Callable[..., Any]]]] = None,
        tool_parser: Optional[ToolParser] = None,
        instructions: Optional[str] = None,
        extra_headers: Headers | None = None,
        json_response_format: bool = False,
    ):
        if json_response_format:
            logger.warning("`json_response_format` is deprecated and will be removed in a future release.")

        if tool_parser is None:
            tool_parser = ReActToolParser()

        tool_list = tools or []
        client_tool_instances = AgentUtils.get_client_tools(tool_list)
        builtin_toolgroups = [x for x in tool_list if isinstance(x, (str, dict, Toolgroup))]

        if instructions is None:
            instructions = get_default_react_instructions(
                client, tuple(builtin_toolgroups), tuple(client_tool_instances)
            )

        super().__init__(
            client=client,
            model=model,
            instructions=instructions,
            tools=tool_list,
            tool_parser=tool_parser,
            extra_headers=extra_headers,
        )
