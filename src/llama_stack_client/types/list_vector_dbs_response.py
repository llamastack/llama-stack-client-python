# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .vector_db_list_response import VectorDBListResponse

__all__ = ["ListVectorDBsResponse"]


class ListVectorDBsResponse(BaseModel):
    data: VectorDBListResponse
    """List of vector databases"""
