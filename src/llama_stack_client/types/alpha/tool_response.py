# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.interleaved_content import InterleavedContent

__all__ = ["ToolResponse"]


class ToolResponse(BaseModel):
    call_id: str
    """Unique identifier for the tool call this response is for"""

    content: InterleavedContent
    """The response content from the tool"""

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]
    """Name of the tool that was invoked"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata about the tool response"""
