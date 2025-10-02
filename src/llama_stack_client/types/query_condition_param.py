# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryConditionParam"]


class QueryConditionParam(TypedDict, total=False):
    key: Required[str]
    """The attribute key to filter on"""

    op: Required[Literal["eq", "ne", "gt", "lt"]]
    """The comparison operator to apply"""

    value: Required[Union[bool, float, str, Iterable[object], object, None]]
    """The value to compare against"""
