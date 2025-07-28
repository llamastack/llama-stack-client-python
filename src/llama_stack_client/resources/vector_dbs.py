# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import vector_db_register_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.vector_db_list_response import VectorDBListResponse
from ..types.vector_db_register_response import VectorDBRegisterResponse
from ..types.vector_db_retrieve_response import VectorDBRetrieveResponse

__all__ = ["VectorDBsResource", "AsyncVectorDBsResource"]


class VectorDBsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VectorDBsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return VectorDBsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorDBsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return VectorDBsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        vector_db_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBRetrieveResponse:
        """
        Get a vector database by its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_db_id:
            raise ValueError(f"Expected a non-empty value for `vector_db_id` but received {vector_db_id!r}")
        return self._get(
            f"/v1/vector-dbs/{vector_db_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBListResponse:
        """List all vector databases."""
        return self._get(
            "/v1/vector-dbs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[VectorDBListResponse]._unwrapper,
            ),
            cast_to=cast(Type[VectorDBListResponse], DataWrapper[VectorDBListResponse]),
        )

    def register(
        self,
        *,
        embedding_model: str,
        vector_db_id: str,
        embedding_dimension: int | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_vector_db_id: str | NotGiven = NOT_GIVEN,
        vector_db_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBRegisterResponse:
        """
        Register a vector database.

        Args:
          embedding_model: The embedding model to use.

          vector_db_id: The identifier of the vector database to register.

          embedding_dimension: The dimension of the embedding model.

          provider_id: The identifier of the provider.

          provider_vector_db_id: The identifier of the vector database in the provider.

          vector_db_name: The name of the vector database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector-dbs",
            body=maybe_transform(
                {
                    "embedding_model": embedding_model,
                    "vector_db_id": vector_db_id,
                    "embedding_dimension": embedding_dimension,
                    "provider_id": provider_id,
                    "provider_vector_db_id": provider_vector_db_id,
                    "vector_db_name": vector_db_name,
                },
                vector_db_register_params.VectorDBRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBRegisterResponse,
        )

    def unregister(
        self,
        vector_db_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unregister a vector database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_db_id:
            raise ValueError(f"Expected a non-empty value for `vector_db_id` but received {vector_db_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/vector-dbs/{vector_db_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncVectorDBsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVectorDBsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorDBsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorDBsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncVectorDBsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        vector_db_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBRetrieveResponse:
        """
        Get a vector database by its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_db_id:
            raise ValueError(f"Expected a non-empty value for `vector_db_id` but received {vector_db_id!r}")
        return await self._get(
            f"/v1/vector-dbs/{vector_db_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBListResponse:
        """List all vector databases."""
        return await self._get(
            "/v1/vector-dbs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[VectorDBListResponse]._unwrapper,
            ),
            cast_to=cast(Type[VectorDBListResponse], DataWrapper[VectorDBListResponse]),
        )

    async def register(
        self,
        *,
        embedding_model: str,
        vector_db_id: str,
        embedding_dimension: int | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_vector_db_id: str | NotGiven = NOT_GIVEN,
        vector_db_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBRegisterResponse:
        """
        Register a vector database.

        Args:
          embedding_model: The embedding model to use.

          vector_db_id: The identifier of the vector database to register.

          embedding_dimension: The dimension of the embedding model.

          provider_id: The identifier of the provider.

          provider_vector_db_id: The identifier of the vector database in the provider.

          vector_db_name: The name of the vector database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector-dbs",
            body=await async_maybe_transform(
                {
                    "embedding_model": embedding_model,
                    "vector_db_id": vector_db_id,
                    "embedding_dimension": embedding_dimension,
                    "provider_id": provider_id,
                    "provider_vector_db_id": provider_vector_db_id,
                    "vector_db_name": vector_db_name,
                },
                vector_db_register_params.VectorDBRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBRegisterResponse,
        )

    async def unregister(
        self,
        vector_db_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unregister a vector database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_db_id:
            raise ValueError(f"Expected a non-empty value for `vector_db_id` but received {vector_db_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/vector-dbs/{vector_db_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class VectorDBsResourceWithRawResponse:
    def __init__(self, vector_dbs: VectorDBsResource) -> None:
        self._vector_dbs = vector_dbs

        self.retrieve = to_raw_response_wrapper(
            vector_dbs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            vector_dbs.list,
        )
        self.register = to_raw_response_wrapper(
            vector_dbs.register,
        )
        self.unregister = to_raw_response_wrapper(
            vector_dbs.unregister,
        )


class AsyncVectorDBsResourceWithRawResponse:
    def __init__(self, vector_dbs: AsyncVectorDBsResource) -> None:
        self._vector_dbs = vector_dbs

        self.retrieve = async_to_raw_response_wrapper(
            vector_dbs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            vector_dbs.list,
        )
        self.register = async_to_raw_response_wrapper(
            vector_dbs.register,
        )
        self.unregister = async_to_raw_response_wrapper(
            vector_dbs.unregister,
        )


class VectorDBsResourceWithStreamingResponse:
    def __init__(self, vector_dbs: VectorDBsResource) -> None:
        self._vector_dbs = vector_dbs

        self.retrieve = to_streamed_response_wrapper(
            vector_dbs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            vector_dbs.list,
        )
        self.register = to_streamed_response_wrapper(
            vector_dbs.register,
        )
        self.unregister = to_streamed_response_wrapper(
            vector_dbs.unregister,
        )


class AsyncVectorDBsResourceWithStreamingResponse:
    def __init__(self, vector_dbs: AsyncVectorDBsResource) -> None:
        self._vector_dbs = vector_dbs

        self.retrieve = async_to_streamed_response_wrapper(
            vector_dbs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            vector_dbs.list,
        )
        self.register = async_to_streamed_response_wrapper(
            vector_dbs.register,
        )
        self.unregister = async_to_streamed_response_wrapper(
            vector_dbs.unregister,
        )
