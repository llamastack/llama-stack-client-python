# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .turn import Turn
from ...._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    session_id: str
    """Unique identifier for the conversation session"""

    session_name: str
    """Human-readable name for the session"""

    started_at: datetime
    """Timestamp when the session was created"""

    turns: List[Turn]
    """List of all turns that have occurred in this session"""
