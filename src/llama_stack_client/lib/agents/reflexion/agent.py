# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import logging
from typing import Any, Callable, List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient
from llama_stack_client.types.agent_create_params import AgentConfig
from llama_stack_client.types.shared_params.agent_config import ToolConfig
from llama_stack_client.types.shared_params.response_format import ResponseFormat
from llama_stack_client.types.shared_params.sampling_params import SamplingParams

from ..react.agent import ReActAgent, get_tool_defs
from ..client_tool import ClientTool
from ..tool_parser import ToolParser
from .prompts import DEFAULT_REFLEXION_AGENT_SYSTEM_PROMPT_TEMPLATE
from .tool_parser import ReflexionToolParser, ReflexionOutput

logger = logging.getLogger(__name__)


def get_default_reflexion_instructions(
    client: LlamaStackClient, builtin_toolgroups: Tuple = (), client_tools: Tuple[ClientTool] = ()
):
    tool_defs = get_tool_defs(client, builtin_toolgroups, client_tools)
    tool_names = ", ".join([x["name"] for x in tool_defs])
    tool_descriptions = "\n".join([f"- {x['name']}: {x}" for x in tool_defs])
    instruction = DEFAULT_REFLEXION_AGENT_SYSTEM_PROMPT_TEMPLATE.replace("<<tool_names>>", tool_names).replace(
        "<<tool_descriptions>>", tool_descriptions
    )
    return instruction


class ReflexionAgent(ReActAgent):
    """Reflexion agent.

    Extends ReAct agent with self-reflection capabilities to improve reasoning and tool use.
    """

    def __init__(
        self,
        client: LlamaStackClient,
        model: str,
        tool_parser: ToolParser = ReflexionToolParser(),
        instructions: Optional[str] = None,
        tools: Optional[List[Union[str, dict, ClientTool, Callable[..., Any]]]] = None,
        tool_config: Optional[ToolConfig] = None,
        sampling_params: Optional[SamplingParams] = None,
        max_infer_iters: Optional[int] = None,
        input_shields: Optional[List[str]] = None,
        output_shields: Optional[List[str]] = None,
        response_format: Optional[ResponseFormat] = None,
        enable_session_persistence: Optional[bool] = None,
        json_response_format: bool = False,
        # The following are deprecated, kept for backward compatibility
        builtin_toolgroups: Tuple[str] = (), 
        client_tools: Tuple[ClientTool] = (),
        custom_agent_config: Optional[AgentConfig] = None,
    ):
        # Dictionary to store reflections for each session
        self.reflection_memory = {}

        # If custom instructions are not provided, use the default Reflexion instructions
        if not instructions and not custom_agent_config:
            # Convert tools to the format expected by get_default_reflexion_instructions if needed
            if tools:
                from ..agent import AgentUtils
                client_tools_from_tools = AgentUtils.get_client_tools(tools)
                builtin_toolgroups_from_tools = [x for x in tools if isinstance(x, str) or isinstance(x, dict)]
                instructions = get_default_reflexion_instructions(client, builtin_toolgroups_from_tools, client_tools_from_tools)
            else:
                # Fallback to deprecated parameters
                instructions = get_default_reflexion_instructions(client, builtin_toolgroups, client_tools)

        # If json_response_format is True and no custom response format is provided,
        # set the response format to use the ReflexionOutput schema
        if json_response_format and not response_format:
            response_format = {
                "type": "json_schema",
                "json_schema": ReflexionOutput.model_json_schema(),
            }

        # Initialize parent ReActAgent
        super().__init__(
            client=client,
            model=model,
            tool_parser=tool_parser,
            instructions=instructions,
            tools=tools if tools is not None else builtin_toolgroups,  # Prefer new tools param, fallback to deprecated
            tool_config=tool_config,
            sampling_params=sampling_params,
            max_infer_iters=max_infer_iters,
            input_shields=input_shields,
            output_shields=output_shields,
            response_format=response_format,
            enable_session_persistence=enable_session_persistence,
            json_response_format=json_response_format,
            client_tools=client_tools,
            custom_agent_config=custom_agent_config,
        )

    def create_turn(self, messages, session_id, stream=False, **kwargs):
        """Override create_turn to add reflection to the context"""
        
        # If we have reflections for this session, add them to the context
        if session_id in self.reflection_memory and self.reflection_memory[session_id]:
            # Create a system message with past reflections
            reflection_summary = "\n".join(self.reflection_memory[session_id])
            reflection_message = {
                "role": "system", 
                "content": f"Your past reflections:\n{reflection_summary}\n\nUse these reflections to improve your reasoning."
            }
            
            # Insert reflection message before the user message
            for i, msg in enumerate(messages):
                if msg["role"] == "user":
                    messages.insert(i, reflection_message)
                    break
        
        # Call the parent method to process the turn
        response = super().create_turn(messages, session_id, stream, **kwargs)
        
        # Store any new reflections
        if not stream:
            try:
                # Extract reflection from response
                content = response.choices[0].message.content
                reflexion_output = ReflexionOutput.model_validate_json(content)
                
                if reflexion_output.reflection:
                    if session_id not in self.reflection_memory:
                        self.reflection_memory[session_id] = []
                    
                    self.reflection_memory[session_id].append(reflexion_output.reflection)
            except Exception as e:
                logger.warning(f"Failed to extract reflection: {e}")
        
        return response