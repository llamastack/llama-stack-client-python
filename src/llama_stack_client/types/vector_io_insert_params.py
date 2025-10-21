# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.interleaved_content import InterleavedContent

__all__ = ["VectorIoInsertParams", "Chunk", "ChunkChunkMetadata"]


class VectorIoInsertParams(TypedDict, total=False):
    chunks: Required[Iterable[Chunk]]
    """The chunks to insert.

    Each `Chunk` should contain content which can be interleaved text, images, or
    other types. `metadata`: `dict[str, Any]` and `embedding`: `List[float]` are
    optional. If `metadata` is provided, you configure how Llama Stack formats the
    chunk during generation. If `embedding` is not provided, it will be computed
    later.
    """

    vector_db_id: Required[str]
    """The identifier of the vector database to insert the chunks into."""

    ttl_seconds: int
    """The time to live of the chunks."""


class ChunkChunkMetadata(TypedDict, total=False):
    chunk_embedding_dimension: int
    """The dimension of the embedding vector for the chunk."""

    chunk_embedding_model: str
    """The embedding model used to create the chunk's embedding."""

    chunk_id: str
    """The ID of the chunk.

    If not set, it will be generated based on the document ID and content.
    """

    chunk_tokenizer: str
    """The tokenizer used to create the chunk. Default is Tiktoken."""

    chunk_window: str
    """The window of the chunk, which can be used to group related chunks together."""

    content_token_count: int
    """The number of tokens in the content of the chunk."""

    created_timestamp: int
    """An optional timestamp indicating when the chunk was created."""

    document_id: str
    """The ID of the document this chunk belongs to."""

    metadata_token_count: int
    """The number of tokens in the metadata of the chunk."""

    source: str
    """The source of the content, such as a URL, file path, or other identifier."""

    updated_timestamp: int
    """An optional timestamp indicating when the chunk was last updated."""


class Chunk(TypedDict, total=False):
    content: Required[InterleavedContent]
    """
    The content of the chunk, which can be interleaved text, images, or other types.
    """

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """
    Metadata associated with the chunk that will be used in the model context during
    inference.
    """

    chunk_metadata: ChunkChunkMetadata
    """Metadata for the chunk that will NOT be used in the context during inference.

    The `chunk_metadata` is required backend functionality.
    """

    embedding: Iterable[float]
    """Optional embedding for the chunk. If not provided, it will be computed later."""

    stored_chunk_id: str
    """The chunk ID that is stored in the vector database.

    Used for backend functionality.
    """
