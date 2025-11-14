# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import vector_io_query_params, vector_io_insert_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.query_chunks_response import QueryChunksResponse

__all__ = ["VectorIoResource", "AsyncVectorIoResource"]


class VectorIoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VectorIoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return VectorIoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorIoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return VectorIoResourceWithStreamingResponse(self)

    def insert(
        self,
        *,
        chunks: Iterable[vector_io_insert_params.Chunk],
        vector_store_id: str,
        ttl_seconds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Insert chunks into a vector database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/vector-io/insert",
            body=maybe_transform(
                {
                    "chunks": chunks,
                    "vector_store_id": vector_store_id,
                    "ttl_seconds": ttl_seconds,
                },
                vector_io_insert_params.VectorIoInsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query(
        self,
        *,
        query: vector_io_query_params.Query,
        vector_store_id: str,
        params: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryChunksResponse:
        """
        Query chunks from a vector database.

        Args:
          query: A image content item

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector-io/query",
            body=maybe_transform(
                {
                    "query": query,
                    "vector_store_id": vector_store_id,
                    "params": params,
                },
                vector_io_query_params.VectorIoQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryChunksResponse,
        )


class AsyncVectorIoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVectorIoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorIoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorIoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncVectorIoResourceWithStreamingResponse(self)

    async def insert(
        self,
        *,
        chunks: Iterable[vector_io_insert_params.Chunk],
        vector_store_id: str,
        ttl_seconds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Insert chunks into a vector database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/vector-io/insert",
            body=await async_maybe_transform(
                {
                    "chunks": chunks,
                    "vector_store_id": vector_store_id,
                    "ttl_seconds": ttl_seconds,
                },
                vector_io_insert_params.VectorIoInsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query(
        self,
        *,
        query: vector_io_query_params.Query,
        vector_store_id: str,
        params: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryChunksResponse:
        """
        Query chunks from a vector database.

        Args:
          query: A image content item

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector-io/query",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "vector_store_id": vector_store_id,
                    "params": params,
                },
                vector_io_query_params.VectorIoQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryChunksResponse,
        )


class VectorIoResourceWithRawResponse:
    def __init__(self, vector_io: VectorIoResource) -> None:
        self._vector_io = vector_io

        self.insert = to_raw_response_wrapper(
            vector_io.insert,
        )
        self.query = to_raw_response_wrapper(
            vector_io.query,
        )


class AsyncVectorIoResourceWithRawResponse:
    def __init__(self, vector_io: AsyncVectorIoResource) -> None:
        self._vector_io = vector_io

        self.insert = async_to_raw_response_wrapper(
            vector_io.insert,
        )
        self.query = async_to_raw_response_wrapper(
            vector_io.query,
        )


class VectorIoResourceWithStreamingResponse:
    def __init__(self, vector_io: VectorIoResource) -> None:
        self._vector_io = vector_io

        self.insert = to_streamed_response_wrapper(
            vector_io.insert,
        )
        self.query = to_streamed_response_wrapper(
            vector_io.query,
        )


class AsyncVectorIoResourceWithStreamingResponse:
    def __init__(self, vector_io: AsyncVectorIoResource) -> None:
        self._vector_io = vector_io

        self.insert = async_to_streamed_response_wrapper(
            vector_io.insert,
        )
        self.query = async_to_streamed_response_wrapper(
            vector_io.query,
        )
