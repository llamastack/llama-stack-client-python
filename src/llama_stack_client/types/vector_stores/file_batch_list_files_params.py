# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileBatchListFilesParams"]


class FileBatchListFilesParams(TypedDict, total=False):
    vector_store_id: Required[str]
    """The vector store identifier."""

    after: Optional[str]
    """Pagination cursor (after)."""

    before: Optional[str]
    """Pagination cursor (before)."""

    filter: Optional[str]
    """Filter by file status."""

    limit: Optional[int]
    """Maximum number of files to return."""

    order: Optional[str]
    """Sort order by created_at: asc or desc."""
