import os
import time

import pytest

from llama_stack_client import BadRequestError
from llama_stack_client.types import response_create_params
from llama_stack_client.lib.agents.agent import Agent

MODEL_ID = os.environ.get("LLAMA_STACK_TEST_MODEL")
BASE_URL = os.environ.get("TEST_API_BASE_URL")


def _wrap_response_retrieval(client) -> None:
    original_retrieve = client.responses.retrieve

    def retrying_retrieve(response_id: str, **kwargs):
        attempts = 0
        while True:
            try:
                return original_retrieve(response_id, **kwargs)
            except BadRequestError as exc:
                if getattr(exc, "status_code", None) != 400 or attempts >= 5:
                    raise
                time.sleep(0.2)
                attempts += 1

    client.responses.retrieve = retrying_retrieve  # type: ignore[assignment]


pytestmark = pytest.mark.skipif(
    MODEL_ID is None or BASE_URL in (None, "http://127.0.0.1:4010"),
    reason="requires a running llama stack server and LLAMA_STACK_TEST_MODEL",
)


def test_agent_create_turn_non_streaming(client) -> None:
    _wrap_response_retrieval(client)
    agent = Agent(
        client=client,
        model=MODEL_ID,
        instructions="You are a helpful assistant that responds succinctly.",
    )

    session_id = agent.create_session("default")
    messages: list[response_create_params.InputUnionMember1] = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "Reply with pong."}],
        }
    ]

    response = agent.create_turn(messages, session_id=session_id, stream=False)

    assert response.id.startswith("resp_")
    assert response.model == MODEL_ID
    assert agent._last_response_id == response.id


def test_agent_create_turn_streaming(client) -> None:
    _wrap_response_retrieval(client)
    agent = Agent(
        client=client,
        model=MODEL_ID,
        instructions="You are a helpful assistant that replies in one word.",
    )

    session_id = agent.create_session("default")
    messages: list[response_create_params.InputUnionMember1] = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "Say hello."}],
        }
    ]

    chunks = list(agent.create_turn(messages, session_id=session_id, stream=True))
    assert any(chunk.response for chunk in chunks)
    assert agent._last_response_id is not None
