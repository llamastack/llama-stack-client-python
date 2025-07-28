# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...types import (
    vector_store_list_params,
    vector_store_create_params,
    vector_store_search_params,
    vector_store_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.vector_store import VectorStore
from ...types.list_vector_stores_response import ListVectorStoresResponse
from ...types.vector_store_delete_response import VectorStoreDeleteResponse
from ...types.vector_store_search_response import VectorStoreSearchResponse

__all__ = ["VectorStoresResource", "AsyncVectorStoresResource"]


class VectorStoresResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return VectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return VectorStoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        chunking_strategy: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        embedding_dimension: int | NotGiven = NOT_GIVEN,
        embedding_model: str | NotGiven = NOT_GIVEN,
        expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        file_ids: List[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Creates a vector store.

        Args:
          name: A name for the vector store.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy.

          embedding_dimension: The dimension of the embedding vectors (default: 384).

          embedding_model: The embedding model to use for this vector store.

          expires_after: The expiration policy for a vector store.

          file_ids: A list of File IDs that the vector store should use. Useful for tools like
              `file_search` that can access files.

          metadata: Set of 16 key-value pairs that can be attached to an object.

          provider_id: The ID of the provider to use for this vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/openai/v1/vector_stores",
            body=maybe_transform(
                {
                    "name": name,
                    "chunking_strategy": chunking_strategy,
                    "embedding_dimension": embedding_dimension,
                    "embedding_model": embedding_model,
                    "expires_after": expires_after,
                    "file_ids": file_ids,
                    "metadata": metadata,
                    "provider_id": provider_id,
                },
                vector_store_create_params.VectorStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def retrieve(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Retrieves a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._get(
            f"/v1/openai/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def update(
        self,
        vector_store_id: str,
        *,
        expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Updates a vector store.

        Args:
          expires_after: The expiration policy for a vector store.

          metadata: Set of 16 key-value pairs that can be attached to an object.

          name: The name of the vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._post(
            f"/v1/openai/v1/vector_stores/{vector_store_id}",
            body=maybe_transform(
                {
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "name": name,
                },
                vector_store_update_params.VectorStoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListVectorStoresResponse:
        """Returns a list of vector stores.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/openai/v1/vector_stores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=ListVectorStoresResponse,
        )

    def delete(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreDeleteResponse:
        """
        Delete a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._delete(
            f"/v1/openai/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    def search(
        self,
        vector_store_id: str,
        *,
        query: Union[str, List[str]],
        filters: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        max_num_results: int | NotGiven = NOT_GIVEN,
        ranking_options: vector_store_search_params.RankingOptions | NotGiven = NOT_GIVEN,
        rewrite_query: bool | NotGiven = NOT_GIVEN,
        search_mode: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreSearchResponse:
        """Search for chunks in a vector store.

        Searches a vector store for relevant chunks
        based on a query and optional file attribute filters.

        Args:
          query: The query string or array for performing the search.

          filters: Filters based on file attributes to narrow the search results.

          max_num_results: Maximum number of results to return (1 to 50 inclusive, default 10).

          ranking_options: Ranking options for fine-tuning the search results.

          rewrite_query: Whether to rewrite the natural language query for vector search (default false)

          search_mode: The search mode to use - "keyword", "vector", or "hybrid" (default "vector")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._post(
            f"/v1/openai/v1/vector_stores/{vector_store_id}/search",
            body=maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "max_num_results": max_num_results,
                    "ranking_options": ranking_options,
                    "rewrite_query": rewrite_query,
                    "search_mode": search_mode,
                },
                vector_store_search_params.VectorStoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreSearchResponse,
        )


class AsyncVectorStoresResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncVectorStoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        chunking_strategy: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        embedding_dimension: int | NotGiven = NOT_GIVEN,
        embedding_model: str | NotGiven = NOT_GIVEN,
        expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        file_ids: List[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Creates a vector store.

        Args:
          name: A name for the vector store.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy.

          embedding_dimension: The dimension of the embedding vectors (default: 384).

          embedding_model: The embedding model to use for this vector store.

          expires_after: The expiration policy for a vector store.

          file_ids: A list of File IDs that the vector store should use. Useful for tools like
              `file_search` that can access files.

          metadata: Set of 16 key-value pairs that can be attached to an object.

          provider_id: The ID of the provider to use for this vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/openai/v1/vector_stores",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "chunking_strategy": chunking_strategy,
                    "embedding_dimension": embedding_dimension,
                    "embedding_model": embedding_model,
                    "expires_after": expires_after,
                    "file_ids": file_ids,
                    "metadata": metadata,
                    "provider_id": provider_id,
                },
                vector_store_create_params.VectorStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def retrieve(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Retrieves a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._get(
            f"/v1/openai/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def update(
        self,
        vector_store_id: str,
        *,
        expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Updates a vector store.

        Args:
          expires_after: The expiration policy for a vector store.

          metadata: Set of 16 key-value pairs that can be attached to an object.

          name: The name of the vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._post(
            f"/v1/openai/v1/vector_stores/{vector_store_id}",
            body=await async_maybe_transform(
                {
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "name": name,
                },
                vector_store_update_params.VectorStoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListVectorStoresResponse:
        """Returns a list of vector stores.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/openai/v1/vector_stores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=ListVectorStoresResponse,
        )

    async def delete(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreDeleteResponse:
        """
        Delete a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._delete(
            f"/v1/openai/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    async def search(
        self,
        vector_store_id: str,
        *,
        query: Union[str, List[str]],
        filters: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        max_num_results: int | NotGiven = NOT_GIVEN,
        ranking_options: vector_store_search_params.RankingOptions | NotGiven = NOT_GIVEN,
        rewrite_query: bool | NotGiven = NOT_GIVEN,
        search_mode: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreSearchResponse:
        """Search for chunks in a vector store.

        Searches a vector store for relevant chunks
        based on a query and optional file attribute filters.

        Args:
          query: The query string or array for performing the search.

          filters: Filters based on file attributes to narrow the search results.

          max_num_results: Maximum number of results to return (1 to 50 inclusive, default 10).

          ranking_options: Ranking options for fine-tuning the search results.

          rewrite_query: Whether to rewrite the natural language query for vector search (default false)

          search_mode: The search mode to use - "keyword", "vector", or "hybrid" (default "vector")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._post(
            f"/v1/openai/v1/vector_stores/{vector_store_id}/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "max_num_results": max_num_results,
                    "ranking_options": ranking_options,
                    "rewrite_query": rewrite_query,
                    "search_mode": search_mode,
                },
                vector_store_search_params.VectorStoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreSearchResponse,
        )


class VectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vector_stores.update,
        )
        self.list = to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_raw_response_wrapper(
            vector_stores.delete,
        )
        self.search = to_raw_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vector_stores.update,
        )
        self.list = async_to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vector_stores.delete,
        )
        self.search = async_to_raw_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._vector_stores.files)


class VectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vector_stores.update,
        )
        self.list = to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_streamed_response_wrapper(
            vector_stores.delete,
        )
        self.search = to_streamed_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vector_stores.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vector_stores.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._vector_stores.files)
