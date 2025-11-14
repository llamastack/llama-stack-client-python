# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileBatchListFilesParams"]


class FileBatchListFilesParams(TypedDict, total=False):
    vector_store_id: Required[str]

    after: Optional[str]

    before: Optional[str]

    filter: Optional[str]

    limit: Optional[int]

    order: Optional[str]
