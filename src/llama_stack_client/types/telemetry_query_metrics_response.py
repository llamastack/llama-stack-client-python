# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "TelemetryQueryMetricsResponse",
    "TelemetryQueryMetricsResponseItem",
    "TelemetryQueryMetricsResponseItemLabel",
    "TelemetryQueryMetricsResponseItemValue",
]


class TelemetryQueryMetricsResponseItemLabel(BaseModel):
    name: str
    """The name of the label"""

    value: str
    """The value of the label"""


class TelemetryQueryMetricsResponseItemValue(BaseModel):
    timestamp: int
    """Unix timestamp when the metric value was recorded"""

    unit: str

    value: float
    """The numeric value of the metric at this timestamp"""


class TelemetryQueryMetricsResponseItem(BaseModel):
    labels: List[TelemetryQueryMetricsResponseItemLabel]
    """List of labels associated with this metric series"""

    metric: str
    """The name of the metric"""

    values: List[TelemetryQueryMetricsResponseItemValue]
    """List of data points in chronological order"""


TelemetryQueryMetricsResponse: TypeAlias = List[TelemetryQueryMetricsResponseItem]
