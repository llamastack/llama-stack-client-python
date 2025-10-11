import os
from types import SimpleNamespace
from typing import Dict, Iterable, List, Optional

import pytest

from llama_stack_client.lib.agents.agent import Agent
from llama_stack_client.lib.agents.client_tool import client_tool
from llama_stack_client.lib.agents.stream_events import (
    AgentResponseCompleted,
    AgentResponseStarted,
    AgentStreamEvent,
    AgentToolCallCompleted,
    AgentToolCallIssued,
)


@client_tool
def echo_tool(text: str) -> str:
    """Echo text back to the caller.

    :param text: phrase to echo
    """
    return text


class FakeResponse:
    def __init__(self, response_id: str, turn_id: str) -> None:
        self.id = response_id
        self.turn = SimpleNamespace(turn_id=turn_id)


class FakeResponsesAPI:
    def __init__(self, event_registry: Dict[object, Iterable[AgentStreamEvent]], responses: Dict[str, FakeResponse]) -> None:
        self._event_registry = event_registry
        self._responses = responses
        self.create_calls: List[Dict[str, Optional[str]]] = []

    def create(self, *, previous_response_id: Optional[str] = None, **_: object) -> object:
        stream = object()
        self.create_calls.append({"previous_response_id": previous_response_id})
        if previous_response_id is None:
            self._event_registry[stream] = [
                AgentResponseStarted(type="response_started", response_id="resp_0"),
                AgentToolCallIssued(
                    type="tool_call_issued",
                    response_id="resp_0",
                    output_index=0,
                    call_id="call_1",
                    name="echo_tool",
                    arguments_json='{"text": "hi"}',
                ),
                AgentToolCallCompleted(
                    type="tool_call_completed",
                    response_id="resp_0",
                    output_index=0,
                    call_id="call_1",
                    arguments_json='{"text": "hi"}',
                ),
            ]
        else:
            self._event_registry[stream] = [
                AgentResponseCompleted(type="response_completed", response_id="resp_1"),
            ]
        return stream

    def retrieve(self, response_id: str, **_: object) -> FakeResponse:
        return self._responses[response_id]


class FakeConversationsAPI:
    def __init__(self) -> None:
        self._counter = 0

    def create(self, **_: object) -> SimpleNamespace:
        self._counter += 1
        return SimpleNamespace(id=f"conv_{self._counter}")


class FakeToolsAPI:
    def list(self, **_: object) -> List[SimpleNamespace]:
        return []


class FakeToolRuntimeAPI:
    def invoke_tool(self, **_: object) -> None:  # pragma: no cover - not exercised here
        raise AssertionError("Should not reach builtin tool execution in this test")


class FakeClient:
    def __init__(self, event_registry: Dict[object, Iterable[AgentStreamEvent]], responses: Dict[str, FakeResponse]) -> None:
        self.responses = FakeResponsesAPI(event_registry, responses)
        self.conversations = FakeConversationsAPI()
        self.tools = FakeToolsAPI()
        self.tool_runtime = FakeToolRuntimeAPI()


@pytest.fixture
def event_registry() -> Dict[object, Iterable[AgentStreamEvent]]:
    return {}


@pytest.fixture
def fake_response() -> FakeResponse:
    return FakeResponse("resp_1", "turn_123")


def test_agent_handles_client_tool_and_finishes_turn(monkeypatch: pytest.MonkeyPatch, event_registry: Dict[object, Iterable[AgentStreamEvent]], fake_response: FakeResponse) -> None:
    client = FakeClient(event_registry, {fake_response.id: fake_response})

    def fake_iter_agent_events(stream: object) -> Iterable[AgentStreamEvent]:
        try:
            events = event_registry[stream]
        except KeyError as exc:  # pragma: no cover - makes debugging simpler if misused
            raise AssertionError("unknown stream") from exc
        for event in events:
            yield event

    monkeypatch.setattr("llama_stack_client.lib.agents.agent.iter_agent_events", fake_iter_agent_events)

    agent = Agent(
        client=client,  # type: ignore[arg-type]
        model="test-model",
        instructions="use the echo_tool",
        tools=[echo_tool],
    )

    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "hi"}],
        }
    ]

    response = agent.create_turn(messages, stream=False)

    assert response is fake_response
    assert len(client.responses.create_calls) == 2
    assert agent._last_response_id == fake_response.id
