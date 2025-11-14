# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
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
    type: Optional[Literal["auto"]] = None


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(BaseModel):
    chunk_overlap_tokens: Optional[int] = None

    max_chunk_size_tokens: Optional[int] = None


class ChunkingStrategyVectorStoreChunkingStrategyStatic(BaseModel):
    static: ChunkingStrategyVectorStoreChunkingStrategyStaticStatic
    """Configuration for static chunking strategy."""

    type: Optional[Literal["static"]] = None


ChunkingStrategy: TypeAlias = Annotated[
    Union[ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic],
    PropertyInfo(discriminator="type"),
]


class LastError(BaseModel):
    code: Literal["server_error", "rate_limit_exceeded"]

    message: str


class VectorStoreFile(BaseModel):
    id: str

    chunking_strategy: ChunkingStrategy
    """Automatic chunking strategy for vector store files."""

    created_at: int

    status: Literal["completed", "in_progress", "cancelled", "failed"]

    vector_store_id: str

    attributes: Optional[Dict[str, object]] = None

    last_error: Optional[LastError] = None
    """Error information for failed vector store file processing."""

    object: Optional[str] = None

    usage_bytes: Optional[int] = None
