# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import (
    telemetry_log_event_params,
    telemetry_query_spans_params,
    telemetry_query_traces_params,
    telemetry_get_span_tree_params,
    telemetry_query_metrics_params,
    telemetry_save_spans_to_dataset_params,
)
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
from ..types.trace import Trace
from .._base_client import make_request_options
from ..types.event_param import EventParam
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/telemetry/traces/{trace_id}/spans/{span_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryGetSpanResponse,
        )

    def get_span_tree(
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
            f"/v1/telemetry/spans/{span_id}/tree",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/telemetry/traces/{trace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trace,
        )

    def log_event(
        self,
        *,
        event: EventParam,
        ttl_seconds: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log an event.

        Args:
          event: The event to log.

          ttl_seconds: The time to live of the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/telemetry/events",
            body=maybe_transform(
                {
                    "event": event,
                    "ttl_seconds": ttl_seconds,
                },
                telemetry_log_event_params.TelemetryLogEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query_metrics(
        self,
        metric_name: str,
        *,
        query_type: Literal["range", "instant"],
        start_time: int,
        end_time: int | NotGiven = NOT_GIVEN,
        granularity: str | NotGiven = NOT_GIVEN,
        label_matchers: Iterable[telemetry_query_metrics_params.LabelMatcher] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/telemetry/metrics/{metric_name}",
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
        attributes_to_return: List[str],
        max_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            "/v1/telemetry/spans",
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
        attribute_filters: Iterable[QueryConditionParam] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            "/v1/telemetry/traces",
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
            "/v1/telemetry/spans/export",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/telemetry/traces/{trace_id}/spans/{span_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryGetSpanResponse,
        )

    async def get_span_tree(
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
            f"/v1/telemetry/spans/{span_id}/tree",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/telemetry/traces/{trace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trace,
        )

    async def log_event(
        self,
        *,
        event: EventParam,
        ttl_seconds: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log an event.

        Args:
          event: The event to log.

          ttl_seconds: The time to live of the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/telemetry/events",
            body=await async_maybe_transform(
                {
                    "event": event,
                    "ttl_seconds": ttl_seconds,
                },
                telemetry_log_event_params.TelemetryLogEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query_metrics(
        self,
        metric_name: str,
        *,
        query_type: Literal["range", "instant"],
        start_time: int,
        end_time: int | NotGiven = NOT_GIVEN,
        granularity: str | NotGiven = NOT_GIVEN,
        label_matchers: Iterable[telemetry_query_metrics_params.LabelMatcher] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/telemetry/metrics/{metric_name}",
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
        attributes_to_return: List[str],
        max_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            "/v1/telemetry/spans",
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
        attribute_filters: Iterable[QueryConditionParam] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            "/v1/telemetry/traces",
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
            "/v1/telemetry/spans/export",
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
        self.log_event = to_raw_response_wrapper(
            telemetry.log_event,
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
        self.log_event = async_to_raw_response_wrapper(
            telemetry.log_event,
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
        self.log_event = to_streamed_response_wrapper(
            telemetry.log_event,
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
        self.log_event = async_to_streamed_response_wrapper(
            telemetry.log_event,
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
