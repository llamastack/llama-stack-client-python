# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .metric_label_matcher_param import MetricLabelMatcherParam
from .metric_query_type_param import MetricQueryTypeParam

__all__ = ["TelemetryQueryMetricsParams"]


class TelemetryQueryMetricsParams(TypedDict, total=False):
    metric_name: Required[str]
    """The name of the metric to query"""

    start_time: Required[int]
    """The start time for the query (Unix timestamp)"""

    end_time: int
    """(Optional) The end time for the query (Unix timestamp)"""

    granularity: str
    """(Optional) The granularity of the query (e.g., '1d', '1h')"""

    query_type: MetricQueryTypeParam
    """(Optional) The type of metric query to perform"""

    label_matchers: Iterable[MetricLabelMatcherParam]
    """(Optional) Label matchers to filter the metrics"""
