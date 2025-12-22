# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileContentResponse", "Data", "DataChunkMetadata"]


class DataChunkMetadata(BaseModel):
    """
    `ChunkMetadata` is backend metadata for a `Chunk` that is used to store additional information about the chunk that
        will not be used in the context during inference, but is required for backend functionality. The `ChunkMetadata`
        is set during chunk creation in `MemoryToolRuntimeImpl().insert()`and is not expected to change after.
        Use `Chunk.metadata` for metadata that will be used in the context during inference.
    """

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


class Data(BaseModel):
    """Content item from a vector store file or search result."""

    text: str

    type: Literal["text"]

    chunk_metadata: Optional[DataChunkMetadata] = None
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


class FileContentResponse(BaseModel):
    """Represents the parsed content of a vector store file."""

    data: List[Data]

    has_more: Optional[bool] = None

    next_page: Optional[str] = None

    object: Optional[Literal["vector_store.file_content.page"]] = None
