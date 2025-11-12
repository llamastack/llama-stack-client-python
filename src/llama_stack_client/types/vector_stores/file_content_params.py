# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileContentParams"]


class FileContentParams(TypedDict, total=False):
    vector_store_id: Required[str]

    include_embeddings: bool
    """Whether to include embedding vectors in the response."""

    include_metadata: bool
    """Whether to include chunk metadata in the response."""
