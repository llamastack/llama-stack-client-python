# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["InputItemListParams"]


class InputItemListParams(TypedDict, total=False):
    after: str
    """An item ID to list items after, used for pagination."""

    before: str
    """An item ID to list items before, used for pagination."""

    include: SequenceNotStr[str]
    """Additional fields to include in the response."""

    limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """

    order: Literal["asc", "desc"]
    """The order to return the input items in. Default is desc."""
