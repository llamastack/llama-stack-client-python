# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.alpha import admin_list_routes_params
from ..._base_client import make_request_options
from ...types.shared.health_info import HealthInfo
from ...types.route_list_response import RouteListResponse
from ...types.shared.version_info import VersionInfo
from ...types.shared.provider_info import ProviderInfo
from ...types.provider_list_response import ProviderListResponse

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)

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
            "/v1alpha/admin/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthInfo,
        )

    def inspect_provider(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderInfo:
        """
        Get detailed information about a specific provider.

        Args:
          provider_id: The ID of the provider to inspect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._get(
            f"/v1alpha/admin/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderInfo,
        )

    def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """List all available providers with their configuration and health status."""
        return self._get(
            "/v1alpha/admin/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ProviderListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProviderListResponse], DataWrapper[ProviderListResponse]),
        )

    def list_routes(
        self,
        *,
        api_filter: Optional[Literal["v1", "v1alpha", "v1beta", "deprecated"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteListResponse:
        """
        List all available API routes with their methods and implementing providers.

        Args:
          api_filter: Filter to control which routes are returned. Can be an API level ('v1',
              'v1alpha', 'v1beta') to show non-deprecated routes at that level, or
              'deprecated' to show deprecated routes across all levels. If not specified,
              returns all non-deprecated routes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1alpha/admin/inspect/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"api_filter": api_filter}, admin_list_routes_params.AdminListRoutesParams),
                post_parser=DataWrapper[RouteListResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteListResponse], DataWrapper[RouteListResponse]),
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
            "/v1alpha/admin/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionInfo,
        )


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)

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
            "/v1alpha/admin/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthInfo,
        )

    async def inspect_provider(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderInfo:
        """
        Get detailed information about a specific provider.

        Args:
          provider_id: The ID of the provider to inspect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._get(
            f"/v1alpha/admin/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderInfo,
        )

    async def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """List all available providers with their configuration and health status."""
        return await self._get(
            "/v1alpha/admin/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ProviderListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProviderListResponse], DataWrapper[ProviderListResponse]),
        )

    async def list_routes(
        self,
        *,
        api_filter: Optional[Literal["v1", "v1alpha", "v1beta", "deprecated"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteListResponse:
        """
        List all available API routes with their methods and implementing providers.

        Args:
          api_filter: Filter to control which routes are returned. Can be an API level ('v1',
              'v1alpha', 'v1beta') to show non-deprecated routes at that level, or
              'deprecated' to show deprecated routes across all levels. If not specified,
              returns all non-deprecated routes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1alpha/admin/inspect/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"api_filter": api_filter}, admin_list_routes_params.AdminListRoutesParams
                ),
                post_parser=DataWrapper[RouteListResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteListResponse], DataWrapper[RouteListResponse]),
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
            "/v1alpha/admin/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionInfo,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.health = to_raw_response_wrapper(
            admin.health,
        )
        self.inspect_provider = to_raw_response_wrapper(
            admin.inspect_provider,
        )
        self.list_providers = to_raw_response_wrapper(
            admin.list_providers,
        )
        self.list_routes = to_raw_response_wrapper(
            admin.list_routes,
        )
        self.version = to_raw_response_wrapper(
            admin.version,
        )


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.health = async_to_raw_response_wrapper(
            admin.health,
        )
        self.inspect_provider = async_to_raw_response_wrapper(
            admin.inspect_provider,
        )
        self.list_providers = async_to_raw_response_wrapper(
            admin.list_providers,
        )
        self.list_routes = async_to_raw_response_wrapper(
            admin.list_routes,
        )
        self.version = async_to_raw_response_wrapper(
            admin.version,
        )


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.health = to_streamed_response_wrapper(
            admin.health,
        )
        self.inspect_provider = to_streamed_response_wrapper(
            admin.inspect_provider,
        )
        self.list_providers = to_streamed_response_wrapper(
            admin.list_providers,
        )
        self.list_routes = to_streamed_response_wrapper(
            admin.list_routes,
        )
        self.version = to_streamed_response_wrapper(
            admin.version,
        )


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.health = async_to_streamed_response_wrapper(
            admin.health,
        )
        self.inspect_provider = async_to_streamed_response_wrapper(
            admin.inspect_provider,
        )
        self.list_providers = async_to_streamed_response_wrapper(
            admin.list_providers,
        )
        self.list_routes = async_to_streamed_response_wrapper(
            admin.list_routes,
        )
        self.version = async_to_streamed_response_wrapper(
            admin.version,
        )
