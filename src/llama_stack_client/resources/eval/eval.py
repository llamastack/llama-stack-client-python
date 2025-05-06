# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .benchmarks.benchmarks import (
    BenchmarksResource,
    AsyncBenchmarksResource,
    BenchmarksResourceWithRawResponse,
    AsyncBenchmarksResourceWithRawResponse,
    BenchmarksResourceWithStreamingResponse,
    AsyncBenchmarksResourceWithStreamingResponse,
)

__all__ = ["EvalResource", "AsyncEvalResource"]


class EvalResource(SyncAPIResource):
    @cached_property
    def benchmarks(self) -> BenchmarksResource:
        return BenchmarksResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return EvalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return EvalResourceWithStreamingResponse(self)


class AsyncEvalResource(AsyncAPIResource):
    @cached_property
    def benchmarks(self) -> AsyncBenchmarksResource:
        return AsyncBenchmarksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncEvalResourceWithStreamingResponse(self)


class EvalResourceWithRawResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

    @cached_property
    def benchmarks(self) -> BenchmarksResourceWithRawResponse:
        return BenchmarksResourceWithRawResponse(self._eval.benchmarks)


class AsyncEvalResourceWithRawResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

    @cached_property
    def benchmarks(self) -> AsyncBenchmarksResourceWithRawResponse:
        return AsyncBenchmarksResourceWithRawResponse(self._eval.benchmarks)


class EvalResourceWithStreamingResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

    @cached_property
    def benchmarks(self) -> BenchmarksResourceWithStreamingResponse:
        return BenchmarksResourceWithStreamingResponse(self._eval.benchmarks)


class AsyncEvalResourceWithStreamingResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

    @cached_property
    def benchmarks(self) -> AsyncBenchmarksResourceWithStreamingResponse:
        return AsyncBenchmarksResourceWithStreamingResponse(self._eval.benchmarks)
