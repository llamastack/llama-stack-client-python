# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .agents.agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)

__all__ = ["AlphaResource", "AsyncAlphaResource"]


class AlphaResource(SyncAPIResource):
    @cached_property
    def inference(self) -> InferenceResource:
        return InferenceResource(self._client)

    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

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
    def inference(self) -> AsyncInferenceResource:
        return AsyncInferenceResource(self._client)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

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
    def inference(self) -> InferenceResourceWithRawResponse:
        return InferenceResourceWithRawResponse(self._alpha.inference)

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._alpha.agents)


class AsyncAlphaResourceWithRawResponse:
    def __init__(self, alpha: AsyncAlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithRawResponse:
        return AsyncInferenceResourceWithRawResponse(self._alpha.inference)

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._alpha.agents)


class AlphaResourceWithStreamingResponse:
    def __init__(self, alpha: AlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def inference(self) -> InferenceResourceWithStreamingResponse:
        return InferenceResourceWithStreamingResponse(self._alpha.inference)

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._alpha.agents)


class AsyncAlphaResourceWithStreamingResponse:
    def __init__(self, alpha: AsyncAlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithStreamingResponse:
        return AsyncInferenceResourceWithStreamingResponse(self._alpha.inference)

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._alpha.agents)
