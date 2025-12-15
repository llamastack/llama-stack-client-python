# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ...types import response_list_params, response_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .input_items import (
    InputItemsResource,
    AsyncInputItemsResource,
    InputItemsResourceWithRawResponse,
    AsyncInputItemsResourceWithRawResponse,
    InputItemsResourceWithStreamingResponse,
    AsyncInputItemsResourceWithStreamingResponse,
)
from ..._streaming import Stream, AsyncStream
from ...pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.response_object import ResponseObject
from ...types.response_list_response import ResponseListResponse
from ...types.response_object_stream import ResponseObjectStream
from ...types.response_delete_response import ResponseDeleteResponse

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def input_items(self) -> InputItemsResource:
        return InputItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """
        Create a model response.

        Args:
          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          text: Text response configuration for OpenAI responses.

          tool_choice: Constrains the tools available to the model to a pre-defined set.

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
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        stream: Literal[True],
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ResponseObjectStream]:
        """
        Create a model response.

        Args:
          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          text: Text response configuration for OpenAI responses.

          tool_choice: Constrains the tools available to the model to a pre-defined set.

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
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        stream: bool,
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject | Stream[ResponseObjectStream]:
        """
        Create a model response.

        Args:
          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          text: Text response configuration for OpenAI responses.

          tool_choice: Constrains the tools available to the model to a pre-defined set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    def create(
        self,
        *,
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject | Stream[ResponseObjectStream]:
        return self._post(
            "/v1/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "conversation": conversation,
                    "include": include,
                    "instructions": instructions,
                    "max_infer_iters": max_infer_iters,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_response_id": previous_response_id,
                    "prompt": prompt,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
            stream=stream or False,
            stream_cls=Stream[ResponseObjectStream],
        )

    def retrieve(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """
        Get a model response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            f"/v1/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        order: Optional[Literal["asc", "desc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOpenAICursorPage[ResponseListResponse]:
        """
        List all responses.

        Args:
          order: Sort order for paginated responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/responses",
            page=SyncOpenAICursorPage[ResponseListResponse],
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
                    response_list_params.ResponseListParams,
                ),
            ),
            model=ResponseListResponse,
        )

    def delete(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseDeleteResponse:
        """
        Delete a response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._delete(
            f"/v1/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseDeleteResponse,
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def input_items(self) -> AsyncInputItemsResource:
        return AsyncInputItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """
        Create a model response.

        Args:
          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          text: Text response configuration for OpenAI responses.

          tool_choice: Constrains the tools available to the model to a pre-defined set.

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
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        stream: Literal[True],
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ResponseObjectStream]:
        """
        Create a model response.

        Args:
          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          text: Text response configuration for OpenAI responses.

          tool_choice: Constrains the tools available to the model to a pre-defined set.

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
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        stream: bool,
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject | AsyncStream[ResponseObjectStream]:
        """
        Create a model response.

        Args:
          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          text: Text response configuration for OpenAI responses.

          tool_choice: Constrains the tools available to the model to a pre-defined set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    async def create(
        self,
        *,
        input: Union[
            str,
            Iterable[
                response_create_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
        ],
        model: str,
        conversation: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject | AsyncStream[ResponseObjectStream]:
        return await self._post(
            "/v1/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "conversation": conversation,
                    "include": include,
                    "instructions": instructions,
                    "max_infer_iters": max_infer_iters,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_response_id": previous_response_id,
                    "prompt": prompt,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
            stream=stream or False,
            stream_cls=AsyncStream[ResponseObjectStream],
        )

    async def retrieve(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseObject:
        """
        Get a model response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            f"/v1/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        order: Optional[Literal["asc", "desc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResponseListResponse, AsyncOpenAICursorPage[ResponseListResponse]]:
        """
        List all responses.

        Args:
          order: Sort order for paginated responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/responses",
            page=AsyncOpenAICursorPage[ResponseListResponse],
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
                    response_list_params.ResponseListParams,
                ),
            ),
            model=ResponseListResponse,
        )

    async def delete(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseDeleteResponse:
        """
        Delete a response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._delete(
            f"/v1/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseDeleteResponse,
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            responses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            responses.list,
        )
        self.delete = to_raw_response_wrapper(
            responses.delete,
        )

    @cached_property
    def input_items(self) -> InputItemsResourceWithRawResponse:
        return InputItemsResourceWithRawResponse(self._responses.input_items)


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            responses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            responses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            responses.delete,
        )

    @cached_property
    def input_items(self) -> AsyncInputItemsResourceWithRawResponse:
        return AsyncInputItemsResourceWithRawResponse(self._responses.input_items)


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            responses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            responses.list,
        )
        self.delete = to_streamed_response_wrapper(
            responses.delete,
        )

    @cached_property
    def input_items(self) -> InputItemsResourceWithStreamingResponse:
        return InputItemsResourceWithStreamingResponse(self._responses.input_items)


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            responses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            responses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            responses.delete,
        )

    @cached_property
    def input_items(self) -> AsyncInputItemsResourceWithStreamingResponse:
        return AsyncInputItemsResourceWithStreamingResponse(self._responses.input_items)
