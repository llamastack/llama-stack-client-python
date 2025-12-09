# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .toolgroup_list_response import ToolgroupListResponse

__all__ = ["ListToolGroupsResponse"]


class ListToolGroupsResponse(BaseModel):
    """Response containing a list of tool groups."""

    data: ToolgroupListResponse
