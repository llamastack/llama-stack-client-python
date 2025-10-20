# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["ToolInvocationResult"]


class ToolInvocationResult(BaseModel):
    content: Optional[InterleavedContent] = None
    """(Optional) The output content from the tool execution"""

    error_code: Optional[int] = None
    """(Optional) Numeric error code if the tool execution failed"""

    error_message: Optional[str] = None
    """(Optional) Error message if the tool execution failed"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata about the tool execution"""
