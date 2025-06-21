# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.openai.v1 import OpenAIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        response = client.openai.v1.responses.create(
            input="string",
            model="model",
        )
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        response = client.openai.v1.responses.create(
            input="string",
            model="model",
            previous_response_id="previous_response_id",
            store=True,
            stream=True,
            temperature=0,
            tools=[
                {
                    "type": "web_search",
                    "search_context_size": "search_context_size",
                }
            ],
        )
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        http_response = client.openai.v1.responses.with_raw_response.create(
            input="string",
            model="model",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.openai.v1.responses.with_streaming_response.create(
            input="string",
            model="model",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(OpenAIResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        response = client.openai.v1.responses.retrieve(
            "id",
        )
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        http_response = client.openai.v1.responses.with_raw_response.retrieve(
            "id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.openai.v1.responses.with_streaming_response.retrieve(
            "id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(OpenAIResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.openai.v1.responses.with_raw_response.retrieve(
                "",
            )


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.openai.v1.responses.create(
            input="string",
            model="model",
        )
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.openai.v1.responses.create(
            input="string",
            model="model",
            previous_response_id="previous_response_id",
            store=True,
            stream=True,
            temperature=0,
            tools=[
                {
                    "type": "web_search",
                    "search_context_size": "search_context_size",
                }
            ],
        )
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        http_response = await async_client.openai.v1.responses.with_raw_response.create(
            input="string",
            model="model",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.openai.v1.responses.with_streaming_response.create(
            input="string",
            model="model",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(OpenAIResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.openai.v1.responses.retrieve(
            "id",
        )
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        http_response = await async_client.openai.v1.responses.with_raw_response.retrieve(
            "id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(OpenAIResponse, response, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.openai.v1.responses.with_streaming_response.retrieve(
            "id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(OpenAIResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.openai.v1.responses.with_raw_response.retrieve(
                "",
            )
