# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Dict, List, Iterable, Iterator

from llama_stack_client.lib.agents.agent import Agent
from llama_stack_client.lib.agents.client_tool import client_tool
from llama_stack_client.lib.agents.turn_events import (
    StepStarted,
    TurnStarted,
    StepProgress,
    StepCompleted,
    TurnCompleted,
    ToolExecutionStepResult,
)


def _event(event_type: str, **payload: Any) -> SimpleNamespace:
    return SimpleNamespace(type=event_type, **payload)


def _in_progress(response_id: str) -> SimpleNamespace:
    return _event("response.in_progress", response=SimpleNamespace(id=response_id))


def _completed(response_id: str, text: str) -> SimpleNamespace:
    response = FakeResponse(response_id, text)
    return _event("response.completed", response=response)


class FakeResponse:
    def __init__(self, response_id: str, text: str) -> None:
        self.id = response_id
        self.output_text = text
        self.turn = SimpleNamespace(turn_id=f"turn_{response_id}")


class FakeResponsesAPI:
    def __init__(self, event_script: Iterable[Iterable[SimpleNamespace]]) -> None:
        self._event_script: List[List[SimpleNamespace]] = [list(events) for events in event_script]
        self.create_calls: List[Dict[str, Any]] = []

    def create(self, **kwargs: Any) -> Iterator[SimpleNamespace]:
        self.create_calls.append(kwargs)
        if not self._event_script:
            raise AssertionError("No scripted events left for responses.create")
        return iter(self._event_script.pop(0))


class FakeConversationsAPI:
    def __init__(self) -> None:
        self._counter = 0

    def create(self, **_: Any) -> SimpleNamespace:
        self._counter += 1
        return SimpleNamespace(id=f"conv_{self._counter}")


class FakeClient:
    def __init__(self, event_script: Iterable[Iterable[SimpleNamespace]]) -> None:
        self.responses = FakeResponsesAPI(event_script)
        self.conversations = FakeConversationsAPI()


def make_completion_events(response_id: str, text: str) -> List[SimpleNamespace]:
    return [
        _in_progress(response_id),
        _event("response.output_text.delta", delta=text, output_index=0),
        _completed(response_id, text),
    ]


def make_function_tool_events(response_id: str, call_id: str, tool_name: str, arguments: str) -> List[SimpleNamespace]:
    tool_item = SimpleNamespace(type="function_call", call_id=call_id, name=tool_name, arguments=arguments)
    return [
        _in_progress(response_id),
        _event("response.output_item.added", item=tool_item),
        _event("response.output_item.done", item=tool_item),
        _completed(response_id, ""),
    ]


def make_server_tool_events(response_id: str, call_id: str, arguments: str, final_text: str) -> List[SimpleNamespace]:
    tool_item = SimpleNamespace(type="file_search_call", id=call_id, arguments=arguments)
    completion = FakeResponse(response_id, final_text)
    return [
        _in_progress(response_id),
        _event("response.output_item.added", item=tool_item),
        _event("response.output_item.done", item=tool_item),
        _event("response.output_text.delta", delta=final_text, output_index=0),
        _completed(response_id, final_text),
    ]


def test_agent_tracks_multiple_sessions() -> None:
    event_script = [
        make_completion_events("resp_a1", "session A turn 1"),
        make_completion_events("resp_b1", "session B turn 1"),
        make_completion_events("resp_a2", "session A turn 2"),
    ]

    client = FakeClient(event_script)
    agent = Agent(client=client, model="test-model", instructions="test")

    session_a = agent.create_session("A")
    session_b = agent.create_session("B")

    message = {
        "type": "message",
        "role": "user",
        "content": [{"type": "input_text", "text": "hi"}],
    }

    agent.create_turn([message], session_id=session_a, stream=False)
    agent.create_turn([message], session_id=session_b, stream=False)
    agent.create_turn([message], session_id=session_a, stream=False)

    calls = client.responses.create_calls
    assert calls[0]["conversation"] == session_a
    assert calls[1]["conversation"] == session_b
    assert calls[2]["conversation"] == session_a

    assert agent._session_last_response_id[session_a] == "resp_a2"
    assert agent._session_last_response_id[session_b] == "resp_b1"
    assert agent._last_response_id == "resp_a2"


def test_agent_handles_client_tool_and_finishes_turn() -> None:
    tool_invocations: List[str] = []

    @client_tool
    def echo_tool(text: str) -> str:
        """Echo text back to the caller.

        :param text: value to echo
        """
        tool_invocations.append(text)
        return text

    event_script = [
        make_function_tool_events("resp_intermediate", "call_1", "echo_tool", '{"text": "pong"}'),
        make_completion_events("resp_final", "all done"),
    ]

    client = FakeClient(event_script)
    agent = Agent(client=client, model="test-model", instructions="use tools", tools=[echo_tool])

    session_id = agent.create_session("default")
    message = {
        "type": "message",
        "role": "user",
        "content": [{"type": "input_text", "text": "run the tool"}],
    }

    response = agent.create_turn([message], session_id=session_id, stream=False)

    assert response.id == "resp_final"
    assert response.output_text == "all done"
    assert tool_invocations == ["pong"]
    assert len(client.responses.create_calls) == 2


def test_agent_streams_server_tool_events() -> None:
    event_script = [
        make_server_tool_events("resp_server", "server_call", '{"query": "docs"}', "tool finished"),
    ]

    client = FakeClient(event_script)
    agent = Agent(client=client, model="test-model", instructions="use server tool")

    session_id = agent.create_session("default")
    message = {
        "type": "message",
        "role": "user",
        "content": [{"type": "input_text", "text": "find info"}],
    }

    chunks = list(agent.create_turn([message], session_id=session_id, stream=True))

    events = [chunk.event for chunk in chunks]
    assert isinstance(events[0], TurnStarted)
    assert isinstance(events[1], StepStarted)
    assert events[1].step_type == "inference"

    # Look for the tool execution step in the stream
    tool_step_started = next(
        event for event in events if isinstance(event, StepStarted) and event.step_type == "tool_execution"
    )
    assert tool_step_started.metadata == {
        "server_side": True,
        "tool_type": "file_search",
        "tool_name": "file_search_call",
    }

    tool_step_completed = next(
        event for event in events if isinstance(event, StepCompleted) and event.step_type == "tool_execution"
    )
    assert isinstance(tool_step_completed.result, ToolExecutionStepResult)
    assert tool_step_completed.result.tool_calls[0].call_id == "server_call"

    text_progress = [
        event.delta.text for event in events if isinstance(event, StepProgress) and hasattr(event.delta, "text")
    ]
    assert text_progress == ["tool finished"]

    assert isinstance(events[-1], TurnCompleted)
    assert chunks[-1].response and chunks[-1].response.output_text == "tool finished"
