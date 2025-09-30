# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import inference_rerank_params
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
from .._wrappers import DataWrapper
from .._base_client import make_request_options
from ..types.inference_rerank_response import InferenceRerankResponse

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

    def rerank(
        self,
        *,
        items: SequenceNotStr[inference_rerank_params.Item],
        model: str,
        query: inference_rerank_params.Query,
        max_num_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceRerankResponse:
        """
        Rerank a list of documents based on their relevance to a query.

        Args:
          items: List of items to rerank. Each item can be a string, text content part, or image
              content part. Each input must not exceed the model's max input token length.

          model: The identifier of the reranking model to use.

          query: The search query to rank items against. Can be a string, text content part, or
              image content part. The input must not exceed the model's max input token
              length.

          max_num_results: (Optional) Maximum number of results to return. Default: returns all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1alpha/inference/rerank",
            body=maybe_transform(
                {
                    "items": items,
                    "model": model,
                    "query": query,
                    "max_num_results": max_num_results,
                },
                inference_rerank_params.InferenceRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[InferenceRerankResponse]._unwrapper,
            ),
            cast_to=cast(Type[InferenceRerankResponse], DataWrapper[InferenceRerankResponse]),
        )

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/completions.")
    @overload
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        stream: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/completions.")
    @overload
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: Literal[True],
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/completions.")
    @overload
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: bool,
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/completions.")
    @required_args(["content", "model_id"], ["content", "model_id", "stream"])
    def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def rerank(
        self,
        *,
        items: SequenceNotStr[inference_rerank_params.Item],
        model: str,
        query: inference_rerank_params.Query,
        max_num_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceRerankResponse:
        """
        Rerank a list of documents based on their relevance to a query.

        Args:
          items: List of items to rerank. Each item can be a string, text content part, or image
              content part. Each input must not exceed the model's max input token length.

          model: The identifier of the reranking model to use.

          query: The search query to rank items against. Can be a string, text content part, or
              image content part. The input must not exceed the model's max input token
              length.

          max_num_results: (Optional) Maximum number of results to return. Default: returns all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1alpha/inference/rerank",
            body=await async_maybe_transform(
                {
                    "items": items,
                    "model": model,
                    "query": query,
                    "max_num_results": max_num_results,
                },
                inference_rerank_params.InferenceRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[InferenceRerankResponse]._unwrapper,
            ),
            cast_to=cast(Type[InferenceRerankResponse], DataWrapper[InferenceRerankResponse]),
        )

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/completions.")
    @overload
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        stream: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/openai/v1/completions.")
    @overload
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: Literal[True],
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/completions.")
    @overload
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        stream: bool,
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated("/v1/inference/completion is deprecated. Please use /v1/completions.")
    @required_args(["content", "model_id"], ["content", "model_id", "stream"])
    async def completion(
        self,
        *,
        content: InterleavedContent,
        model_id: str,
        logprobs: inference_completion_params.Logprobs | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        sampling_params: SamplingParams | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
    


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.rerank = to_raw_response_wrapper(
            inference.rerank,
        )


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.rerank = async_to_raw_response_wrapper(
            inference.rerank,
        )


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.rerank = to_streamed_response_wrapper(
            inference.rerank,
        )


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.rerank = async_to_streamed_response_wrapper(
            inference.rerank,
        )
