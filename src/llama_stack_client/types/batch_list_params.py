# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    after: Optional[str]
    """Optional cursor for pagination. Returns batches after this ID."""

    limit: int
    """Maximum number of batches to return. Defaults to 20."""
