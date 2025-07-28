# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["VectorDBListResponse", "VectorDBListResponseItem"]


class VectorDBListResponseItem(BaseModel):
    embedding_dimension: int

    embedding_model: str

    identifier: str

    provider_id: str

    type: Literal["vector_db"]

    provider_resource_id: Optional[str] = None

    vector_db_name: Optional[str] = None


VectorDBListResponse: TypeAlias = List[VectorDBListResponseItem]
