# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .interleaved_content import InterleavedContent

__all__ = ["UserMessage"]


class UserMessage(TypedDict, total=False):
    content: Required[InterleavedContent]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""

    context: InterleavedContent
    """(Optional) This field is used internally by Llama Stack to pass RAG context.

    This field may be removed in the API in the future.
    """
