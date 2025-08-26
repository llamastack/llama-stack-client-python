# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ToolDefParam", "Parameter"]


class Parameter(TypedDict, total=False):
    description: Required[str]
    """Human-readable description of what the parameter does"""

    name: Required[str]
    """Name of the parameter"""

    parameter_type: Required[str]
    """Type of the parameter (e.g., string, integer)"""

    required: Required[bool]
    """Whether this parameter is required for tool invocation"""

    default: Union[bool, float, str, Iterable[object], object, None]
    """(Optional) Default value for the parameter if not provided"""


class ToolDefParam(TypedDict, total=False):
    name: Required[str]
    """Name of the tool"""

    description: str
    """(Optional) Human-readable description of what the tool does"""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Additional metadata about the tool"""

    parameters: Iterable[Parameter]
    """(Optional) List of parameters this tool accepts"""
