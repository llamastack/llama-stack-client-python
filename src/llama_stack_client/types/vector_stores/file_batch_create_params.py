# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "FileBatchCreateParams",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
]


class FileBatchCreateParams(TypedDict, total=False):
    file_ids: Required[SequenceNotStr[str]]
    """A list of File IDs that the vector store should use"""

    attributes: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Key-value attributes to store with the files"""

    chunking_strategy: ChunkingStrategy
    """(Optional) The chunking strategy used to chunk the file(s). Defaults to auto"""


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
