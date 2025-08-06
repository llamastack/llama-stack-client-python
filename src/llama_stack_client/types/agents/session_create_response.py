# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SessionCreateResponse"]


class SessionCreateResponse(BaseModel):
    session_id: str
    """Unique identifier for the created session"""
