# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RouteInfo"]


class RouteInfo(BaseModel):
    method: str
    """HTTP method for the route"""

    provider_types: List[str]
    """List of provider types that implement this route"""

    route: str
    """The API endpoint path"""
