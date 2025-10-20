# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Union, Iterable, cast

import httpx

from ..types import toolgroup_register_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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

    def register(
        self,
        *,
        provider_id: str,
        toolgroup_id: str,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        mcp_endpoint: toolgroup_register_params.McpEndpoint | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Register a tool group.

        Args:
          provider_id: The ID of the provider to use for the tool group.

          toolgroup_id: The ID of the tool group to register.

          args: A dictionary of arguments to pass to the tool group.

          mcp_endpoint: The MCP endpoint to use for the tool group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/toolgroups",
            body=maybe_transform(
                {
                    "provider_id": provider_id,
                    "toolgroup_id": toolgroup_id,
                    "args": args,
                    "mcp_endpoint": mcp_endpoint,
                },
                toolgroup_register_params.ToolgroupRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unregister(
        self,
        toolgroup_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a tool group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not toolgroup_id:
            raise ValueError(f"Expected a non-empty value for `toolgroup_id` but received {toolgroup_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/toolgroups/{toolgroup_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

    async def register(
        self,
        *,
        provider_id: str,
        toolgroup_id: str,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        mcp_endpoint: toolgroup_register_params.McpEndpoint | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Register a tool group.

        Args:
          provider_id: The ID of the provider to use for the tool group.

          toolgroup_id: The ID of the tool group to register.

          args: A dictionary of arguments to pass to the tool group.

          mcp_endpoint: The MCP endpoint to use for the tool group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/toolgroups",
            body=await async_maybe_transform(
                {
                    "provider_id": provider_id,
                    "toolgroup_id": toolgroup_id,
                    "args": args,
                    "mcp_endpoint": mcp_endpoint,
                },
                toolgroup_register_params.ToolgroupRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unregister(
        self,
        toolgroup_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a tool group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not toolgroup_id:
            raise ValueError(f"Expected a non-empty value for `toolgroup_id` but received {toolgroup_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/toolgroups/{toolgroup_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        self.register = to_raw_response_wrapper(
            toolgroups.register,
        )
        self.unregister = to_raw_response_wrapper(
            toolgroups.unregister,
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
        self.register = async_to_raw_response_wrapper(
            toolgroups.register,
        )
        self.unregister = async_to_raw_response_wrapper(
            toolgroups.unregister,
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
        self.register = to_streamed_response_wrapper(
            toolgroups.register,
        )
        self.unregister = to_streamed_response_wrapper(
            toolgroups.unregister,
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
        self.register = async_to_streamed_response_wrapper(
            toolgroups.register,
        )
        self.unregister = async_to_streamed_response_wrapper(
            toolgroups.unregister,
        )
