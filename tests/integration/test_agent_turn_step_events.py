# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

"""Integration tests for agent turn/step event model.

These tests verify the core architecture of the turn/step event system:
1. Turn = complete interaction loop
2. Inference steps = model thinking/deciding
3. Tool execution steps = ANY tool executing (server OR client-side)

Key architectural validations:
- Server-side tools (file_search, web_search) appear as tool_execution steps
- Client-side tools (function) appear as tool_execution steps
- Both are properly annotated with metadata
"""

import io
import os
import time
from uuid import uuid4

import pytest
from openai import OpenAI

from llama_stack_client.lib.agents.agent import Agent
from llama_stack_client.lib.agents.turn_events import (
    TextDelta,
    StepStarted,
    TurnStarted,
    StepProgress,
    StepCompleted,
    TurnCompleted,
    ToolCallIssuedDelta,
)

# Test configuration
MODEL_ID = os.environ.get("LLAMA_STACK_TEST_MODEL", "openai/gpt-4o")
BASE_URL = os.environ.get("TEST_API_BASE_URL", "http://localhost:8321/v1")


pytestmark = pytest.mark.skipif(
    not BASE_URL or BASE_URL == "http://127.0.0.1:4010",
    reason="requires a running llama stack server",
)


@pytest.fixture
def openai_client():
    return OpenAI(api_key="fake", base_url=BASE_URL)


@pytest.fixture
def agent_with_no_tools(openai_client):
    """Create an agent with no tools for basic text-only tests."""
    return Agent(
        client=openai_client,
        model=MODEL_ID,
        instructions="You are a helpful assistant. Keep responses brief and concise.",
        tools=None,
    )


@pytest.fixture
def agent_with_file_search(openai_client):
    """Create an agent with file_search tool (server-side)."""
    # Create a vector store with test content (unique info to force tool use)
    file_content = "Project Nightingale is a classified initiative. The project codename is BLUE_FALCON_7. The lead researcher is Dr. Elena Vasquez."
    file_payload = io.BytesIO(file_content.encode("utf-8"))

    uploaded_file = openai_client.files.create(
        file=("test_knowledge.txt", file_payload, "text/plain"),
        purpose="assistants",
    )

    vector_store = openai_client.vector_stores.create(
        name=f"test-vs-{uuid4().hex[:8]}",
        extra_body={
            "provider_id": "faiss",
            "embedding_model": "nomic-ai/nomic-embed-text-v1.5",
        },
    )
    vector_store_file = openai_client.vector_stores.files.create(
        vector_store_id=vector_store.id,
        file_id=uploaded_file.id,
    )

    # Wait for vector store to be ready
    deadline = time.time() + 60.0
    while vector_store_file.status != "completed":
        if vector_store_file.status in {"failed", "cancelled"}:
            raise RuntimeError(f"Vector store ingestion failed: {vector_store_file.status}")
        if time.time() > deadline:
            raise TimeoutError("Vector store file ingest timed out")
        time.sleep(0.5)
        vector_store_file = openai_client.vector_stores.files.retrieve(
            vector_store_id=vector_store.id,
            file_id=vector_store_file.id,
        )

    return Agent(
        client=openai_client,
        model=MODEL_ID,
        instructions="You MUST search the knowledge base to answer every question. Never answer from your own knowledge.",
        tools=[{"type": "file_search", "vector_store_ids": [vector_store.id]}],
    )


