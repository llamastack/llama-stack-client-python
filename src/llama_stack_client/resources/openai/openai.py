# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OpenAIResource", "AsyncOpenAIResource"]


class OpenAIResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> OpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return OpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return OpenAIResourceWithStreamingResponse(self)


class AsyncOpenAIResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncOpenAIResourceWithStreamingResponse(self)


class OpenAIResourceWithRawResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._openai.v1)


class AsyncOpenAIResourceWithRawResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._openai.v1)


class OpenAIResourceWithStreamingResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._openai.v1)


class AsyncOpenAIResourceWithStreamingResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._openai.v1)
