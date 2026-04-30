# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ModerationCreateParams"]


class ModerationCreateParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str]]]
    """Input (or inputs) to classify. Can be a single string or an array of strings."""

    model: Optional[str]
    """The content moderation model to use.

    If not specified, the default shield will be used.
    """
