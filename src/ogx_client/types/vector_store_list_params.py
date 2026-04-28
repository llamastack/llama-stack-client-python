# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VectorStoreListParams"]


class VectorStoreListParams(TypedDict, total=False):
    after: Optional[str]
    """Pagination cursor (after)."""

    before: Optional[str]
    """Pagination cursor (before)."""

    limit: Optional[int]
    """Maximum number of vector stores to return."""

    order: Optional[str]
    """Sort order by created_at: asc or desc."""
