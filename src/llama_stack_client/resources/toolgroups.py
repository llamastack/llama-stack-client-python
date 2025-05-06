# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import toolgroup_register_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.url_param import URLParam
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

    def retrieve(
        self,
        toolgroup_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolGroup:
        """
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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolgroupListResponse:
        """List tool groups with optional provider"""
        return self._get(
            "/v1/toolgroups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolgroupListResponse,
        )

    def register(
        self,
        *,
        provider_id: str,
        toolgroup_id: str,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        mcp_endpoint: URLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Register a tool group

        Args:
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unregister a tool group

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

    async def retrieve(
        self,
        toolgroup_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolGroup:
        """
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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolgroupListResponse:
        """List tool groups with optional provider"""
        return await self._get(
            "/v1/toolgroups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolgroupListResponse,
        )

    async def register(
        self,
        *,
        provider_id: str,
        toolgroup_id: str,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        mcp_endpoint: URLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Register a tool group

        Args:
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unregister a tool group

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

        self.retrieve = to_raw_response_wrapper(
            toolgroups.retrieve,
        )
        self.list = to_raw_response_wrapper(
            toolgroups.list,
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

        self.retrieve = async_to_raw_response_wrapper(
            toolgroups.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            toolgroups.list,
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

        self.retrieve = to_streamed_response_wrapper(
            toolgroups.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            toolgroups.list,
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

        self.retrieve = async_to_streamed_response_wrapper(
            toolgroups.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            toolgroups.list,
        )
        self.register = async_to_streamed_response_wrapper(
            toolgroups.register,
        )
        self.unregister = async_to_streamed_response_wrapper(
            toolgroups.unregister,
        )
