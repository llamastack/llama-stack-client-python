# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ResponseListParams"]


class ResponseListParams(TypedDict, total=False):
    after: Optional[str]

    limit: Optional[int]

    model: Optional[str]

    order: Optional[Literal["asc", "desc"]]
    """Sort order for paginated responses."""
