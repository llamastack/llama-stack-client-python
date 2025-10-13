# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

"""Event synthesizer that translates response stream events to turn/step events.

This module provides the TurnEventSynthesizer class which maintains state
and translates low-level response stream events into high-level turn and
step events that provide semantic meaning to agent interactions.
"""

from typing import Iterator, Optional, Dict, List, Any

from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types import ResponseObject

from .stream_events import (
    AgentStreamEvent,
    AgentResponseStarted,
    AgentTextDelta,
    AgentTextCompleted,
    AgentToolCallIssued,
    AgentToolCallDelta,
    AgentToolCallCompleted,
    AgentResponseCompleted,
    AgentResponseFailed,
)
from .turn_events import (
    AgentEvent,
    TurnStarted,
    TurnCompleted,
    StepStarted,
    StepProgress,
    StepCompleted,
    TextDelta,
    ToolCallIssuedDelta,
    ToolCallDelta,
    ToolCallCompletedDelta,
    InferenceStepResult,
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

    The synthesizer emits high-level events that client code can easily
    consume without needing to understand the underlying response API details.
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

        # Separate tracking for client vs server tool calls
        self.function_calls_building: Dict[str, ToolCall] = {}  # Client-side
        self.server_tool_executions: List[Dict[str, Any]] = []  # Server-side

        # Turn-level accumulation
        self.all_response_ids: List[str] = []
        self.turn_started = False

    def process_low_level_event(self, event: AgentStreamEvent) -> Iterator[AgentEvent]:
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

        if isinstance(event, AgentResponseStarted):
            # Start new inference step
            self.current_step_id = f"{self.turn_id}_step_{self.step_counter}"
            self.step_counter += 1
            self.current_response_id = event.response_id
            self.all_response_ids.append(event.response_id)
            self.text_parts = []
            self.function_calls_building = {}
            self.server_tool_executions = []

            yield StepStarted(step_id=self.current_step_id, step_type="inference", turn_id=self.turn_id)

        elif isinstance(event, AgentTextDelta):
            # Accumulate text and emit progress
            self.text_parts.append(event.text)
            yield StepProgress(
                step_id=self.current_step_id or "",
                step_type="inference",
                turn_id=self.turn_id,
                delta=TextDelta(text=event.text),
            )

        elif isinstance(event, AgentTextCompleted):
            # Text completion - just update our accumulated text
            # (we already have it from deltas, but this ensures we have the complete text)
            pass

        elif isinstance(event, AgentToolCallIssued):
            # Determine if server-side or client-side
            tool_type = self._classify_tool_type(event.name)

            if tool_type == "function":
                # Client-side: accumulate for later execution
                self.function_calls_building[event.call_id] = ToolCall(
                    call_id=event.call_id, tool_name=event.name, arguments=event.arguments_json or ""
                )
            else:
                # Server-side: track for logging
                self.server_tool_executions.append(
                    {
                        "call_id": event.call_id,
                        "tool_type": tool_type,
                        "tool_name": event.name,
                        "arguments": event.arguments_json or "{}",
                        "result": None,  # Will be populated later
                    }
                )

            yield StepProgress(
                step_id=self.current_step_id or "",
                step_type="inference",
                turn_id=self.turn_id,
                delta=ToolCallIssuedDelta(
                    call_id=event.call_id,
                    tool_type=tool_type,  # type: ignore
                    tool_name=event.name,
                    arguments=event.arguments_json or "{}",
                ),
            )

        elif isinstance(event, AgentToolCallDelta):
            # Update arguments (for both client and server-side)
            if event.call_id in self.function_calls_building:
                current = self.function_calls_building[event.call_id].arguments
                self.function_calls_building[event.call_id].arguments = current + (event.arguments_delta or "")

            # Update server tool executions
            for exec_info in self.server_tool_executions:
                if exec_info["call_id"] == event.call_id:
                    exec_info["arguments"] = exec_info["arguments"] + (event.arguments_delta or "")
                    break

            yield StepProgress(
                step_id=self.current_step_id or "",
                step_type="inference",
                turn_id=self.turn_id,
                delta=ToolCallDelta(call_id=event.call_id, arguments_delta=event.arguments_delta or ""),
            )

        elif isinstance(event, AgentToolCallCompleted):
            # Update final arguments
            if event.call_id in self.function_calls_building:
                self.function_calls_building[event.call_id].arguments = event.arguments_json or ""

            # Check if this is a server-side tool
            server_exec = next((e for e in self.server_tool_executions if e["call_id"] == event.call_id), None)
            if server_exec:
                server_exec["arguments"] = event.arguments_json or ""
                # Emit completed delta (result will be populated later from ResponseObject)
                yield StepProgress(
                    step_id=self.current_step_id or "",
                    step_type="inference",
                    turn_id=self.turn_id,
                    delta=ToolCallCompletedDelta(
                        call_id=event.call_id,
                        tool_type=server_exec["tool_type"],  # type: ignore
                        tool_name=server_exec["tool_name"],
                        result=None,  # Will be enriched from ResponseObject
                    ),
                )

        elif isinstance(event, AgentResponseCompleted):
            # Inference step completes
            yield StepCompleted(
                step_id=self.current_step_id or "",
                step_type="inference",
                turn_id=self.turn_id,
                result=InferenceStepResult(
                    step_id=self.current_step_id or "",
                    response_id=event.response_id,
                    text_content="".join(self.text_parts),
                    function_calls=list(self.function_calls_building.values()),
                    server_tool_executions=self.server_tool_executions.copy(),
                    stop_reason="tool_calls" if self.function_calls_building else "end_of_turn",
                ),
            )

        elif isinstance(event, AgentResponseFailed):
            # Don't yield here, let agent.py handle it by checking the event type
            pass

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
            "web_search",
            "query_from_memory",
            "mcp_call",
            "mcp_list_tools",
        }

        if tool_name in server_side_tools:
            return tool_name

        # Default to function for client-side tools
        return "function"

    def enrich_with_response(self, response: ResponseObject) -> None:
        """Enrich server tool executions with results from ResponseObject.

        After a response completes, we can extract the actual results of
        server-side tool executions from the response.output field and
        attach them to our tracked server_tool_executions.

        Args:
            response: Completed response object
        """
        # Extract file_search, web_search, etc. results from response.output
        for item in response.output:
            item_type = getattr(item, "type", None)
            if item_type in ("file_search_call", "web_search_call", "mcp_call"):
                # Find matching execution and add result
                tool_type_key = item_type.replace("_call", "")
                for exec_info in self.server_tool_executions:
                    if exec_info["tool_type"] == tool_type_key:
                        # Store entire output item for maximum information
                        exec_info["result"] = item
                        break

    def finish_turn(self, final_response: ResponseObject) -> Iterator[AgentEvent]:
        """Emit TurnCompleted event.

        This should be called when the turn is complete (no more function
        calls to execute).

        Args:
            final_response: The final response object for this turn

        Yields:
            TurnCompleted event
        """
        yield TurnCompleted(
            turn_id=self.turn_id,
            session_id=self.session_id,
            final_text=final_response.output_text,
            response_ids=self.all_response_ids,
            num_steps=self.step_counter,
        )
