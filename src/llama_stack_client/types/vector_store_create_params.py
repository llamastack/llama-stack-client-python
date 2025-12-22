# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
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
    chunking_strategy: Optional[ChunkingStrategy]
    """Automatic chunking strategy for vector store files."""

    expires_after: Optional[Dict[str, object]]

    file_ids: Optional[SequenceNotStr[str]]

    metadata: Optional[Dict[str, object]]

    name: Optional[str]


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


ChunkingStrategy: TypeAlias = Union[
    ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic
]
