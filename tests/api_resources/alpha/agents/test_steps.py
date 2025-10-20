# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.alpha.agents import StepRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        step = client.alpha.agents.steps.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.alpha.agents.steps.with_raw_response.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.alpha.agents.steps.with_streaming_response.retrieve(
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

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="",
                session_id="session_id",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="turn_id",
            )


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        step = await async_client.alpha.agents.steps.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.agents.steps.with_raw_response.retrieve(
            step_id="step_id",
            agent_id="agent_id",
            session_id="session_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.agents.steps.with_streaming_response.retrieve(
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

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="",
                session_id="session_id",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="",
                turn_id="turn_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            await async_client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="step_id",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.alpha.agents.steps.with_raw_response.retrieve(
                step_id="",
                agent_id="agent_id",
                session_id="session_id",
                turn_id="turn_id",
            )
