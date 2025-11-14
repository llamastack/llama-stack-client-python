# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .provider_list_response import ProviderListResponse

__all__ = ["ListProvidersResponse"]


class ListProvidersResponse(BaseModel):
    data: ProviderListResponse
