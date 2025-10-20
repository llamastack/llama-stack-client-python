# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .interleaved_content import InterleavedContent

__all__ = ["UserMessage"]


class UserMessage(BaseModel):
    content: InterleavedContent
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    context: Optional[InterleavedContent] = None
    """(Optional) This field is used internally by Llama Stack to pass RAG context.

    This field may be removed in the API in the future.
    """
