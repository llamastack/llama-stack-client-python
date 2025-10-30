# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.completion_message import CompletionMessage

__all__ = ["InferenceStep"]


class InferenceStep(BaseModel):
    api_model_response: CompletionMessage = FieldInfo(alias="model_response")
    """The response from the LLM."""

    step_id: str
    """The ID of the step."""

    step_type: Literal["inference"]
    """Type of the step in an agent turn."""

    turn_id: str
    """The ID of the turn."""

    completed_at: Optional[datetime] = None
    """The time the step completed."""

    started_at: Optional[datetime] = None
    """The time the step started."""
