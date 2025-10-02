# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .trace import Trace

__all__ = ["TelemetryQueryTracesResponse"]

TelemetryQueryTracesResponse: TypeAlias = List[Trace]
