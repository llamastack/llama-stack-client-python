# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import datasetio_append_rows_params, datasetio_iterate_rows_params
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
from .._base_client import make_request_options
from ..types.datasetio_iterate_rows_response import DatasetioIterateRowsResponse

__all__ = ["DatasetioResource", "AsyncDatasetioResource"]


class DatasetioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return DatasetioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return DatasetioResourceWithStreamingResponse(self)

    def append_rows(
        self,
        dataset_id: str,
        *,
        rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
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
            f"/v1/datasetio/append-rows/{dataset_id}",
            body=maybe_transform({"rows": rows}, datasetio_append_rows_params.DatasetioAppendRowsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def iterate_rows(
        self,
        dataset_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        start_index: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetioIterateRowsResponse:
        """Get a paginated list of rows from a dataset.

        Uses offset-based pagination where:

        - start_index: The starting index (0-based). If None, starts from beginning.
        - limit: Number of items to return. If None or -1, returns all items.

        The response includes:

        - data: List of items for the current page
        - has_more: Whether there are more items available after this set

        Args:
          limit: The number of rows to get.

          start_index: Index into dataset for the first row to get. Get all rows if None.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v1/datasetio/iterrows/{dataset_id}",
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
                    datasetio_iterate_rows_params.DatasetioIterateRowsParams,
                ),
            ),
            cast_to=DatasetioIterateRowsResponse,
        )


class AsyncDatasetioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncDatasetioResourceWithStreamingResponse(self)

    async def append_rows(
        self,
        dataset_id: str,
        *,
        rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
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
            f"/v1/datasetio/append-rows/{dataset_id}",
            body=await async_maybe_transform({"rows": rows}, datasetio_append_rows_params.DatasetioAppendRowsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def iterate_rows(
        self,
        dataset_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        start_index: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetioIterateRowsResponse:
        """Get a paginated list of rows from a dataset.

        Uses offset-based pagination where:

        - start_index: The starting index (0-based). If None, starts from beginning.
        - limit: Number of items to return. If None or -1, returns all items.

        The response includes:

        - data: List of items for the current page
        - has_more: Whether there are more items available after this set

        Args:
          limit: The number of rows to get.

          start_index: Index into dataset for the first row to get. Get all rows if None.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v1/datasetio/iterrows/{dataset_id}",
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
                    datasetio_iterate_rows_params.DatasetioIterateRowsParams,
                ),
            ),
            cast_to=DatasetioIterateRowsResponse,
        )


class DatasetioResourceWithRawResponse:
    def __init__(self, datasetio: DatasetioResource) -> None:
        self._datasetio = datasetio

        self.append_rows = to_raw_response_wrapper(
            datasetio.append_rows,
        )
        self.iterate_rows = to_raw_response_wrapper(
            datasetio.iterate_rows,
        )


class AsyncDatasetioResourceWithRawResponse:
    def __init__(self, datasetio: AsyncDatasetioResource) -> None:
        self._datasetio = datasetio

        self.append_rows = async_to_raw_response_wrapper(
            datasetio.append_rows,
        )
        self.iterate_rows = async_to_raw_response_wrapper(
            datasetio.iterate_rows,
        )


class DatasetioResourceWithStreamingResponse:
    def __init__(self, datasetio: DatasetioResource) -> None:
        self._datasetio = datasetio

        self.append_rows = to_streamed_response_wrapper(
            datasetio.append_rows,
        )
        self.iterate_rows = to_streamed_response_wrapper(
            datasetio.iterate_rows,
        )


class AsyncDatasetioResourceWithStreamingResponse:
    def __init__(self, datasetio: AsyncDatasetioResource) -> None:
        self._datasetio = datasetio

        self.append_rows = async_to_streamed_response_wrapper(
            datasetio.append_rows,
        )
        self.iterate_rows = async_to_streamed_response_wrapper(
            datasetio.iterate_rows,
        )
