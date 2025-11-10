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
from ..types.tool_group import ToolGroup
from ..types.toolgroup_list_response import ToolgroupListResponse

__all__ = ["ToolgroupsResource", "AsyncToolgroupsResource"]


class ToolgroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolgroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ToolgroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolgroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ToolgroupsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolgroupListResponse:
        """List tool groups with optional provider."""
        return self._get(
            "/v1/toolgroups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ToolgroupListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ToolgroupListResponse], DataWrapper[ToolgroupListResponse]),
        )

    def get(
        self,
        toolgroup_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolGroup:
        """
        Get a tool group by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not toolgroup_id:
            raise ValueError(f"Expected a non-empty value for `toolgroup_id` but received {toolgroup_id!r}")
        return self._get(
            f"/v1/toolgroups/{toolgroup_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGroup,
        )


class AsyncToolgroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolgroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolgroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolgroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncToolgroupsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolgroupListResponse:
        """List tool groups with optional provider."""
        return await self._get(
            "/v1/toolgroups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ToolgroupListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ToolgroupListResponse], DataWrapper[ToolgroupListResponse]),
        )

    async def get(
        self,
        toolgroup_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolGroup:
        """
        Get a tool group by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not toolgroup_id:
            raise ValueError(f"Expected a non-empty value for `toolgroup_id` but received {toolgroup_id!r}")
        return await self._get(
            f"/v1/toolgroups/{toolgroup_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGroup,
        )


class ToolgroupsResourceWithRawResponse:
    def __init__(self, toolgroups: ToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = to_raw_response_wrapper(
            toolgroups.list,
        )
        self.get = to_raw_response_wrapper(
            toolgroups.get,
        )


class AsyncToolgroupsResourceWithRawResponse:
    def __init__(self, toolgroups: AsyncToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = async_to_raw_response_wrapper(
            toolgroups.list,
        )
        self.get = async_to_raw_response_wrapper(
            toolgroups.get,
        )


class ToolgroupsResourceWithStreamingResponse:
    def __init__(self, toolgroups: ToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = to_streamed_response_wrapper(
            toolgroups.list,
        )
        self.get = to_streamed_response_wrapper(
            toolgroups.get,
        )


class AsyncToolgroupsResourceWithStreamingResponse:
    def __init__(self, toolgroups: AsyncToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = async_to_streamed_response_wrapper(
            toolgroups.list,
        )
        self.get = async_to_streamed_response_wrapper(
            toolgroups.get,
        )
