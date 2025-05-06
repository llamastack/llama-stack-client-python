# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable

import httpx

from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from .responses import (
    ResponsesResource,
    AsyncResponsesResource,
    ResponsesResourceWithRawResponse,
    AsyncResponsesResourceWithRawResponse,
    ResponsesResourceWithStreamingResponse,
    AsyncResponsesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.openai import v1_generate_completion_params
from ....types.openai.v1_list_models_response import V1ListModelsResponse
from ....types.openai.v1_generate_completion_response import V1GenerateCompletionResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def responses(self) -> ResponsesResource:
        return ResponsesResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def generate_completion(
        self,
        *,
        model: str,
        prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]]],
        best_of: int | NotGiven = NOT_GIVEN,
        echo: bool | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        guided_choice: List[str] | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        prompt_logprobs: int | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GenerateCompletionResponse:
        """
        Generate an OpenAI-compatible completion for the given prompt using the
        specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for

          best_of: (Optional) The number of completions to generate

          echo: (Optional) Whether to echo the prompt

          frequency_penalty: (Optional) The penalty for repeated tokens

          logit_bias: (Optional) The logit bias to use

          logprobs: (Optional) The log probabilities to use

          max_tokens: (Optional) The maximum number of tokens to generate

          n: (Optional) The number of completions to generate

          presence_penalty: (Optional) The penalty for repeated tokens

          seed: (Optional) The seed to use

          stop: (Optional) The stop tokens to use

          stream: (Optional) Whether to stream the response

          stream_options: (Optional) The stream options to use

          temperature: (Optional) The temperature to use

          top_p: (Optional) The top p to use

          user: (Optional) The user to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/openai/v1/completions",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "guided_choice": guided_choice,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "prompt_logprobs": prompt_logprobs,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "top_p": top_p,
                    "user": user,
                },
                v1_generate_completion_params.V1GenerateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GenerateCompletionResponse,
        )

    def list_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListModelsResponse:
        return self._get(
            "/v1/openai/v1/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListModelsResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def responses(self) -> AsyncResponsesResource:
        return AsyncResponsesResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def generate_completion(
        self,
        *,
        model: str,
        prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]]],
        best_of: int | NotGiven = NOT_GIVEN,
        echo: bool | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        guided_choice: List[str] | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        prompt_logprobs: int | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GenerateCompletionResponse:
        """
        Generate an OpenAI-compatible completion for the given prompt using the
        specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for

          best_of: (Optional) The number of completions to generate

          echo: (Optional) Whether to echo the prompt

          frequency_penalty: (Optional) The penalty for repeated tokens

          logit_bias: (Optional) The logit bias to use

          logprobs: (Optional) The log probabilities to use

          max_tokens: (Optional) The maximum number of tokens to generate

          n: (Optional) The number of completions to generate

          presence_penalty: (Optional) The penalty for repeated tokens

          seed: (Optional) The seed to use

          stop: (Optional) The stop tokens to use

          stream: (Optional) Whether to stream the response

          stream_options: (Optional) The stream options to use

          temperature: (Optional) The temperature to use

          top_p: (Optional) The top p to use

          user: (Optional) The user to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/openai/v1/completions",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "guided_choice": guided_choice,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "prompt_logprobs": prompt_logprobs,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "top_p": top_p,
                    "user": user,
                },
                v1_generate_completion_params.V1GenerateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GenerateCompletionResponse,
        )

    async def list_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListModelsResponse:
        return await self._get(
            "/v1/openai/v1/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListModelsResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.generate_completion = to_raw_response_wrapper(
            v1.generate_completion,
        )
        self.list_models = to_raw_response_wrapper(
            v1.list_models,
        )

    @cached_property
    def responses(self) -> ResponsesResourceWithRawResponse:
        return ResponsesResourceWithRawResponse(self._v1.responses)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._v1.chat)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.generate_completion = async_to_raw_response_wrapper(
            v1.generate_completion,
        )
        self.list_models = async_to_raw_response_wrapper(
            v1.list_models,
        )

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithRawResponse:
        return AsyncResponsesResourceWithRawResponse(self._v1.responses)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._v1.chat)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.generate_completion = to_streamed_response_wrapper(
            v1.generate_completion,
        )
        self.list_models = to_streamed_response_wrapper(
            v1.list_models,
        )

    @cached_property
    def responses(self) -> ResponsesResourceWithStreamingResponse:
        return ResponsesResourceWithStreamingResponse(self._v1.responses)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._v1.chat)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.generate_completion = async_to_streamed_response_wrapper(
            v1.generate_completion,
        )
        self.list_models = async_to_streamed_response_wrapper(
            v1.list_models,
        )

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithStreamingResponse:
        return AsyncResponsesResourceWithStreamingResponse(self._v1.responses)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._v1.chat)
