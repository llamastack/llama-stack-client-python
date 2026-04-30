# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "VectorStoreFile",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyContextual",
    "ChunkingStrategyVectorStoreChunkingStrategyContextualContextual",
    "LastError",
]


class ChunkingStrategyVectorStoreChunkingStrategyAuto(BaseModel):
    """Automatic chunking strategy for vector store files."""

    type: Optional[Literal["auto"]] = None


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(BaseModel):
    """Configuration for static chunking strategy."""

    chunk_overlap_tokens: Optional[int] = None

    max_chunk_size_tokens: Optional[int] = None


class ChunkingStrategyVectorStoreChunkingStrategyStatic(BaseModel):
    """Static chunking strategy with configurable parameters."""

    static: ChunkingStrategyVectorStoreChunkingStrategyStaticStatic
    """Configuration for static chunking strategy."""

    type: Optional[Literal["static"]] = None


class ChunkingStrategyVectorStoreChunkingStrategyContextualContextual(BaseModel):
    """Configuration for contextual chunking."""

    chunk_overlap_tokens: Optional[int] = None
    """Tokens to overlap between adjacent chunks.

    Must be less than max_chunk_size_tokens.
    """

    context_prompt: Optional[str] = None
    """Prompt template for contextual retrieval.

    Uses WHOLE_DOCUMENT and CHUNK_CONTENT placeholders wrapped in double curly
    braces.
    """

    max_chunk_size_tokens: Optional[int] = None
    """Maximum tokens per chunk. Suggested ~700 to allow room for prepended context."""

    max_concurrency: Optional[int] = None
    """Maximum concurrent LLM calls. Falls back to config default if not provided."""

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """LLM model for generating context.

    Falls back to VectorStoresConfig.contextual_retrieval_params.model if not
    provided.
    """

    timeout_seconds: Optional[int] = None
    """Timeout per LLM call in seconds. Falls back to config default if not provided."""


class ChunkingStrategyVectorStoreChunkingStrategyContextual(BaseModel):
    """
    Contextual chunking strategy that uses an LLM to situate chunks within the document.
    """

    contextual: ChunkingStrategyVectorStoreChunkingStrategyContextualContextual
    """Configuration for contextual chunking."""

    type: Optional[Literal["contextual"]] = None
    """Strategy type identifier."""


ChunkingStrategy: TypeAlias = Annotated[
    Union[
        ChunkingStrategyVectorStoreChunkingStrategyAuto,
        ChunkingStrategyVectorStoreChunkingStrategyStatic,
        ChunkingStrategyVectorStoreChunkingStrategyContextual,
    ],
    PropertyInfo(discriminator="type"),
]


class LastError(BaseModel):
    """Error information for failed vector store file processing."""

    code: Literal["server_error", "unsupported_file", "invalid_file"]

    message: str


class VectorStoreFile(BaseModel):
    """OpenAI Vector Store File object."""

    id: str

    chunking_strategy: ChunkingStrategy
    """Automatic chunking strategy for vector store files."""

    created_at: int

    status: Literal["in_progress", "completed", "cancelled", "failed"]

    vector_store_id: str

    attributes: Optional[Dict[str, Union[str, float, bool]]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    last_error: Optional[LastError] = None
    """Error information for failed vector store file processing."""

    object: Optional[Literal["vector_store.file"]] = None

    usage_bytes: Optional[int] = None
