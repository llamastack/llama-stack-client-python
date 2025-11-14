# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "QueryChunksResponse",
    "Chunk",
    "ChunkContent",
    "ChunkContentImageContentItemOutput",
    "ChunkContentImageContentItemOutputImage",
    "ChunkContentImageContentItemOutputImageURL",
    "ChunkContentTextContentItem",
    "ChunkContentListImageContentItemOutputTextContentItem",
    "ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutput",
    "ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutputImage",
    "ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutputImageURL",
    "ChunkContentListImageContentItemOutputTextContentItemTextContentItem",
    "ChunkChunkMetadata",
]


class ChunkContentImageContentItemOutputImageURL(BaseModel):
    uri: str


class ChunkContentImageContentItemOutputImage(BaseModel):
    data: Optional[str] = None

    url: Optional[ChunkContentImageContentItemOutputImageURL] = None
    """A URL reference to external content."""


class ChunkContentImageContentItemOutput(BaseModel):
    image: ChunkContentImageContentItemOutputImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ChunkContentTextContentItem(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutputImageURL(BaseModel):
    uri: str


class ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutputImage(BaseModel):
    data: Optional[str] = None

    url: Optional[ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutputImageURL] = None
    """A URL reference to external content."""


class ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutput(BaseModel):
    image: ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutputImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ChunkContentListImageContentItemOutputTextContentItemTextContentItem(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


ChunkContentListImageContentItemOutputTextContentItem: TypeAlias = Annotated[
    Union[
        ChunkContentListImageContentItemOutputTextContentItemImageContentItemOutput,
        ChunkContentListImageContentItemOutputTextContentItemTextContentItem,
    ],
    PropertyInfo(discriminator="type"),
]

ChunkContent: TypeAlias = Union[
    str,
    ChunkContentImageContentItemOutput,
    ChunkContentTextContentItem,
    List[ChunkContentListImageContentItemOutputTextContentItem],
]


class ChunkChunkMetadata(BaseModel):
    chunk_embedding_dimension: Optional[int] = None

    chunk_embedding_model: Optional[str] = None

    chunk_id: Optional[str] = None

    chunk_tokenizer: Optional[str] = None

    chunk_window: Optional[str] = None

    content_token_count: Optional[int] = None

    created_timestamp: Optional[int] = None

    document_id: Optional[str] = None

    metadata_token_count: Optional[int] = None

    source: Optional[str] = None

    updated_timestamp: Optional[int] = None


class Chunk(BaseModel):
    chunk_id: str

    content: ChunkContent
    """A image content item"""

    chunk_metadata: Optional[ChunkChunkMetadata] = None
    """
    `ChunkMetadata` is backend metadata for a `Chunk` that is used to store
    additional information about the chunk that will not be used in the context
    during inference, but is required for backend functionality. The `ChunkMetadata`
    is set during chunk creation in `MemoryToolRuntimeImpl().insert()`and is not
    expected to change after. Use `Chunk.metadata` for metadata that will be used in
    the context during inference.
    """

    embedding: Optional[List[float]] = None

    metadata: Optional[Dict[str, object]] = None


class QueryChunksResponse(BaseModel):
    chunks: List[Chunk]

    scores: List[float]
