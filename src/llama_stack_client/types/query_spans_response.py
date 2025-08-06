# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .telemetry_query_spans_response import TelemetryQuerySpansResponse

__all__ = ["QuerySpansResponse"]


class QuerySpansResponse(BaseModel):
    data: TelemetryQuerySpansResponse
    """List of spans matching the query criteria"""
