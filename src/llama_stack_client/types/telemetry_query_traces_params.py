# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .query_condition_param import QueryConditionParam

__all__ = ["TelemetryQueryTracesParams"]


class TelemetryQueryTracesParams(TypedDict, total=False):
    attribute_filters: Iterable[QueryConditionParam]
    """The attribute filters to apply to the traces."""

    limit: int
    """The limit of traces to return."""

    offset: int
    """The offset of the traces to return."""

    order_by: SequenceNotStr[str]
    """The order by of the traces to return."""
