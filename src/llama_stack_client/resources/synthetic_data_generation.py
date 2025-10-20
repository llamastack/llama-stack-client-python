# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import synthetic_data_generation_generate_params
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
from .._base_client import make_request_options
from ..types.shared_params.message import Message
from ..types.synthetic_data_generation_response import SyntheticDataGenerationResponse

__all__ = ["SyntheticDataGenerationResource", "AsyncSyntheticDataGenerationResource"]


class SyntheticDataGenerationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyntheticDataGenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return SyntheticDataGenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyntheticDataGenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return SyntheticDataGenerationResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        dialogs: Iterable[Message],
        filtering_function: Literal["none", "random", "top_k", "top_p", "top_k_top_p", "sigmoid"],
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyntheticDataGenerationResponse:
        """
        Generate synthetic data based on input dialogs and apply filtering.

        Args:
          dialogs: List of conversation messages to use as input for synthetic data generation

          filtering_function: Type of filtering to apply to generated synthetic data samples

          model: (Optional) The identifier of the model to use. The model must be registered with
              Llama Stack and available via the /models endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/synthetic-data-generation/generate",
            body=maybe_transform(
                {
                    "dialogs": dialogs,
                    "filtering_function": filtering_function,
                    "model": model,
                },
                synthetic_data_generation_generate_params.SyntheticDataGenerationGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataGenerationResponse,
        )


class AsyncSyntheticDataGenerationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyntheticDataGenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSyntheticDataGenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyntheticDataGenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncSyntheticDataGenerationResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        dialogs: Iterable[Message],
        filtering_function: Literal["none", "random", "top_k", "top_p", "top_k_top_p", "sigmoid"],
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyntheticDataGenerationResponse:
        """
        Generate synthetic data based on input dialogs and apply filtering.

        Args:
          dialogs: List of conversation messages to use as input for synthetic data generation

          filtering_function: Type of filtering to apply to generated synthetic data samples

          model: (Optional) The identifier of the model to use. The model must be registered with
              Llama Stack and available via the /models endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/synthetic-data-generation/generate",
            body=await async_maybe_transform(
                {
                    "dialogs": dialogs,
                    "filtering_function": filtering_function,
                    "model": model,
                },
                synthetic_data_generation_generate_params.SyntheticDataGenerationGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataGenerationResponse,
        )


class SyntheticDataGenerationResourceWithRawResponse:
    def __init__(self, synthetic_data_generation: SyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = to_raw_response_wrapper(
            synthetic_data_generation.generate,
        )


class AsyncSyntheticDataGenerationResourceWithRawResponse:
    def __init__(self, synthetic_data_generation: AsyncSyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = async_to_raw_response_wrapper(
            synthetic_data_generation.generate,
        )


class SyntheticDataGenerationResourceWithStreamingResponse:
    def __init__(self, synthetic_data_generation: SyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = to_streamed_response_wrapper(
            synthetic_data_generation.generate,
        )


class AsyncSyntheticDataGenerationResourceWithStreamingResponse:
    def __init__(self, synthetic_data_generation: AsyncSyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = async_to_streamed_response_wrapper(
            synthetic_data_generation.generate,
        )
