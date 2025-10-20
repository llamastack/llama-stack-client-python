# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolRuntimeListToolsParams", "McpEndpoint"]


class ToolRuntimeListToolsParams(TypedDict, total=False):
    mcp_endpoint: McpEndpoint
    """The MCP endpoint to use for the tool group."""

    tool_group_id: str
    """The ID of the tool group to list tools for."""


class McpEndpoint(TypedDict, total=False):
    uri: Required[str]
    """The URL string pointing to the resource"""
