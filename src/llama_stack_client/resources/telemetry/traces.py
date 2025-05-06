# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

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
from ...types.telemetry import trace_create_params
from ...types.telemetry.span import Span
from ...types.telemetry.trace import Trace
from ...types.telemetry.query_condition_param import QueryConditionParam
from ...types.telemetry.trace_create_response import TraceCreateResponse

__all__ = ["TracesResource", "AsyncTracesResource"]


class TracesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TracesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return TracesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return TracesResourceWithStreamingResponse(self)

    def create(
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
    ) -> TraceCreateResponse:
        """
        Args:
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
                trace_create_params.TraceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TraceCreateResponse,
        )

    def retrieve_span(
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
    ) -> Span:
        """
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
            cast_to=Span,
        )

    def retrieve_trace(
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


class AsyncTracesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTracesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTracesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncTracesResourceWithStreamingResponse(self)

    async def create(
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
    ) -> TraceCreateResponse:
        """
        Args:
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
                trace_create_params.TraceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TraceCreateResponse,
        )

    async def retrieve_span(
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
    ) -> Span:
        """
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
            cast_to=Span,
        )

    async def retrieve_trace(
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


class TracesResourceWithRawResponse:
    def __init__(self, traces: TracesResource) -> None:
        self._traces = traces

        self.create = to_raw_response_wrapper(
            traces.create,
        )
        self.retrieve_span = to_raw_response_wrapper(
            traces.retrieve_span,
        )
        self.retrieve_trace = to_raw_response_wrapper(
            traces.retrieve_trace,
        )


class AsyncTracesResourceWithRawResponse:
    def __init__(self, traces: AsyncTracesResource) -> None:
        self._traces = traces

        self.create = async_to_raw_response_wrapper(
            traces.create,
        )
        self.retrieve_span = async_to_raw_response_wrapper(
            traces.retrieve_span,
        )
        self.retrieve_trace = async_to_raw_response_wrapper(
            traces.retrieve_trace,
        )


class TracesResourceWithStreamingResponse:
    def __init__(self, traces: TracesResource) -> None:
        self._traces = traces

        self.create = to_streamed_response_wrapper(
            traces.create,
        )
        self.retrieve_span = to_streamed_response_wrapper(
            traces.retrieve_span,
        )
        self.retrieve_trace = to_streamed_response_wrapper(
            traces.retrieve_trace,
        )


class AsyncTracesResourceWithStreamingResponse:
    def __init__(self, traces: AsyncTracesResource) -> None:
        self._traces = traces

        self.create = async_to_streamed_response_wrapper(
            traces.create,
        )
        self.retrieve_span = async_to_streamed_response_wrapper(
            traces.retrieve_span,
        )
        self.retrieve_trace = async_to_streamed_response_wrapper(
            traces.retrieve_trace,
        )
