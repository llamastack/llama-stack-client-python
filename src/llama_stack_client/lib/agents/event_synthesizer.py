# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

"""Event synthesizer that translates response stream events to turn/step events.

This module provides the TurnEventSynthesizer class which maintains state
and translates low-level response stream events into high-level turn and
step events that provide semantic meaning to agent interactions.

Key architectural principle:
- inference steps = model thinking/deciding what to do
- tool_execution steps = ANY tool executing (server-side OR client-side)

Server-side tools (file_search, web_search, mcp_call):
- Execute within the response stream
- We synthesize tool_execution step boundaries from stream events
- Results automatically fed back to model

Client-side tools (function):
- Require breaking the response stream
- Agent.py emits tool_execution steps when executing them
- Results manually fed back via new response
"""

from dataclasses import dataclass
from typing import Iterator, Optional, Dict, List, Any, Iterable

from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types import ResponseObject

from logging import getLogger

logger = getLogger(__name__)

# ============= Internal Low-Level Stream Events =============
# These are private internal events used during translation from
# raw ResponseObjectStream to high-level turn/step events.
# NOT part of the public API.


@dataclass
class _AgentStreamEvent:
    """Base class for internal low-level stream events."""

    type: str


@dataclass
class _AgentResponseStarted(_AgentStreamEvent):
    response_id: str


@dataclass
class _AgentTextDelta(_AgentStreamEvent):
    text: str
    response_id: str
    output_index: int


@dataclass
class _AgentTextCompleted(_AgentStreamEvent):
    text: str
    response_id: str
    output_index: int


@dataclass
class _AgentToolCallIssued(_AgentStreamEvent):
    response_id: str
    output_index: int
    call_id: str
    name: str
    arguments_json: str


@dataclass
class _AgentToolCallDelta(_AgentStreamEvent):
    response_id: str
    output_index: int
    call_id: str
    arguments_delta: Optional[str]


@dataclass
class _AgentToolCallCompleted(_AgentStreamEvent):
    response_id: str
    output_index: int
    call_id: str
    arguments_json: str


@dataclass
class _AgentResponseCompleted(_AgentStreamEvent):
    response_id: str


@dataclass
class _AgentResponseFailed(_AgentStreamEvent):
    response_id: str
    error_message: str


from typing import Any

# Note: We use duck typing on event.type instead of isinstance checks
# to support both OpenAI SDK and LlamaStack SDK events

from .turn_events import (
    AgentEvent,
    TurnStarted,
    TurnCompleted,
    TurnFailed,
    StepStarted,
    StepProgress,
    StepCompleted,
    TextDelta,
    ToolCallIssuedDelta,
    ToolCallDelta,
    InferenceStepResult,
    ToolExecutionStepResult,
)

__all__ = ["TurnEventSynthesizer"]


