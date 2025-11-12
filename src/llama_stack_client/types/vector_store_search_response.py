# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreSearchResponse", "Data", "DataContent", "DataContentChunkMetadata"]


class DataContentChunkMetadata(BaseModel):
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


class DataContent(BaseModel):
    text: str
    """The actual text content"""

    type: Literal["text"]
    """Content type, currently only "text" is supported"""

    chunk_metadata: Optional[DataContentChunkMetadata] = None
    """Optional chunk metadata"""

    embedding: Optional[List[float]] = None
    """Optional embedding vector for this content chunk"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """Optional user-defined metadata"""


class Data(BaseModel):
    content: List[DataContent]
    """List of content items matching the search query"""

    file_id: str
    """Unique identifier of the file containing the result"""

    filename: str
    """Name of the file containing the result"""

    score: float
    """Relevance score for this search result"""

    attributes: Optional[Dict[str, Union[str, float, bool]]] = None
    """(Optional) Key-value attributes associated with the file"""


class VectorStoreSearchResponse(BaseModel):
    data: List[Data]
    """List of search result objects"""

    has_more: bool
    """Whether there are more results available beyond this page"""

    object: str
    """Object type identifier for the search results page"""

    search_query: List[str]
    """The original search query that was executed"""

    next_page: Optional[str] = None
    """(Optional) Token for retrieving the next page of results"""
