# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

"""High-level turn and step events for agent interactions.

This module defines the semantic event model that wraps the lower-level
responses API stream events. It provides a turn/step conceptual model that
makes agent interactions easier to understand and work with.

Key concepts:
- Turn: A complete interaction loop that may span multiple responses
- Step: A distinct phase within a turn (inference or tool_execution)
- Delta: Incremental updates during step execution
- Result: Complete output when a step finishes
"""

from dataclasses import dataclass
from typing import Union, List, Optional, Dict, Any, Literal

from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types import ResponseObject

__all__ = [
    "TurnStarted",
    "TurnCompleted",
    "TurnFailed",
    "StepStarted",
    "StepProgress",
    "StepCompleted",
    "TextDelta",
    "ToolCallIssuedDelta",
    "ToolCallDelta",
    "ToolCallCompletedDelta",
    "StepDelta",
    "InferenceStepResult",
    "ToolExecutionStepResult",
    "StepResult",
    "AgentEvent",
    "AgentStreamChunk",
]


# ============= Turn-Level Events =============


@dataclass
class TurnStarted:
    """Emitted when agent begins processing user input.

    This marks the beginning of a complete interaction cycle that may
    involve multiple inference steps and tool executions.
    """

    event_type: Literal["turn_started"] = "turn_started"
    turn_id: str
    session_id: str


@dataclass
class TurnCompleted:
    """Emitted when agent finishes with final answer.

    This marks the end of a turn when the model has produced a final
    response without any pending client-side tool calls.
    """

    event_type: Literal["turn_completed"] = "turn_completed"
    turn_id: str
    session_id: str
    final_text: str
    response_ids: List[str]  # All response IDs involved in this turn
    num_steps: int


@dataclass
class TurnFailed:
    """Emitted if turn processing fails.

    This indicates an unrecoverable error during turn processing.
    """

    event_type: Literal["turn_failed"] = "turn_failed"
    turn_id: str
    session_id: str
    error_message: str


# ============= Step-Level Events =============


@dataclass
class StepStarted:
    """Emitted when a distinct work phase begins.

    Steps represent distinct phases of work within a turn:
    - inference: Model thinking/generation (may include server-side tools)
    - tool_execution: Client-side tool execution between responses
    """

    event_type: Literal["step_started"] = "step_started"
    step_id: str
    step_type: Literal["inference", "tool_execution"]
    turn_id: str
    metadata: Optional[Dict[str, Any]] = None


# ============= Progress Delta Types =============


@dataclass
class TextDelta:
    """Incremental text during inference.

    Emitted as the model generates text token by token.
    """

    delta_type: Literal["text"] = "text"
    text: str


@dataclass
class ToolCallIssuedDelta:
    """Model initiates a tool call (client or server-side).

    This is emitted when the model decides to call a tool. The tool_type
    field indicates whether this is:
    - "function": Client-side tool requiring client execution
    - Other types: Server-side tools executed within the response
    """

    delta_type: Literal["tool_call_issued"] = "tool_call_issued"
    call_id: str
    tool_type: Literal["function", "file_search", "web_search", "mcp_call", "mcp_list_tools", "memory_retrieval"]
    tool_name: str
    arguments: str  # JSON string


@dataclass
class ToolCallDelta:
    """Incremental tool call arguments (streaming).

    Emitted as the model streams tool call arguments. The arguments
    are accumulated over multiple deltas to form the complete JSON.
    """

    delta_type: Literal["tool_call_delta"] = "tool_call_delta"
    call_id: str
    arguments_delta: str


@dataclass
class ToolCallCompletedDelta:
    """Server-side tool execution completed.

    Emitted when a server-side tool (file_search, web_search, etc.)
    finishes execution. The result field contains the tool output.

    Note: Client-side function tools do NOT emit this event; instead
    they trigger a separate tool_execution step.
    """

    delta_type: Literal["tool_call_completed"] = "tool_call_completed"
    call_id: str
    tool_type: Literal["file_search", "web_search", "mcp_call", "mcp_list_tools", "memory_retrieval"]
    tool_name: str
    result: Any  # Tool execution result from server


# Union of all delta types
StepDelta = Union[TextDelta, ToolCallIssuedDelta, ToolCallDelta, ToolCallCompletedDelta]


@dataclass
class StepProgress:
    """Emitted during step execution with streaming updates.

    Progress events provide real-time updates as a step executes,
    including text deltas and tool call information.
    """

    event_type: Literal["step_progress"] = "step_progress"
    step_id: str
    step_type: Literal["inference", "tool_execution"]
    turn_id: str
    delta: StepDelta


# ============= Step Result Types =============


@dataclass
class InferenceStepResult:
    """Complete inference step output.

    This contains the final accumulated state after an inference step
    completes. It separates client-side function calls (which need
    client execution) from server-side tool executions (which are
    included for logging/reference only).
    """

    step_id: str
    response_id: str
    text_content: str

    # Client-side function calls that need execution
    function_calls: List[ToolCall]

    # Server-side tool calls that were executed (for reference/logging)
    server_tool_executions: List[Dict[str, Any]]  # {"tool_type": "file_search", "call_id": "...", "result": ...}

    stop_reason: str


@dataclass
class ToolExecutionStepResult:
    """Complete tool execution step output (client-side only).

    This contains the results of executing client-side function tools.
    These results will be fed back to the model in the next inference step.
    """

    step_id: str
    tool_calls: List[ToolCall]  # Function calls executed
    tool_responses: List[Dict[str, Any]]  # Normalized responses


# Union of all result types
StepResult = Union[InferenceStepResult, ToolExecutionStepResult]


@dataclass
class StepCompleted:
    """Emitted when a step finishes.

    This provides the complete result of the step execution, including
    all accumulated data and final state.
    """

    event_type: Literal["step_completed"] = "step_completed"
    step_id: str
    step_type: Literal["inference", "tool_execution"]
    turn_id: str
    result: StepResult


# ============= Unified Event Type =============


# Union of all event types
AgentEvent = Union[
    TurnStarted,
    StepStarted,
    StepProgress,
    StepCompleted,
    TurnCompleted,
    TurnFailed,
]


@dataclass
class AgentStreamChunk:
    """What the agent yields to users.

    This is the top-level container for streaming events. Each chunk
    contains a high-level event (turn or step) and optionally the
    final ResponseObject when the turn completes.

    Usage:
        for chunk in agent.create_turn(messages, session_id, stream=True):
            if isinstance(chunk.event, StepProgress):
                if isinstance(chunk.event.delta, TextDelta):
                    print(chunk.event.delta.text, end="")
            elif isinstance(chunk.event, TurnCompleted):
                print(f"\\nDone! Response: {chunk.response}")
    """

    event: AgentEvent
    response: Optional[ResponseObject] = None  # Only set on TurnCompleted
