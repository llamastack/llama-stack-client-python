# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, Type, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ...types.alpha import benchmark_register_params
from ..._base_client import make_request_options
from ...types.alpha.benchmark import Benchmark
from ...types.alpha.benchmark_list_response import BenchmarkListResponse

__all__ = ["BenchmarksResource", "AsyncBenchmarksResource"]


class BenchmarksResource(SyncAPIResource):
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

    def retrieve(
        self,
        benchmark_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Benchmark:
        """
        Get a benchmark by its ID.

        Args:
          benchmark_id: The ID of the benchmark to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return self._get(
            f"/v1alpha/eval/benchmarks/{benchmark_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListResponse:
        """List all benchmarks."""
        return self._get(
            "/v1alpha/eval/benchmarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[BenchmarkListResponse]._unwrapper,
            ),
            cast_to=cast(Type[BenchmarkListResponse], DataWrapper[BenchmarkListResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def register(
        self,
        *,
        benchmark_id: str,
        dataset_id: str,
        scoring_functions: SequenceNotStr[str],
        metadata: Optional[Dict[str, object]] | Omit = omit,
        provider_benchmark_id: Optional[str] | Omit = omit,
        provider_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Register a benchmark.

        Args:
          benchmark_id: The ID of the benchmark to register.

          dataset_id: The ID of the dataset to use for the benchmark.

          scoring_functions: The scoring functions to use for the benchmark.

          metadata: The metadata to use for the benchmark.

          provider_benchmark_id: The ID of the provider benchmark to use for the benchmark.

          provider_id: The ID of the provider to use for the benchmark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1alpha/eval/benchmarks",
            body=maybe_transform(
                {
                    "benchmark_id": benchmark_id,
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                    "metadata": metadata,
                    "provider_benchmark_id": provider_benchmark_id,
                    "provider_id": provider_id,
                },
                benchmark_register_params.BenchmarkRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def unregister(
        self,
        benchmark_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a benchmark.

        Args:
          benchmark_id: The ID of the benchmark to unregister.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1alpha/eval/benchmarks/{benchmark_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBenchmarksResource(AsyncAPIResource):
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

    async def retrieve(
        self,
        benchmark_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Benchmark:
        """
        Get a benchmark by its ID.

        Args:
          benchmark_id: The ID of the benchmark to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        return await self._get(
            f"/v1alpha/eval/benchmarks/{benchmark_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListResponse:
        """List all benchmarks."""
        return await self._get(
            "/v1alpha/eval/benchmarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[BenchmarkListResponse]._unwrapper,
            ),
            cast_to=cast(Type[BenchmarkListResponse], DataWrapper[BenchmarkListResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def register(
        self,
        *,
        benchmark_id: str,
        dataset_id: str,
        scoring_functions: SequenceNotStr[str],
        metadata: Optional[Dict[str, object]] | Omit = omit,
        provider_benchmark_id: Optional[str] | Omit = omit,
        provider_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Register a benchmark.

        Args:
          benchmark_id: The ID of the benchmark to register.

          dataset_id: The ID of the dataset to use for the benchmark.

          scoring_functions: The scoring functions to use for the benchmark.

          metadata: The metadata to use for the benchmark.

          provider_benchmark_id: The ID of the provider benchmark to use for the benchmark.

          provider_id: The ID of the provider to use for the benchmark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1alpha/eval/benchmarks",
            body=await async_maybe_transform(
                {
                    "benchmark_id": benchmark_id,
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                    "metadata": metadata,
                    "provider_benchmark_id": provider_benchmark_id,
                    "provider_id": provider_id,
                },
                benchmark_register_params.BenchmarkRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def unregister(
        self,
        benchmark_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a benchmark.

        Args:
          benchmark_id: The ID of the benchmark to unregister.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benchmark_id:
            raise ValueError(f"Expected a non-empty value for `benchmark_id` but received {benchmark_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1alpha/eval/benchmarks/{benchmark_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BenchmarksResourceWithRawResponse:
    def __init__(self, benchmarks: BenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.retrieve = to_raw_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            benchmarks.list,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                benchmarks.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                benchmarks.unregister,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncBenchmarksResourceWithRawResponse:
    def __init__(self, benchmarks: AsyncBenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.retrieve = async_to_raw_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            benchmarks.list,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                benchmarks.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                benchmarks.unregister,  # pyright: ignore[reportDeprecated],
            )
        )


class BenchmarksResourceWithStreamingResponse:
    def __init__(self, benchmarks: BenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.retrieve = to_streamed_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            benchmarks.list,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                benchmarks.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                benchmarks.unregister,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncBenchmarksResourceWithStreamingResponse:
    def __init__(self, benchmarks: AsyncBenchmarksResource) -> None:
        self._benchmarks = benchmarks

        self.retrieve = async_to_streamed_response_wrapper(
            benchmarks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            benchmarks.list,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                benchmarks.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                benchmarks.unregister,  # pyright: ignore[reportDeprecated],
            )
        )
