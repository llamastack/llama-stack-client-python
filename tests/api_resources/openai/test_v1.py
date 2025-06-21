# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.openai import (
    V1ListModelsResponse,
    V1GenerateCompletionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_completion(self, client: LlamaStackClient) -> None:
        v1 = client.openai.v1.generate_completion(
            model="model",
            prompt="string",
        )
        assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_completion_with_all_params(self, client: LlamaStackClient) -> None:
        v1 = client.openai.v1.generate_completion(
            model="model",
            prompt="string",
            best_of=0,
            echo=True,
            frequency_penalty=0,
            guided_choice=["string"],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            prompt_logprobs=0,
            seed=0,
            stop="string",
            stream=True,
            stream_options={"foo": True},
            temperature=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate_completion(self, client: LlamaStackClient) -> None:
        response = client.openai.v1.with_raw_response.generate_completion(
            model="model",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate_completion(self, client: LlamaStackClient) -> None:
        with client.openai.v1.with_streaming_response.generate_completion(
            model="model",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_models(self, client: LlamaStackClient) -> None:
        v1 = client.openai.v1.list_models()
        assert_matches_type(V1ListModelsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_models(self, client: LlamaStackClient) -> None:
        response = client.openai.v1.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListModelsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_models(self, client: LlamaStackClient) -> None:
        with client.openai.v1.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListModelsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_completion(self, async_client: AsyncLlamaStackClient) -> None:
        v1 = await async_client.openai.v1.generate_completion(
            model="model",
            prompt="string",
        )
        assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_completion_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        v1 = await async_client.openai.v1.generate_completion(
            model="model",
            prompt="string",
            best_of=0,
            echo=True,
            frequency_penalty=0,
            guided_choice=["string"],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            prompt_logprobs=0,
            seed=0,
            stop="string",
            stream=True,
            stream_options={"foo": True},
            temperature=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate_completion(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.openai.v1.with_raw_response.generate_completion(
            model="model",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate_completion(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.openai.v1.with_streaming_response.generate_completion(
            model="model",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GenerateCompletionResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_models(self, async_client: AsyncLlamaStackClient) -> None:
        v1 = await async_client.openai.v1.list_models()
        assert_matches_type(V1ListModelsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_models(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.openai.v1.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListModelsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_models(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.openai.v1.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListModelsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
