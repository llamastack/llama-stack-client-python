# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreDeleteResponse"]


class VectorStoreDeleteResponse(BaseModel):
    """Response from deleting a vector store."""

    id: str

    deleted: bool

    object: Optional[Literal["vector_store.deleted"]] = None
