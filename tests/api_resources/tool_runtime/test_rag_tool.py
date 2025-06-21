# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.tool_runtime import (
    RagToolQueryContextResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRagTool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_insert_documents(self, client: LlamaStackClient) -> None:
        rag_tool = client.tool_runtime.rag_tool.insert_documents(
            chunk_size_in_tokens=0,
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )
        assert rag_tool is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_insert_documents(self, client: LlamaStackClient) -> None:
        response = client.tool_runtime.rag_tool.with_raw_response.insert_documents(
            chunk_size_in_tokens=0,
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rag_tool = response.parse()
        assert rag_tool is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_insert_documents(self, client: LlamaStackClient) -> None:
        with client.tool_runtime.rag_tool.with_streaming_response.insert_documents(
            chunk_size_in_tokens=0,
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rag_tool = response.parse()
            assert rag_tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_query_context(self, client: LlamaStackClient) -> None:
        rag_tool = client.tool_runtime.rag_tool.query_context(
            content="string",
            vector_db_ids=["string"],
        )
        assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_context_with_all_params(self, client: LlamaStackClient) -> None:
        rag_tool = client.tool_runtime.rag_tool.query_context(
            content="string",
            vector_db_ids=["string"],
            query_config={
                "max_chunks": 0,
                "max_tokens_in_context": 0,
                "query_generator_config": {
                    "separator": "separator",
                    "type": "default",
                },
            },
        )
        assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query_context(self, client: LlamaStackClient) -> None:
        response = client.tool_runtime.rag_tool.with_raw_response.query_context(
            content="string",
            vector_db_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rag_tool = response.parse()
        assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query_context(self, client: LlamaStackClient) -> None:
        with client.tool_runtime.rag_tool.with_streaming_response.query_context(
            content="string",
            vector_db_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rag_tool = response.parse()
            assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRagTool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_insert_documents(self, async_client: AsyncLlamaStackClient) -> None:
        rag_tool = await async_client.tool_runtime.rag_tool.insert_documents(
            chunk_size_in_tokens=0,
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )
        assert rag_tool is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_insert_documents(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_runtime.rag_tool.with_raw_response.insert_documents(
            chunk_size_in_tokens=0,
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rag_tool = await response.parse()
        assert rag_tool is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_insert_documents(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_runtime.rag_tool.with_streaming_response.insert_documents(
            chunk_size_in_tokens=0,
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                }
            ],
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rag_tool = await response.parse()
            assert rag_tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_context(self, async_client: AsyncLlamaStackClient) -> None:
        rag_tool = await async_client.tool_runtime.rag_tool.query_context(
            content="string",
            vector_db_ids=["string"],
        )
        assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_context_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        rag_tool = await async_client.tool_runtime.rag_tool.query_context(
            content="string",
            vector_db_ids=["string"],
            query_config={
                "max_chunks": 0,
                "max_tokens_in_context": 0,
                "query_generator_config": {
                    "separator": "separator",
                    "type": "default",
                },
            },
        )
        assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query_context(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_runtime.rag_tool.with_raw_response.query_context(
            content="string",
            vector_db_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rag_tool = await response.parse()
        assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query_context(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_runtime.rag_tool.with_streaming_response.query_context(
            content="string",
            vector_db_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rag_tool = await response.parse()
            assert_matches_type(RagToolQueryContextResponse, rag_tool, path=["response"])

        assert cast(Any, response.is_closed) is True
