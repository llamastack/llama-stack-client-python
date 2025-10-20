# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .telemetry_query_spans_response import TelemetryQuerySpansResponse

__all__ = ["QuerySpansResponse"]


class QuerySpansResponse(BaseModel):
    data: TelemetryQuerySpansResponse
    """List of spans matching the query criteria"""
