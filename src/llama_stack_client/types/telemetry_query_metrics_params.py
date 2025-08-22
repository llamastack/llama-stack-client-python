# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TelemetryQueryMetricsParams", "LabelMatcher"]


class TelemetryQueryMetricsParams(TypedDict, total=False):
    query_type: Required[Literal["range", "instant"]]
    """The type of query to perform."""

    start_time: Required[int]
    """The start time of the metric to query."""

    end_time: int
    """The end time of the metric to query."""

    granularity: str
    """The granularity of the metric to query."""

    label_matchers: Iterable[LabelMatcher]
    """The label matchers to apply to the metric."""


class LabelMatcher(TypedDict, total=False):
    name: Required[str]
    """The name of the label to match"""

    operator: Required[Literal["=", "!=", "=~", "!~"]]
    """The comparison operator to use for matching"""

    value: Required[str]
    """The value to match against"""
