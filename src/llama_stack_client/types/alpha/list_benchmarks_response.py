# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .benchmark_list_response import BenchmarkListResponse

__all__ = ["ListBenchmarksResponse"]


class ListBenchmarksResponse(BaseModel):
    """Response containing a list of benchmark objects."""

    data: BenchmarkListResponse
    """List of benchmark objects."""
