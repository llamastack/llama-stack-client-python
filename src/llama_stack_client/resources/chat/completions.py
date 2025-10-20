# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage
from ...types.chat import completion_list_params, completion_create_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.chat_completion_chunk import ChatCompletionChunk
from ...types.chat.completion_list_response import CompletionListResponse
from ...types.chat.completion_create_response import CompletionCreateResponse
from ...types.chat.completion_retrieve_response import CompletionRetrieveResponse

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
        messages: Iterable[completion_create_params.Message],
        model: str,
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """Create chat completions.

        Generate an OpenAI-compatible chat completion for the
        given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          function_call: (Optional) The function call to use.

          functions: (Optional) List of functions to use.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_completion_tokens: (Optional) The maximum number of tokens to generate.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          parallel_tool_calls: (Optional) Whether to parallelize tool calls.

          presence_penalty: (Optional) The penalty for repeated tokens.

          response_format: (Optional) The response format to use.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream: (Optional) Whether to stream the response.

          stream_options: (Optional) The stream options to use.

          temperature: (Optional) The temperature to use.

          tool_choice: (Optional) The tool choice to use.

          tools: (Optional) The tools to use.

          top_logprobs: (Optional) The top log probabilities to use.

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
        messages: Iterable[completion_create_params.Message],
        model: str,
        stream: Literal[True],
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ChatCompletionChunk]:
        """Create chat completions.

        Generate an OpenAI-compatible chat completion for the
        given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) Whether to stream the response.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          function_call: (Optional) The function call to use.

          functions: (Optional) List of functions to use.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_completion_tokens: (Optional) The maximum number of tokens to generate.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          parallel_tool_calls: (Optional) Whether to parallelize tool calls.

          presence_penalty: (Optional) The penalty for repeated tokens.

          response_format: (Optional) The response format to use.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          temperature: (Optional) The temperature to use.

          tool_choice: (Optional) The tool choice to use.

          tools: (Optional) The tools to use.

          top_logprobs: (Optional) The top log probabilities to use.

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
        messages: Iterable[completion_create_params.Message],
        model: str,
        stream: bool,
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | Stream[ChatCompletionChunk]:
        """Create chat completions.

        Generate an OpenAI-compatible chat completion for the
        given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) Whether to stream the response.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          function_call: (Optional) The function call to use.

          functions: (Optional) List of functions to use.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_completion_tokens: (Optional) The maximum number of tokens to generate.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          parallel_tool_calls: (Optional) Whether to parallelize tool calls.

          presence_penalty: (Optional) The penalty for repeated tokens.

          response_format: (Optional) The response format to use.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          temperature: (Optional) The temperature to use.

          tool_choice: (Optional) The tool choice to use.

          tools: (Optional) The tools to use.

          top_logprobs: (Optional) The top log probabilities to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: str,
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | Stream[ChatCompletionChunk]:
        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
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
            cast_to=cast(
                Any, CompletionCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )

    def retrieve(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionRetrieveResponse:
        """Get chat completion.

        Describe a chat completion by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._get(
            f"/v1/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        model: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOpenAICursorPage[CompletionListResponse]:
        """
        List chat completions.

        Args:
          after: The ID of the last chat completion to return.

          limit: The maximum number of chat completions to return.

          model: The model to filter by.

          order: The order to sort the chat completions by: "asc" or "desc". Defaults to "desc".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/chat/completions",
            page=SyncOpenAICursorPage[CompletionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "model": model,
                        "order": order,
                    },
                    completion_list_params.CompletionListParams,
                ),
            ),
            model=CompletionListResponse,
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
        messages: Iterable[completion_create_params.Message],
        model: str,
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """Create chat completions.

        Generate an OpenAI-compatible chat completion for the
        given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          function_call: (Optional) The function call to use.

          functions: (Optional) List of functions to use.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_completion_tokens: (Optional) The maximum number of tokens to generate.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          parallel_tool_calls: (Optional) Whether to parallelize tool calls.

          presence_penalty: (Optional) The penalty for repeated tokens.

          response_format: (Optional) The response format to use.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream: (Optional) Whether to stream the response.

          stream_options: (Optional) The stream options to use.

          temperature: (Optional) The temperature to use.

          tool_choice: (Optional) The tool choice to use.

          tools: (Optional) The tools to use.

          top_logprobs: (Optional) The top log probabilities to use.

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
        messages: Iterable[completion_create_params.Message],
        model: str,
        stream: Literal[True],
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ChatCompletionChunk]:
        """Create chat completions.

        Generate an OpenAI-compatible chat completion for the
        given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) Whether to stream the response.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          function_call: (Optional) The function call to use.

          functions: (Optional) List of functions to use.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_completion_tokens: (Optional) The maximum number of tokens to generate.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          parallel_tool_calls: (Optional) Whether to parallelize tool calls.

          presence_penalty: (Optional) The penalty for repeated tokens.

          response_format: (Optional) The response format to use.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          temperature: (Optional) The temperature to use.

          tool_choice: (Optional) The tool choice to use.

          tools: (Optional) The tools to use.

          top_logprobs: (Optional) The top log probabilities to use.

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
        messages: Iterable[completion_create_params.Message],
        model: str,
        stream: bool,
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | AsyncStream[ChatCompletionChunk]:
        """Create chat completions.

        Generate an OpenAI-compatible chat completion for the
        given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) Whether to stream the response.

          frequency_penalty: (Optional) The penalty for repeated tokens.

          function_call: (Optional) The function call to use.

          functions: (Optional) List of functions to use.

          logit_bias: (Optional) The logit bias to use.

          logprobs: (Optional) The log probabilities to use.

          max_completion_tokens: (Optional) The maximum number of tokens to generate.

          max_tokens: (Optional) The maximum number of tokens to generate.

          n: (Optional) The number of completions to generate.

          parallel_tool_calls: (Optional) Whether to parallelize tool calls.

          presence_penalty: (Optional) The penalty for repeated tokens.

          response_format: (Optional) The response format to use.

          seed: (Optional) The seed to use.

          stop: (Optional) The stop tokens to use.

          stream_options: (Optional) The stream options to use.

          temperature: (Optional) The temperature to use.

          tool_choice: (Optional) The tool choice to use.

          tools: (Optional) The tools to use.

          top_logprobs: (Optional) The top log probabilities to use.

          top_p: (Optional) The top p to use.

          user: (Optional) The user to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: str,
        frequency_penalty: float | Omit = omit,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        logit_bias: Dict[str, float] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | AsyncStream[ChatCompletionChunk]:
        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
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
            cast_to=cast(
                Any, CompletionCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )

    async def retrieve(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionRetrieveResponse:
        """Get chat completion.

        Describe a chat completion by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._get(
            f"/v1/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        model: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CompletionListResponse, AsyncOpenAICursorPage[CompletionListResponse]]:
        """
        List chat completions.

        Args:
          after: The ID of the last chat completion to return.

          limit: The maximum number of chat completions to return.

          model: The model to filter by.

          order: The order to sort the chat completions by: "asc" or "desc". Defaults to "desc".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/chat/completions",
            page=AsyncOpenAICursorPage[CompletionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "model": model,
                        "order": order,
                    },
                    completion_list_params.CompletionListParams,
                ),
            ),
            model=CompletionListResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            completions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            completions.list,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            completions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            completions.list,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            completions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            completions.list,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            completions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            completions.list,
        )
