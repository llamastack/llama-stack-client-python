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

from ..types import tool_runtime_list_tools_params, tool_runtime_invoke_tool_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.tool_invocation_result import ToolInvocationResult
from ..types.tool_runtime_list_tools_response import ToolRuntimeListToolsResponse

__all__ = ["ToolRuntimeResource", "AsyncToolRuntimeResource"]


class ToolRuntimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolRuntimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ToolRuntimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolRuntimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ToolRuntimeResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def invoke_tool(
        self,
        *,
        kwargs: Dict[str, object],
        tool_name: str,
        authorization: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolInvocationResult:
        """
        Run a tool with the given arguments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tool-runtime/invoke",
            body=maybe_transform(
                {
                    "kwargs": kwargs,
                    "tool_name": tool_name,
                    "authorization": authorization,
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolInvocationResult,
        )

    @typing_extensions.deprecated("deprecated")
    def list_tools(
        self,
        *,
        authorization: Optional[str] | Omit = omit,
        mcp_endpoint: Optional[tool_runtime_list_tools_params.McpEndpoint] | Omit = omit,
        tool_group_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRuntimeListToolsResponse:
        """
        List all tools in the runtime.

        Args:
          mcp_endpoint: A URL reference to external content.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tool-runtime/list-tools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "authorization": authorization,
                        "mcp_endpoint": mcp_endpoint,
                        "tool_group_id": tool_group_id,
                    },
                    tool_runtime_list_tools_params.ToolRuntimeListToolsParams,
                ),
                post_parser=DataWrapper[ToolRuntimeListToolsResponse]._unwrapper,
            ),
            cast_to=cast(Type[ToolRuntimeListToolsResponse], DataWrapper[ToolRuntimeListToolsResponse]),
        )


class AsyncToolRuntimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolRuntimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolRuntimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolRuntimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncToolRuntimeResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def invoke_tool(
        self,
        *,
        kwargs: Dict[str, object],
        tool_name: str,
        authorization: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolInvocationResult:
        """
        Run a tool with the given arguments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tool-runtime/invoke",
            body=await async_maybe_transform(
                {
                    "kwargs": kwargs,
                    "tool_name": tool_name,
                    "authorization": authorization,
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolInvocationResult,
        )

    @typing_extensions.deprecated("deprecated")
    async def list_tools(
        self,
        *,
        authorization: Optional[str] | Omit = omit,
        mcp_endpoint: Optional[tool_runtime_list_tools_params.McpEndpoint] | Omit = omit,
        tool_group_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRuntimeListToolsResponse:
        """
        List all tools in the runtime.

        Args:
          mcp_endpoint: A URL reference to external content.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tool-runtime/list-tools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "authorization": authorization,
                        "mcp_endpoint": mcp_endpoint,
                        "tool_group_id": tool_group_id,
                    },
                    tool_runtime_list_tools_params.ToolRuntimeListToolsParams,
                ),
                post_parser=DataWrapper[ToolRuntimeListToolsResponse]._unwrapper,
            ),
            cast_to=cast(Type[ToolRuntimeListToolsResponse], DataWrapper[ToolRuntimeListToolsResponse]),
        )


class ToolRuntimeResourceWithRawResponse:
    def __init__(self, tool_runtime: ToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                tool_runtime.invoke_tool,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_tools = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                tool_runtime.list_tools,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncToolRuntimeResourceWithRawResponse:
    def __init__(self, tool_runtime: AsyncToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                tool_runtime.invoke_tool,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_tools = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                tool_runtime.list_tools,  # pyright: ignore[reportDeprecated],
            )
        )


class ToolRuntimeResourceWithStreamingResponse:
    def __init__(self, tool_runtime: ToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                tool_runtime.invoke_tool,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_tools = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                tool_runtime.list_tools,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncToolRuntimeResourceWithStreamingResponse:
    def __init__(self, tool_runtime: AsyncToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                tool_runtime.invoke_tool,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_tools = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                tool_runtime.list_tools,  # pyright: ignore[reportDeprecated],
            )
        )
