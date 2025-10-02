# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .benchmark_list_response import BenchmarkListResponse

__all__ = ["ListBenchmarksResponse"]


class ListBenchmarksResponse(BaseModel):
    data: BenchmarkListResponse
