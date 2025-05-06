# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tool_runtime import rag_tool_query_context_params, rag_tool_insert_documents_params
from ...types.interleaved_content_param import InterleavedContentParam
from ...types.tool_runtime.rag_tool_query_context_response import RagToolQueryContextResponse

__all__ = ["RagToolResource", "AsyncRagToolResource"]


class RagToolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RagToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return RagToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RagToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return RagToolResourceWithStreamingResponse(self)

    def insert_documents(
        self,
        *,
        chunk_size_in_tokens: int,
        documents: Iterable[rag_tool_insert_documents_params.Document],
        vector_db_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Index documents so they can be used by the RAG system

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/tool-runtime/rag-tool/insert",
            body=maybe_transform(
                {
                    "chunk_size_in_tokens": chunk_size_in_tokens,
                    "documents": documents,
                    "vector_db_id": vector_db_id,
                },
                rag_tool_insert_documents_params.RagToolInsertDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query_context(
        self,
        *,
        content: InterleavedContentParam,
        vector_db_ids: List[str],
        query_config: rag_tool_query_context_params.QueryConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RagToolQueryContextResponse:
        """
        Query the RAG system for context; typically invoked by the agent

        Args:
          content: A image content item

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tool-runtime/rag-tool/query",
            body=maybe_transform(
                {
                    "content": content,
                    "vector_db_ids": vector_db_ids,
                    "query_config": query_config,
                },
                rag_tool_query_context_params.RagToolQueryContextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RagToolQueryContextResponse,
        )


class AsyncRagToolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRagToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRagToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRagToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncRagToolResourceWithStreamingResponse(self)

    async def insert_documents(
        self,
        *,
        chunk_size_in_tokens: int,
        documents: Iterable[rag_tool_insert_documents_params.Document],
        vector_db_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Index documents so they can be used by the RAG system

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/tool-runtime/rag-tool/insert",
            body=await async_maybe_transform(
                {
                    "chunk_size_in_tokens": chunk_size_in_tokens,
                    "documents": documents,
                    "vector_db_id": vector_db_id,
                },
                rag_tool_insert_documents_params.RagToolInsertDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query_context(
        self,
        *,
        content: InterleavedContentParam,
        vector_db_ids: List[str],
        query_config: rag_tool_query_context_params.QueryConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RagToolQueryContextResponse:
        """
        Query the RAG system for context; typically invoked by the agent

        Args:
          content: A image content item

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tool-runtime/rag-tool/query",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "vector_db_ids": vector_db_ids,
                    "query_config": query_config,
                },
                rag_tool_query_context_params.RagToolQueryContextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RagToolQueryContextResponse,
        )


class RagToolResourceWithRawResponse:
    def __init__(self, rag_tool: RagToolResource) -> None:
        self._rag_tool = rag_tool

        self.insert_documents = to_raw_response_wrapper(
            rag_tool.insert_documents,
        )
        self.query_context = to_raw_response_wrapper(
            rag_tool.query_context,
        )


class AsyncRagToolResourceWithRawResponse:
    def __init__(self, rag_tool: AsyncRagToolResource) -> None:
        self._rag_tool = rag_tool

        self.insert_documents = async_to_raw_response_wrapper(
            rag_tool.insert_documents,
        )
        self.query_context = async_to_raw_response_wrapper(
            rag_tool.query_context,
        )


class RagToolResourceWithStreamingResponse:
    def __init__(self, rag_tool: RagToolResource) -> None:
        self._rag_tool = rag_tool

        self.insert_documents = to_streamed_response_wrapper(
            rag_tool.insert_documents,
        )
        self.query_context = to_streamed_response_wrapper(
            rag_tool.query_context,
        )


class AsyncRagToolResourceWithStreamingResponse:
    def __init__(self, rag_tool: AsyncRagToolResource) -> None:
        self._rag_tool = rag_tool

        self.insert_documents = async_to_streamed_response_wrapper(
            rag_tool.insert_documents,
        )
        self.query_context = async_to_streamed_response_wrapper(
            rag_tool.query_context,
        )
