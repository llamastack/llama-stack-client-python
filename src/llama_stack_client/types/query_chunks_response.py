# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["QueryChunksResponse", "Chunk", "ChunkChunkMetadata"]


class ChunkChunkMetadata(BaseModel):
    chunk_embedding_dimension: Optional[int] = None
    """The dimension of the embedding vector for the chunk."""

    chunk_embedding_model: Optional[str] = None
    """The embedding model used to create the chunk's embedding."""

    chunk_id: Optional[str] = None
    """The ID of the chunk.

    If not set, it will be generated based on the document ID and content.
    """

    chunk_tokenizer: Optional[str] = None
    """The tokenizer used to create the chunk. Default is Tiktoken."""

    chunk_window: Optional[str] = None
    """The window of the chunk, which can be used to group related chunks together."""

    content_token_count: Optional[int] = None
    """The number of tokens in the content of the chunk."""

    created_timestamp: Optional[int] = None
    """An optional timestamp indicating when the chunk was created."""

    document_id: Optional[str] = None
    """The ID of the document this chunk belongs to."""

    metadata_token_count: Optional[int] = None
    """The number of tokens in the metadata of the chunk."""

    source: Optional[str] = None
    """The source of the content, such as a URL, file path, or other identifier."""

    updated_timestamp: Optional[int] = None
    """An optional timestamp indicating when the chunk was last updated."""


class Chunk(BaseModel):
    content: InterleavedContent
    """
    The content of the chunk, which can be interleaved text, images, or other types.
    """

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """
    Metadata associated with the chunk that will be used in the model context during
    inference.
    """

    chunk_metadata: Optional[ChunkChunkMetadata] = None
    """Metadata for the chunk that will NOT be used in the context during inference.

    The `chunk_metadata` is required backend functionality.
    """

    embedding: Optional[List[float]] = None
    """Optional embedding for the chunk. If not provided, it will be computed later."""

    stored_chunk_id: Optional[str] = None
    """The chunk ID that is stored in the vector database.

    Used for backend functionality.
    """


class QueryChunksResponse(BaseModel):
    chunks: List[Chunk]
    """List of content chunks returned from the query"""

    scores: List[float]
    """Relevance scores corresponding to each returned chunk"""
