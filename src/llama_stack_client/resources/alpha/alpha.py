# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .inference import (
    InferenceResource,
    AsyncInferenceResource,
    InferenceResourceWithRawResponse,
    AsyncInferenceResourceWithRawResponse,
    InferenceResourceWithStreamingResponse,
    AsyncInferenceResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AlphaResource", "AsyncAlphaResource"]


class AlphaResource(SyncAPIResource):
    @cached_property
    def admin(self) -> AdminResource:
        """Administrative APIs for inspecting providers, routes, health, and version."""
        return AdminResource(self._client)

    @cached_property
    def inference(self) -> InferenceResource:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        return InferenceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AlphaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AlphaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlphaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AlphaResourceWithStreamingResponse(self)


class AsyncAlphaResource(AsyncAPIResource):
    @cached_property
    def admin(self) -> AsyncAdminResource:
        """Administrative APIs for inspecting providers, routes, health, and version."""
        return AsyncAdminResource(self._client)

    @cached_property
    def inference(self) -> AsyncInferenceResource:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        return AsyncInferenceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlphaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlphaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlphaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncAlphaResourceWithStreamingResponse(self)


class AlphaResourceWithRawResponse:
    def __init__(self, alpha: AlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        """Administrative APIs for inspecting providers, routes, health, and version."""
        return AdminResourceWithRawResponse(self._alpha.admin)

    @cached_property
    def inference(self) -> InferenceResourceWithRawResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        return InferenceResourceWithRawResponse(self._alpha.inference)


class AsyncAlphaResourceWithRawResponse:
    def __init__(self, alpha: AsyncAlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        """Administrative APIs for inspecting providers, routes, health, and version."""
        return AsyncAdminResourceWithRawResponse(self._alpha.admin)

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithRawResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        return AsyncInferenceResourceWithRawResponse(self._alpha.inference)


class AlphaResourceWithStreamingResponse:
    def __init__(self, alpha: AlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        """Administrative APIs for inspecting providers, routes, health, and version."""
        return AdminResourceWithStreamingResponse(self._alpha.admin)

    @cached_property
    def inference(self) -> InferenceResourceWithStreamingResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        return InferenceResourceWithStreamingResponse(self._alpha.inference)


class AsyncAlphaResourceWithStreamingResponse:
    def __init__(self, alpha: AsyncAlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        """Administrative APIs for inspecting providers, routes, health, and version."""
        return AsyncAdminResourceWithStreamingResponse(self._alpha.admin)

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        return AsyncInferenceResourceWithStreamingResponse(self._alpha.inference)
