# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .span_with_status import SpanWithStatus

__all__ = ["TelemetryGetSpanTreeResponse"]

TelemetryGetSpanTreeResponse: TypeAlias = Dict[str, SpanWithStatus]
