# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileContentParams"]


class FileContentParams(TypedDict, total=False):
    vector_store_id: Required[str]

    include_embeddings: Optional[bool]

    include_metadata: Optional[bool]
