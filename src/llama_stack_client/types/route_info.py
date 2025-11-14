# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RouteInfo"]


class RouteInfo(BaseModel):
    method: str

    provider_types: List[str]

    route: str
