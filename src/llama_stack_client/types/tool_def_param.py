# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ToolDefParam"]


class ToolDefParam(TypedDict, total=False):
    name: Required[str]
    """Name of the tool"""

    description: str
    """(Optional) Human-readable description of what the tool does"""

    input_schema: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) JSON Schema for tool inputs (MCP inputSchema)"""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Additional metadata about the tool"""

    output_schema: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) JSON Schema for tool outputs (MCP outputSchema)"""

    toolgroup_id: str
    """(Optional) ID of the tool group this tool belongs to"""
