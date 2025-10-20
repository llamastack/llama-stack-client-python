# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .tool_response import ToolResponse
from ..shared.tool_call import ToolCall

__all__ = ["ToolExecutionStep"]


class ToolExecutionStep(BaseModel):
    step_id: str
    """The ID of the step."""

    step_type: Literal["tool_execution"]
    """Type of the step in an agent turn."""

    tool_calls: List[ToolCall]
    """The tool calls to execute."""

    tool_responses: List[ToolResponse]
    """The tool responses from the tool calls."""

    turn_id: str
    """The ID of the turn."""

    completed_at: Optional[datetime] = None
    """The time the step completed."""

    started_at: Optional[datetime] = None
    """The time the step started."""
