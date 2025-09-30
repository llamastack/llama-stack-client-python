# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .model_list_response import ModelListResponse

__all__ = ["ListModelsResponse"]


class ListModelsResponse(BaseModel):
    data: ModelListResponse
