# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorDBRetrieveResponse"]


class VectorDBRetrieveResponse(BaseModel):
    embedding_dimension: int

    embedding_model: str

    identifier: str

    provider_id: str

    type: Literal["vector_db"]

    provider_resource_id: Optional[str] = None

    vector_db_name: Optional[str] = None
