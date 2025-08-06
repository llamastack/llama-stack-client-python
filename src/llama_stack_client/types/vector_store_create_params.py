# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import TypedDict

__all__ = ["VectorStoreCreateParams"]


class VectorStoreCreateParams(TypedDict, total=False):
    chunking_strategy: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The chunking strategy used to chunk the file(s).

    If not set, will use the `auto` strategy.
    """

    embedding_dimension: int
    """The dimension of the embedding vectors (default: 384)."""

    embedding_model: str
    """The embedding model to use for this vector store."""

    expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The expiration policy for a vector store."""

    file_ids: List[str]
    """A list of File IDs that the vector store should use.

    Useful for tools like `file_search` that can access files.
    """

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """Set of 16 key-value pairs that can be attached to an object."""

    name: str
    """A name for the vector store."""

    provider_id: str
    """The ID of the provider to use for this vector store."""
