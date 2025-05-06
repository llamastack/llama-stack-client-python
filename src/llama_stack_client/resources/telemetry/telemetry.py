# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .spans import (
    SpansResource,
    AsyncSpansResource,
    SpansResourceWithRawResponse,
    AsyncSpansResourceWithRawResponse,
    SpansResourceWithStreamingResponse,
    AsyncSpansResourceWithStreamingResponse,
)
from .traces import (
    TracesResource,
    AsyncTracesResource,
    TracesResourceWithRawResponse,
    AsyncTracesResourceWithRawResponse,
    TracesResourceWithStreamingResponse,
    AsyncTracesResourceWithStreamingResponse,
)
from ...types import telemetry_create_event_params
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

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    @cached_property
    def traces(self) -> TracesResource:
        return TracesResource(self._client)

    @cached_property
    def spans(self) -> SpansResource:
        return SpansResource(self._client)

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

    def create_event(
        self,
        *,
        event: telemetry_create_event_params.Event,
        ttl_seconds: int,
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
            "/v1/telemetry/events",
            body=maybe_transform(
                {
                    "event": event,
                    "ttl_seconds": ttl_seconds,
                },
                telemetry_create_event_params.TelemetryCreateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTelemetryResource(AsyncAPIResource):
    @cached_property
    def traces(self) -> AsyncTracesResource:
        return AsyncTracesResource(self._client)

    @cached_property
    def spans(self) -> AsyncSpansResource:
        return AsyncSpansResource(self._client)

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

    async def create_event(
        self,
        *,
        event: telemetry_create_event_params.Event,
        ttl_seconds: int,
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
            "/v1/telemetry/events",
            body=await async_maybe_transform(
                {
                    "event": event,
                    "ttl_seconds": ttl_seconds,
                },
                telemetry_create_event_params.TelemetryCreateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.create_event = to_raw_response_wrapper(
            telemetry.create_event,
        )

    @cached_property
    def traces(self) -> TracesResourceWithRawResponse:
        return TracesResourceWithRawResponse(self._telemetry.traces)

    @cached_property
    def spans(self) -> SpansResourceWithRawResponse:
        return SpansResourceWithRawResponse(self._telemetry.spans)


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.create_event = async_to_raw_response_wrapper(
            telemetry.create_event,
        )

    @cached_property
    def traces(self) -> AsyncTracesResourceWithRawResponse:
        return AsyncTracesResourceWithRawResponse(self._telemetry.traces)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithRawResponse:
        return AsyncSpansResourceWithRawResponse(self._telemetry.spans)


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.create_event = to_streamed_response_wrapper(
            telemetry.create_event,
        )

    @cached_property
    def traces(self) -> TracesResourceWithStreamingResponse:
        return TracesResourceWithStreamingResponse(self._telemetry.traces)

    @cached_property
    def spans(self) -> SpansResourceWithStreamingResponse:
        return SpansResourceWithStreamingResponse(self._telemetry.spans)


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.create_event = async_to_streamed_response_wrapper(
            telemetry.create_event,
        )

    @cached_property
    def traces(self) -> AsyncTracesResourceWithStreamingResponse:
        return AsyncTracesResourceWithStreamingResponse(self._telemetry.traces)

    @cached_property
    def spans(self) -> AsyncSpansResourceWithStreamingResponse:
        return AsyncSpansResourceWithStreamingResponse(self._telemetry.spans)
