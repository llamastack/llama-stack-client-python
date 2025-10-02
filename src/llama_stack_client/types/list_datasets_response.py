# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .dataset_list_response import DatasetListResponse

__all__ = ["ListDatasetsResponse"]


class ListDatasetsResponse(BaseModel):
    data: DatasetListResponse
    """List of datasets"""
