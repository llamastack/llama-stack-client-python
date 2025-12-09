# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SafetyViolation"]


class SafetyViolation(BaseModel):
    """Details of a safety violation detected by content moderation."""

    violation_level: Literal["info", "warn", "error"]
    """Severity level of a safety violation."""

    metadata: Optional[Dict[str, object]] = None

    user_message: Optional[str] = None
