# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import io
import os
import time
from uuid import uuid4

import pytest

from llama_stack_client import BadRequestError, AgentEventLogger
from llama_stack_client.types import ResponseObject, response_create_params
from llama_stack_client.lib.agents.agent import Agent

MODEL_ID = os.environ.get("LLAMA_STACK_TEST_MODEL")
BASE_URL = os.environ.get("TEST_API_BASE_URL")
KNOWLEDGE_SNIPPET = "SKYRIM-DRAGON-ALLOY"
_VECTOR_STORE_READY_TIMEOUT = 60.0
_VECTOR_STORE_POLL_INTERVAL = 0.5


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


def _create_vector_store_with_document(client) -> str:
    file_payload = io.BytesIO(
        f"The secret project codename is {KNOWLEDGE_SNIPPET}. Preserve the hyphens exactly.".encode("utf-8")
    )
    uploaded_file = client.files.create(
        file=("agent_e2e_notes.txt", file_payload, "text/plain"),
        purpose="assistants",
    )

    vector_store = client.vector_stores.create(name=f"agent-e2e-{uuid4().hex[:8]}")
    vector_store_file = client.vector_stores.files.create(
        vector_store_id=vector_store.id,
        file_id=uploaded_file.id,
    )

    deadline = time.time() + _VECTOR_STORE_READY_TIMEOUT
    while vector_store_file.status != "completed":
        if vector_store_file.status in {"failed", "cancelled"}:
            raise RuntimeError(f"Vector store ingestion did not succeed: {vector_store_file.status}")
        if time.time() > deadline:
            raise TimeoutError("Vector store file ingest timed out")
        time.sleep(_VECTOR_STORE_POLL_INTERVAL)
        vector_store_file = client.vector_stores.files.retrieve(
            vector_store_id=vector_store.id,
            file_id=vector_store_file.id,
        )

    return vector_store.id


pytestmark = pytest.mark.skipif(
    MODEL_ID is None or BASE_URL in (None, "http://127.0.0.1:4010"),
    reason="requires a running llama stack server, TEST_API_BASE_URL, and LLAMA_STACK_TEST_MODEL",
)


def test_agent_streaming_and_follow_up_turn(client) -> None:
    _wrap_response_retrieval(client)
    vector_store_id = _create_vector_store_with_document(client)

    agent = Agent(
        client=client,
        model=MODEL_ID,
        instructions="You can search the uploaded vector store to answer with precise facts.",
        tools=[{"type": "file_search", "vector_store_ids": [vector_store_id]}],
    )

    session_id = agent.create_session(f"agent-session-{uuid4().hex[:8]}")

    messages: list[response_create_params.InputUnionMember1] = [
        {
            "type": "message",
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Retrieve the secret project codename from the knowledge base and reply as 'codename: <value>'.",
                }
            ],
        }
    ]

    event_logger = AgentEventLogger()
    stream_chunks = []

    for chunk in agent.create_turn(messages=messages, session_id=session_id, stream=True):
        stream_chunks.append(chunk)
        # Drain the event logger for streaming responses (no-op assertions but ensures coverage).
        for printable in event_logger.log([chunk]):
            _ = printable

    completed_chunks = [chunk for chunk in stream_chunks if chunk.response is not None]
    assert completed_chunks, "Expected streaming turn to yield a final response chunk"

    streamed_response = completed_chunks[-1].response
    assert isinstance(streamed_response, ResponseObject)
    first_response_id = streamed_response.id

    assert streamed_response.model == MODEL_ID
    assert agent._last_response_id == first_response_id
    assert agent._session_last_response_id.get(session_id) == first_response_id
    assert streamed_response.output, "Response output should include tool and message items"

    tool_call_outputs = [item for item in streamed_response.output if getattr(item, "type", None) == "file_search_call"]
    assert tool_call_outputs, "Expected a file_search tool call in the response output"
    assert any(
        KNOWLEDGE_SNIPPET in getattr(result, "text", "")
        for output in tool_call_outputs
        for result in getattr(output, "results", []) or []
    ), "Vector store results should surface the knowledge snippet"

    assert KNOWLEDGE_SNIPPET in streamed_response.output_text, "Assistant reply should incorporate retrieved snippet"

    follow_up_messages: list[response_create_params.InputUnionMember1] = [
        {
            "type": "message",
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Briefly explain why that codename matters.",
                }
            ],
        }
    ]

    follow_up_response = agent.create_turn(
        messages=follow_up_messages,
        session_id=session_id,
        stream=False,
    )

    assert isinstance(follow_up_response, ResponseObject)
    assert follow_up_response.previous_response_id == first_response_id
    assert agent._last_response_id == follow_up_response.id
    assert KNOWLEDGE_SNIPPET in follow_up_response.output_text
