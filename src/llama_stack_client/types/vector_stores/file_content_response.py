# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileContentResponse", "Data", "DataChunkMetadata"]


class DataChunkMetadata(BaseModel):
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


class Data(BaseModel):
    text: str
    """The actual text content"""

    type: Literal["text"]
    """Content type, currently only "text" is supported"""

    chunk_metadata: Optional[DataChunkMetadata] = None
    """Optional chunk metadata"""

    embedding: Optional[List[float]] = None
    """Optional embedding vector for this content chunk"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """Optional user-defined metadata"""


class FileContentResponse(BaseModel):
    data: List[Data]
    """Parsed content of the file"""

    has_more: bool
    """Indicates if there are more content pages to fetch"""

    object: Literal["vector_store.file_content.page"]
    """The object type, which is always `vector_store.file_content.page`"""

    next_page: Optional[str] = None
    """The token for the next page, if any"""
