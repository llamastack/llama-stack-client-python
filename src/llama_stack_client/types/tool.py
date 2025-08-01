# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tool", "Parameter"]


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


class Tool(BaseModel):
    description: str
    """Human-readable description of what the tool does"""

    identifier: str

    parameters: List[Parameter]
    """List of parameters this tool accepts"""

    provider_id: str

    toolgroup_id: str
    """ID of the tool group this tool belongs to"""

    type: Literal["tool"]
    """Type of resource, always 'tool'"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata about the tool"""

    provider_resource_id: Optional[str] = None