def test_basic_turn_without_tools(agent_with_no_tools):
    # Expected event sequence:
    # 1. TurnStarted
    # 2. StepStarted(inference)
    # 3. StepProgress(TextDelta) x N
    # 4. StepCompleted(inference)
    # 5. TurnCompleted
    agent = agent_with_no_tools
    session_id = agent.create_session(f"test-session-{uuid4().hex[:8]}")

    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "Say hello in exactly 3 words."}],
        }
    ]

    events = []
    for chunk in agent.create_turn(messages=messages, session_id=session_id, stream=True):
        events.append(chunk.event)

    # Verify event sequence
    assert len(events) > 0, "Should have at least some events"

    # First event should be TurnStarted
    assert isinstance(events[0], TurnStarted), f"First event should be TurnStarted, got {type(events[0])}"
    assert events[0].session_id == session_id

    # Second event should be StepStarted(inference)
    assert isinstance(events[1], StepStarted), f"Second event should be StepStarted, got {type(events[1])}"
    assert events[1].step_type == "inference"
    assert events[1].metadata is None or events[1].metadata.get("server_side") is None

    # Should have some StepProgress(TextDelta) events
    text_deltas = [e for e in events if isinstance(e, StepProgress) and isinstance(e.delta, TextDelta)]
    assert len(text_deltas) > 0, "Should have at least one text delta"

    # Should have NO tool_execution steps (no tools configured)
    tool_execution_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "tool_execution"]
    assert len(tool_execution_starts) == 0, "Should have no tool_execution steps without tools"

    # Second-to-last event should be StepCompleted(inference)
    inference_completes = [e for e in events if isinstance(e, StepCompleted) and e.step_type == "inference"]
    assert len(inference_completes) >= 1, "Should have at least one inference step completion"

    # Last inference completion should have no function calls
    last_inference = inference_completes[-1]
    assert len(last_inference.result.function_calls) == 0, "Should have no function calls"
    assert last_inference.result.stop_reason == "end_of_turn"

    # Last event should be TurnCompleted
    assert isinstance(events[-1], TurnCompleted), f"Last event should be TurnCompleted, got {type(events[-1])}"
    assert events[-1].session_id == session_id
    assert len(events[-1].final_text) > 0, "Should have some final text"


def test_server_side_file_search_tool(agent_with_file_search):
    # Expected event sequence:
    # 1. TurnStarted
    # 2. StepStarted(inference) - model decides to search
    # 3. StepProgress(TextDelta) - optional text before tool
    # 4. StepCompleted(inference) - inference done, decided to use file_search
    # 5. StepStarted(tool_execution, metadata.server_side=True)
    # 6. StepCompleted(tool_execution) - file_search results
    # 7. StepStarted(inference) - model processes results
    # 8. StepProgress(TextDelta) - model generates response
    # 9. StepCompleted(inference)
    # 10. TurnCompleted
    agent = agent_with_file_search
    session_id = agent.create_session(f"test-session-{uuid4().hex[:8]}")

    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "What is the codename for Project Nightingale?"}],
        }
    ]

    events = []
    for chunk in agent.create_turn(messages=messages, session_id=session_id, stream=True):
        events.append(chunk.event)

    # Verify Turn started and completed
    assert isinstance(events[0], TurnStarted)
    assert isinstance(events[-1], TurnCompleted)

    # KEY ASSERTION: Should have at least one tool_execution step (server-side file_search)
    tool_execution_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "tool_execution"]
    assert len(tool_execution_starts) >= 1, (
        f"Should have at least one tool_execution step, found {len(tool_execution_starts)}"
    )

    # KEY ASSERTION: The tool_execution step should be marked as server_side
    file_search_step = tool_execution_starts[0]
    assert file_search_step.metadata is not None, "Tool execution step should have metadata"
    assert file_search_step.metadata.get("server_side") is True, "file_search should be marked as server_side"
    assert file_search_step.metadata.get("tool_type") == "file_search", "Should identify as file_search tool"

    # Should have tool_execution completion
    tool_execution_completes = [e for e in events if isinstance(e, StepCompleted) and e.step_type == "tool_execution"]
    assert len(tool_execution_completes) >= 1, "Should have at least one tool_execution completion"

    # Should have multiple inference steps (before and after tool execution)
    inference_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "inference"]
    assert len(inference_starts) >= 2, (
        f"Should have at least 2 inference steps (before/after tool), found {len(inference_starts)}"
    )

    # Final response should contain the answer (BLUE_FALCON_7)
    assert "BLUE_FALCON" in events[-1].final_text or "BLUE_FALCON_7" in events[-1].final_text, (
        "Response should contain the codename"
    )


