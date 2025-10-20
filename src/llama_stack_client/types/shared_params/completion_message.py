# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .tool_call import ToolCall
from .interleaved_content import InterleavedContent

__all__ = ["CompletionMessage"]


class CompletionMessage(TypedDict, total=False):
    content: Required[InterleavedContent]
    """The content of the model's response"""

    role: Required[Literal["assistant"]]
    """Must be "assistant" to identify this as the model's response"""

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]
    """Reason why the model stopped generating.

    Options are: - `StopReason.end_of_turn`: The model finished generating the
    entire response. - `StopReason.end_of_message`: The model finished generating
    but generated a partial response -- usually, a tool call. The user may call the
    tool and continue the conversation with the tool's response. -
    `StopReason.out_of_tokens`: The model ran out of token budget.
    """

    tool_calls: Iterable[ToolCall]
    """List of tool calls. Each tool call is a ToolCall object."""
