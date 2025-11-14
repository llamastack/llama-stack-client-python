# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["InferenceRerankResponse", "InferenceRerankResponseItem"]


class InferenceRerankResponseItem(BaseModel):
    index: int

    relevance_score: float


InferenceRerankResponse: TypeAlias = List[InferenceRerankResponseItem]