def test_client_side_function_tool(openai_client):
    # We are going to test
    # Expected event sequence:
    # 1. TurnStarted
    # 2. StepStarted(inference)
    # 3. StepProgress(ToolCallIssuedDelta) - function call
    # 4. StepCompleted(inference) - with function_calls
    # 5. StepStarted(tool_execution, metadata.server_side=False)
    # 6. StepCompleted(tool_execution) - client executed function
    # 7. StepStarted(inference) - model processes results
    # 8. StepProgress(TextDelta)
    # 9. StepCompleted(inference)
    # 10. TurnCompleted

    # Create a function that returns data requiring model processing
    def get_user_secret_token(user_id: str) -> str:
        """Get the encrypted authentication token for a user from the secure database.

        The token is returned in encrypted hex format and must be decoded by the AI.

        :param user_id: The unique identifier of the user
        """
        import time
        import hashlib

        unique = f"{user_id}-{time.time()}-SECRET"
        token_hash = hashlib.sha256(unique.encode()).hexdigest()[:16]
        return f'{{"status": "success", "encrypted_token": "{token_hash}", "format": "hex", "expires_in_hours": 24}}'

    agent = Agent(
        client=openai_client,
        model=MODEL_ID,
        instructions="You are a helpful assistant. When retrieving tokens, you MUST call get_user_secret_token, then parse the JSON response and present it in a user-friendly format. Explain what the token is and when it expires.",
        tools=[get_user_secret_token],
    )

    session_id = agent.create_session(f"test-session-{uuid4().hex[:8]}")
    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Can you get me the authentication token for user_12345? Please explain what it is.",
                }
            ],
        }
    ]

    events = []

    for chunk in agent.create_turn(messages=messages, session_id=session_id, stream=True):
        events.append(chunk.event)

    # Verify Turn started and completed
    assert isinstance(events[0], TurnStarted)
    assert isinstance(events[-1], TurnCompleted)

    # Should have ToolCallIssuedDelta for the function call
    function_calls = [
        e
        for e in events
        if isinstance(e, StepProgress) and isinstance(e.delta, ToolCallIssuedDelta) and e.delta.tool_type == "function"
    ]
    assert len(function_calls) >= 1, (
        f"Should have at least one function call (get_user_secret_token), found {len(function_calls)}"
    )

    # KEY ASSERTION: Should have tool_execution step (client-side function)
    tool_execution_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "tool_execution"]
    assert len(tool_execution_starts) >= 1, (
        f"Should have at least one tool_execution step, found {len(tool_execution_starts)}"
    )

    # KEY ASSERTION: The tool_execution step should be marked as client-side
    function_step = tool_execution_starts[0]
    assert function_step.metadata is not None, "Tool execution step should have metadata"
    assert function_step.metadata.get("server_side") is False, "Function tool should be marked as client_side"

    # Should have at least one inference step (before tool execution)
    inference_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "inference"]
    assert len(inference_starts) >= 1, f"Should have at least 1 inference step, found {len(inference_starts)}"

    # Verify the tool was actually executed with proper arguments
    tool_execution_completes = [e for e in events if isinstance(e, StepCompleted) and e.step_type == "tool_execution"]
    assert len(tool_execution_completes) >= 1, "Should have at least one tool_execution completion"

    # Final response should contain the token data (proves function was called and processed)
    final_text = events[-1].final_text.lower()
    assert "token" in final_text or "encrypted" in final_text, (
        "Response should contain token information from function call"
    )
    assert "24" in events[-1].final_text or "hour" in final_text or "expire" in final_text, (
        "Response should mention expiration from parsed JSON"
    )


if __name__ == "__main__":
    # Allow running tests directly for development
    pytest.main([__file__, "-v", "-s"])
