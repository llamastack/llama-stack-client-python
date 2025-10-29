# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RouteListParams"]


class RouteListParams(TypedDict, total=False):
    api_filter: Literal["v1", "v1alpha", "v1beta", "deprecated"]
    """Optional filter to control which routes are returned.

    Can be an API level ('v1', 'v1alpha', 'v1beta') to show non-deprecated routes at
    that level, or 'deprecated' to show deprecated routes across all levels. If not
    specified, returns only non-deprecated v1 routes.
    """
