# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable

import httpx

from ..types import safety_run_shield_params, safety_openai_moderations_params
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
from ..types.run_shield_response import RunShieldResponse
from ..types.shared_params.message import Message
from ..types.openai_moderations_response import OpenAIModerationsResponse

__all__ = ["SafetyResource", "AsyncSafetyResource"]


class SafetyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return SafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return SafetyResourceWithStreamingResponse(self)

    def openai_moderations(
        self,
        *,
        input: Union[str, List[str]],
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OpenAIModerationsResponse:
        """
        Classifies if text and/or image inputs are potentially harmful.

        Args:
          input: Input (or inputs) to classify. Can be a single string, an array of strings, or
              an array of multi-modal input objects similar to other models.

          model: The content moderation model you would like to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/openai/v1/moderations",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                },
                safety_openai_moderations_params.SafetyOpenAIModerationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIModerationsResponse,
        )

    def run_shield(
        self,
        *,
        messages: Iterable[Message],
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        shield_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunShieldResponse:
        """
        Run a shield.

        Args:
          messages: The messages to run the shield on.

          params: The parameters of the shield.

          shield_id: The identifier of the shield to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/safety/run-shield",
            body=maybe_transform(
                {
                    "messages": messages,
                    "params": params,
                    "shield_id": shield_id,
                },
                safety_run_shield_params.SafetyRunShieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunShieldResponse,
        )


class AsyncSafetyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncSafetyResourceWithStreamingResponse(self)

    async def openai_moderations(
        self,
        *,
        input: Union[str, List[str]],
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OpenAIModerationsResponse:
        """
        Classifies if text and/or image inputs are potentially harmful.

        Args:
          input: Input (or inputs) to classify. Can be a single string, an array of strings, or
              an array of multi-modal input objects similar to other models.

          model: The content moderation model you would like to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/openai/v1/moderations",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                },
                safety_openai_moderations_params.SafetyOpenAIModerationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIModerationsResponse,
        )

    async def run_shield(
        self,
        *,
        messages: Iterable[Message],
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        shield_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunShieldResponse:
        """
        Run a shield.

        Args:
          messages: The messages to run the shield on.

          params: The parameters of the shield.

          shield_id: The identifier of the shield to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/safety/run-shield",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "params": params,
                    "shield_id": shield_id,
                },
                safety_run_shield_params.SafetyRunShieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunShieldResponse,
        )


class SafetyResourceWithRawResponse:
    def __init__(self, safety: SafetyResource) -> None:
        self._safety = safety

        self.openai_moderations = to_raw_response_wrapper(
            safety.openai_moderations,
        )
        self.run_shield = to_raw_response_wrapper(
            safety.run_shield,
        )


class AsyncSafetyResourceWithRawResponse:
    def __init__(self, safety: AsyncSafetyResource) -> None:
        self._safety = safety

        self.openai_moderations = async_to_raw_response_wrapper(
            safety.openai_moderations,
        )
        self.run_shield = async_to_raw_response_wrapper(
            safety.run_shield,
        )


class SafetyResourceWithStreamingResponse:
    def __init__(self, safety: SafetyResource) -> None:
        self._safety = safety

        self.openai_moderations = to_streamed_response_wrapper(
            safety.openai_moderations,
        )
        self.run_shield = to_streamed_response_wrapper(
            safety.run_shield,
        )


class AsyncSafetyResourceWithStreamingResponse:
    def __init__(self, safety: AsyncSafetyResource) -> None:
        self._safety = safety

        self.openai_moderations = async_to_streamed_response_wrapper(
            safety.openai_moderations,
        )
        self.run_shield = async_to_streamed_response_wrapper(
            safety.run_shield,
        )
