# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "VectorStoreCreateParams",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
]


class VectorStoreCreateParams(TypedDict, total=False):
    chunking_strategy: ChunkingStrategy
    """(Optional) Strategy for splitting files into chunks"""

    expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Expiration policy for the vector store"""

    file_ids: SequenceNotStr[str]
    """List of file IDs to include in the vector store"""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """Set of key-value pairs that can be attached to the vector store"""

    name: str
    """(Optional) A name for the vector store"""


class ChunkingStrategyVectorStoreChunkingStrategyAuto(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Strategy type, always "auto" for automatic chunking"""


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(TypedDict, total=False):
    chunk_overlap_tokens: Required[int]
    """Number of tokens to overlap between adjacent chunks"""

    max_chunk_size_tokens: Required[int]
    """Maximum number of tokens per chunk, must be between 100 and 4096"""


class ChunkingStrategyVectorStoreChunkingStrategyStatic(TypedDict, total=False):
    static: Required[ChunkingStrategyVectorStoreChunkingStrategyStaticStatic]
    """Configuration parameters for the static chunking strategy"""

    type: Required[Literal["static"]]
    """Strategy type, always "static" for static chunking"""


ChunkingStrategy: TypeAlias = Union[
    ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic
]
