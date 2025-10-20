# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import (
    telemetry_query_spans_params,
    telemetry_query_traces_params,
    telemetry_get_span_tree_params,
    telemetry_query_metrics_params,
    telemetry_save_spans_to_dataset_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.trace import Trace
from .._base_client import make_request_options
from ..types.query_condition_param import QueryConditionParam
from ..types.telemetry_get_span_response import TelemetryGetSpanResponse
from ..types.telemetry_query_spans_response import TelemetryQuerySpansResponse
from ..types.telemetry_query_traces_response import TelemetryQueryTracesResponse
from ..types.telemetry_get_span_tree_response import TelemetryGetSpanTreeResponse
from ..types.telemetry_query_metrics_response import TelemetryQueryMetricsResponse

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return TelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return TelemetryResourceWithStreamingResponse(self)

    def get_span(
        self,
        span_id: str,
        *,
        trace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryGetSpanResponse:
        """
        Get a span by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trace_id:
            raise ValueError(f"Expected a non-empty value for `trace_id` but received {trace_id!r}")
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return self._get(
            f"/v1alpha/telemetry/traces/{trace_id}/spans/{span_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryGetSpanResponse,
        )

    def get_span_tree(
        self,
        span_id: str,
        *,
        attributes_to_return: SequenceNotStr[str] | Omit = omit,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryGetSpanTreeResponse:
        """
        Get a span tree by its ID.

        Args:
          attributes_to_return: The attributes to return in the tree.

          max_depth: The maximum depth of the tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return self._post(
            f"/v1alpha/telemetry/spans/{span_id}/tree",
            body=maybe_transform(
                {
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                telemetry_get_span_tree_params.TelemetryGetSpanTreeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryGetSpanTreeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryGetSpanTreeResponse], DataWrapper[TelemetryGetSpanTreeResponse]),
        )

    def get_trace(
        self,
        trace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Trace:
        """
        Get a trace by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trace_id:
            raise ValueError(f"Expected a non-empty value for `trace_id` but received {trace_id!r}")
        return self._get(
            f"/v1alpha/telemetry/traces/{trace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trace,
        )

    def query_metrics(
        self,
        metric_name: str,
        *,
        query_type: Literal["range", "instant"],
        start_time: int,
        end_time: int | Omit = omit,
        granularity: str | Omit = omit,
        label_matchers: Iterable[telemetry_query_metrics_params.LabelMatcher] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryMetricsResponse:
        """
        Query metrics.

        Args:
          query_type: The type of query to perform.

          start_time: The start time of the metric to query.

          end_time: The end time of the metric to query.

          granularity: The granularity of the metric to query.

          label_matchers: The label matchers to apply to the metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_name:
            raise ValueError(f"Expected a non-empty value for `metric_name` but received {metric_name!r}")
        return self._post(
            f"/v1alpha/telemetry/metrics/{metric_name}",
            body=maybe_transform(
                {
                    "query_type": query_type,
                    "start_time": start_time,
                    "end_time": end_time,
                    "granularity": granularity,
                    "label_matchers": label_matchers,
                },
                telemetry_query_metrics_params.TelemetryQueryMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryQueryMetricsResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQueryMetricsResponse], DataWrapper[TelemetryQueryMetricsResponse]),
        )

    def query_spans(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_return: SequenceNotStr[str],
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQuerySpansResponse:
        """
        Query spans.

        Args:
          attribute_filters: The attribute filters to apply to the spans.

          attributes_to_return: The attributes to return in the spans.

          max_depth: The maximum depth of the tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1alpha/telemetry/spans",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                telemetry_query_spans_params.TelemetryQuerySpansParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryQuerySpansResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQuerySpansResponse], DataWrapper[TelemetryQuerySpansResponse]),
        )

    def query_traces(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryTracesResponse:
        """
        Query traces.

        Args:
          attribute_filters: The attribute filters to apply to the traces.

          limit: The limit of traces to return.

          offset: The offset of the traces to return.

          order_by: The order by of the traces to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1alpha/telemetry/traces",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "limit": limit,
                    "offset": offset,
                    "order_by": order_by,
                },
                telemetry_query_traces_params.TelemetryQueryTracesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryQueryTracesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQueryTracesResponse], DataWrapper[TelemetryQueryTracesResponse]),
        )

    def save_spans_to_dataset(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_save: SequenceNotStr[str],
        dataset_id: str,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Save spans to a dataset.

        Args:
          attribute_filters: The attribute filters to apply to the spans.

          attributes_to_save: The attributes to save to the dataset.

          dataset_id: The ID of the dataset to save the spans to.

          max_depth: The maximum depth of the tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1alpha/telemetry/spans/export",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_save": attributes_to_save,
                    "dataset_id": dataset_id,
                    "max_depth": max_depth,
                },
                telemetry_save_spans_to_dataset_params.TelemetrySaveSpansToDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTelemetryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncTelemetryResourceWithStreamingResponse(self)

    async def get_span(
        self,
        span_id: str,
        *,
        trace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryGetSpanResponse:
        """
        Get a span by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trace_id:
            raise ValueError(f"Expected a non-empty value for `trace_id` but received {trace_id!r}")
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return await self._get(
            f"/v1alpha/telemetry/traces/{trace_id}/spans/{span_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryGetSpanResponse,
        )

    async def get_span_tree(
        self,
        span_id: str,
        *,
        attributes_to_return: SequenceNotStr[str] | Omit = omit,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryGetSpanTreeResponse:
        """
        Get a span tree by its ID.

        Args:
          attributes_to_return: The attributes to return in the tree.

          max_depth: The maximum depth of the tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_id:
            raise ValueError(f"Expected a non-empty value for `span_id` but received {span_id!r}")
        return await self._post(
            f"/v1alpha/telemetry/spans/{span_id}/tree",
            body=await async_maybe_transform(
                {
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                telemetry_get_span_tree_params.TelemetryGetSpanTreeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryGetSpanTreeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryGetSpanTreeResponse], DataWrapper[TelemetryGetSpanTreeResponse]),
        )

    async def get_trace(
        self,
        trace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Trace:
        """
        Get a trace by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trace_id:
            raise ValueError(f"Expected a non-empty value for `trace_id` but received {trace_id!r}")
        return await self._get(
            f"/v1alpha/telemetry/traces/{trace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trace,
        )

    async def query_metrics(
        self,
        metric_name: str,
        *,
        query_type: Literal["range", "instant"],
        start_time: int,
        end_time: int | Omit = omit,
        granularity: str | Omit = omit,
        label_matchers: Iterable[telemetry_query_metrics_params.LabelMatcher] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryMetricsResponse:
        """
        Query metrics.

        Args:
          query_type: The type of query to perform.

          start_time: The start time of the metric to query.

          end_time: The end time of the metric to query.

          granularity: The granularity of the metric to query.

          label_matchers: The label matchers to apply to the metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_name:
            raise ValueError(f"Expected a non-empty value for `metric_name` but received {metric_name!r}")
        return await self._post(
            f"/v1alpha/telemetry/metrics/{metric_name}",
            body=await async_maybe_transform(
                {
                    "query_type": query_type,
                    "start_time": start_time,
                    "end_time": end_time,
                    "granularity": granularity,
                    "label_matchers": label_matchers,
                },
                telemetry_query_metrics_params.TelemetryQueryMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryQueryMetricsResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQueryMetricsResponse], DataWrapper[TelemetryQueryMetricsResponse]),
        )

    async def query_spans(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_return: SequenceNotStr[str],
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQuerySpansResponse:
        """
        Query spans.

        Args:
          attribute_filters: The attribute filters to apply to the spans.

          attributes_to_return: The attributes to return in the spans.

          max_depth: The maximum depth of the tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1alpha/telemetry/spans",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                telemetry_query_spans_params.TelemetryQuerySpansParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryQuerySpansResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQuerySpansResponse], DataWrapper[TelemetryQuerySpansResponse]),
        )

    async def query_traces(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryTracesResponse:
        """
        Query traces.

        Args:
          attribute_filters: The attribute filters to apply to the traces.

          limit: The limit of traces to return.

          offset: The offset of the traces to return.

          order_by: The order by of the traces to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1alpha/telemetry/traces",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "limit": limit,
                    "offset": offset,
                    "order_by": order_by,
                },
                telemetry_query_traces_params.TelemetryQueryTracesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[TelemetryQueryTracesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQueryTracesResponse], DataWrapper[TelemetryQueryTracesResponse]),
        )

    async def save_spans_to_dataset(
        self,
        *,
        attribute_filters: Iterable[QueryConditionParam],
        attributes_to_save: SequenceNotStr[str],
        dataset_id: str,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Save spans to a dataset.

        Args:
          attribute_filters: The attribute filters to apply to the spans.

          attributes_to_save: The attributes to save to the dataset.

          dataset_id: The ID of the dataset to save the spans to.

          max_depth: The maximum depth of the tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1alpha/telemetry/spans/export",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_save": attributes_to_save,
                    "dataset_id": dataset_id,
                    "max_depth": max_depth,
                },
                telemetry_save_spans_to_dataset_params.TelemetrySaveSpansToDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span = to_raw_response_wrapper(
            telemetry.get_span,
        )
        self.get_span_tree = to_raw_response_wrapper(
            telemetry.get_span_tree,
        )
        self.get_trace = to_raw_response_wrapper(
            telemetry.get_trace,
        )
        self.query_metrics = to_raw_response_wrapper(
            telemetry.query_metrics,
        )
        self.query_spans = to_raw_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = to_raw_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = to_raw_response_wrapper(
            telemetry.save_spans_to_dataset,
        )


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span = async_to_raw_response_wrapper(
            telemetry.get_span,
        )
        self.get_span_tree = async_to_raw_response_wrapper(
            telemetry.get_span_tree,
        )
        self.get_trace = async_to_raw_response_wrapper(
            telemetry.get_trace,
        )
        self.query_metrics = async_to_raw_response_wrapper(
            telemetry.query_metrics,
        )
        self.query_spans = async_to_raw_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = async_to_raw_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = async_to_raw_response_wrapper(
            telemetry.save_spans_to_dataset,
        )


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span = to_streamed_response_wrapper(
            telemetry.get_span,
        )
        self.get_span_tree = to_streamed_response_wrapper(
            telemetry.get_span_tree,
        )
        self.get_trace = to_streamed_response_wrapper(
            telemetry.get_trace,
        )
        self.query_metrics = to_streamed_response_wrapper(
            telemetry.query_metrics,
        )
        self.query_spans = to_streamed_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = to_streamed_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = to_streamed_response_wrapper(
            telemetry.save_spans_to_dataset,
        )


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span = async_to_streamed_response_wrapper(
            telemetry.get_span,
        )
        self.get_span_tree = async_to_streamed_response_wrapper(
            telemetry.get_span_tree,
        )
        self.get_trace = async_to_streamed_response_wrapper(
            telemetry.get_trace,
        )
        self.query_metrics = async_to_streamed_response_wrapper(
            telemetry.query_metrics,
        )
        self.query_spans = async_to_streamed_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = async_to_streamed_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = async_to_streamed_response_wrapper(
            telemetry.save_spans_to_dataset,
        )
