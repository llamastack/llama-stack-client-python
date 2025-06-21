# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.openai.v1 import ChatGenerateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_completion(self, client: LlamaStackClient) -> None:
        chat = client.openai.v1.chat.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_completion_with_all_params(self, client: LlamaStackClient) -> None:
        chat = client.openai.v1.chat.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="model",
            frequency_penalty=0,
            function_call="string",
            functions=[{"foo": True}],
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            n=0,
            parallel_tool_calls=True,
            presence_penalty=0,
            response_format={"type": "text"},
            seed=0,
            stop="string",
            stream=True,
            stream_options={"foo": True},
            temperature=0,
            tool_choice="string",
            tools=[{"foo": True}],
            top_logprobs=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate_completion(self, client: LlamaStackClient) -> None:
        response = client.openai.v1.chat.with_raw_response.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate_completion(self, client: LlamaStackClient) -> None:
        with client.openai.v1.chat.with_streaming_response.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_completion(self, async_client: AsyncLlamaStackClient) -> None:
        chat = await async_client.openai.v1.chat.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_completion_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        chat = await async_client.openai.v1.chat.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="model",
            frequency_penalty=0,
            function_call="string",
            functions=[{"foo": True}],
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            n=0,
            parallel_tool_calls=True,
            presence_penalty=0,
            response_format={"type": "text"},
            seed=0,
            stop="string",
            stream=True,
            stream_options={"foo": True},
            temperature=0,
            tool_choice="string",
            tools=[{"foo": True}],
            top_logprobs=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate_completion(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.openai.v1.chat.with_raw_response.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate_completion(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.openai.v1.chat.with_streaming_response.generate_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
