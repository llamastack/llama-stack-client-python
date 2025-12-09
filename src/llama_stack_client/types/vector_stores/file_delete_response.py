# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FileDeleteResponse"]


class FileDeleteResponse(BaseModel):
    """Response from deleting a vector store file."""

    id: str

    deleted: Optional[bool] = None

    object: Optional[str] = None
