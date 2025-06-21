# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    VectorIoQueryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorIo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_insert(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )
        assert vector_io is None

    @pytest.mark.skip()
    @parametrize
    def test_method_insert_with_all_params(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
            ttl_seconds=0,
        )
        assert vector_io is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_insert(self, client: LlamaStackClient) -> None:
        response = client.vector_io.with_raw_response.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = response.parse()
        assert vector_io is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_insert(self, client: LlamaStackClient) -> None:
        with client.vector_io.with_streaming_response.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = response.parse()
            assert vector_io is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.query(
            query="string",
            vector_db_id="vector_db_id",
        )
        assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_with_all_params(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.query(
            query="string",
            vector_db_id="vector_db_id",
            params={"foo": True},
        )
        assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query(self, client: LlamaStackClient) -> None:
        response = client.vector_io.with_raw_response.query(
            query="string",
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = response.parse()
        assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query(self, client: LlamaStackClient) -> None:
        with client.vector_io.with_streaming_response.query(
            query="string",
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = response.parse()
            assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVectorIo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_insert(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )
        assert vector_io is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_insert_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
            ttl_seconds=0,
        )
        assert vector_io is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_io.with_raw_response.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = await response.parse()
        assert vector_io is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_io.with_streaming_response.insert(
            chunks=[
                {
                    "content": "string",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = await response.parse()
            assert vector_io is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.query(
            query="string",
            vector_db_id="vector_db_id",
        )
        assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.query(
            query="string",
            vector_db_id="vector_db_id",
            params={"foo": True},
        )
        assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_io.with_raw_response.query(
            query="string",
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = await response.parse()
        assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_io.with_streaming_response.query(
            query="string",
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = await response.parse()
            assert_matches_type(VectorIoQueryResponse, vector_io, path=["response"])

        assert cast(Any, response.is_closed) is True
