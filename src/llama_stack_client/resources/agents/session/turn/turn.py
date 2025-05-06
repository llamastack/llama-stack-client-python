# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from .step import (
    StepResource,
    AsyncStepResource,
    StepResourceWithRawResponse,
    AsyncStepResourceWithRawResponse,
    StepResourceWithStreamingResponse,
    AsyncStepResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.agents.session import turn_create_params, turn_resume_params
from .....types.tool_config_param import ToolConfigParam
from .....types.agents.session.turn.turn import Turn
from .....types.agents.session.agent_tool_param import AgentToolParam
from .....types.agents.session.tool_response_param import ToolResponseParam

__all__ = ["TurnResource", "AsyncTurnResource"]


class TurnResource(SyncAPIResource):
    @cached_property
    def step(self) -> StepResource:
        return StepResource(self._client)

    @cached_property
    def with_raw_response(self) -> TurnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return TurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TurnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return TurnResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        tool_config: ToolConfigParam | NotGiven = NOT_GIVEN,
        toolgroups: List[AgentToolParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """
        Create a new turn for an agent.

        Args:
          messages: List of messages to start the turn with.

          documents: (Optional) List of documents to create the turn with.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          tool_config: (Optional) The tool configuration to create the turn with, will be used to
              override the agent's tool_config.

          toolgroups: (Optional) List of toolgroups to create the turn with, will be used in addition
              to the agent's config toolgroups for the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/session/{session_id}/turn",
            body=maybe_transform(
                {
                    "messages": messages,
                    "documents": documents,
                    "stream": stream,
                    "tool_config": tool_config,
                    "toolgroups": toolgroups,
                },
                turn_create_params.TurnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    def retrieve(
        self,
        turn_id: str,
        *,
        agent_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """
        Retrieve an agent turn by its ID.

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
        return self._get(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    def resume(
        self,
        turn_id: str,
        *,
        agent_id: str,
        session_id: str,
        tool_responses: Iterable[ToolResponseParam],
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """Resume an agent turn with executed tool call responses.

        When a Turn has the
        status `awaiting_input` due to pending input from client side tool calls, this
        endpoint can be used to submit the outputs from the tool calls once they are
        ready.

        Args:
          tool_responses: The tool call responses to resume the turn with.

          stream: Whether to stream the response.

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
        return self._post(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/resume",
            body=maybe_transform(
                {
                    "tool_responses": tool_responses,
                    "stream": stream,
                },
                turn_resume_params.TurnResumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )


class AsyncTurnResource(AsyncAPIResource):
    @cached_property
    def step(self) -> AsyncStepResource:
        return AsyncStepResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTurnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTurnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncTurnResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        tool_config: ToolConfigParam | NotGiven = NOT_GIVEN,
        toolgroups: List[AgentToolParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """
        Create a new turn for an agent.

        Args:
          messages: List of messages to start the turn with.

          documents: (Optional) List of documents to create the turn with.

          stream: (Optional) If True, generate an SSE event stream of the response. Defaults to
              False.

          tool_config: (Optional) The tool configuration to create the turn with, will be used to
              override the agent's tool_config.

          toolgroups: (Optional) List of toolgroups to create the turn with, will be used in addition
              to the agent's config toolgroups for the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/session/{session_id}/turn",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "documents": documents,
                    "stream": stream,
                    "tool_config": tool_config,
                    "toolgroups": toolgroups,
                },
                turn_create_params.TurnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    async def retrieve(
        self,
        turn_id: str,
        *,
        agent_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """
        Retrieve an agent turn by its ID.

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
        return await self._get(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    async def resume(
        self,
        turn_id: str,
        *,
        agent_id: str,
        session_id: str,
        tool_responses: Iterable[ToolResponseParam],
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """Resume an agent turn with executed tool call responses.

        When a Turn has the
        status `awaiting_input` due to pending input from client side tool calls, this
        endpoint can be used to submit the outputs from the tool calls once they are
        ready.

        Args:
          tool_responses: The tool call responses to resume the turn with.

          stream: Whether to stream the response.

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
        return await self._post(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/resume",
            body=await async_maybe_transform(
                {
                    "tool_responses": tool_responses,
                    "stream": stream,
                },
                turn_resume_params.TurnResumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )


class TurnResourceWithRawResponse:
    def __init__(self, turn: TurnResource) -> None:
        self._turn = turn

        self.create = to_raw_response_wrapper(
            turn.create,
        )
        self.retrieve = to_raw_response_wrapper(
            turn.retrieve,
        )
        self.resume = to_raw_response_wrapper(
            turn.resume,
        )

    @cached_property
    def step(self) -> StepResourceWithRawResponse:
        return StepResourceWithRawResponse(self._turn.step)


class AsyncTurnResourceWithRawResponse:
    def __init__(self, turn: AsyncTurnResource) -> None:
        self._turn = turn

        self.create = async_to_raw_response_wrapper(
            turn.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            turn.retrieve,
        )
        self.resume = async_to_raw_response_wrapper(
            turn.resume,
        )

    @cached_property
    def step(self) -> AsyncStepResourceWithRawResponse:
        return AsyncStepResourceWithRawResponse(self._turn.step)


class TurnResourceWithStreamingResponse:
    def __init__(self, turn: TurnResource) -> None:
        self._turn = turn

        self.create = to_streamed_response_wrapper(
            turn.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            turn.retrieve,
        )
        self.resume = to_streamed_response_wrapper(
            turn.resume,
        )

    @cached_property
    def step(self) -> StepResourceWithStreamingResponse:
        return StepResourceWithStreamingResponse(self._turn.step)


class AsyncTurnResourceWithStreamingResponse:
    def __init__(self, turn: AsyncTurnResource) -> None:
        self._turn = turn

        self.create = async_to_streamed_response_wrapper(
            turn.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            turn.retrieve,
        )
        self.resume = async_to_streamed_response_wrapper(
            turn.resume,
        )

    @cached_property
    def step(self) -> AsyncStepResourceWithStreamingResponse:
        return AsyncStepResourceWithStreamingResponse(self._turn.step)
