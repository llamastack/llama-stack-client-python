# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.interleaved_content import InterleavedContent

__all__ = ["MemoryRetrievalStep"]


class MemoryRetrievalStep(BaseModel):
    inserted_context: InterleavedContent
    """The context retrieved from the vector databases."""

    step_id: str
    """The ID of the step."""

    step_type: Literal["memory_retrieval"]
    """Type of the step in an agent turn."""

    turn_id: str
    """The ID of the turn."""

    vector_db_ids: str
    """The IDs of the vector databases to retrieve context from."""

    completed_at: Optional[datetime] = None
    """The time the step completed."""

    started_at: Optional[datetime] = None
    """The time the step started."""
