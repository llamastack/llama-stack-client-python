# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..tool_def import ToolDef
from .response_format import ResponseFormat
from .sampling_params import SamplingParams

__all__ = ["AgentConfig", "ToolConfig", "Toolgroup", "ToolgroupAgentToolGroupWithArgs"]


class ToolConfig(BaseModel):
    system_message_behavior: Optional[Literal["append", "replace"]] = None
    """(Optional) Config for how to override the default system prompt.

    - `SystemMessageBehavior.append`: Appends the provided system message to the
      default system prompt. - `SystemMessageBehavior.replace`: Replaces the default
      system prompt with the provided system message. The system message can include
      the string '{{function_definitions}}' to indicate where the function
      definitions should be inserted.
    """

    tool_choice: Union[Literal["auto", "required", "none"], str, None] = None
    """(Optional) Whether tool use is automatic, required, or none.

    Can also specify a tool name to use a specific tool. Defaults to
    ToolChoice.auto.
    """

    tool_prompt_format: Optional[Literal["json", "function_tag", "python_list"]] = None
    """(Optional) Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls.
    """


class ToolgroupAgentToolGroupWithArgs(BaseModel):
    args: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str


Toolgroup: TypeAlias = Union[str, ToolgroupAgentToolGroupWithArgs]


class AgentConfig(BaseModel):
    instructions: str
    """The system instructions for the agent"""

    model: str
    """The model identifier to use for the agent"""

    client_tools: Optional[List[ToolDef]] = None

    enable_session_persistence: Optional[bool] = None
    """Optional flag indicating whether session data has to be persisted"""

    input_shields: Optional[List[str]] = None

    max_infer_iters: Optional[int] = None

    name: Optional[str] = None
    """Optional name for the agent, used in telemetry and identification"""

    output_shields: Optional[List[str]] = None

    response_format: Optional[ResponseFormat] = None
    """Optional response format configuration"""

    sampling_params: Optional[SamplingParams] = None
    """Sampling parameters."""

    tool_choice: Optional[Literal["auto", "required", "none"]] = None
    """Whether tool use is required or automatic.

    This is a hint to the model which may not be followed. It depends on the
    Instruction Following capabilities of the model.
    """

    tool_config: Optional[ToolConfig] = None
    """Configuration for tool use."""

    tool_prompt_format: Optional[Literal["json", "function_tag", "python_list"]] = None
    """Prompt format for calling custom / zero shot tools."""

    toolgroups: Optional[List[Toolgroup]] = None
