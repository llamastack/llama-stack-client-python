# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.eval import benchmark_create_params, benchmark_evaluate_params
from ...._base_client import make_request_options
from ....types.eval.benchmark import Benchmark
from ....types.eval.evaluate_response import EvaluateResponse
from ....types.eval.benchmark_config_param import BenchmarkConfigParam
from ....types.eval.benchmark_list_response import BenchmarkListResponse

__all__ = ["BenchmarksResource", "AsyncBenchmarksResource"]


class BenchmarksResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BenchmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return BenchmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenchmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return BenchmarksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        benchmark_id: str,
        dataset_id: str,
        scoring_functions: List[str],
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_benchmark_id: str | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/eval/benchmarks",
            body=maybe_transform(
                {
                    "benchmark_id": benchmark_id,
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                    "metadata": metadata,
                    "provider_benchmark_id": provider_benchmark_id,
                    "provider_id": provider_id,
                },
                benchmark_create_params.BenchmarkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        benchmark_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Benchmark:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._get(
            f"/v1/eval/benchmarks/{benchmark_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Benchmark,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BenchmarkListResponse:
        return self._get(
            "/v1/eval/benchmarks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenchmarkListResponse,
        )

    def evaluate(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        input_rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        scoring_functions: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """
        Evaluate a list of rows on a benchmark.

        Args:
          benchmark_config: The configuration for the benchmark.

          input_rows: The rows to evaluate.

          scoring_functions: The scoring functions to use for the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._post(
            f"/v1/eval/benchmarks/{benchmark_id}/evaluations",
            body=maybe_transform(
                {
                    "benchmark_config": benchmark_config,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                benchmark_evaluate_params.BenchmarkEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )


class AsyncBenchmarksResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBenchmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenchmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenchmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncBenchmarksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        benchmark_id: str,
        dataset_id: str,
        scoring_functions: List[str],
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_benchmark_id: str | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/eval/benchmarks",
            body=await async_maybe_transform(
                {
                    "benchmark_id": benchmark_id,
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                    "metadata": metadata,
                    "provider_benchmark_id": provider_benchmark_id,
                    "provider_id": provider_id,
                },
                benchmark_create_params.BenchmarkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        benchmark_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Benchmark:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._get(
            f"/v1/eval/benchmarks/{benchmark_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Benchmark,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BenchmarkListResponse:
        return await self._get(
            "/v1/eval/benchmarks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenchmarkListResponse,
        )

    async def evaluate(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        input_rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        scoring_functions: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """
        Evaluate a list of rows on a benchmark.

        Args:
          benchmark_config: The configuration for the benchmark.

          input_rows: The rows to evaluate.

          scoring_functions: The scoring functions to use for the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._post(
            f"/v1/eval/benchmarks/{benchmark_id}/evaluations",
            body=await async_maybe_transform(
                {
                    "benchmark_config": benchmark_config,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                benchmark_evaluate_params.BenchmarkEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )


class BenchmarksResourceWithRawResponse:
    def __init__(self, benchmarks: BenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.create = to_raw_response_wrapper(
            benchmarks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            benchmarks.list,
        )
        self.evaluate = to_raw_response_wrapper(
            benchmarks.evaluate,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._benchmarks.jobs)


class AsyncBenchmarksResourceWithRawResponse:
    def __init__(self, benchmarks: AsyncBenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.create = async_to_raw_response_wrapper(
            benchmarks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            benchmarks.list,
        )
        self.evaluate = async_to_raw_response_wrapper(
            benchmarks.evaluate,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._benchmarks.jobs)


class BenchmarksResourceWithStreamingResponse:
    def __init__(self, benchmarks: BenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.create = to_streamed_response_wrapper(
            benchmarks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            benchmarks.list,
        )
        self.evaluate = to_streamed_response_wrapper(
            benchmarks.evaluate,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._benchmarks.jobs)


class AsyncBenchmarksResourceWithStreamingResponse:
    def __init__(self, benchmarks: AsyncBenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.create = async_to_streamed_response_wrapper(
            benchmarks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            benchmarks.list,
        )
        self.evaluate = async_to_streamed_response_wrapper(
            benchmarks.evaluate,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._benchmarks.jobs)
