# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.vector_stores import file_batch_create_params, file_batch_list_files_params
from ...types.vector_stores.vector_store_file import VectorStoreFile
from ...types.vector_stores.vector_store_file_batches import VectorStoreFileBatches

__all__ = ["FileBatchesResource", "AsyncFileBatchesResource"]


class FileBatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return FileBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return FileBatchesResourceWithStreamingResponse(self)

    def create(
        self,
        vector_store_id: str,
        *,
        file_ids: SequenceNotStr[str],
        attributes: Optional[Dict[str, object]] | Omit = omit,
        chunking_strategy: Optional[file_batch_create_params.ChunkingStrategy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFileBatches:
        """
        Create a vector store file batch.

        Generate an OpenAI-compatible vector store file batch for the given vector
        store.

        Args:
          chunking_strategy: Automatic chunking strategy for vector store files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._post(
            f"/v1/vector_stores/{vector_store_id}/file_batches",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "attributes": attributes,
                    "chunking_strategy": chunking_strategy,
                },
                file_batch_create_params.FileBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatches,
        )

    def retrieve(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFileBatches:
        """
        Retrieve a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            f"/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatches,
        )

    def cancel(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFileBatches:
        """
        Cancels a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._post(
            f"/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatches,
        )

    def list_files(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOpenAICursorPage[VectorStoreFile]:
        """
        Returns a list of vector store files in a batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get_api_list(
            f"/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/files",
            page=SyncOpenAICursorPage[VectorStoreFile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter": filter,
                        "limit": limit,
                        "order": order,
                    },
                    file_batch_list_files_params.FileBatchListFilesParams,
                ),
            ),
            model=VectorStoreFile,
        )


class AsyncFileBatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncFileBatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        vector_store_id: str,
        *,
        file_ids: SequenceNotStr[str],
        attributes: Optional[Dict[str, object]] | Omit = omit,
        chunking_strategy: Optional[file_batch_create_params.ChunkingStrategy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFileBatches:
        """
        Create a vector store file batch.

        Generate an OpenAI-compatible vector store file batch for the given vector
        store.

        Args:
          chunking_strategy: Automatic chunking strategy for vector store files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._post(
            f"/v1/vector_stores/{vector_store_id}/file_batches",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "attributes": attributes,
                    "chunking_strategy": chunking_strategy,
                },
                file_batch_create_params.FileBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatches,
        )

    async def retrieve(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFileBatches:
        """
        Retrieve a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            f"/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatches,
        )

    async def cancel(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFileBatches:
        """
        Cancels a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._post(
            f"/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatches,
        )

    def list_files(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VectorStoreFile, AsyncOpenAICursorPage[VectorStoreFile]]:
        """
        Returns a list of vector store files in a batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get_api_list(
            f"/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/files",
            page=AsyncOpenAICursorPage[VectorStoreFile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter": filter,
                        "limit": limit,
                        "order": order,
                    },
                    file_batch_list_files_params.FileBatchListFilesParams,
                ),
            ),
            model=VectorStoreFile,
        )


class FileBatchesResourceWithRawResponse:
    def __init__(self, file_batches: FileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = to_raw_response_wrapper(
            file_batches.create,
        )
        self.retrieve = to_raw_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = to_raw_response_wrapper(
            file_batches.list_files,
        )


class AsyncFileBatchesResourceWithRawResponse:
    def __init__(self, file_batches: AsyncFileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = async_to_raw_response_wrapper(
            file_batches.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = async_to_raw_response_wrapper(
            file_batches.list_files,
        )


class FileBatchesResourceWithStreamingResponse:
    def __init__(self, file_batches: FileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = to_streamed_response_wrapper(
            file_batches.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = to_streamed_response_wrapper(
            file_batches.list_files,
        )


class AsyncFileBatchesResourceWithStreamingResponse:
    def __init__(self, file_batches: AsyncFileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = async_to_streamed_response_wrapper(
            file_batches.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = async_to_streamed_response_wrapper(
            file_batches.list_files,
        )
