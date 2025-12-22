# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "VectorStoreFile",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
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


ChunkingStrategy: TypeAlias = Annotated[
    Union[ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic],
    PropertyInfo(discriminator="type"),
]


class LastError(BaseModel):
    """Error information for failed vector store file processing."""

    code: Literal["server_error", "rate_limit_exceeded"]

    message: str


class VectorStoreFile(BaseModel):
    """OpenAI Vector Store File object."""

    id: str

    chunking_strategy: ChunkingStrategy
    """Automatic chunking strategy for vector store files."""

    created_at: int

    status: Literal["completed", "in_progress", "cancelled", "failed"]

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

    object: Optional[str] = None

    usage_bytes: Optional[int] = None
