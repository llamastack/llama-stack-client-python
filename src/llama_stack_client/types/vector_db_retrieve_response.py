# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorDBRetrieveResponse"]


class VectorDBRetrieveResponse(BaseModel):
    embedding_dimension: int
    """Dimension of the embedding vectors"""

    embedding_model: str
    """Name of the embedding model to use for vector generation"""

    identifier: str

    provider_id: str

    type: Literal["vector_db"]
    """Type of resource, always 'vector_db' for vector databases"""

    provider_resource_id: Optional[str] = None

    vector_db_name: Optional[str] = None
