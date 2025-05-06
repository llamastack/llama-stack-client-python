# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import shield_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

    def create(
        self,
        *,
        shield_id: str,
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_shield_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Shield:
        """
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
                shield_create_params.ShieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )

    def retrieve(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Shield:
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShieldListResponse:
        return self._get(
            "/v1/shields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShieldListResponse,
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

    async def create(
        self,
        *,
        shield_id: str,
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_shield_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Shield:
        """
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
                shield_create_params.ShieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )

    async def retrieve(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Shield:
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShieldListResponse:
        return await self._get(
            "/v1/shields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShieldListResponse,
        )


class ShieldsResourceWithRawResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.create = to_raw_response_wrapper(
            shields.create,
        )
        self.retrieve = to_raw_response_wrapper(
            shields.retrieve,
        )
        self.list = to_raw_response_wrapper(
            shields.list,
        )


class AsyncShieldsResourceWithRawResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.create = async_to_raw_response_wrapper(
            shields.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            shields.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            shields.list,
        )


class ShieldsResourceWithStreamingResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.create = to_streamed_response_wrapper(
            shields.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            shields.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            shields.list,
        )


class AsyncShieldsResourceWithStreamingResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.create = async_to_streamed_response_wrapper(
            shields.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            shields.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            shields.list,
        )
