# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolGroup", "McpEndpoint"]


class McpEndpoint(BaseModel):
    uri: str


class ToolGroup(BaseModel):
    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    args: Optional[Dict[str, object]] = None

    mcp_endpoint: Optional[McpEndpoint] = None
    """A URL reference to external content."""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["tool_group"]] = None
