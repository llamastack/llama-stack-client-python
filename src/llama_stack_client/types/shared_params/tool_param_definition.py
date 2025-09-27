# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ToolParamDefinition"]


class ToolParamDefinition(TypedDict, total=False):
    param_type: Required[str]

    default: Union[bool, float, str, Iterable[object], object, None]

    description: str

    items: Union[bool, float, str, Iterable[object], object, None]

    required: bool

    title: str
