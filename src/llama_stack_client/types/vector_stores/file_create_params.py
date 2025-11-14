# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "FileCreateParams",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
]


class FileCreateParams(TypedDict, total=False):
    file_id: Required[str]

    attributes: Optional[Dict[str, object]]

    chunking_strategy: Optional[ChunkingStrategy]
    """Automatic chunking strategy for vector store files."""


class ChunkingStrategyVectorStoreChunkingStrategyAuto(TypedDict, total=False):
    type: Literal["auto"]


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(TypedDict, total=False):
    chunk_overlap_tokens: int

    max_chunk_size_tokens: int


class ChunkingStrategyVectorStoreChunkingStrategyStatic(TypedDict, total=False):
    static: Required[ChunkingStrategyVectorStoreChunkingStrategyStaticStatic]
    """Configuration for static chunking strategy."""

    type: Literal["static"]


ChunkingStrategy: TypeAlias = Union[
    ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic
]
