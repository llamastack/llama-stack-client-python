# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import agent_create_params
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
from ...types.agent import Agent
from ..._base_client import make_request_options
from .session.session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ...types.agent_config_param import AgentConfigParam
from ...types.agent_list_response import AgentListResponse
from ...types.agent_create_response import AgentCreateResponse
from ...types.agent_list_sessions_response import AgentListSessionsResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def session(self) -> SessionResource:
        return SessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_config: AgentConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """
        Create an agent with the given configuration.

        Args:
          agent_config: The configuration for the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents",
            body=maybe_transform({"agent_config": agent_config}, agent_create_params.AgentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Describe an agent by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
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
    ) -> AgentListResponse:
        """List all agents."""
        return self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an agent by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_sessions(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListSessionsResponse:
        """
        List all session(s) of a given agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/sessions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentListSessionsResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def session(self) -> AsyncSessionResource:
        return AsyncSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_config: AgentConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """
        Create an agent with the given configuration.

        Args:
          agent_config: The configuration for the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents",
            body=await async_maybe_transform({"agent_config": agent_config}, agent_create_params.AgentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Describe an agent by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
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
    ) -> AgentListResponse:
        """List all agents."""
        return await self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an agent by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_sessions(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListSessionsResponse:
        """
        List all session(s) of a given agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/sessions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentListSessionsResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.list_sessions = to_raw_response_wrapper(
            agents.list_sessions,
        )

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._agents.session)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.list_sessions = async_to_raw_response_wrapper(
            agents.list_sessions,
        )

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._agents.session)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.list_sessions = to_streamed_response_wrapper(
            agents.list_sessions,
        )

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._agents.session)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.list_sessions = async_to_streamed_response_wrapper(
            agents.list_sessions,
        )

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._agents.session)
