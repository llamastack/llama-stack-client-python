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

from ..types import shield_register_params
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
from ..types.shield import Shield
from ..types.shield_list_response import ShieldListResponse

__all__ = ["ShieldsResource", "AsyncShieldsResource"]


class ShieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ShieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ShieldsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Shield:
        """
        Get a shield by its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/v1/shields/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
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
    ) -> ShieldListResponse:
        """List all shields."""
        return self._get(
            "/v1/shields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ShieldListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ShieldListResponse], DataWrapper[ShieldListResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a shield.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/shields/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def register(
        self,
        *,
        shield_id: str,
        params: Optional[Dict[str, object]] | Omit = omit,
        provider_id: Optional[str] | Omit = omit,
        provider_shield_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Shield:
        """
        Register a shield.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/shields",
            body=maybe_transform(
                {
                    "shield_id": shield_id,
                    "params": params,
                    "provider_id": provider_id,
                    "provider_shield_id": provider_shield_id,
                },
                shield_register_params.ShieldRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )


class AsyncShieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncShieldsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Shield:
        """
        Get a shield by its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/v1/shields/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
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
    ) -> ShieldListResponse:
        """List all shields."""
        return await self._get(
            "/v1/shields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ShieldListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ShieldListResponse], DataWrapper[ShieldListResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a shield.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/shields/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def register(
        self,
        *,
        shield_id: str,
        params: Optional[Dict[str, object]] | Omit = omit,
        provider_id: Optional[str] | Omit = omit,
        provider_shield_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Shield:
        """
        Register a shield.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/shields",
            body=await async_maybe_transform(
                {
                    "shield_id": shield_id,
                    "params": params,
                    "provider_id": provider_id,
                    "provider_shield_id": provider_shield_id,
                },
                shield_register_params.ShieldRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )


class ShieldsResourceWithRawResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.retrieve = to_raw_response_wrapper(
            shields.retrieve,
        )
        self.list = to_raw_response_wrapper(
            shields.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                shields.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                shields.register,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncShieldsResourceWithRawResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.retrieve = async_to_raw_response_wrapper(
            shields.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            shields.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                shields.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                shields.register,  # pyright: ignore[reportDeprecated],
            )
        )


class ShieldsResourceWithStreamingResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.retrieve = to_streamed_response_wrapper(
            shields.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            shields.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                shields.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                shields.register,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncShieldsResourceWithStreamingResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.retrieve = async_to_streamed_response_wrapper(
            shields.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            shields.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                shields.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                shields.register,  # pyright: ignore[reportDeprecated],
            )
        )
