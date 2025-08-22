# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .response_format import ResponseFormat
from .sampling_params import SamplingParams

__all__ = [
    "AgentConfig",
    "ClientTool",
    "ClientToolParameter",
    "ToolConfig",
    "Toolgroup",
    "ToolgroupAgentToolGroupWithArgs",
]


class ClientToolParameter(TypedDict, total=False):
    description: Required[str]
    """Human-readable description of what the parameter does"""

    name: Required[str]
    """Name of the parameter"""

    parameter_type: Required[str]
    """Type of the parameter (e.g., string, integer)"""

    required: Required[bool]
    """Whether this parameter is required for tool invocation"""

    default: Union[bool, float, str, Iterable[object], object, None]
    """(Optional) Default value for the parameter if not provided"""


class ClientTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool"""

    description: str
    """(Optional) Human-readable description of what the tool does"""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Additional metadata about the tool"""

    parameters: Iterable[ClientToolParameter]
    """(Optional) List of parameters this tool accepts"""


class ToolConfig(TypedDict, total=False):
    system_message_behavior: Literal["append", "replace"]
    """(Optional) Config for how to override the default system prompt.

    - `SystemMessageBehavior.append`: Appends the provided system message to the
      default system prompt. - `SystemMessageBehavior.replace`: Replaces the default
      system prompt with the provided system message. The system message can include
      the string '{{function_definitions}}' to indicate where the function
      definitions should be inserted.
    """

    tool_choice: Union[Literal["auto", "required", "none"], str]
    """(Optional) Whether tool use is automatic, required, or none.

    Can also specify a tool name to use a specific tool. Defaults to
    ToolChoice.auto.
    """

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """(Optional) Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls.
    """


class ToolgroupAgentToolGroupWithArgs(TypedDict, total=False):
    args: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]


Toolgroup: TypeAlias = Union[str, ToolgroupAgentToolGroupWithArgs]


class AgentConfig(TypedDict, total=False):
    instructions: Required[str]
    """The system instructions for the agent"""

    model: Required[str]
    """The model identifier to use for the agent"""

    client_tools: Iterable[ClientTool]

    enable_session_persistence: bool
    """Optional flag indicating whether session data has to be persisted"""

    input_shields: List[str]

    max_infer_iters: int

    name: str
    """Optional name for the agent, used in telemetry and identification"""

    output_shields: List[str]

    response_format: ResponseFormat
    """Optional response format configuration"""

    sampling_params: SamplingParams
    """Sampling parameters."""

    tool_choice: Literal["auto", "required", "none"]
    """Whether tool use is required or automatic.

    This is a hint to the model which may not be followed. It depends on the
    Instruction Following capabilities of the model.
    """

    tool_config: ToolConfig
    """Configuration for tool use."""

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """Prompt format for calling custom / zero shot tools."""

    toolgroups: List[Toolgroup]
