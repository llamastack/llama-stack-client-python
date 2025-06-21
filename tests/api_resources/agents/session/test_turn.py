# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.agents.session.turn import Turn

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTurn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        turn = client.agents.session.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        turn = client.agents.session.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            documents=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                }
            ],
            stream=True,
            tool_config={
                "system_message_behavior": "append",
                "tool_choice": "auto",
                "tool_prompt_format": "json",
            },
            toolgroups=["string"],
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.agents.session.turn.with_raw_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.agents.session.turn.with_streaming_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.session.turn.with_raw_response.create(
                session_id="session_id",
                agent_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.agents.session.turn.with_raw_response.create(
                session_id="",
                agent_id="agent_id",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        turn = client.agents.session.turn.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.agents.session.turn.with_raw_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.agents.session.turn.with_streaming_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.session.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.agents.session.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="agent_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            client.agents.session.turn.with_raw_response.retrieve(
                turn_id="",
                agent_id="agent_id",
                session_id="session_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_resume(self, client: LlamaStackClient) -> None:
        turn = client.agents.session.turn.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                }
            ],
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_resume_with_all_params(self, client: LlamaStackClient) -> None:
        turn = client.agents.session.turn.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                    "metadata": {"foo": True},
                }
            ],
            stream=True,
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_resume(self, client: LlamaStackClient) -> None:
        response = client.agents.session.turn.with_raw_response.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_resume(self, client: LlamaStackClient) -> None:
        with client.agents.session.turn.with_streaming_response.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_resume(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.session.turn.with_raw_response.resume(
                turn_id="turn_id",
                agent_id="",
                session_id="session_id",
                tool_responses=[
                    {
                        "call_id": "call_id",
                        "content": "string",
                        "tool_name": "brave_search",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.agents.session.turn.with_raw_response.resume(
                turn_id="turn_id",
                agent_id="agent_id",
                session_id="",
                tool_responses=[
                    {
                        "call_id": "call_id",
                        "content": "string",
                        "tool_name": "brave_search",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            client.agents.session.turn.with_raw_response.resume(
                turn_id="",
                agent_id="agent_id",
                session_id="session_id",
                tool_responses=[
                    {
                        "call_id": "call_id",
                        "content": "string",
                        "tool_name": "brave_search",
                    }
                ],
            )


class TestAsyncTurn:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.session.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.session.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            documents=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                }
            ],
            stream=True,
            tool_config={
                "system_message_behavior": "append",
                "tool_choice": "auto",
                "tool_prompt_format": "json",
            },
            toolgroups=["string"],
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.session.turn.with_raw_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = await response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.session.turn.with_streaming_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = await response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.create(
                session_id="session_id",
                agent_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.create(
                session_id="",
                agent_id="agent_id",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.session.turn.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.session.turn.with_raw_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = await response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.session.turn.with_streaming_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = await response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="agent_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.retrieve(
                turn_id="",
                agent_id="agent_id",
                session_id="session_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_resume(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.session.turn.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                }
            ],
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_resume_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.session.turn.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                    "metadata": {"foo": True},
                }
            ],
            stream=True,
        )
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.session.turn.with_raw_response.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = await response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.session.turn.with_streaming_response.resume(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            tool_responses=[
                {
                    "call_id": "call_id",
                    "content": "string",
                    "tool_name": "brave_search",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = await response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_resume(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.resume(
                turn_id="turn_id",
                agent_id="",
                session_id="session_id",
                tool_responses=[
                    {
                        "call_id": "call_id",
                        "content": "string",
                        "tool_name": "brave_search",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.resume(
                turn_id="turn_id",
                agent_id="agent_id",
                session_id="",
                tool_responses=[
                    {
                        "call_id": "call_id",
                        "content": "string",
                        "tool_name": "brave_search",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            await async_client.agents.session.turn.with_raw_response.resume(
                turn_id="",
                agent_id="agent_id",
                session_id="session_id",
                tool_responses=[
                    {
                        "call_id": "call_id",
                        "content": "string",
                        "tool_name": "brave_search",
                    }
                ],
            )
