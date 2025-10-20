# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Union, Iterable, cast

import httpx

from ...types import tool_runtime_list_tools_params, tool_runtime_invoke_tool_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .rag_tool import (
    RagToolResource,
    AsyncRagToolResource,
    RagToolResourceWithRawResponse,
    AsyncRagToolResourceWithRawResponse,
    RagToolResourceWithStreamingResponse,
    AsyncRagToolResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.tool_invocation_result import ToolInvocationResult
from ...types.tool_runtime_list_tools_response import ToolRuntimeListToolsResponse

__all__ = ["ToolRuntimeResource", "AsyncToolRuntimeResource"]


class ToolRuntimeResource(SyncAPIResource):
    @cached_property
    def rag_tool(self) -> RagToolResource:
        return RagToolResource(self._client)

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

    def invoke_tool(
        self,
        *,
        kwargs: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        tool_name: str,
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
          kwargs: A dictionary of arguments to pass to the tool.

          tool_name: The name of the tool to invoke.

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
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolInvocationResult,
        )

    def list_tools(
        self,
        *,
        mcp_endpoint: tool_runtime_list_tools_params.McpEndpoint | Omit = omit,
        tool_group_id: str | Omit = omit,
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
          mcp_endpoint: The MCP endpoint to use for the tool group.

          tool_group_id: The ID of the tool group to list tools for.

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
    def rag_tool(self) -> AsyncRagToolResource:
        return AsyncRagToolResource(self._client)

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

    async def invoke_tool(
        self,
        *,
        kwargs: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        tool_name: str,
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
          kwargs: A dictionary of arguments to pass to the tool.

          tool_name: The name of the tool to invoke.

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
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolInvocationResult,
        )

    async def list_tools(
        self,
        *,
        mcp_endpoint: tool_runtime_list_tools_params.McpEndpoint | Omit = omit,
        tool_group_id: str | Omit = omit,
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
          mcp_endpoint: The MCP endpoint to use for the tool group.

          tool_group_id: The ID of the tool group to list tools for.

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

        self.invoke_tool = to_raw_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = to_raw_response_wrapper(
            tool_runtime.list_tools,
        )

    @cached_property
    def rag_tool(self) -> RagToolResourceWithRawResponse:
        return RagToolResourceWithRawResponse(self._tool_runtime.rag_tool)


class AsyncToolRuntimeResourceWithRawResponse:
    def __init__(self, tool_runtime: AsyncToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = async_to_raw_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = async_to_raw_response_wrapper(
            tool_runtime.list_tools,
        )

    @cached_property
    def rag_tool(self) -> AsyncRagToolResourceWithRawResponse:
        return AsyncRagToolResourceWithRawResponse(self._tool_runtime.rag_tool)


class ToolRuntimeResourceWithStreamingResponse:
    def __init__(self, tool_runtime: ToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = to_streamed_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = to_streamed_response_wrapper(
            tool_runtime.list_tools,
        )

    @cached_property
    def rag_tool(self) -> RagToolResourceWithStreamingResponse:
        return RagToolResourceWithStreamingResponse(self._tool_runtime.rag_tool)


class AsyncToolRuntimeResourceWithStreamingResponse:
    def __init__(self, tool_runtime: AsyncToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = async_to_streamed_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = async_to_streamed_response_wrapper(
            tool_runtime.list_tools,
        )

    @cached_property
    def rag_tool(self) -> AsyncRagToolResourceWithStreamingResponse:
        return AsyncRagToolResourceWithStreamingResponse(self._tool_runtime.rag_tool)
