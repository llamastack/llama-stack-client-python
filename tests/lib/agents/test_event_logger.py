# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from llama_stack_client.lib.agents.event_logger import AgentEventLogger
from llama_stack_client.lib.agents.turn_events import StepCompleted, ToolExecutionStepResult


def test_agent_event_logger_omits_empty_tool_response_fields() -> None:
    event = StepCompleted(
        step_id="step_empty_fields",
        step_type="tool_execution",
        turn_id="turn_empty_fields",
        result=ToolExecutionStepResult(
            step_id="step_empty_fields",
            tool_calls=[],
            tool_responses=[
                {"tool_name": "no_content_tool", "content": ""},
                {"tool_name": "null_content_tool", "content": None},
                {"tool_name": "valid_content_tool", "content": "abc"},
            ],
        ),
    )

    logger = AgentEventLogger()
    messages = list(logger.log(iter([event])))

    assert messages == [
        "  → no_content_tool\n",
        "  → null_content_tool\n",
        "  → valid_content_tool: abc\n",
    ]

