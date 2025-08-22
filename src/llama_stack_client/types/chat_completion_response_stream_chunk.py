# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .metric import Metric
from .._models import BaseModel
from .shared.content_delta import ContentDelta
from .shared.shared_token_log_probs import SharedTokenLogProbs

__all__ = ["ChatCompletionResponseStreamChunk", "Event"]


class Event(BaseModel):
    delta: ContentDelta
    """Content generated since last event.

    This can be one or more tokens, or a tool call.
    """

    event_type: Literal["start", "complete", "progress"]
    """Type of the event"""

    logprobs: Optional[List[SharedTokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None
    """Optional reason why generation stopped, if complete"""


class ChatCompletionResponseStreamChunk(BaseModel):
    event: Event
    """The event containing the new content"""

    metrics: Optional[List[Metric]] = None
    """(Optional) List of metrics associated with the API response"""
