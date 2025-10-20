# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import completion_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """Create completion.

        Generate an OpenAI-compatible completion for the given prompt
        using the specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for.

          best_of: (Optional) The number of completions to generate.

          echo: (Optional) Whether to echo the prompt.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          presence_penalty: (Optional) The penalty for repeated tokens.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream: (Optional) Whether to stream the response.

          stream_options: (Optional) The stream options to use.

          suffix: (Optional) The suffix that should be appended to the completion.

          temperature: (Optional) The temperature to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        stream: Literal[True],
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[CompletionCreateResponse]:
        """Create completion.

        Generate an OpenAI-compatible completion for the given prompt
        using the specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for.

          stream: (Optional) Whether to stream the response.

          best_of: (Optional) The number of completions to generate.

          echo: (Optional) Whether to echo the prompt.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          presence_penalty: (Optional) The penalty for repeated tokens.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          suffix: (Optional) The suffix that should be appended to the completion.

          temperature: (Optional) The temperature to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        stream: bool,
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | Stream[CompletionCreateResponse]:
        """Create completion.

        Generate an OpenAI-compatible completion for the given prompt
        using the specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for.

          stream: (Optional) Whether to stream the response.

          best_of: (Optional) The number of completions to generate.

          echo: (Optional) Whether to echo the prompt.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          presence_penalty: (Optional) The penalty for repeated tokens.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          suffix: (Optional) The suffix that should be appended to the completion.

          temperature: (Optional) The temperature to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt"], ["model", "prompt", "stream"])
    def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | Stream[CompletionCreateResponse]:
        return self._post(
            "/v1/completions",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "suffix": suffix,
                    "temperature": temperature,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
            stream=stream or False,
            stream_cls=Stream[CompletionCreateResponse],
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """Create completion.

        Generate an OpenAI-compatible completion for the given prompt
        using the specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for.

          best_of: (Optional) The number of completions to generate.

          echo: (Optional) Whether to echo the prompt.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          presence_penalty: (Optional) The penalty for repeated tokens.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream: (Optional) Whether to stream the response.

          stream_options: (Optional) The stream options to use.

          suffix: (Optional) The suffix that should be appended to the completion.

          temperature: (Optional) The temperature to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        stream: Literal[True],
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[CompletionCreateResponse]:
        """Create completion.

        Generate an OpenAI-compatible completion for the given prompt
        using the specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for.

          stream: (Optional) Whether to stream the response.

          best_of: (Optional) The number of completions to generate.

          echo: (Optional) Whether to echo the prompt.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          presence_penalty: (Optional) The penalty for repeated tokens.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          suffix: (Optional) The suffix that should be appended to the completion.

          temperature: (Optional) The temperature to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        stream: bool,
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | AsyncStream[CompletionCreateResponse]:
        """Create completion.

        Generate an OpenAI-compatible completion for the given prompt
        using the specified model.

        Args:
          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          prompt: The prompt to generate a completion for.

          stream: (Optional) Whether to stream the response.

          best_of: (Optional) The number of completions to generate.

          echo: (Optional) Whether to echo the prompt.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          presence_penalty: (Optional) The penalty for repeated tokens.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          suffix: (Optional) The suffix that should be appended to the completion.

          temperature: (Optional) The temperature to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt"], ["model", "prompt", "stream"])
    async def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]],
        best_of: int | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        presence_penalty: float | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        suffix: str | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | AsyncStream[CompletionCreateResponse]:
        return await self._post(
            "/v1/completions",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "suffix": suffix,
                    "temperature": temperature,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
            stream=stream or False,
            stream_cls=AsyncStream[CompletionCreateResponse],
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
