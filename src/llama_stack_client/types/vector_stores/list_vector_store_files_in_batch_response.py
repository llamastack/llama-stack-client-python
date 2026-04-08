# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .vector_store_file import VectorStoreFile

__all__ = ["ListVectorStoreFilesInBatchResponse"]


class ListVectorStoreFilesInBatchResponse(BaseModel):
    """Response from listing files in a vector store file batch."""

    data: List[VectorStoreFile]

    first_id: str

    has_more: bool

    last_id: str

    object: Optional[Literal["list"]] = None
