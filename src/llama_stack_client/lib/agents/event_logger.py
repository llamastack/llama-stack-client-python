# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Any, Iterator, Optional, Tuple

from termcolor import cprint

from llama_stack_client.types import InterleavedContent


def interleaved_content_as_str(content: InterleavedContent, sep: str = " ") -> str:
    def _process(c: Any) -> str:
        if isinstance(c, str):
            return c
        elif hasattr(c, "type"):
            if c.type == "text":
                return c.text
            elif c.type == "image":
                return "<image>"
            else:
                raise ValueError(f"Unexpected type {c}")
        else:
            raise ValueError(f"Unsupported content type: {type(c)}")

    if isinstance(content, list):
        return sep.join(_process(c) for c in content)
    else:
        return _process(content)


class TurnStreamPrintableEvent:
    def __init__(
        self,
        role: Optional[str] = None,
        content: str = "",
        end: Optional[str] = "\n",
        color: str = "white",
    ) -> None:
        self.role = role
        self.content = content
        self.color = color
        self.end = "\n" if end is None else end

    def __str__(self) -> str:
        if self.role is not None:
            return f"{self.role}> {self.content}"
        else:
            return f"{self.content}"

    def print(self, flush: bool = True) -> None:
        cprint(f"{str(self)}", color=self.color, end=self.end, flush=flush)


class TurnStreamEventPrinter:
    def __init__(self) -> None:
        self.previous_event_type: Optional[str] = None
        self.previous_step_type: Optional[str] = None

    def yield_printable_events(self, chunk: Any) -> Iterator[TurnStreamPrintableEvent]:
        for printable_event in self._yield_printable_events(chunk, self.previous_event_type, self.previous_step_type):
            yield printable_event

        if not hasattr(chunk, "error"):
            self.previous_event_type, self.previous_step_type = self._get_event_type_step_type(chunk)

    def _yield_printable_events(
        self, chunk: Any, previous_event_type: Optional[str] = None, previous_step_type: Optional[str] = None
    ) -> Iterator[TurnStreamPrintableEvent]:
        if hasattr(chunk, "error"):
            yield TurnStreamPrintableEvent(role=None, content=chunk.error["message"], color="red")
            return

        event = chunk.event
        event_type = event.payload.event_type

        if event_type in {"turn_start", "turn_complete", "turn_awaiting_input"}:
            # Currently not logging any turn realted info
            yield TurnStreamPrintableEvent(role=None, content="", end="", color="grey")
            return

        step_type = event.payload.step_type
        # handle safety
        if step_type == "shield_call" and event_type == "step_complete":
            violation = event.payload.step_details.violation
            if not violation:
                yield TurnStreamPrintableEvent(role=step_type, content="No Violation", color="magenta")
            else:
                yield TurnStreamPrintableEvent(
                    role=step_type,
                    content=f"{violation.metadata} {violation.user_message}",
                    color="red",
                )

        # handle inference
        if step_type == "inference":
            if event_type == "step_start":
                yield TurnStreamPrintableEvent(role=step_type, content="", end="", color="yellow")
            elif event_type == "step_progress":
                if event.payload.delta.type == "tool_call":
                    if isinstance(event.payload.delta.tool_call, str):
                        yield TurnStreamPrintableEvent(
                            role=None,
                            content=event.payload.delta.tool_call,
                            end="",
                            color="cyan",
                        )
                elif event.payload.delta.type == "text":
                    yield TurnStreamPrintableEvent(
                        role=None,
                        content=event.payload.delta.text,
                        end="",
                        color="yellow",
                    )
            else:
                # step complete
                yield TurnStreamPrintableEvent(role=None, content="")

        # handle tool_execution
        if step_type == "tool_execution" and event_type == "step_complete":
            # Only print tool calls and responses at the step_complete event
            details = event.payload.step_details
            for t in details.tool_calls:
                yield TurnStreamPrintableEvent(
                    role=step_type,
                    content=f"Tool:{t.tool_name} Args:{t.arguments}",
                    color="green",
                )

            for r in details.tool_responses:
                if r.tool_name == "query_from_memory":
                    inserted_context = interleaved_content_as_str(r.content)
                    content = f"fetched {len(inserted_context)} bytes from memory"

                    yield TurnStreamPrintableEvent(
                        role=step_type,
                        content=content,
                        color="cyan",
                    )
                else:
                    yield TurnStreamPrintableEvent(
                        role=step_type,
                        content=f"Tool:{r.tool_name} Response:{r.content}",
                        color="green",
                    )

    def _get_event_type_step_type(self, chunk: Any) -> Tuple[Optional[str], Optional[str]]:
        if hasattr(chunk, "event"):
            previous_event_type = chunk.event.payload.event_type if hasattr(chunk, "event") else None
            previous_step_type = (
                chunk.event.payload.step_type
                if previous_event_type not in {"turn_start", "turn_complete", "turn_awaiting_input"}
                else None
            )
            return previous_event_type, previous_step_type
        return None, None


class EventLogger:
    def log(self, event_generator: Iterator[Any]) -> Iterator[TurnStreamPrintableEvent]:
        printer = TurnStreamEventPrinter()
        for chunk in event_generator:
            yield from printer.yield_printable_events(chunk)
