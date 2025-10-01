# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tool"]


class Tool(BaseModel):
    description: str
    """Human-readable description of what the tool does"""

    identifier: str

    provider_id: str

    toolgroup_id: str
    """ID of the tool group this tool belongs to"""

    type: Literal["tool"]
    """Type of resource, always 'tool'"""

    input_schema: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """JSON Schema for the tool's input parameters"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata about the tool"""

    output_schema: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """JSON Schema for the tool's output"""

    provider_resource_id: Optional[str] = None