class TurnEventSynthesizer:
    """Translates low-level response events to high-level turn/step events.

    This class maintains state across the event stream to provide semantic
    meaning and structure. It tracks:
    - Turn lifecycle (started, completed)
    - Step boundaries (inference, tool_execution)
    - Content accumulation (text, tool calls)
    - Tool classification (client-side vs server-side)
    """

    def __init__(self, session_id: str, turn_id: str):
        """Initialize synthesizer for a new turn.

        Args:
            session_id: The conversation session ID
            turn_id: Unique identifier for this turn
        """
        self.session_id = session_id
        self.turn_id = turn_id

        # Step tracking
        self.step_counter = 0
        self.current_step_id: Optional[str] = None
        self.current_step_type: Optional[str] = None

        # Inference step accumulation
        self.current_response_id: Optional[str] = None
        self.text_parts: List[str] = []

        # Tool call tracking (both server and client-side)
        # For server-side tools, these are used within tool_execution steps
        # For client-side tools, these are accumulated and returned in inference step result
        self.tool_calls_building: Dict[str, Dict[str, Any]] = {}  # call_id -> {tool_call, is_server_side, ...}

        # Current server-side tool execution (for handling call_id mismatches)
        self.current_server_tool: Optional[Dict[str, Any]] = None

        # Current client-side tool (for handling call_id mismatches)
        self.current_client_tool: Optional[Dict[str, Any]] = None

        # Client-side function calls (accumulated for agent.py to execute)
        self.function_calls: List[ToolCall] = []

        # Turn-level accumulation
        self.all_response_ids: List[str] = []
        self.turn_started = False
        self.last_response: Optional[ResponseObject] = None

    def process_low_level_event(self, event: _AgentStreamEvent) -> Iterator[AgentEvent]:
        """Map low-level events to high-level turn/step events.

        This is the core translation logic. It processes each low-level
        event from the response stream and emits corresponding high-level
        events that provide semantic meaning.

        Args:
            event: Low-level event from response stream

        Yields:
            High-level turn/step events
        """
        # Emit TurnStarted on first event
        if not self.turn_started:
            self.turn_started = True
            yield TurnStarted(turn_id=self.turn_id, session_id=self.session_id)

        if isinstance(event, _AgentResponseStarted):
            # Start new inference step
            self.current_step_id = f"{self.turn_id}_step_{self.step_counter}"
            self.step_counter += 1
            self.current_step_type = "inference"
            self.current_response_id = event.response_id
            self.all_response_ids.append(event.response_id)
            self.text_parts = []
            self.tool_calls_building = {}
            self.function_calls = []

            yield StepStarted(
                step_id=self.current_step_id,
                step_type="inference",
                turn_id=self.turn_id,
            )

        elif isinstance(event, _AgentTextDelta):
            # Only emit text if we're in an inference step
            if self.current_step_type == "inference":
                self.text_parts.append(event.text)
                yield StepProgress(
                    step_id=self.current_step_id or "",
                    step_type="inference",
                    turn_id=self.turn_id,
                    delta=TextDelta(text=event.text),
                )

        elif isinstance(event, _AgentTextCompleted):
            # Text completion - just ensure we have the complete text
            pass

        elif isinstance(event, _AgentToolCallIssued):
            # Determine if server-side or client-side
            tool_type = self._classify_tool_type(event.name)
            is_server_side = tool_type != "function"

            # Create tool call object
            tool_call = ToolCall(
                call_id=event.call_id,
                tool_name=event.name,
                arguments=event.arguments_json or "",
            )

            # Track this tool call
            self.tool_calls_building[event.call_id] = {
                "tool_call": tool_call,
                "tool_type": tool_type,
                "is_server_side": is_server_side,
                "arguments": event.arguments_json or "",
            }

            if is_server_side:
                # SERVER-SIDE TOOL: Complete current inference step and start tool_execution step
                # First complete the inference step
                if self.current_step_type == "inference":
                    yield StepCompleted(
                        step_id=self.current_step_id or "",
                        step_type="inference",
                        turn_id=self.turn_id,
                        result=InferenceStepResult(
                            step_id=self.current_step_id or "",
                            response_id=self.current_response_id or "",
                            text_content="".join(self.text_parts),
                            function_calls=[],  # No client-side function calls yet
                            server_tool_executions=[],  # Will be populated in tool_execution step
                            stop_reason="server_tool_call",
                        ),
                    )

                # Start tool_execution step for server-side tool
                self.current_step_id = f"{self.turn_id}_step_{self.step_counter}"
                self.step_counter += 1
                self.current_step_type = "tool_execution"
                self.text_parts = []  # Reset for next inference step

                # Remember the current server tool for handling call_id mismatches
                self.current_server_tool = self.tool_calls_building[event.call_id]

                yield StepStarted(
                    step_id=self.current_step_id,
                    step_type="tool_execution",
                    turn_id=self.turn_id,
                    metadata={
                        "server_side": True,
                        "tool_type": tool_type,
                        "tool_name": event.name,
                    },
                )

                # Emit the tool call issued as progress
                yield StepProgress(
                    step_id=self.current_step_id,
                    step_type="tool_execution",
                    turn_id=self.turn_id,
                    delta=ToolCallIssuedDelta(
                        call_id=event.call_id,
                        tool_type=tool_type,  # type: ignore
                        tool_name=event.name,
                        arguments=event.arguments_json or "{}",
                    ),
                )
            else:
                # CLIENT-SIDE FUNCTION: Just accumulate, agent.py will handle execution
                self.function_calls.append(tool_call)

                # Remember current client tool for handling call_id mismatches
                self.current_client_tool = self.tool_calls_building[event.call_id]

                # Emit as progress within current inference step
                yield StepProgress(
                    step_id=self.current_step_id or "",
                    step_type="inference",
                    turn_id=self.turn_id,
                    delta=ToolCallIssuedDelta(
                        call_id=event.call_id,
                        tool_type="function",
                        tool_name=event.name,
                        arguments=event.arguments_json or "{}",
                    ),
                )

        elif isinstance(event, _AgentToolCallDelta):
            # Update arguments
            builder = None
            if event.call_id in self.tool_calls_building:
                builder = self.tool_calls_building[event.call_id]
            elif self.current_server_tool and self.current_step_type == "tool_execution":
                # Handle call_id mismatch for server-side tool
                builder = self.current_server_tool
                self.tool_calls_building[event.call_id] = builder
            elif self.current_client_tool and self.current_step_type == "inference":
                # Handle call_id mismatch for client-side tool
                builder = self.current_client_tool
                self.tool_calls_building[event.call_id] = builder

            if builder:
                builder["arguments"] += event.arguments_delta or ""
                # Update the ToolCall object (Pydantic models are immutable, so replace it)
                builder["tool_call"] = ToolCall(
                    call_id=builder["tool_call"].call_id,
                    tool_name=builder["tool_call"].tool_name,
                    arguments=builder["arguments"],
                )

                # If client-side, also update the function_calls list
                if not builder["is_server_side"]:
                    for i, func_call in enumerate(self.function_calls):
                        # Match by tool_name since call_id might have changed
                        if func_call.tool_name == builder["tool_call"].tool_name:
                            self.function_calls[i] = builder["tool_call"]
                            break

                # Emit delta
                step_type = "tool_execution" if builder["is_server_side"] else "inference"
                yield StepProgress(
                    step_id=self.current_step_id or "",
                    step_type=step_type,  # type: ignore
                    turn_id=self.turn_id,
                    delta=ToolCallDelta(
                        call_id=event.call_id,
                        arguments_delta=event.arguments_delta or "",
                    ),
                )

        elif isinstance(event, _AgentToolCallCompleted):
            # Update final arguments
            builder = None
            if event.call_id in self.tool_calls_building:
                builder = self.tool_calls_building[event.call_id]
            elif self.current_server_tool and self.current_step_type == "tool_execution":
                # Handle call_id mismatch for server-side tool
                builder = self.current_server_tool
                self.tool_calls_building[event.call_id] = builder
            elif self.current_client_tool and self.current_step_type == "inference":
                # Handle call_id mismatch for client-side tool
                builder = self.current_client_tool
                self.tool_calls_building[event.call_id] = builder

            if builder:
                builder["arguments"] = event.arguments_json or ""
                # Update the ToolCall object (Pydantic models are immutable, so replace it)
                # Keep the original call_id - the server stores tool calls with the original call_id
                builder["tool_call"] = ToolCall(
                    call_id=builder["tool_call"].call_id,  # Keep the original call_id
                    tool_name=builder["tool_call"].tool_name,
                    arguments=event.arguments_json or "{}",
                )

                if builder["is_server_side"]:
                    # SERVER-SIDE TOOL: Complete tool_execution step and start new inference step
                    tool_call = builder["tool_call"]

                    # Complete the tool_execution step
                    yield StepCompleted(
                        step_id=self.current_step_id or "",
                        step_type="tool_execution",
                        turn_id=self.turn_id,
                        result=ToolExecutionStepResult(
                            step_id=self.current_step_id or "",
                            tool_calls=[tool_call],
                            tool_responses=[],  # Will be enriched from ResponseObject later if needed
                        ),
                    )

                    # Clear current server tool
                    self.current_server_tool = None

                    # Start new inference step for model to process results
                    self.current_step_id = f"{self.turn_id}_step_{self.step_counter}"
                    self.step_counter += 1
                    self.current_step_type = "inference"

                    yield StepStarted(
                        step_id=self.current_step_id,
                        step_type="inference",
                        turn_id=self.turn_id,
                    )

                else:
                    # CLIENT-SIDE FUNCTION: Update the accumulated function call
                    # Use the updated ToolCall from builder
                    # Note: We search by the tool_call in builder, which has the original call_id,
                    # because event.call_id might be different due to call_id mismatches
                    old_call_id = builder["tool_call"].call_id
                    for i, func_call in enumerate(self.function_calls):
                        # Match by tool_name since call_id might have changed
                        if func_call.tool_name == builder["tool_call"].tool_name:
                            self.function_calls[i] = builder["tool_call"]
                            break

                    # Clear current client tool
                    self.current_client_tool = None

        elif isinstance(event, _AgentResponseCompleted):
            # Response completes - finish current step
            if self.current_step_type == "inference":
                yield StepCompleted(
                    step_id=self.current_step_id or "",
                    step_type="inference",
                    turn_id=self.turn_id,
                    result=InferenceStepResult(
                        step_id=self.current_step_id or "",
                        response_id=event.response_id,
                        text_content="".join(self.text_parts),
                        function_calls=self.function_calls.copy(),
                        server_tool_executions=[],  # Server tools already handled as separate steps
                        stop_reason="tool_calls" if self.function_calls else "end_of_turn",
                    ),
                )
            elif self.current_step_type == "tool_execution":
                # This shouldn't normally happen, but if it does, complete the tool execution step
                pass

        elif isinstance(event, _AgentResponseFailed):
            # Emit TurnFailed for response failures
            yield TurnFailed(
                turn_id=self.turn_id,
                session_id=self.session_id,
                error_message=event.error_message,
            )

    def _classify_tool_type(self, tool_name: str) -> str:
        """Determine if tool is client-side or server-side.

        Args:
            tool_name: Name of the tool

        Returns:
            Tool type string: "function" for client-side, or specific
            server-side type (e.g., "file_search", "web_search")
        """
        # Known server-side tools that execute within the response
        server_side_tools = {
            "file_search",
            "knowledge_search",  # file_search appears as knowledge_search in OpenAI-compatible mode
            "web_search",
            "query_from_memory",
            "mcp_call",
            "mcp_list_tools",
        }

        if tool_name in server_side_tools:
            # Return a normalized type name
            if tool_name == "knowledge_search":
                return "file_search"  # Normalize to file_search for consistency
            return tool_name

        # Default to function for client-side tools
        return "function"

    def process_raw_stream(self, events: Iterable[Any]) -> Iterator[AgentEvent]:
        """Process raw response stream events and emit high-level turn/step events.

        This method uses duck typing to work with both OpenAI SDK and LlamaStack SDK events.
        It checks the event.type field instead of using isinstance checks.

        Args:
            events: Raw event stream from responses.create() (OpenAI or LlamaStack client)

        Yields:
            High-level turn/step events
        """
        current_response_id: Optional[str] = None

        for event in events:
            # Extract response_id
            response_id = getattr(event, "response_id", None)
            if response_id is None and hasattr(event, "response"):
                response_id = getattr(event.response, "id", None)
            if response_id is not None:
                current_response_id = response_id

            # Translate raw event to _AgentStreamEvent and process it
            # Use duck typing on event.type to support both OpenAI and LlamaStack SDKs
            event_type = getattr(event, "type", None)
            if "delta" not in event_type:
                from rich.pretty import pprint

                pprint(event)

            if event_type == "response.in_progress":
                low_level_event = _AgentResponseStarted(type="response_started", response_id=event.response.id)
                yield from self.process_low_level_event(low_level_event)

            elif event_type == "response.output_text.delta":
                low_level_event = _AgentTextDelta(
                    type="text_delta",
                    text=event.delta,
                    response_id=current_response_id or "",
                    output_index=event.output_index,
                )
                yield from self.process_low_level_event(low_level_event)

            elif event_type == "response.output_text.done":
                low_level_event = _AgentTextCompleted(
                    type="text_completed",
                    text=event.text,
                    response_id=current_response_id or "",
                    output_index=event.output_index,
                )
                yield from self.process_low_level_event(low_level_event)

            elif event_type == "response.output_item.done":
                item = event.item
                if item.type in ("function_call", "web_search_call"):
                    low_level_event = _AgentToolCallCompleted(
                        type="tool_call_completed",
                        response_id=current_response_id or "",
                        output_index=event.output_index,
                        call_id=item.call_id,
                        arguments_json=item.arguments,
                    )
                    yield from self.process_low_level_event(low_level_event)
                elif item.type == "file_search_call":
                    low_level_event = _AgentToolCallCompleted(
                        type="tool_call_completed",
                        response_id=current_response_id or "",
                        output_index=event.output_index,
                        call_id=item.id,
                        arguments_json="{}",
                    )
                    yield from self.process_low_level_event(low_level_event)
                else:
                    logger.warning(f"Unhandled item type: {item.type}")

            elif event_type == "response.output_item.added":
                item = event.item
                item_type = getattr(item, "type", None)

                if item_type == "function_call":
                    low_level_event = _AgentToolCallIssued(
                        type="tool_call_issued",
                        response_id=current_response_id or event.response_id,
                        output_index=event.output_index,
                        call_id=item.call_id,
                        name=item.name,
                        arguments_json=item.arguments,
                    )
                    yield from self.process_low_level_event(low_level_event)

                elif item_type == "web_search":
                    low_level_event = _AgentToolCallIssued(
                        type="tool_call_issued",
                        response_id=current_response_id or event.response_id,
                        output_index=event.output_index,
                        call_id=item.id,
                        name=item.type,
                        arguments_json="{}",
                    )
                    yield from self.process_low_level_event(low_level_event)

                elif item_type == "mcp_call":
                    low_level_event = _AgentToolCallIssued(
                        type="tool_call_issued",
                        response_id=current_response_id or event.response_id,
                        output_index=event.output_index,
                        call_id=item.id,
                        name=item.name,
                        arguments_json=item.arguments,
                    )
                    yield from self.process_low_level_event(low_level_event)

                elif item_type == "mcp_list_tools":
                    low_level_event = _AgentToolCallIssued(
                        type="tool_call_issued",
                        response_id=current_response_id or event.response_id,
                        output_index=event.output_index,
                        call_id=item.id,
                        name=item.type,
                        arguments_json="{}",
                    )
                    yield from self.process_low_level_event(low_level_event)

                elif item_type == "message":
                    # Text message output
                    low_level_event = _AgentTextCompleted(
                        type="text_completed",
                        text=str(item.content) if hasattr(item, "content") else item.text,
                        response_id=current_response_id or event.response_id,
                        output_index=event.output_index,
                    )
                    yield from self.process_low_level_event(low_level_event)

            elif event_type == "response.completed":
                # Capture the response object for later use
                self.last_response = event.response
                low_level_event = _AgentResponseCompleted(type="response_completed", response_id=event.response.id)
                yield from self.process_low_level_event(low_level_event)

            elif event_type == "response.failed":
                low_level_event = _AgentResponseFailed(
                    type="response_failed",
                    response_id=event.response.id,
                    error_message=event.response.error.message
                    if hasattr(event.response, "error") and event.response.error
                    else "Unknown error",
                )
                yield from self.process_low_level_event(low_level_event)

    def finish_turn(self) -> Iterator[AgentEvent]:
        """Emit TurnCompleted event.

        This should be called when the turn is complete (no more function
        calls to execute).

        Yields:
            TurnCompleted event
        """
        if not self.last_response:
            raise RuntimeError("Cannot finish turn without a response")

        yield TurnCompleted(
            turn_id=self.turn_id,
            session_id=self.session_id,
            final_text=self.last_response.output_text,
            response_ids=self.all_response_ids,
            num_steps=self.step_counter,
        )
