# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.alpha import (
    eval_run_eval_params,
    eval_evaluate_rows_params,
    eval_run_eval_alpha_params,
    eval_evaluate_rows_alpha_params,
)
from ...._base_client import make_request_options
from ....types.alpha.job import Job
from ....types.alpha.evaluate_response import EvaluateResponse
from ....types.alpha.benchmark_config_param import BenchmarkConfigParam

__all__ = ["EvalResource", "AsyncEvalResource"]


class EvalResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

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

    def evaluate_rows(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        input_rows: Iterable[Dict[str, object]],
        scoring_functions: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateResponse:
        """
        Evaluate a list of rows on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/evaluations",
            body=maybe_transform(
                {
                    "benchmark_config": benchmark_config,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                eval_evaluate_rows_params.EvalEvaluateRowsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    def evaluate_rows_alpha(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        input_rows: Iterable[Dict[str, object]],
        scoring_functions: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateResponse:
        """
        Evaluate a list of rows on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/evaluations",
            body=maybe_transform(
                {
                    "benchmark_config": benchmark_config,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                eval_evaluate_rows_alpha_params.EvalEvaluateRowsAlphaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    def run_eval(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Run an evaluation on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/jobs",
            body=maybe_transform({"benchmark_config": benchmark_config}, eval_run_eval_params.EvalRunEvalParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    def run_eval_alpha(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Run an evaluation on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/jobs",
            body=maybe_transform(
                {"benchmark_config": benchmark_config}, eval_run_eval_alpha_params.EvalRunEvalAlphaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class AsyncEvalResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

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

    async def evaluate_rows(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        input_rows: Iterable[Dict[str, object]],
        scoring_functions: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateResponse:
        """
        Evaluate a list of rows on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/evaluations",
            body=await async_maybe_transform(
                {
                    "benchmark_config": benchmark_config,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                eval_evaluate_rows_params.EvalEvaluateRowsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    async def evaluate_rows_alpha(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        input_rows: Iterable[Dict[str, object]],
        scoring_functions: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateResponse:
        """
        Evaluate a list of rows on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/evaluations",
            body=await async_maybe_transform(
                {
                    "benchmark_config": benchmark_config,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                eval_evaluate_rows_alpha_params.EvalEvaluateRowsAlphaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    async def run_eval(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Run an evaluation on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/jobs",
            body=await async_maybe_transform(
                {"benchmark_config": benchmark_config}, eval_run_eval_params.EvalRunEvalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    async def run_eval_alpha(
        self,
        benchmark_id: str,
        *,
        benchmark_config: BenchmarkConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Run an evaluation on a benchmark.

        Args:
          benchmark_config: A benchmark configuration for evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._post(
            f"/v1alpha/eval/benchmarks/{benchmark_id}/jobs",
            body=await async_maybe_transform(
                {"benchmark_config": benchmark_config}, eval_run_eval_alpha_params.EvalRunEvalAlphaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class EvalResourceWithRawResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = to_raw_response_wrapper(
            eval.evaluate_rows,
        )
        self.evaluate_rows_alpha = to_raw_response_wrapper(
            eval.evaluate_rows_alpha,
        )
        self.run_eval = to_raw_response_wrapper(
            eval.run_eval,
        )
        self.run_eval_alpha = to_raw_response_wrapper(
            eval.run_eval_alpha,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._eval.jobs)


class AsyncEvalResourceWithRawResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = async_to_raw_response_wrapper(
            eval.evaluate_rows,
        )
        self.evaluate_rows_alpha = async_to_raw_response_wrapper(
            eval.evaluate_rows_alpha,
        )
        self.run_eval = async_to_raw_response_wrapper(
            eval.run_eval,
        )
        self.run_eval_alpha = async_to_raw_response_wrapper(
            eval.run_eval_alpha,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._eval.jobs)


class EvalResourceWithStreamingResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = to_streamed_response_wrapper(
            eval.evaluate_rows,
        )
        self.evaluate_rows_alpha = to_streamed_response_wrapper(
            eval.evaluate_rows_alpha,
        )
        self.run_eval = to_streamed_response_wrapper(
            eval.run_eval,
        )
        self.run_eval_alpha = to_streamed_response_wrapper(
            eval.run_eval_alpha,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._eval.jobs)


class AsyncEvalResourceWithStreamingResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = async_to_streamed_response_wrapper(
            eval.evaluate_rows,
        )
        self.evaluate_rows_alpha = async_to_streamed_response_wrapper(
            eval.evaluate_rows_alpha,
        )
        self.run_eval = async_to_streamed_response_wrapper(
            eval.run_eval,
        )
        self.run_eval_alpha = async_to_streamed_response_wrapper(
            eval.run_eval_alpha,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._eval.jobs)
