# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import DataWrapper
from .._base_client import make_request_options
from ..types.scoring_fn import ScoringFn
from ..types.scoring_function_list_response import ScoringFunctionListResponse

__all__ = ["ScoringFunctionsResource", "AsyncScoringFunctionsResource"]


class ScoringFunctionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoringFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ScoringFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoringFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ScoringFunctionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        scoring_fn_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringFn:
        """
        Get a scoring function by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scoring_fn_id:
            raise ValueError(f"Expected a non-empty value for `scoring_fn_id` but received {scoring_fn_id!r}")
        return self._get(
            f"/v1/scoring-functions/{scoring_fn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringFn,
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
    ) -> ScoringFunctionListResponse:
        """List all scoring functions."""
        return self._get(
            "/v1/scoring-functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ScoringFunctionListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScoringFunctionListResponse], DataWrapper[ScoringFunctionListResponse]),
        )


class AsyncScoringFunctionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoringFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoringFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoringFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncScoringFunctionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        scoring_fn_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringFn:
        """
        Get a scoring function by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scoring_fn_id:
            raise ValueError(f"Expected a non-empty value for `scoring_fn_id` but received {scoring_fn_id!r}")
        return await self._get(
            f"/v1/scoring-functions/{scoring_fn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringFn,
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
    ) -> ScoringFunctionListResponse:
        """List all scoring functions."""
        return await self._get(
            "/v1/scoring-functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ScoringFunctionListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScoringFunctionListResponse], DataWrapper[ScoringFunctionListResponse]),
        )


class ScoringFunctionsResourceWithRawResponse:
    def __init__(self, scoring_functions: ScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = to_raw_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            scoring_functions.list,
        )


class AsyncScoringFunctionsResourceWithRawResponse:
    def __init__(self, scoring_functions: AsyncScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = async_to_raw_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            scoring_functions.list,
        )


class ScoringFunctionsResourceWithStreamingResponse:
    def __init__(self, scoring_functions: ScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = to_streamed_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            scoring_functions.list,
        )


class AsyncScoringFunctionsResourceWithStreamingResponse:
    def __init__(self, scoring_functions: AsyncScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = async_to_streamed_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            scoring_functions.list,
        )
