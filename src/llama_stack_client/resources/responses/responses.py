# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ...types import response_list_params, response_create_params, response_compact_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
from ...types.compacted_response import CompactedResponse
from ...types.response_list_response import ResponseListResponse
from ...types.response_object_stream import ResponseObjectStream
from ...types.response_delete_response import ResponseDeleteResponse

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    """
    OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
    """

    @cached_property
    def input_items(self) -> InputItemsResource:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          background: Whether to run the model response in the background. When true, returns
              immediately with status 'queued'.

          context_management: Context management configuration. When set with type 'compaction', automatically
              compacts conversation history when token count exceeds the compact_threshold.

          conversation: Optional ID of a conversation to add the response to.

          frequency_penalty: Penalizes new tokens based on their frequency in the text so far.

          guardrails: List of guardrails to apply during response generation.

          include: Additional fields to include in the response.

          instructions: Instructions to guide the model's behavior.

          max_infer_iters: Maximum number of inference iterations.

          max_output_tokens: Upper bound for the number of tokens that can be generated for a response.

          max_tool_calls: Max number of total calls to built-in tools that can be processed in a response.

          metadata: Dictionary of metadata key-value pairs to attach to the response.

          parallel_tool_calls: Whether to enable parallel tool calls.

          presence_penalty: Penalizes new tokens based on whether they appear in the text so far.

          previous_response_id: Optional ID of a previous response to continue from.

          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          safety_identifier: A stable identifier used for safety monitoring and abuse detection.

          service_tier: The service tier for the request.

          store: Whether to store the response in the database.

          stream: Whether to stream the response.

          stream_options: Options that control streamed response behavior.

          temperature: Sampling temperature.

          text: Text response configuration for OpenAI responses.

          tool_choice: How the model should select which tool to call (if any).

          tools: List of tools available to the model.

          top_logprobs: The number of most likely tokens to return at each position, along with their
              log probabilities.

          top_p: Nucleus sampling parameter that controls response diversity (lower values
              increase focus).

          truncation: Controls how the service truncates input when it exceeds the model context
              window.

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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          stream: Whether to stream the response.

          background: Whether to run the model response in the background. When true, returns
              immediately with status 'queued'.

          context_management: Context management configuration. When set with type 'compaction', automatically
              compacts conversation history when token count exceeds the compact_threshold.

          conversation: Optional ID of a conversation to add the response to.

          frequency_penalty: Penalizes new tokens based on their frequency in the text so far.

          guardrails: List of guardrails to apply during response generation.

          include: Additional fields to include in the response.

          instructions: Instructions to guide the model's behavior.

          max_infer_iters: Maximum number of inference iterations.

          max_output_tokens: Upper bound for the number of tokens that can be generated for a response.

          max_tool_calls: Max number of total calls to built-in tools that can be processed in a response.

          metadata: Dictionary of metadata key-value pairs to attach to the response.

          parallel_tool_calls: Whether to enable parallel tool calls.

          presence_penalty: Penalizes new tokens based on whether they appear in the text so far.

          previous_response_id: Optional ID of a previous response to continue from.

          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          safety_identifier: A stable identifier used for safety monitoring and abuse detection.

          service_tier: The service tier for the request.

          store: Whether to store the response in the database.

          stream_options: Options that control streamed response behavior.

          temperature: Sampling temperature.

          text: Text response configuration for OpenAI responses.

          tool_choice: How the model should select which tool to call (if any).

          tools: List of tools available to the model.

          top_logprobs: The number of most likely tokens to return at each position, along with their
              log probabilities.

          top_p: Nucleus sampling parameter that controls response diversity (lower values
              increase focus).

          truncation: Controls how the service truncates input when it exceeds the model context
              window.

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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          stream: Whether to stream the response.

          background: Whether to run the model response in the background. When true, returns
              immediately with status 'queued'.

          context_management: Context management configuration. When set with type 'compaction', automatically
              compacts conversation history when token count exceeds the compact_threshold.

          conversation: Optional ID of a conversation to add the response to.

          frequency_penalty: Penalizes new tokens based on their frequency in the text so far.

          guardrails: List of guardrails to apply during response generation.

          include: Additional fields to include in the response.

          instructions: Instructions to guide the model's behavior.

          max_infer_iters: Maximum number of inference iterations.

          max_output_tokens: Upper bound for the number of tokens that can be generated for a response.

          max_tool_calls: Max number of total calls to built-in tools that can be processed in a response.

          metadata: Dictionary of metadata key-value pairs to attach to the response.

          parallel_tool_calls: Whether to enable parallel tool calls.

          presence_penalty: Penalizes new tokens based on whether they appear in the text so far.

          previous_response_id: Optional ID of a previous response to continue from.

          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          safety_identifier: A stable identifier used for safety monitoring and abuse detection.

          service_tier: The service tier for the request.

          store: Whether to store the response in the database.

          stream_options: Options that control streamed response behavior.

          temperature: Sampling temperature.

          text: Text response configuration for OpenAI responses.

          tool_choice: How the model should select which tool to call (if any).

          tools: List of tools available to the model.

          top_logprobs: The number of most likely tokens to return at each position, along with their
              log probabilities.

          top_p: Nucleus sampling parameter that controls response diversity (lower values
              increase focus).

          truncation: Controls how the service truncates input when it exceeds the model context
              window.

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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
                    "background": background,
                    "context_management": context_management,
                    "conversation": conversation,
                    "frequency_penalty": frequency_penalty,
                    "guardrails": guardrails,
                    "include": include,
                    "instructions": instructions,
                    "max_infer_iters": max_infer_iters,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "previous_response_id": previous_response_id,
                    "prompt": prompt,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "safety_identifier": safety_identifier,
                    "service_tier": service_tier,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
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
          response_id: The ID of the OpenAI response to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            path_template("/v1/responses/{response_id}", response_id=response_id),
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
          after: The ID of the last response to return.

          limit: The number of responses to return.

          model: The model to filter responses by.

          order: The order to sort responses by when sorted by created_at ('asc' or 'desc').

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
          response_id: The ID of the OpenAI response to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._delete(
            path_template("/v1/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseDeleteResponse,
        )

    def compact(
        self,
        *,
        model: str,
        input: Union[
            str,
            Iterable[
                response_compact_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
            None,
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_compact_params.Reasoning] | Omit = omit,
        text: Optional[response_compact_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_compact_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompactedResponse:
        """
        **[alpha]** Compresses conversation history into a smaller representation while
        preserving context. This endpoint is in alpha and may change without notice.

        Args:
          model: The model to use for generating the compacted summary.

          input: Input message(s) to compact.

          instructions: Instructions to guide the compaction.

          parallel_tool_calls: Whether to enable parallel tool calls. Accepted for compatibility but not used
              during compaction.

          previous_response_id: ID of a previous response whose history to compact.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          text: Text response configuration for OpenAI responses.

          tools: List of tools available to the model. Accepted for compatibility but not used
              during compaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/responses/compact",
            body=maybe_transform(
                {
                    "model": model,
                    "input": input,
                    "instructions": instructions,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_response_id": previous_response_id,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "text": text,
                    "tools": tools,
                },
                response_compact_params.ResponseCompactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompactedResponse,
        )


class AsyncResponsesResource(AsyncAPIResource):
    """
    OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
    """

    @cached_property
    def input_items(self) -> AsyncInputItemsResource:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          background: Whether to run the model response in the background. When true, returns
              immediately with status 'queued'.

          context_management: Context management configuration. When set with type 'compaction', automatically
              compacts conversation history when token count exceeds the compact_threshold.

          conversation: Optional ID of a conversation to add the response to.

          frequency_penalty: Penalizes new tokens based on their frequency in the text so far.

          guardrails: List of guardrails to apply during response generation.

          include: Additional fields to include in the response.

          instructions: Instructions to guide the model's behavior.

          max_infer_iters: Maximum number of inference iterations.

          max_output_tokens: Upper bound for the number of tokens that can be generated for a response.

          max_tool_calls: Max number of total calls to built-in tools that can be processed in a response.

          metadata: Dictionary of metadata key-value pairs to attach to the response.

          parallel_tool_calls: Whether to enable parallel tool calls.

          presence_penalty: Penalizes new tokens based on whether they appear in the text so far.

          previous_response_id: Optional ID of a previous response to continue from.

          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          safety_identifier: A stable identifier used for safety monitoring and abuse detection.

          service_tier: The service tier for the request.

          store: Whether to store the response in the database.

          stream: Whether to stream the response.

          stream_options: Options that control streamed response behavior.

          temperature: Sampling temperature.

          text: Text response configuration for OpenAI responses.

          tool_choice: How the model should select which tool to call (if any).

          tools: List of tools available to the model.

          top_logprobs: The number of most likely tokens to return at each position, along with their
              log probabilities.

          top_p: Nucleus sampling parameter that controls response diversity (lower values
              increase focus).

          truncation: Controls how the service truncates input when it exceeds the model context
              window.

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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          stream: Whether to stream the response.

          background: Whether to run the model response in the background. When true, returns
              immediately with status 'queued'.

          context_management: Context management configuration. When set with type 'compaction', automatically
              compacts conversation history when token count exceeds the compact_threshold.

          conversation: Optional ID of a conversation to add the response to.

          frequency_penalty: Penalizes new tokens based on their frequency in the text so far.

          guardrails: List of guardrails to apply during response generation.

          include: Additional fields to include in the response.

          instructions: Instructions to guide the model's behavior.

          max_infer_iters: Maximum number of inference iterations.

          max_output_tokens: Upper bound for the number of tokens that can be generated for a response.

          max_tool_calls: Max number of total calls to built-in tools that can be processed in a response.

          metadata: Dictionary of metadata key-value pairs to attach to the response.

          parallel_tool_calls: Whether to enable parallel tool calls.

          presence_penalty: Penalizes new tokens based on whether they appear in the text so far.

          previous_response_id: Optional ID of a previous response to continue from.

          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          safety_identifier: A stable identifier used for safety monitoring and abuse detection.

          service_tier: The service tier for the request.

          store: Whether to store the response in the database.

          stream_options: Options that control streamed response behavior.

          temperature: Sampling temperature.

          text: Text response configuration for OpenAI responses.

          tool_choice: How the model should select which tool to call (if any).

          tools: List of tools available to the model.

          top_logprobs: The number of most likely tokens to return at each position, along with their
              log probabilities.

          top_p: Nucleus sampling parameter that controls response diversity (lower values
              increase focus).

          truncation: Controls how the service truncates input when it exceeds the model context
              window.

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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          stream: Whether to stream the response.

          background: Whether to run the model response in the background. When true, returns
              immediately with status 'queued'.

          context_management: Context management configuration. When set with type 'compaction', automatically
              compacts conversation history when token count exceeds the compact_threshold.

          conversation: Optional ID of a conversation to add the response to.

          frequency_penalty: Penalizes new tokens based on their frequency in the text so far.

          guardrails: List of guardrails to apply during response generation.

          include: Additional fields to include in the response.

          instructions: Instructions to guide the model's behavior.

          max_infer_iters: Maximum number of inference iterations.

          max_output_tokens: Upper bound for the number of tokens that can be generated for a response.

          max_tool_calls: Max number of total calls to built-in tools that can be processed in a response.

          metadata: Dictionary of metadata key-value pairs to attach to the response.

          parallel_tool_calls: Whether to enable parallel tool calls.

          presence_penalty: Penalizes new tokens based on whether they appear in the text so far.

          previous_response_id: Optional ID of a previous response to continue from.

          prompt: OpenAI compatible Prompt object that is used in OpenAI responses.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          safety_identifier: A stable identifier used for safety monitoring and abuse detection.

          service_tier: The service tier for the request.

          store: Whether to store the response in the database.

          stream_options: Options that control streamed response behavior.

          temperature: Sampling temperature.

          text: Text response configuration for OpenAI responses.

          tool_choice: How the model should select which tool to call (if any).

          tools: List of tools available to the model.

          top_logprobs: The number of most likely tokens to return at each position, along with their
              log probabilities.

          top_p: Nucleus sampling parameter that controls response diversity (lower values
              increase focus).

          truncation: Controls how the service truncates input when it exceeds the model context
              window.

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
        background: bool | Omit = omit,
        context_management: Optional[Iterable[response_create_params.ContextManagement]] | Omit = omit,
        conversation: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        guardrails: Optional[SequenceNotStr[response_create_params.Guardrail]] | Omit = omit,
        include: List[
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
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_infer_iters: Optional[int] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        safety_identifier: Optional[str] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "priority"]] | Omit = omit,
        store: bool | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: Optional[response_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
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
                    "background": background,
                    "context_management": context_management,
                    "conversation": conversation,
                    "frequency_penalty": frequency_penalty,
                    "guardrails": guardrails,
                    "include": include,
                    "instructions": instructions,
                    "max_infer_iters": max_infer_iters,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "previous_response_id": previous_response_id,
                    "prompt": prompt,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "safety_identifier": safety_identifier,
                    "service_tier": service_tier,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
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
          response_id: The ID of the OpenAI response to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            path_template("/v1/responses/{response_id}", response_id=response_id),
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
          after: The ID of the last response to return.

          limit: The number of responses to return.

          model: The model to filter responses by.

          order: The order to sort responses by when sorted by created_at ('asc' or 'desc').

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
          response_id: The ID of the OpenAI response to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._delete(
            path_template("/v1/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseDeleteResponse,
        )

    async def compact(
        self,
        *,
        model: str,
        input: Union[
            str,
            Iterable[
                response_compact_params.InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput
            ],
            None,
        ]
        | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_compact_params.Reasoning] | Omit = omit,
        text: Optional[response_compact_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_compact_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompactedResponse:
        """
        **[alpha]** Compresses conversation history into a smaller representation while
        preserving context. This endpoint is in alpha and may change without notice.

        Args:
          model: The model to use for generating the compacted summary.

          input: Input message(s) to compact.

          instructions: Instructions to guide the compaction.

          parallel_tool_calls: Whether to enable parallel tool calls. Accepted for compatibility but not used
              during compaction.

          previous_response_id: ID of a previous response whose history to compact.

          prompt_cache_key: A key to use when reading from or writing to the prompt cache.

          reasoning: Configuration for reasoning effort in OpenAI responses.

              Controls how much reasoning the model performs before generating a response.

          text: Text response configuration for OpenAI responses.

          tools: List of tools available to the model. Accepted for compatibility but not used
              during compaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/responses/compact",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "input": input,
                    "instructions": instructions,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_response_id": previous_response_id,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "text": text,
                    "tools": tools,
                },
                response_compact_params.ResponseCompactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompactedResponse,
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
        self.compact = to_raw_response_wrapper(
            responses.compact,
        )

    @cached_property
    def input_items(self) -> InputItemsResourceWithRawResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
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
        self.compact = async_to_raw_response_wrapper(
            responses.compact,
        )

    @cached_property
    def input_items(self) -> AsyncInputItemsResourceWithRawResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
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
        self.compact = to_streamed_response_wrapper(
            responses.compact,
        )

    @cached_property
    def input_items(self) -> InputItemsResourceWithStreamingResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
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
        self.compact = async_to_streamed_response_wrapper(
            responses.compact,
        )

    @cached_property
    def input_items(self) -> AsyncInputItemsResourceWithStreamingResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
        return AsyncInputItemsResourceWithStreamingResponse(self._responses.input_items)
