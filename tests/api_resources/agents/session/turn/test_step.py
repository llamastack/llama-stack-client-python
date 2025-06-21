# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.agents.session.turn import StepRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStep:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        step = client.agents.session.turn.step.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.agents.session.turn.step.with_raw_response.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.agents.session.turn.step.with_streaming_response.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(StepRetrieveResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="",
                session_id="session_id",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="turn_id",
            )


class TestAsyncStep:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        step = await async_client.agents.session.turn.step.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.session.turn.step.with_raw_response.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.session.turn.step.with_streaming_response.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(StepRetrieveResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="",
                session_id="session_id",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            await async_client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.agents.session.turn.step.with_raw_response.retrieve(
                step_id="",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="turn_id",
            )
