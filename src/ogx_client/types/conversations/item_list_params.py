# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ItemListParams"]


class ItemListParams(TypedDict, total=False):
    after: Optional[str]

    include: Optional[
        List[
            Literal[
                "web_search_call.action.sources",
                "code_interpreter_call.outputs",
                "computer_call_output.output.image_url",
                "file_search_call.results",
                "message.input_image.image_url",
                "message.output_text.logprobs",
                "reasoning.encrypted_content",
            ]
        ]
    ]

    limit: Optional[int]

    order: Optional[Literal["asc", "desc"]]
