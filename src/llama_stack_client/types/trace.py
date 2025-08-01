# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Trace"]


class Trace(BaseModel):
    root_span_id: str
    """Unique identifier for the root span that started this trace"""

    start_time: datetime
    """Timestamp when the trace began"""

    trace_id: str
    """Unique identifier for the trace"""

    end_time: Optional[datetime] = None
    """(Optional) Timestamp when the trace finished, if completed"""
