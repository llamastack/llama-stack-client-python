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

from llama_stack_client import LlamaStackClient, AgentEventLogger
from llama_stack_client.types import response_create_params
from llama_stack_client.lib.agents.agent import Agent
from llama_stack_client.lib.agents.turn_events import (
    TurnStarted,
    TurnCompleted,
    StepStarted,
    StepProgress,
    StepCompleted,
    TextDelta,
    ToolCallIssuedDelta,
)

# Test configuration
MODEL_ID = os.environ.get("LLAMA_STACK_TEST_MODEL", "ollama/llama3.2:3b-instruct-fp16")
BASE_URL = os.environ.get("TEST_API_BASE_URL", "http://localhost:8321")


pytestmark = pytest.mark.skipif(
    not BASE_URL or BASE_URL == "http://127.0.0.1:4010",
    reason="requires a running llama stack server",
)


@pytest.fixture
def client():
    """Create a LlamaStackClient for testing."""
    return LlamaStackClient(base_url=BASE_URL)


@pytest.fixture
def agent_with_no_tools(client):
    """Create an agent with no tools for basic text-only tests."""
    return Agent(
        client=client,
        model=MODEL_ID,
        instructions="You are a helpful assistant. Keep responses brief and concise.",
        tools=None,
    )


@pytest.fixture
def agent_with_file_search(client):
    """Create an agent with file_search tool (server-side)."""
    # Create a vector store with test content
    file_content = "The capital of France is Paris. Paris is known for the Eiffel Tower."
    file_payload = io.BytesIO(file_content.encode("utf-8"))

    uploaded_file = client.files.create(
        file=("test_knowledge.txt", file_payload, "text/plain"),
        purpose="assistants",
    )

    vector_store = client.vector_stores.create(name=f"test-vs-{uuid4().hex[:8]}")
    vector_store_file = client.vector_stores.files.create(
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
        vector_store_file = client.vector_stores.files.retrieve(
            vector_store_id=vector_store.id,
            file_id=vector_store_file.id,
        )

    return Agent(
        client=client,
        model=MODEL_ID,
        instructions="Search the knowledge base to answer questions accurately.",
        tools=[{"type": "file_search", "vector_store_ids": [vector_store.id]}],
    )


def test_basic_turn_without_tools(agent_with_no_tools):
    """Test 1: Basic turn with text-only response (no tools).

    Expected event sequence:
    1. TurnStarted
    2. StepStarted(inference)
    3. StepProgress(TextDelta) x N
    4. StepCompleted(inference)
    5. TurnCompleted
    """
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

    print(f"\n✅ Test 1 passed: Basic turn with {len(events)} events")
    print(f"   - Text deltas: {len(text_deltas)}")
    print(f"   - Final text: {events[-1].final_text}")


def test_server_side_file_search_tool(agent_with_file_search):
    """Test 2: Server-side file_search tool execution.

    THE KEY TEST: Verifies that server-side tools appear as tool_execution steps.

    Expected event sequence:
    1. TurnStarted
    2. StepStarted(inference) - model decides to search
    3. StepProgress(TextDelta) - optional text before tool
    4. StepCompleted(inference) - inference done, decided to use file_search
    5. StepStarted(tool_execution, metadata.server_side=True)
    6. StepCompleted(tool_execution) - file_search results
    7. StepStarted(inference) - model processes results
    8. StepProgress(TextDelta) - model generates response
    9. StepCompleted(inference)
    10. TurnCompleted
    """
    agent = agent_with_file_search
    session_id = agent.create_session(f"test-session-{uuid4().hex[:8]}")

    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "What is the capital of France?"}],
        }
    ]

    events = []
    event_logger = AgentEventLogger()

    print("\n" + "="*80)
    print("Test 2: Server-side file_search tool")
    print("="*80)

    for chunk in agent.create_turn(messages=messages, session_id=session_id, stream=True):
        events.append(chunk.event)
        # Log events for debugging
        for log_msg in event_logger.log([chunk]):
            print(log_msg, end="", flush=True)

    print("\n" + "="*80)

    # Verify Turn started and completed
    assert isinstance(events[0], TurnStarted)
    assert isinstance(events[-1], TurnCompleted)

    # KEY ASSERTION: Should have at least one tool_execution step (server-side file_search)
    tool_execution_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "tool_execution"]
    assert len(tool_execution_starts) >= 1, f"Should have at least one tool_execution step, found {len(tool_execution_starts)}"

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
    assert len(inference_starts) >= 2, f"Should have at least 2 inference steps (before/after tool), found {len(inference_starts)}"

    # Final response should contain the answer (Paris)
    assert "Paris" in events[-1].final_text, "Response should contain 'Paris'"

    print(f"\n✅ Test 2 passed: Server-side file_search with {len(events)} events")
    print(f"   - Tool execution steps: {len(tool_execution_starts)}")
    print(f"   - Inference steps: {len(inference_starts)}")
    print(f"   - Final answer: {events[-1].final_text}")


