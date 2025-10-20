# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["ToolDef"]


class ToolDef(BaseModel):
    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Human-readable description of what the tool does"""

    input_schema: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) JSON Schema for tool inputs (MCP inputSchema)"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata about the tool"""

    output_schema: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) JSON Schema for tool outputs (MCP outputSchema)"""

    toolgroup_id: Optional[str] = None
    """(Optional) ID of the tool group this tool belongs to"""
