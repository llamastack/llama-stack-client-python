# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...._base_client import make_request_options
from ....types.eval.benchmarks import job_run_params
from ....types.eval.benchmarks.job import Job
from ....types.eval.evaluate_response import EvaluateResponse
from ....types.eval.benchmark_config_param import BenchmarkConfigParam

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        job_id: str,
        *,
        benchmark_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
        """
        Get the status of a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    def cancel(
        self,
        job_id: str,
        *,
        benchmark_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancel a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def result(
        self,
        job_id: str,
        *,
        benchmark_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """
        Get the result of a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}/result",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    def run(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
        """
        Run an evaluation on a benchmark.

        Args:
          benchmark_config: The configuration for the benchmark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._post(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs",
            body=maybe_transform({"benchmark_config": benchmark_config}, job_run_params.JobRunParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        job_id: str,
        *,
        benchmark_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
        """
        Get the status of a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    async def cancel(
        self,
        job_id: str,
        *,
        benchmark_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancel a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def result(
        self,
        job_id: str,
        *,
        benchmark_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """
        Get the result of a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}/result",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    async def run(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
        """
        Run an evaluation on a benchmark.

        Args:
          benchmark_config: The configuration for the benchmark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._post(
            f"/v1/eval/benchmarks/{benchmark_id}/jobs",
            body=await async_maybe_transform({"benchmark_config": benchmark_config}, job_run_params.JobRunParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            jobs.cancel,
        )
        self.result = to_raw_response_wrapper(
            jobs.result,
        )
        self.run = to_raw_response_wrapper(
            jobs.run,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            jobs.cancel,
        )
        self.result = async_to_raw_response_wrapper(
            jobs.result,
        )
        self.run = async_to_raw_response_wrapper(
            jobs.run,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            jobs.cancel,
        )
        self.result = to_streamed_response_wrapper(
            jobs.result,
        )
        self.run = to_streamed_response_wrapper(
            jobs.run,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            jobs.cancel,
        )
        self.result = async_to_streamed_response_wrapper(
            jobs.result,
        )
        self.run = async_to_streamed_response_wrapper(
            jobs.run,
        )
