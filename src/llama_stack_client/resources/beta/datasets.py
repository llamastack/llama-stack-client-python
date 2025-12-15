# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ...types.beta import dataset_iterrows_params, dataset_register_params, dataset_appendrows_params
from ..._base_client import make_request_options
from ...types.beta.dataset_list_response import DatasetListResponse
from ...types.beta.dataset_iterrows_response import DatasetIterrowsResponse
from ...types.beta.dataset_register_response import DatasetRegisterResponse
from ...types.beta.dataset_retrieve_response import DatasetRetrieveResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetRetrieveResponse:
        """
        Get a dataset by its ID.

        Args:
          dataset_id: The ID of the dataset to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v1beta/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetListResponse:
        """List all datasets."""
        return self._get(
            "/v1beta/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[DatasetListResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatasetListResponse], DataWrapper[DatasetListResponse]),
        )

    def appendrows(
        self,
        dataset_id: str,
        *,
        rows: Iterable[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Append rows to a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1beta/datasetio/append-rows/{dataset_id}",
            body=maybe_transform({"rows": rows}, dataset_appendrows_params.DatasetAppendrowsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def iterrows(
        self,
        dataset_id: str,
        *,
        limit: Optional[int] | Omit = omit,
        start_index: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetIterrowsResponse:
        """
        Get a paginated list of rows from a dataset.

        Uses offset-based pagination where:

        - start_index: The starting index (0-based). If None, starts from beginning.
        - limit: Number of items to return. If None or -1, returns all items.

        The response includes:

        - data: List of items for the current page.
        - has_more: Whether there are more items available after this set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v1beta/datasetio/iterrows/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "start_index": start_index,
                    },
                    dataset_iterrows_params.DatasetIterrowsParams,
                ),
            ),
            cast_to=DatasetIterrowsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def register(
        self,
        *,
        purpose: Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"],
        source: dataset_register_params.Source,
        dataset_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetRegisterResponse:
        """
        Register a new dataset.

        Args:
          purpose: The purpose of the dataset.

          source: The data source of the dataset.

          dataset_id: The ID of the dataset. If not provided, an ID will be generated.

          metadata: The metadata for the dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1beta/datasets",
            body=maybe_transform(
                {
                    "purpose": purpose,
                    "source": source,
                    "dataset_id": dataset_id,
                    "metadata": metadata,
                },
                dataset_register_params.DatasetRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRegisterResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def unregister(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a dataset by its ID.

        Args:
          dataset_id: The ID of the dataset to unregister.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1beta/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetRetrieveResponse:
        """
        Get a dataset by its ID.

        Args:
          dataset_id: The ID of the dataset to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v1beta/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetListResponse:
        """List all datasets."""
        return await self._get(
            "/v1beta/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[DatasetListResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatasetListResponse], DataWrapper[DatasetListResponse]),
        )

    async def appendrows(
        self,
        dataset_id: str,
        *,
        rows: Iterable[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Append rows to a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1beta/datasetio/append-rows/{dataset_id}",
            body=await async_maybe_transform({"rows": rows}, dataset_appendrows_params.DatasetAppendrowsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def iterrows(
        self,
        dataset_id: str,
        *,
        limit: Optional[int] | Omit = omit,
        start_index: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetIterrowsResponse:
        """
        Get a paginated list of rows from a dataset.

        Uses offset-based pagination where:

        - start_index: The starting index (0-based). If None, starts from beginning.
        - limit: Number of items to return. If None or -1, returns all items.

        The response includes:

        - data: List of items for the current page.
        - has_more: Whether there are more items available after this set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v1beta/datasetio/iterrows/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "start_index": start_index,
                    },
                    dataset_iterrows_params.DatasetIterrowsParams,
                ),
            ),
            cast_to=DatasetIterrowsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def register(
        self,
        *,
        purpose: Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"],
        source: dataset_register_params.Source,
        dataset_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetRegisterResponse:
        """
        Register a new dataset.

        Args:
          purpose: The purpose of the dataset.

          source: The data source of the dataset.

          dataset_id: The ID of the dataset. If not provided, an ID will be generated.

          metadata: The metadata for the dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1beta/datasets",
            body=await async_maybe_transform(
                {
                    "purpose": purpose,
                    "source": source,
                    "dataset_id": dataset_id,
                    "metadata": metadata,
                },
                dataset_register_params.DatasetRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRegisterResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def unregister(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unregister a dataset by its ID.

        Args:
          dataset_id: The ID of the dataset to unregister.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1beta/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.retrieve = to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.appendrows = to_raw_response_wrapper(
            datasets.appendrows,
        )
        self.iterrows = to_raw_response_wrapper(
            datasets.iterrows,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                datasets.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                datasets.unregister,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.retrieve = async_to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.appendrows = async_to_raw_response_wrapper(
            datasets.appendrows,
        )
        self.iterrows = async_to_raw_response_wrapper(
            datasets.iterrows,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                datasets.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                datasets.unregister,  # pyright: ignore[reportDeprecated],
            )
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.retrieve = to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.appendrows = to_streamed_response_wrapper(
            datasets.appendrows,
        )
        self.iterrows = to_streamed_response_wrapper(
            datasets.iterrows,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                datasets.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                datasets.unregister,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.retrieve = async_to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.appendrows = async_to_streamed_response_wrapper(
            datasets.appendrows,
        )
        self.iterrows = async_to_streamed_response_wrapper(
            datasets.iterrows,
        )
        self.register = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                datasets.register,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unregister = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                datasets.unregister,  # pyright: ignore[reportDeprecated],
            )
        )
