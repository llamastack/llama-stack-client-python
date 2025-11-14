# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional

import httpx

from ..types import moderation_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.create_response import CreateResponse

__all__ = ["ModerationsResource", "AsyncModerationsResource"]


class ModerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ModerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ModerationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        model: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponse:
        """
        Create moderation.

        Classifies if text and/or image inputs are potentially harmful.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/moderations",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                },
                moderation_create_params.ModerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateResponse,
        )


class AsyncModerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncModerationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        model: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponse:
        """
        Create moderation.

        Classifies if text and/or image inputs are potentially harmful.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/moderations",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                },
                moderation_create_params.ModerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateResponse,
        )


class ModerationsResourceWithRawResponse:
    def __init__(self, moderations: ModerationsResource) -> None:
        self._moderations = moderations

        self.create = to_raw_response_wrapper(
            moderations.create,
        )


class AsyncModerationsResourceWithRawResponse:
    def __init__(self, moderations: AsyncModerationsResource) -> None:
        self._moderations = moderations

        self.create = async_to_raw_response_wrapper(
            moderations.create,
        )


class ModerationsResourceWithStreamingResponse:
    def __init__(self, moderations: ModerationsResource) -> None:
        self._moderations = moderations

        self.create = to_streamed_response_wrapper(
            moderations.create,
        )


class AsyncModerationsResourceWithStreamingResponse:
    def __init__(self, moderations: AsyncModerationsResource) -> None:
        self._moderations = moderations

        self.create = async_to_streamed_response_wrapper(
            moderations.create,
        )
