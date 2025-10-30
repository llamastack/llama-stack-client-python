# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.interleaved_content import InterleavedContent

__all__ = ["ToolResponseParam"]


class ToolResponseParam(TypedDict, total=False):
    call_id: Required[str]
    """Unique identifier for the tool call this response is for"""

    content: Required[InterleavedContent]
    """The response content from the tool"""

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]
    """Name of the tool that was invoked"""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Additional metadata about the tool response"""
