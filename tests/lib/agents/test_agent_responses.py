from types import SimpleNamespace
from typing import Any, Dict, List, Iterable, Optional

import pytest

from llama_stack_client.lib.agents.agent import Agent
from llama_stack_client.lib.agents.client_tool import client_tool
from llama_stack_client.lib.agents.stream_events import (
    AgentStreamEvent,
    AgentToolCallDelta,
    AgentToolCallIssued,
    AgentResponseStarted,
    AgentResponseCompleted,
    AgentToolCallCompleted,
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
    def __init__(
        self,
        event_registry: Dict[object, Iterable[AgentStreamEvent]],
        responses: Dict[str, FakeResponse],
        event_script: Optional[List[List[AgentStreamEvent]]] = None,
    ) -> None:
        self._event_registry = event_registry
        self._responses = responses
        self.create_calls: List[Dict[str, object]] = []
        self._event_script = list(event_script or [])

    def create(self, *, previous_response_id: Optional[str] = None, **kwargs: object) -> object:
        stream = object()
        record: Dict[str, object] = {"previous_response_id": previous_response_id}
        record.update(kwargs)
        self.create_calls.append(record)

        if self._event_script:
            self._event_registry[stream] = self._event_script.pop(0)
        elif previous_response_id is None:
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

def test_agent_tracks_multiple_sessions(monkeypatch: pytest.MonkeyPatch) -> None:
    event_registry: Dict[object, Iterable[AgentStreamEvent]] = {}
    responses = {
        "resp_a1": FakeResponse("resp_a1", "turn_a1"),
        "resp_a2": FakeResponse("resp_a2", "turn_a2"),
        "resp_b1": FakeResponse("resp_b1", "turn_b1"),
    }
    scripted_events = [
        [AgentResponseCompleted(type="response_completed", response_id="resp_a1")],
        [AgentResponseCompleted(type="response_completed", response_id="resp_b1")],
        [AgentResponseCompleted(type="response_completed", response_id="resp_a2")],
    ]
    client = FakeClient(event_registry, responses, event_script=scripted_events)  # type: ignore[arg-type]

    def fake_iter_agent_events(stream: object) -> Iterable[AgentStreamEvent]:
        return event_registry[stream]

    monkeypatch.setattr("llama_stack_client.lib.agents.agent.iter_agent_events", fake_iter_agent_events)

    agent = Agent(
        client=client,  # type: ignore[arg-type]
        model="test-model",
        instructions="test",
    )

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
    assert calls[0]["previous_response_id"] is None
    assert calls[1]["conversation"] == session_b
    assert calls[1]["previous_response_id"] is None
    assert calls[2]["conversation"] == session_a
    assert calls[2]["previous_response_id"] == "resp_a1"
    assert agent._session_last_response_id[session_a] == "resp_a2"
    assert agent._session_last_response_id[session_b] == "resp_b1"


def test_agent_streams_server_and_client_tools(monkeypatch: pytest.MonkeyPatch) -> None:
    event_registry: Dict[object, Iterable[AgentStreamEvent]] = {}
    responses = {
        "resp_final": FakeResponse("resp_final", "turn_final"),
    }
    event_script = [
        [
            AgentResponseStarted(type="response_started", response_id="resp_0"),
            AgentToolCallIssued(
                type="tool_call_issued",
                response_id="resp_0",
                output_index=0,
                call_id="server_call",
                name="server_tool",
                arguments_json="",
            ),
            AgentToolCallDelta(
                type="tool_call_delta",
                response_id="resp_0",
                output_index=0,
                call_id="server_call",
                arguments_delta='{"value": ',
            ),
            AgentToolCallDelta(
                type="tool_call_delta",
                response_id="resp_0",
                output_index=0,
                call_id="server_call",
                arguments_delta='1}',
            ),
            AgentToolCallCompleted(
                type="tool_call_completed",
                response_id="resp_0",
                output_index=0,
                call_id="server_call",
                arguments_json='{"value": 1}',
            ),
        ],
        [
            AgentToolCallIssued(
                type="tool_call_issued",
                response_id="resp_1",
                output_index=0,
                call_id="client_call",
                name="echo_tool",
                arguments_json='{"text": "pong"}',
            ),
            AgentToolCallCompleted(
                type="tool_call_completed",
                response_id="resp_1",
                output_index=0,
                call_id="client_call",
                arguments_json='{"text": "pong"}',
            ),
        ],
        [
            AgentResponseCompleted(type="response_completed", response_id="resp_final"),
        ],
    ]
    client = FakeClient(event_registry, responses, event_script=event_script)  # type: ignore[arg-type]

    def fake_iter_agent_events(stream: object) -> Iterable[AgentStreamEvent]:
        return event_registry[stream]

    monkeypatch.setattr("llama_stack_client.lib.agents.agent.iter_agent_events", fake_iter_agent_events)

    server_calls: List[Dict[str, Any]] = []

    def fake_invoke_tool(*, tool_name: str, kwargs: Dict[str, Any], extra_headers: object | None = None) -> SimpleNamespace:
        _ = extra_headers
        server_calls.append({"tool_name": tool_name, "kwargs": kwargs})
        return SimpleNamespace(content={"result": "ok"})

    client.tool_runtime.invoke_tool = fake_invoke_tool  # type: ignore[assignment]

    agent = Agent(
        client=client,  # type: ignore[arg-type]
        model="test-model",
        instructions="use tools",
        tools=[echo_tool],
    )
    agent.builtin_tools["server_tool"] = {}

    session_id = agent.create_session("default")
    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "run tools"}],
        }
    ]

    chunks = list(agent.create_turn(messages, session_id=session_id, stream=True))

    assert any(isinstance(chunk.event, AgentResponseCompleted) for chunk in chunks)
    assert server_calls == [{"tool_name": "server_tool", "kwargs": {"value": 1}}]
    assert any(call["previous_response_id"] == "resp_0" for call in client.responses.create_calls if call.get("conversation"))

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
    def __init__(
        self,
        event_registry: Dict[object, Iterable[AgentStreamEvent]],
        responses: Dict[str, FakeResponse],
        event_script: Optional[List[List[AgentStreamEvent]]] = None,
    ) -> None:
        self.responses = FakeResponsesAPI(event_registry, responses, event_script=event_script)
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

    session_id = agent.create_session("default")
    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "hi"}],
        }
    ]

    response = agent.create_turn(messages, session_id=session_id, stream=False)

    assert response is fake_response
    assert len(client.responses.create_calls) == 2
    assert agent._last_response_id == fake_response.id
