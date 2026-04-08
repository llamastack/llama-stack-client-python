# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: Optional[str]
    """Pagination cursor (after)."""

    before: Optional[str]
    """Pagination cursor (before)."""

    filter: Optional[Literal["in_progress", "completed", "cancelled", "failed"]]
    """Filter by file status."""

    limit: Optional[int]
    """Maximum number of files to return."""

    order: Optional[str]
    """Sort order by created_at: asc or desc."""
