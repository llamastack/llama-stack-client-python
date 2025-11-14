# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: Optional[str]

    before: Optional[str]

    filter: Optional[Literal["completed", "in_progress", "cancelled", "failed"]]

    limit: Optional[int]

    order: Optional[str]
