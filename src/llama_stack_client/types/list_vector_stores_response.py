# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .vector_store import VectorStore

__all__ = ["ListVectorStoresResponse"]


class ListVectorStoresResponse(BaseModel):
    """Response from listing vector stores."""

    data: List[VectorStore]

    first_id: str

    has_more: bool

    last_id: str

    object: Optional[Literal["list"]] = None
