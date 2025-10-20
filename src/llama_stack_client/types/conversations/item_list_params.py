# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemListParams"]


class ItemListParams(TypedDict, total=False):
    after: Required[Union[str, object]]
    """An item ID to list items after, used in pagination."""

    include: Required[
        Union[
            List[
                Literal[
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ],
            object,
        ]
    ]
    """Specify additional output data to include in the response."""

    limit: Required[Union[int, object]]
    """A limit on the number of objects to be returned (1-100, default 20)."""

    order: Required[Union[Literal["asc", "desc"], object]]
    """The order to return items in (asc or desc, default desc)."""
