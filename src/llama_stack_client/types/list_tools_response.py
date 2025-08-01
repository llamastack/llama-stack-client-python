# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .tool_list_response import ToolListResponse

__all__ = ["ListToolsResponse"]


class ListToolsResponse(BaseModel):
    data: ToolListResponse
    """List of tools"""