def test_client_side_function_tool():
    """Test 3: Client-side function tool execution.

    Expected event sequence:
    1. TurnStarted
    2. StepStarted(inference)
    3. StepProgress(ToolCallIssuedDelta) - function call
    4. StepCompleted(inference) - with function_calls
    5. StepStarted(tool_execution, metadata.server_side=False)
    6. StepCompleted(tool_execution) - client executed function
    7. StepStarted(inference) - model processes results
    8. StepProgress(TextDelta)
    9. StepCompleted(inference)
    10. TurnCompleted
    """
    # Create a simple client-side function tool
    def get_weather(location: str) -> str:
        """Get the weather for a location."""
        return f"Sunny and 72°F in {location}"

    client = LlamaStackClient(base_url=BASE_URL)

    agent = Agent(
        client=client,
        model=MODEL_ID,
        instructions="Use the get_weather function to answer weather questions.",
        tools=[get_weather],
    )

    session_id = agent.create_session(f"test-session-{uuid4().hex[:8]}")

    messages = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "What's the weather in Paris?"}],
        }
    ]

    events = []
    event_logger = AgentEventLogger()

    print("\n" + "="*80)
    print("Test 3: Client-side function tool")
    print("="*80)

    for chunk in agent.create_turn(messages=messages, session_id=session_id, stream=True):
        events.append(chunk.event)
        # Log events for debugging
        for log_msg in event_logger.log([chunk]):
            print(log_msg, end="", flush=True)

    print("\n" + "="*80)

    # Verify Turn started and completed
    assert isinstance(events[0], TurnStarted)
    assert isinstance(events[-1], TurnCompleted)

    # Should have ToolCallIssuedDelta for the function call
    function_calls = [
        e for e in events
        if isinstance(e, StepProgress) and isinstance(e.delta, ToolCallIssuedDelta) and e.delta.tool_type == "function"
    ]
    assert len(function_calls) >= 1, "Should have at least one function call"

    # KEY ASSERTION: Should have tool_execution step (client-side function)
    tool_execution_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "tool_execution"]
    assert len(tool_execution_starts) >= 1, f"Should have at least one tool_execution step, found {len(tool_execution_starts)}"

    # KEY ASSERTION: The tool_execution step should be marked as client-side
    function_step = tool_execution_starts[0]
    assert function_step.metadata is not None, "Tool execution step should have metadata"
    assert function_step.metadata.get("server_side") is False, "Function tool should be marked as client_side"

    # Should have multiple inference steps (before and after tool execution)
    inference_starts = [e for e in events if isinstance(e, StepStarted) and e.step_type == "inference"]
    assert len(inference_starts) >= 2, f"Should have at least 2 inference steps (before/after tool), found {len(inference_starts)}"

    # Final response should contain weather info
    assert "72" in events[-1].final_text or "Sunny" in events[-1].final_text, "Response should contain weather info"

    print(f"\n✅ Test 3 passed: Client-side function with {len(events)} events")
    print(f"   - Tool execution steps: {len(tool_execution_starts)}")
    print(f"   - Inference steps: {len(inference_starts)}")
    print(f"   - Final answer: {events[-1].final_text}")


if __name__ == "__main__":
    # Allow running tests directly for development
    pytest.main([__file__, "-v", "-s"])
