# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .._base_client import make_request_options
from ..types.shared.health_info import HealthInfo
from ..types.shared.version_info import VersionInfo

__all__ = ["InspectResource", "AsyncInspectResource"]


class InspectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InspectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return InspectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InspectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return InspectResourceWithStreamingResponse(self)

    def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthInfo:
        """Get the current health status of the service."""
        return self._get(
            "/v1/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthInfo,
        )

    def version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionInfo:
        """Get the version of the service."""
        return self._get(
            "/v1/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionInfo,
        )


class AsyncInspectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInspectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInspectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInspectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncInspectResourceWithStreamingResponse(self)

    async def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthInfo:
        """Get the current health status of the service."""
        return await self._get(
            "/v1/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthInfo,
        )

    async def version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionInfo:
        """Get the version of the service."""
        return await self._get(
            "/v1/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionInfo,
        )


class InspectResourceWithRawResponse:
    def __init__(self, inspect: InspectResource) -> None:
        self._inspect = inspect

        self.health = to_raw_response_wrapper(
            inspect.health,
        )
        self.version = to_raw_response_wrapper(
            inspect.version,
        )


class AsyncInspectResourceWithRawResponse:
    def __init__(self, inspect: AsyncInspectResource) -> None:
        self._inspect = inspect

        self.health = async_to_raw_response_wrapper(
            inspect.health,
        )
        self.version = async_to_raw_response_wrapper(
            inspect.version,
        )


class InspectResourceWithStreamingResponse:
    def __init__(self, inspect: InspectResource) -> None:
        self._inspect = inspect

        self.health = to_streamed_response_wrapper(
            inspect.health,
        )
        self.version = to_streamed_response_wrapper(
            inspect.version,
        )


class AsyncInspectResourceWithStreamingResponse:
    def __init__(self, inspect: AsyncInspectResource) -> None:
        self._inspect = inspect

        self.health = async_to_streamed_response_wrapper(
            inspect.health,
        )
        self.version = async_to_streamed_response_wrapper(
            inspect.version,
        )
