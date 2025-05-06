# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.openai.v1 import chat_generate_completion_params
from ....types.openai.v1.message_param_param import MessageParamParam
from ....types.openai.v1.chat_generate_completion_response import ChatGenerateCompletionResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def generate_completion(
        self,
        *,
        messages: Iterable[MessageParamParam],
        model: str,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
        | NotGiven = NOT_GIVEN,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: chat_generate_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
        | NotGiven = NOT_GIVEN,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatGenerateCompletionResponse:
        """
        Generate an OpenAI-compatible chat completion for the given messages using the
        specified model.

        Args:
          messages: List of messages in the conversation

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          frequency_penalty: (Optional) The penalty for repeated tokens

          function_call: (Optional) The function call to use

          functions: (Optional) List of functions to use

          logit_bias: (Optional) The logit bias to use

          logprobs: (Optional) The log probabilities to use

          max_completion_tokens: (Optional) The maximum number of tokens to generate

          max_tokens: (Optional) The maximum number of tokens to generate

          n: (Optional) The number of completions to generate

          parallel_tool_calls: (Optional) Whether to parallelize tool calls

          presence_penalty: (Optional) The penalty for repeated tokens

          response_format: (Optional) The response format to use

          seed: (Optional) The seed to use

          stop: (Optional) The stop tokens to use

          stream: (Optional) Whether to stream the response

          stream_options: (Optional) The stream options to use

          temperature: (Optional) The temperature to use

          tool_choice: (Optional) The tool choice to use

          tools: (Optional) The tools to use

          top_logprobs: (Optional) The top log probabilities to use

          top_p: (Optional) The top p to use

          user: (Optional) The user to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ChatGenerateCompletionResponse,
            self._post(
                "/v1/openai/v1/chat/completions",
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
                    chat_generate_completion_params.ChatGenerateCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatGenerateCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def generate_completion(
        self,
        *,
        messages: Iterable[MessageParamParam],
        model: str,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
        | NotGiven = NOT_GIVEN,
        functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: chat_generate_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
        | NotGiven = NOT_GIVEN,
        tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]] | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatGenerateCompletionResponse:
        """
        Generate an OpenAI-compatible chat completion for the given messages using the
        specified model.

        Args:
          messages: List of messages in the conversation

          model: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          frequency_penalty: (Optional) The penalty for repeated tokens

          function_call: (Optional) The function call to use

          functions: (Optional) List of functions to use

          logit_bias: (Optional) The logit bias to use

          logprobs: (Optional) The log probabilities to use

          max_completion_tokens: (Optional) The maximum number of tokens to generate

          max_tokens: (Optional) The maximum number of tokens to generate

          n: (Optional) The number of completions to generate

          parallel_tool_calls: (Optional) Whether to parallelize tool calls

          presence_penalty: (Optional) The penalty for repeated tokens

          response_format: (Optional) The response format to use

          seed: (Optional) The seed to use

          stop: (Optional) The stop tokens to use

          stream: (Optional) Whether to stream the response

          stream_options: (Optional) The stream options to use

          temperature: (Optional) The temperature to use

          tool_choice: (Optional) The tool choice to use

          tools: (Optional) The tools to use

          top_logprobs: (Optional) The top log probabilities to use

          top_p: (Optional) The top p to use

          user: (Optional) The user to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ChatGenerateCompletionResponse,
            await self._post(
                "/v1/openai/v1/chat/completions",
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
                    chat_generate_completion_params.ChatGenerateCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatGenerateCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.generate_completion = to_raw_response_wrapper(
            chat.generate_completion,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.generate_completion = async_to_raw_response_wrapper(
            chat.generate_completion,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.generate_completion = to_streamed_response_wrapper(
            chat.generate_completion,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.generate_completion = async_to_streamed_response_wrapper(
            chat.generate_completion,
        )
