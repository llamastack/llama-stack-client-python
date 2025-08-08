# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["TelemetryQueryMetricsResponse", "MetricSeries", "MetricLabel", "MetricDataPoint"]


class MetricLabel(BaseModel):
    """A label associated with a metric.
    :param name: The name of the label
    :param value: The value of the label
    """

    name: str
    """The name of the label"""

    value: str
    """The value of the label"""


class MetricDataPoint(BaseModel):
    """A single data point in a metric time series.
    :param timestamp: Unix timestamp when the metric value was recorded
    :param value: The numeric value of the metric at this timestamp
    """

    timestamp: int
    """Unix timestamp when the metric value was recorded"""

    value: float
    """The numeric value of the metric at this timestamp"""


class MetricSeries(BaseModel):
    """A time series of metric data points.
    :param metric: The name of the metric
    :param labels: List of labels associated with this metric series
    :param values: List of data points in chronological order
    """

    metric: str
    """The name of the metric"""

    labels: List[MetricLabel]
    """List of labels associated with this metric series"""

    values: List[MetricDataPoint]
    """List of data points in chronological order"""


class TelemetryQueryMetricsResponse: TypeAlias = List[MetricSeries]
