# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ...types import tool_runtime_list_tools_params, tool_runtime_invoke_tool_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..._base_client import make_request_options
from ...types.url_param import URLParam
from ...types.tool_runtime_list_tools_response import ToolRuntimeListToolsResponse
from ...types.tool_runtime_invoke_tool_response import ToolRuntimeInvokeToolResponse

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolRuntimeInvokeToolResponse:
        """
        Run a tool with the given arguments

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
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRuntimeInvokeToolResponse,
        )

    def list_tools(
        self,
        *,
        mcp_endpoint: URLParam | NotGiven = NOT_GIVEN,
        tool_group_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolRuntimeListToolsResponse:
        """
        Args:
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
            ),
            cast_to=ToolRuntimeListToolsResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolRuntimeInvokeToolResponse:
        """
        Run a tool with the given arguments

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
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRuntimeInvokeToolResponse,
        )

    async def list_tools(
        self,
        *,
        mcp_endpoint: URLParam | NotGiven = NOT_GIVEN,
        tool_group_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolRuntimeListToolsResponse:
        """
        Args:
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
            ),
            cast_to=ToolRuntimeListToolsResponse,
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
