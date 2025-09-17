# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RerankResponse", "RerankData"]


class RerankData(BaseModel):
    index: int
    """The original index of the document in the input list."""

    relevance_score: float
    """The relevance score from the model output. Values are inverted when applicable so that higher scores indicate greater relevance."""


class RerankResponse(BaseModel):
    data: List[RerankData]
    """List of rerank result objects, sorted by relevance score (descending)."""
