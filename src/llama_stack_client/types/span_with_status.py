# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SpanWithStatus"]


class SpanWithStatus(BaseModel):
    name: str
    """Human-readable name describing the operation this span represents"""

    span_id: str
    """Unique identifier for the span"""

    start_time: datetime
    """Timestamp when the operation began"""

    trace_id: str
    """Unique identifier for the trace this span belongs to"""

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Key-value pairs containing additional metadata about the span"""

    end_time: Optional[datetime] = None
    """(Optional) Timestamp when the operation finished, if completed"""

    parent_span_id: Optional[str] = None
    """(Optional) Unique identifier for the parent span, if this is a child span"""

    status: Optional[Literal["ok", "error"]] = None
    """(Optional) The current status of the span"""
