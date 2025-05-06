# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.inspect_list_routes_response import InspectListRoutesResponse

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

    def list_routes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InspectListRoutesResponse:
        return self._get(
            "/v1/inspect/routes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InspectListRoutesResponse,
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

    async def list_routes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InspectListRoutesResponse:
        return await self._get(
            "/v1/inspect/routes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InspectListRoutesResponse,
        )


class InspectResourceWithRawResponse:
    def __init__(self, inspect: InspectResource) -> None:
        self._inspect = inspect

        self.list_routes = to_raw_response_wrapper(
            inspect.list_routes,
        )


class AsyncInspectResourceWithRawResponse:
    def __init__(self, inspect: AsyncInspectResource) -> None:
        self._inspect = inspect

        self.list_routes = async_to_raw_response_wrapper(
            inspect.list_routes,
        )


class InspectResourceWithStreamingResponse:
    def __init__(self, inspect: InspectResource) -> None:
        self._inspect = inspect

        self.list_routes = to_streamed_response_wrapper(
            inspect.list_routes,
        )


class AsyncInspectResourceWithStreamingResponse:
    def __init__(self, inspect: AsyncInspectResource) -> None:
        self._inspect = inspect

        self.list_routes = async_to_streamed_response_wrapper(
            inspect.list_routes,
        )
