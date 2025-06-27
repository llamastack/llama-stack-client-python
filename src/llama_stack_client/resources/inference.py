# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import (
    inference_completion_params,
    inference_embeddings_params,
    inference_chat_completion_params,
    inference_batch_completion_params,
    inference_batch_chat_completion_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.completion_response import CompletionResponse
from ..types.embeddings_response import EmbeddingsResponse
from ..types.shared_params.message import Message
from ..types.shared.batch_completion import BatchCompletion
from ..types.shared_params.response_format import ResponseFormat
from ..types.shared_params.sampling_params import SamplingParams
from ..types.shared.chat_completion_response import ChatCompletionResponse
from ..types.shared_params.interleaved_content import InterleavedContent
from ..types.chat_completion_response_stream_chunk import ChatCompletionResponseStreamChunk
from ..types.shared_params.interleaved_content_item import InterleavedContentItem
from ..types.inference_batch_chat_completion_response import InferenceBatchChatCompletionResponse

__all__ = ["InferenceResource", "AsyncInferenceResource"]


class InferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return InferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return InferenceResourceWithStreamingResponse(self)

    def batch_chat_completion(
        self,
        *,
        messages_batch: Iterable[Iterable[Message]],
        model_id: str,
        logprobs: inference_batch_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_config: inference_batch_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_batch_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceBatchChatCompletionResponse:
        """
        Generate chat completions for a batch of messages using the specified model.

        Args:
          messages_batch: The messages to generate completions for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          tool_config: (Optional) Configuration for tool use.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/inference/batch-chat-completion",
            body=maybe_transform(
                {
                    "messages_batch": messages_batch,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "tool_config": tool_config,
                    "tools": tools,
                },
                inference_batch_chat_completion_params.InferenceBatchChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceBatchChatCompletionResponse,
        )

    def batch_completion(
        self,
        *,
        content_batch: List[InterleavedContent],
        model_id: str,
        logprobs: inference_batch_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCompletion:
        """
        Generate completions for a batch of content using the specified model.

        Args:
          content_batch: The content to generate completions for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/inference/batch-completion",
            body=maybe_transform(
                {
                    "content_batch": content_batch,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                },
                inference_batch_completion_params.InferenceBatchCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCompletion,
        )

    @overload
    def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding. There are two
              options: - `ResponseFormat.json_schema`: The grammar is a JSON schema. Most
              providers support this format. - `ResponseFormat.grammar`: The grammar is a BNF
              grammar. This format is more flexible, but not all providers support it.

          sampling_params: Parameters to control the sampling strategy.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          tool_choice: (Optional) Whether tool use is required or automatic. Defaults to
              ToolChoice.auto. .. deprecated:: Use tool_config instead.

          tool_config: (Optional) Configuration for tool use.

          tool_prompt_format: (Optional) Instructs the model how to format tool calls. By default, Llama Stack
              will attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        stream: Literal[True],
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding. There are two
              options: - `ResponseFormat.json_schema`: The grammar is a JSON schema. Most
              providers support this format. - `ResponseFormat.grammar`: The grammar is a BNF
              grammar. This format is more flexible, but not all providers support it.

          sampling_params: Parameters to control the sampling strategy.

          tool_choice: (Optional) Whether tool use is required or automatic. Defaults to
              ToolChoice.auto. .. deprecated:: Use tool_config instead.

          tool_config: (Optional) Configuration for tool use.

          tool_prompt_format: (Optional) Instructs the model how to format tool calls. By default, Llama Stack
              will attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        stream: bool,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | Stream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding. There are two
              options: - `ResponseFormat.json_schema`: The grammar is a JSON schema. Most
              providers support this format. - `ResponseFormat.grammar`: The grammar is a BNF
              grammar. This format is more flexible, but not all providers support it.

          sampling_params: Parameters to control the sampling strategy.

          tool_choice: (Optional) Whether tool use is required or automatic. Defaults to
              ToolChoice.auto. .. deprecated:: Use tool_config instead.

          tool_config: (Optional) Configuration for tool use.

          tool_prompt_format: (Optional) Instructs the model how to format tool calls. By default, Llama Stack
              will attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model_id"], ["messages", "model_id", "stream"])
    def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | Stream[ChatCompletionResponseStreamChunk]:
        if stream:
            extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/inference/chat-completion",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "stream": stream,
                    "tool_choice": tool_choice,
                    "tool_config": tool_config,
                    "tool_prompt_format": tool_prompt_format,
                    "tools": tools,
                },
                inference_chat_completion_params.InferenceChatCompletionParamsStreaming
                if stream
                else inference_chat_completion_params.InferenceChatCompletionParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionResponse,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionResponseStreamChunk],
        )

    @overload
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse:
        """
        Generate a completion for the given content using the specified model.

        Args:
          content: The content to generate a completion for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: Literal[True],
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[CompletionResponse]:
        """
        Generate a completion for the given content using the specified model.

        Args:
          content: The content to generate a completion for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: bool,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | Stream[CompletionResponse]:
        """
        Generate a completion for the given content using the specified model.

        Args:
          content: The content to generate a completion for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["content", "model_id"], ["content", "model_id", "stream"])
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | Stream[CompletionResponse]:
        if stream:
            extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/inference/completion",
            body=maybe_transform(
                {
                    "content": content,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "stream": stream,
                },
                inference_completion_params.InferenceCompletionParamsStreaming
                if stream
                else inference_completion_params.InferenceCompletionParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionResponse,
            stream=stream or False,
            stream_cls=Stream[CompletionResponse],
        )

    def embeddings(
        self,
        *,
        contents: Union[List[str], Iterable[InterleavedContentItem]],
        model_id: str,
        output_dimension: int | NotGiven = NOT_GIVEN,
        task_type: Literal["query", "document"] | NotGiven = NOT_GIVEN,
        text_truncation: Literal["none", "start", "end"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingsResponse:
        """
        Generate embeddings for content pieces using the specified model.

        Args:
          contents: List of contents to generate embeddings for. Each content can be a string or an
              InterleavedContentItem (and hence can be multimodal). The behavior depends on
              the model and provider. Some models may only support text.

          model_id: The identifier of the model to use. The model must be an embedding model
              registered with Llama Stack and available via the /models endpoint.

          output_dimension: (Optional) Output dimensionality for the embeddings. Only supported by
              Matryoshka models.

          task_type: (Optional) How is the embedding being used? This is only supported by asymmetric
              embedding models.

          text_truncation: (Optional) Config for how to truncate text for embedding when text is longer
              than the model's max sequence length.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/inference/embeddings",
            body=maybe_transform(
                {
                    "contents": contents,
                    "model_id": model_id,
                    "output_dimension": output_dimension,
                    "task_type": task_type,
                    "text_truncation": text_truncation,
                },
                inference_embeddings_params.InferenceEmbeddingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingsResponse,
        )


class AsyncInferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncInferenceResourceWithStreamingResponse(self)

    async def batch_chat_completion(
        self,
        *,
        messages_batch: Iterable[Iterable[Message]],
        model_id: str,
        logprobs: inference_batch_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_config: inference_batch_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_batch_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceBatchChatCompletionResponse:
        """
        Generate chat completions for a batch of messages using the specified model.

        Args:
          messages_batch: The messages to generate completions for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          tool_config: (Optional) Configuration for tool use.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/inference/batch-chat-completion",
            body=await async_maybe_transform(
                {
                    "messages_batch": messages_batch,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "tool_config": tool_config,
                    "tools": tools,
                },
                inference_batch_chat_completion_params.InferenceBatchChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceBatchChatCompletionResponse,
        )

    async def batch_completion(
        self,
        *,
        content_batch: List[InterleavedContent],
        model_id: str,
        logprobs: inference_batch_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCompletion:
        """
        Generate completions for a batch of content using the specified model.

        Args:
          content_batch: The content to generate completions for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/inference/batch-completion",
            body=await async_maybe_transform(
                {
                    "content_batch": content_batch,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                },
                inference_batch_completion_params.InferenceBatchCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCompletion,
        )

    @overload
    async def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding. There are two
              options: - `ResponseFormat.json_schema`: The grammar is a JSON schema. Most
              providers support this format. - `ResponseFormat.grammar`: The grammar is a BNF
              grammar. This format is more flexible, but not all providers support it.

          sampling_params: Parameters to control the sampling strategy.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          tool_choice: (Optional) Whether tool use is required or automatic. Defaults to
              ToolChoice.auto. .. deprecated:: Use tool_config instead.

          tool_config: (Optional) Configuration for tool use.

          tool_prompt_format: (Optional) Instructs the model how to format tool calls. By default, Llama Stack
              will attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        stream: Literal[True],
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding. There are two
              options: - `ResponseFormat.json_schema`: The grammar is a JSON schema. Most
              providers support this format. - `ResponseFormat.grammar`: The grammar is a BNF
              grammar. This format is more flexible, but not all providers support it.

          sampling_params: Parameters to control the sampling strategy.

          tool_choice: (Optional) Whether tool use is required or automatic. Defaults to
              ToolChoice.auto. .. deprecated:: Use tool_config instead.

          tool_config: (Optional) Configuration for tool use.

          tool_prompt_format: (Optional) Instructs the model how to format tool calls. By default, Llama Stack
              will attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        stream: bool,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | AsyncStream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding. There are two
              options: - `ResponseFormat.json_schema`: The grammar is a JSON schema. Most
              providers support this format. - `ResponseFormat.grammar`: The grammar is a BNF
              grammar. This format is more flexible, but not all providers support it.

          sampling_params: Parameters to control the sampling strategy.

          tool_choice: (Optional) Whether tool use is required or automatic. Defaults to
              ToolChoice.auto. .. deprecated:: Use tool_config instead.

          tool_config: (Optional) Configuration for tool use.

          tool_prompt_format: (Optional) Instructs the model how to format tool calls. By default, Llama Stack
              will attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: (Optional) List of tool definitions available to the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model_id"], ["messages", "model_id", "stream"])
    async def chat_completion(
        self,
        *,
        messages: Iterable[Message],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | AsyncStream[ChatCompletionResponseStreamChunk]:
        if stream:
            extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/inference/chat-completion",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "stream": stream,
                    "tool_choice": tool_choice,
                    "tool_config": tool_config,
                    "tool_prompt_format": tool_prompt_format,
                    "tools": tools,
                },
                inference_chat_completion_params.InferenceChatCompletionParamsStreaming
                if stream
                else inference_chat_completion_params.InferenceChatCompletionParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionResponse,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionResponseStreamChunk],
        )

    @overload
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse:
        """
        Generate a completion for the given content using the specified model.

        Args:
          content: The content to generate a completion for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: Literal[True],
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[CompletionResponse]:
        """
        Generate a completion for the given content using the specified model.

        Args:
          content: The content to generate a completion for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: bool,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | AsyncStream[CompletionResponse]:
        """
        Generate a completion for the given content using the specified model.

        Args:
          content: The content to generate a completion for.

          model_id: The identifier of the model to use. The model must be registered with Llama
              Stack and available via the /models endpoint.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          logprobs: (Optional) If specified, log probabilities for each token position will be
              returned.

          response_format: (Optional) Grammar specification for guided (structured) decoding.

          sampling_params: (Optional) Parameters to control the sampling strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["content", "model_id"], ["content", "model_id", "stream"])
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | AsyncStream[CompletionResponse]:
        if stream:
            extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/inference/completion",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "stream": stream,
                },
                inference_completion_params.InferenceCompletionParamsStreaming
                if stream
                else inference_completion_params.InferenceCompletionParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionResponse,
            stream=stream or False,
            stream_cls=AsyncStream[CompletionResponse],
        )

    async def embeddings(
        self,
        *,
        contents: Union[List[str], Iterable[InterleavedContentItem]],
        model_id: str,
        output_dimension: int | NotGiven = NOT_GIVEN,
        task_type: Literal["query", "document"] | NotGiven = NOT_GIVEN,
        text_truncation: Literal["none", "start", "end"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingsResponse:
        """
        Generate embeddings for content pieces using the specified model.

        Args:
          contents: List of contents to generate embeddings for. Each content can be a string or an
              InterleavedContentItem (and hence can be multimodal). The behavior depends on
              the model and provider. Some models may only support text.

          model_id: The identifier of the model to use. The model must be an embedding model
              registered with Llama Stack and available via the /models endpoint.

          output_dimension: (Optional) Output dimensionality for the embeddings. Only supported by
              Matryoshka models.

          task_type: (Optional) How is the embedding being used? This is only supported by asymmetric
              embedding models.

          text_truncation: (Optional) Config for how to truncate text for embedding when text is longer
              than the model's max sequence length.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/inference/embeddings",
            body=await async_maybe_transform(
                {
                    "contents": contents,
                    "model_id": model_id,
                    "output_dimension": output_dimension,
                    "task_type": task_type,
                    "text_truncation": text_truncation,
                },
                inference_embeddings_params.InferenceEmbeddingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingsResponse,
        )


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.batch_chat_completion = to_raw_response_wrapper(
            inference.batch_chat_completion,
        )
        self.batch_completion = to_raw_response_wrapper(
            inference.batch_completion,
        )
        self.chat_completion = to_raw_response_wrapper(
            inference.chat_completion,
        )
        self.completion = to_raw_response_wrapper(
            inference.completion,
        )
        self.embeddings = to_raw_response_wrapper(
            inference.embeddings,
        )


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.batch_chat_completion = async_to_raw_response_wrapper(
            inference.batch_chat_completion,
        )
        self.batch_completion = async_to_raw_response_wrapper(
            inference.batch_completion,
        )
        self.chat_completion = async_to_raw_response_wrapper(
            inference.chat_completion,
        )
        self.completion = async_to_raw_response_wrapper(
            inference.completion,
        )
        self.embeddings = async_to_raw_response_wrapper(
            inference.embeddings,
        )


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.batch_chat_completion = to_streamed_response_wrapper(
            inference.batch_chat_completion,
        )
        self.batch_completion = to_streamed_response_wrapper(
            inference.batch_completion,
        )
        self.chat_completion = to_streamed_response_wrapper(
            inference.chat_completion,
        )
        self.completion = to_streamed_response_wrapper(
            inference.completion,
        )
        self.embeddings = to_streamed_response_wrapper(
            inference.embeddings,
        )


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.batch_chat_completion = async_to_streamed_response_wrapper(
            inference.batch_chat_completion,
        )
        self.batch_completion = async_to_streamed_response_wrapper(
            inference.batch_completion,
        )
        self.chat_completion = async_to_streamed_response_wrapper(
            inference.chat_completion,
        )
        self.completion = async_to_streamed_response_wrapper(
            inference.completion,
        )
        self.embeddings = async_to_streamed_response_wrapper(
            inference.embeddings,
        )
