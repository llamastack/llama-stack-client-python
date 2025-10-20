# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolGroup", "McpEndpoint"]


class McpEndpoint(BaseModel):
    uri: str
    """The URL string pointing to the resource"""


class ToolGroup(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["tool_group"]
    """Type of resource, always 'tool_group'"""

    args: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional arguments for the tool group"""

    mcp_endpoint: Optional[McpEndpoint] = None
    """(Optional) Model Context Protocol endpoint for remote tools"""

    provider_resource_id: Optional[str] = None
