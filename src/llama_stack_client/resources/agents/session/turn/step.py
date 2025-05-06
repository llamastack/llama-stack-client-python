# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.agents.session.turn.step_retrieve_response import StepRetrieveResponse

__all__ = ["StepResource", "AsyncStepResource"]


class StepResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StepResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return StepResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StepResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return StepResourceWithStreamingResponse(self)

    def retrieve(
        self,
        step_id: str,
        *,
        agent_id: str,
        session_id: str,
        turn_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepRetrieveResponse:
        """
        Retrieve an agent step by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/step/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StepRetrieveResponse,
        )


class AsyncStepResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStepResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStepResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStepResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncStepResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        step_id: str,
        *,
        agent_id: str,
        session_id: str,
        turn_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepRetrieveResponse:
        """
        Retrieve an agent step by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/step/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StepRetrieveResponse,
        )


class StepResourceWithRawResponse:
    def __init__(self, step: StepResource) -> None:
        self._step = step

        self.retrieve = to_raw_response_wrapper(
            step.retrieve,
        )


class AsyncStepResourceWithRawResponse:
    def __init__(self, step: AsyncStepResource) -> None:
        self._step = step

        self.retrieve = async_to_raw_response_wrapper(
            step.retrieve,
        )


class StepResourceWithStreamingResponse:
    def __init__(self, step: StepResource) -> None:
        self._step = step

        self.retrieve = to_streamed_response_wrapper(
            step.retrieve,
        )


class AsyncStepResourceWithStreamingResponse:
    def __init__(self, step: AsyncStepResource) -> None:
        self._step = step

        self.retrieve = async_to_streamed_response_wrapper(
            step.retrieve,
        )
