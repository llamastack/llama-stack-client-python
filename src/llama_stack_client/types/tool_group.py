# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolGroup", "McpEndpoint"]


class McpEndpoint(BaseModel):
    """A URL reference to external content."""

    uri: str


class ToolGroup(BaseModel):
    """A group of related tools managed together."""

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
