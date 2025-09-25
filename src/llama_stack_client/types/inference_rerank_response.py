# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["InferenceRerankResponse", "InferenceRerankResponseItem"]


class InferenceRerankResponseItem(BaseModel):
    index: int
    """The original index of the document in the input list"""

    relevance_score: float
    """The relevance score from the model output.

    Values are inverted when applicable so that higher scores indicate greater
    relevance.
    """


InferenceRerankResponse: TypeAlias = List[InferenceRerankResponseItem]
