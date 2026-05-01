# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.route_info import RouteInfo

__all__ = ["RouteListResponse"]

RouteListResponse: TypeAlias = List[RouteInfo]
