# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RouteListParams"]


class RouteListParams(TypedDict, total=False):
    api_filter: Optional[Literal["v1", "v1alpha", "v1beta", "deprecated"]]
