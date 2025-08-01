# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["ToolDef", "Parameter"]


class Parameter(BaseModel):
    description: str
    """Human-readable description of what the parameter does"""

    name: str
    """Name of the parameter"""

    parameter_type: str
    """Type of the parameter (e.g., string, integer)"""

    required: bool
    """Whether this parameter is required for tool invocation"""

    default: Union[bool, float, str, List[object], object, None] = None
    """(Optional) Default value for the parameter if not provided"""


class ToolDef(BaseModel):
    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Human-readable description of what the tool does"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata about the tool"""

    parameters: Optional[List[Parameter]] = None
    """(Optional) List of parameters this tool accepts"""
