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
from ...types.telemetry import span_create_params, span_export_params, span_build_tree_params
from ...types.telemetry.span_create_response import SpanCreateResponse
from ...types.telemetry.query_condition_param import QueryConditionParam
from ...types.telemetry.span_build_tree_response import SpanBuildTreeResponse

__all__ = ["SpansResource", "AsyncSpansResource"]


class SpansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return SpansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return SpansResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_return: List[str],
        max_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/telemetry/spans",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                span_create_params.SpanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanCreateResponse,
        )

    def build_tree(
        self,
        span_id: str,
        *,
        attributes_to_return: List[str] | NotGiven = NOT_GIVEN,
        max_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanBuildTreeResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return self._post(
            f"/v1/telemetry/spans/{span_id}/tree",
            body=maybe_transform(
                {
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                span_build_tree_params.SpanBuildTreeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanBuildTreeResponse,
        )

    def export(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_save: List[str],
        dataset_id: str,
        max_depth: int | NotGiven = NOT_GIVEN,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/telemetry/spans/export",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_save": attributes_to_save,
                    "dataset_id": dataset_id,
                    "max_depth": max_depth,
                },
                span_export_params.SpanExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSpansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncSpansResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_return: List[str],
        max_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/telemetry/spans",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                span_create_params.SpanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanCreateResponse,
        )

    async def build_tree(
        self,
        span_id: str,
        *,
        attributes_to_return: List[str] | NotGiven = NOT_GIVEN,
        max_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanBuildTreeResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return await self._post(
            f"/v1/telemetry/spans/{span_id}/tree",
            body=await async_maybe_transform(
                {
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                span_build_tree_params.SpanBuildTreeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanBuildTreeResponse,
        )

    async def export(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_save: List[str],
        dataset_id: str,
        max_depth: int | NotGiven = NOT_GIVEN,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/telemetry/spans/export",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_save": attributes_to_save,
                    "dataset_id": dataset_id,
                    "max_depth": max_depth,
                },
                span_export_params.SpanExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SpansResourceWithRawResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.create = to_raw_response_wrapper(
            spans.create,
        )
        self.build_tree = to_raw_response_wrapper(
            spans.build_tree,
        )
        self.export = to_raw_response_wrapper(
            spans.export,
        )


class AsyncSpansResourceWithRawResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.create = async_to_raw_response_wrapper(
            spans.create,
        )
        self.build_tree = async_to_raw_response_wrapper(
            spans.build_tree,
        )
        self.export = async_to_raw_response_wrapper(
            spans.export,
        )


class SpansResourceWithStreamingResponse:
    def __init__(self, spans: SpansResource) -> None:
        self._spans = spans

        self.create = to_streamed_response_wrapper(
            spans.create,
        )
        self.build_tree = to_streamed_response_wrapper(
            spans.build_tree,
        )
        self.export = to_streamed_response_wrapper(
            spans.export,
        )


class AsyncSpansResourceWithStreamingResponse:
    def __init__(self, spans: AsyncSpansResource) -> None:
        self._spans = spans

        self.create = async_to_streamed_response_wrapper(
            spans.create,
        )
        self.build_tree = async_to_streamed_response_wrapper(
            spans.build_tree,
        )
        self.export = async_to_streamed_response_wrapper(
            spans.export,
        )
