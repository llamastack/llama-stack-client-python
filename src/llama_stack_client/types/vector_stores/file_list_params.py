# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: str

    before: str

    filter: Literal["completed", "in_progress", "cancelled", "failed"]

    limit: int

    order: str
