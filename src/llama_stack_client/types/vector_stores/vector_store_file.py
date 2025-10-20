# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
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
    type: Literal["auto"]
    """Strategy type, always "auto" for automatic chunking"""


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(BaseModel):
    chunk_overlap_tokens: int
    """Number of tokens to overlap between adjacent chunks"""

    max_chunk_size_tokens: int
    """Maximum number of tokens per chunk, must be between 100 and 4096"""


class ChunkingStrategyVectorStoreChunkingStrategyStatic(BaseModel):
    static: ChunkingStrategyVectorStoreChunkingStrategyStaticStatic
    """Configuration parameters for the static chunking strategy"""

    type: Literal["static"]
    """Strategy type, always "static" for static chunking"""


ChunkingStrategy: TypeAlias = Annotated[
    Union[ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic],
    PropertyInfo(discriminator="type"),
]


class LastError(BaseModel):
    code: Literal["server_error", "rate_limit_exceeded"]
    """Error code indicating the type of failure"""

    message: str
    """Human-readable error message describing the failure"""


class VectorStoreFile(BaseModel):
    id: str
    """Unique identifier for the file"""

    attributes: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Key-value attributes associated with the file"""

    chunking_strategy: ChunkingStrategy
    """Strategy used for splitting the file into chunks"""

    created_at: int
    """Timestamp when the file was added to the vector store"""

    object: str
    """Object type identifier, always "vector_store.file" """

    status: Literal["completed", "in_progress", "cancelled", "failed"]
    """Current processing status of the file"""

    usage_bytes: int
    """Storage space used by this file in bytes"""

    vector_store_id: str
    """ID of the vector store containing this file"""

    last_error: Optional[LastError] = None
    """(Optional) Error information if file processing failed"""
