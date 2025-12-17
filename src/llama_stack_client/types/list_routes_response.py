# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .route_list_response import RouteListResponse

__all__ = ["ListRoutesResponse"]


class ListRoutesResponse(BaseModel):
    """Response containing a list of all available API routes."""

    data: RouteListResponse
    """List of available API routes"""
