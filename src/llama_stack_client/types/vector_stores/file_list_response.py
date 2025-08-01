# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .vector_store_file import VectorStoreFile

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
    data: List[VectorStoreFile]
    """List of vector store file objects"""

    has_more: bool
    """Whether there are more files available beyond this page"""

    object: str
    """Object type identifier, always "list" """

    first_id: Optional[str] = None
    """(Optional) ID of the first file in the list for pagination"""

    last_id: Optional[str] = None
    """(Optional) ID of the last file in the list for pagination"""
