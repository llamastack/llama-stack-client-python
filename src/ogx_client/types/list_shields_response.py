# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .shield_list_response import ShieldListResponse

__all__ = ["ListShieldsResponse"]


class ListShieldsResponse(BaseModel):
    """Response containing a list of all shields."""

    data: ShieldListResponse
    """List of shield objects"""
