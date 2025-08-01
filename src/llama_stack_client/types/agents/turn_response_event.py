# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .turn_response_event_payload import TurnResponseEventPayload

__all__ = ["TurnResponseEvent"]


class TurnResponseEvent(BaseModel):
    payload: TurnResponseEventPayload
    """Event-specific payload containing event data"""
