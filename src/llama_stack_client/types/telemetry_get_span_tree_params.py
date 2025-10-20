# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["TelemetryGetSpanTreeParams"]


class TelemetryGetSpanTreeParams(TypedDict, total=False):
    attributes_to_return: SequenceNotStr[str]
    """The attributes to return in the tree."""

    max_depth: int
    """The maximum depth of the tree."""
