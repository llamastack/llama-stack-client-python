# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "FileBatchCreateParams",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyContextual",
    "ChunkingStrategyVectorStoreChunkingStrategyContextualContextual",
    "File",
    "FileChunkingStrategy",
    "FileChunkingStrategyVectorStoreChunkingStrategyAuto",
    "FileChunkingStrategyVectorStoreChunkingStrategyStatic",
    "FileChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
    "FileChunkingStrategyVectorStoreChunkingStrategyContextual",
    "FileChunkingStrategyVectorStoreChunkingStrategyContextualContextual",
]


class FileBatchCreateParams(TypedDict, total=False):
    attributes: Optional[Dict[str, Union[str, float, bool]]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    chunking_strategy: Optional[ChunkingStrategy]
    """Automatic chunking strategy for vector store files."""

    file_ids: SequenceNotStr[str]

    files: Optional[Iterable[File]]


class ChunkingStrategyVectorStoreChunkingStrategyAuto(TypedDict, total=False):
    """Automatic chunking strategy for vector store files."""

    type: Literal["auto"]


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(TypedDict, total=False):
    """Configuration for static chunking strategy."""

    chunk_overlap_tokens: int

    max_chunk_size_tokens: int


class ChunkingStrategyVectorStoreChunkingStrategyStatic(TypedDict, total=False):
    """Static chunking strategy with configurable parameters."""

    static: Required[ChunkingStrategyVectorStoreChunkingStrategyStaticStatic]
    """Configuration for static chunking strategy."""

    type: Literal["static"]


class ChunkingStrategyVectorStoreChunkingStrategyContextualContextual(TypedDict, total=False):
    """Configuration for contextual chunking."""

    chunk_overlap_tokens: int
    """Tokens to overlap between adjacent chunks.

    Must be less than max_chunk_size_tokens.
    """

    context_prompt: str
    """Prompt template for contextual retrieval.

    Uses WHOLE_DOCUMENT and CHUNK_CONTENT placeholders wrapped in double curly
    braces.
    """

    max_chunk_size_tokens: int
    """Maximum tokens per chunk. Suggested ~700 to allow room for prepended context."""

    max_concurrency: Optional[int]
    """Maximum concurrent LLM calls. Falls back to config default if not provided."""

    model_id: Optional[str]
    """LLM model for generating context.

    Falls back to VectorStoresConfig.contextual_retrieval_params.model if not
    provided.
    """

    timeout_seconds: Optional[int]
    """Timeout per LLM call in seconds. Falls back to config default if not provided."""


class ChunkingStrategyVectorStoreChunkingStrategyContextual(TypedDict, total=False):
    """
    Contextual chunking strategy that uses an LLM to situate chunks within the document.
    """

    contextual: Required[ChunkingStrategyVectorStoreChunkingStrategyContextualContextual]
    """Configuration for contextual chunking."""

    type: Literal["contextual"]
    """Strategy type identifier."""


ChunkingStrategy: TypeAlias = Union[
    ChunkingStrategyVectorStoreChunkingStrategyAuto,
    ChunkingStrategyVectorStoreChunkingStrategyStatic,
    ChunkingStrategyVectorStoreChunkingStrategyContextual,
]


class FileChunkingStrategyVectorStoreChunkingStrategyAuto(TypedDict, total=False):
    """Automatic chunking strategy for vector store files."""

    type: Literal["auto"]


class FileChunkingStrategyVectorStoreChunkingStrategyStaticStatic(TypedDict, total=False):
    """Configuration for static chunking strategy."""

    chunk_overlap_tokens: int

    max_chunk_size_tokens: int


class FileChunkingStrategyVectorStoreChunkingStrategyStatic(TypedDict, total=False):
    """Static chunking strategy with configurable parameters."""

    static: Required[FileChunkingStrategyVectorStoreChunkingStrategyStaticStatic]
    """Configuration for static chunking strategy."""

    type: Literal["static"]


class FileChunkingStrategyVectorStoreChunkingStrategyContextualContextual(TypedDict, total=False):
    """Configuration for contextual chunking."""

    chunk_overlap_tokens: int
    """Tokens to overlap between adjacent chunks.

    Must be less than max_chunk_size_tokens.
    """

    context_prompt: str
    """Prompt template for contextual retrieval.

    Uses WHOLE_DOCUMENT and CHUNK_CONTENT placeholders wrapped in double curly
    braces.
    """

    max_chunk_size_tokens: int
    """Maximum tokens per chunk. Suggested ~700 to allow room for prepended context."""

    max_concurrency: Optional[int]
    """Maximum concurrent LLM calls. Falls back to config default if not provided."""

    model_id: Optional[str]
    """LLM model for generating context.

    Falls back to VectorStoresConfig.contextual_retrieval_params.model if not
    provided.
    """

    timeout_seconds: Optional[int]
    """Timeout per LLM call in seconds. Falls back to config default if not provided."""


class FileChunkingStrategyVectorStoreChunkingStrategyContextual(TypedDict, total=False):
    """
    Contextual chunking strategy that uses an LLM to situate chunks within the document.
    """

    contextual: Required[FileChunkingStrategyVectorStoreChunkingStrategyContextualContextual]
    """Configuration for contextual chunking."""

    type: Literal["contextual"]
    """Strategy type identifier."""


FileChunkingStrategy: TypeAlias = Union[
    FileChunkingStrategyVectorStoreChunkingStrategyAuto,
    FileChunkingStrategyVectorStoreChunkingStrategyStatic,
    FileChunkingStrategyVectorStoreChunkingStrategyContextual,
]


class File(TypedDict, total=False):
    """A file entry for creating a vector store file batch with per-file options."""

    file_id: Required[str]

    attributes: Optional[Dict[str, Union[str, float, bool]]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    chunking_strategy: Optional[FileChunkingStrategy]
    """Automatic chunking strategy for vector store files."""
