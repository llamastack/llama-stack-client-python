# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ToolRuntimeListToolsParams", "McpEndpoint"]


class ToolRuntimeListToolsParams(TypedDict, total=False):
    authorization: Optional[str]

    mcp_endpoint: Optional[McpEndpoint]
    """A URL reference to external content."""

    tool_group_id: Optional[str]


class McpEndpoint(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]
