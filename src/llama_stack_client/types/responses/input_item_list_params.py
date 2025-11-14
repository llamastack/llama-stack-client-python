# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["InputItemListParams"]


class InputItemListParams(TypedDict, total=False):
    after: Optional[str]

    before: Optional[str]

    include: Optional[SequenceNotStr[str]]

    limit: Optional[int]

    order: Optional[Literal["asc", "desc"]]
    """Sort order for paginated responses."""
