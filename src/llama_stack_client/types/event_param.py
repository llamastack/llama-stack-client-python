# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EventParam",
    "UnstructuredLogEvent",
    "MetricEvent",
    "StructuredLogEvent",
    "StructuredLogEventPayload",
    "StructuredLogEventPayloadSpanStartPayload",
    "StructuredLogEventPayloadSpanEndPayload",
]


class UnstructuredLogEvent(TypedDict, total=False):
    message: Required[str]
    """The log message text"""

    severity: Required[Literal["verbose", "debug", "info", "warn", "error", "critical"]]
    """The severity level of the log message"""

    span_id: Required[str]
    """Unique identifier for the span this event belongs to"""

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp when the event occurred"""

    trace_id: Required[str]
    """Unique identifier for the trace this event belongs to"""

    type: Required[Literal["unstructured_log"]]
    """Event type identifier set to UNSTRUCTURED_LOG"""

    attributes: Dict[str, Union[str, float, bool, None]]
    """(Optional) Key-value pairs containing additional metadata about the event"""


class MetricEvent(TypedDict, total=False):
    metric: Required[str]
    """The name of the metric being measured"""

    span_id: Required[str]
    """Unique identifier for the span this event belongs to"""

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp when the event occurred"""

    trace_id: Required[str]
    """Unique identifier for the trace this event belongs to"""

    type: Required[Literal["metric"]]
    """Event type identifier set to METRIC"""

    unit: Required[str]
    """The unit of measurement for the metric value"""

    value: Required[float]
    """The numeric value of the metric measurement"""

    attributes: Dict[str, Union[str, float, bool, None]]
    """(Optional) Key-value pairs containing additional metadata about the event"""


class StructuredLogEventPayloadSpanStartPayload(TypedDict, total=False):
    name: Required[str]
    """Human-readable name describing the operation this span represents"""

    type: Required[Literal["span_start"]]
    """Payload type identifier set to SPAN_START"""

    parent_span_id: str
    """(Optional) Unique identifier for the parent span, if this is a child span"""


class StructuredLogEventPayloadSpanEndPayload(TypedDict, total=False):
    status: Required[Literal["ok", "error"]]
    """The final status of the span indicating success or failure"""

    type: Required[Literal["span_end"]]
    """Payload type identifier set to SPAN_END"""


StructuredLogEventPayload: TypeAlias = Union[
    StructuredLogEventPayloadSpanStartPayload, StructuredLogEventPayloadSpanEndPayload
]


class StructuredLogEvent(TypedDict, total=False):
    payload: Required[StructuredLogEventPayload]
    """The structured payload data for the log event"""

    span_id: Required[str]
    """Unique identifier for the span this event belongs to"""

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp when the event occurred"""

    trace_id: Required[str]
    """Unique identifier for the trace this event belongs to"""

    type: Required[Literal["structured_log"]]
    """Event type identifier set to STRUCTURED_LOG"""

    attributes: Dict[str, Union[str, float, bool, None]]
    """(Optional) Key-value pairs containing additional metadata about the event"""


EventParam: TypeAlias = Union[UnstructuredLogEvent, MetricEvent, StructuredLogEvent]
