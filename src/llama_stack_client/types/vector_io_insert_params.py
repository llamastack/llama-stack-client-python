# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VectorIoInsertParams",
    "Chunk",
    "ChunkContent",
    "ChunkContentImageContentItemInput",
    "ChunkContentImageContentItemInputImage",
    "ChunkContentImageContentItemInputImageURL",
    "ChunkContentTextContentItem",
    "ChunkContentListImageContentItemInputTextContentItem",
    "ChunkContentListImageContentItemInputTextContentItemImageContentItemInput",
    "ChunkContentListImageContentItemInputTextContentItemImageContentItemInputImage",
    "ChunkContentListImageContentItemInputTextContentItemImageContentItemInputImageURL",
    "ChunkContentListImageContentItemInputTextContentItemTextContentItem",
    "ChunkChunkMetadata",
]


class VectorIoInsertParams(TypedDict, total=False):
    chunks: Required[Iterable[Chunk]]

    vector_store_id: Required[str]

    ttl_seconds: Optional[int]


class ChunkContentImageContentItemInputImageURL(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]


class ChunkContentImageContentItemInputImage(TypedDict, total=False):
    """A URL or a base64 encoded string"""

    data: Optional[str]

    url: Optional[ChunkContentImageContentItemInputImageURL]
    """A URL reference to external content."""


class ChunkContentImageContentItemInput(TypedDict, total=False):
    """A image content item"""

    image: Required[ChunkContentImageContentItemInputImage]
    """A URL or a base64 encoded string"""

    type: Literal["image"]


class ChunkContentTextContentItem(TypedDict, total=False):
    """A text content item"""

    text: Required[str]

    type: Literal["text"]


class ChunkContentListImageContentItemInputTextContentItemImageContentItemInputImageURL(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]


class ChunkContentListImageContentItemInputTextContentItemImageContentItemInputImage(TypedDict, total=False):
    """A URL or a base64 encoded string"""

    data: Optional[str]

    url: Optional[ChunkContentListImageContentItemInputTextContentItemImageContentItemInputImageURL]
    """A URL reference to external content."""


class ChunkContentListImageContentItemInputTextContentItemImageContentItemInput(TypedDict, total=False):
    """A image content item"""

    image: Required[ChunkContentListImageContentItemInputTextContentItemImageContentItemInputImage]
    """A URL or a base64 encoded string"""

    type: Literal["image"]


class ChunkContentListImageContentItemInputTextContentItemTextContentItem(TypedDict, total=False):
    """A text content item"""

    text: Required[str]

    type: Literal["text"]


ChunkContentListImageContentItemInputTextContentItem: TypeAlias = Union[
    ChunkContentListImageContentItemInputTextContentItemImageContentItemInput,
    ChunkContentListImageContentItemInputTextContentItemTextContentItem,
]

ChunkContent: TypeAlias = Union[
    str,
    ChunkContentImageContentItemInput,
    ChunkContentTextContentItem,
    Iterable[ChunkContentListImageContentItemInputTextContentItem],
]


class ChunkChunkMetadata(TypedDict, total=False):
    """
    `ChunkMetadata` is backend metadata for a `Chunk` that is used to store additional information about the chunk that
        will not be used in the context during inference, but is required for backend functionality. The `ChunkMetadata`
        is set during chunk creation in `MemoryToolRuntimeImpl().insert()`and is not expected to change after.
        Use `Chunk.metadata` for metadata that will be used in the context during inference.
    """

    chunk_embedding_dimension: Optional[int]

    chunk_embedding_model: Optional[str]

    chunk_id: Optional[str]

    chunk_tokenizer: Optional[str]

    chunk_window: Optional[str]

    content_token_count: Optional[int]

    created_timestamp: Optional[int]

    document_id: Optional[str]

    metadata_token_count: Optional[int]

    source: Optional[str]

    updated_timestamp: Optional[int]


class Chunk(TypedDict, total=False):
    """A chunk of content that can be inserted into a vector database."""

    chunk_id: Required[str]

    content: Required[ChunkContent]
    """A image content item"""

    chunk_metadata: Optional[ChunkChunkMetadata]
    """
    `ChunkMetadata` is backend metadata for a `Chunk` that is used to store
    additional information about the chunk that will not be used in the context
    during inference, but is required for backend functionality. The `ChunkMetadata`
    is set during chunk creation in `MemoryToolRuntimeImpl().insert()`and is not
    expected to change after. Use `Chunk.metadata` for metadata that will be used in
    the context during inference.
    """

    embedding: Optional[Iterable[float]]

    metadata: Dict[str, object]
