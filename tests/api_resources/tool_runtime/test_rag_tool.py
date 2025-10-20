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
from llama_stack_client.types.shared import QueryResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRagTool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_insert(self, client: LlamaStackClient) -> None:
        rag_tool = client.tool_runtime.rag_tool.insert(
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

    @parametrize
    def test_raw_response_insert(self, client: LlamaStackClient) -> None:
        response = client.tool_runtime.rag_tool.with_raw_response.insert(
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

    @parametrize
    def test_streaming_response_insert(self, client: LlamaStackClient) -> None:
        with client.tool_runtime.rag_tool.with_streaming_response.insert(
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

    @parametrize
    def test_method_query(self, client: LlamaStackClient) -> None:
        rag_tool = client.tool_runtime.rag_tool.query(
            content="string",
            vector_db_ids=["string"],
        )
        assert_matches_type(QueryResult, rag_tool, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: LlamaStackClient) -> None:
        rag_tool = client.tool_runtime.rag_tool.query(
            content="string",
            vector_db_ids=["string"],
            query_config={
                "chunk_template": "chunk_template",
                "max_chunks": 0,
                "max_tokens_in_context": 0,
                "query_generator_config": {
                    "separator": "separator",
                    "type": "default",
                },
                "mode": "vector",
                "ranker": {
                    "impact_factor": 0,
                    "type": "rrf",
                },
            },
        )
        assert_matches_type(QueryResult, rag_tool, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: LlamaStackClient) -> None:
        response = client.tool_runtime.rag_tool.with_raw_response.query(
            content="string",
            vector_db_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rag_tool = response.parse()
        assert_matches_type(QueryResult, rag_tool, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: LlamaStackClient) -> None:
        with client.tool_runtime.rag_tool.with_streaming_response.query(
            content="string",
            vector_db_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rag_tool = response.parse()
            assert_matches_type(QueryResult, rag_tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRagTool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_insert(self, async_client: AsyncLlamaStackClient) -> None:
        rag_tool = await async_client.tool_runtime.rag_tool.insert(
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

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_runtime.rag_tool.with_raw_response.insert(
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

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_runtime.rag_tool.with_streaming_response.insert(
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

    @parametrize
    async def test_method_query(self, async_client: AsyncLlamaStackClient) -> None:
        rag_tool = await async_client.tool_runtime.rag_tool.query(
            content="string",
            vector_db_ids=["string"],
        )
        assert_matches_type(QueryResult, rag_tool, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        rag_tool = await async_client.tool_runtime.rag_tool.query(
            content="string",
            vector_db_ids=["string"],
            query_config={
                "chunk_template": "chunk_template",
                "max_chunks": 0,
                "max_tokens_in_context": 0,
                "query_generator_config": {
                    "separator": "separator",
                    "type": "default",
                },
                "mode": "vector",
                "ranker": {
                    "impact_factor": 0,
                    "type": "rrf",
                },
            },
        )
        assert_matches_type(QueryResult, rag_tool, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_runtime.rag_tool.with_raw_response.query(
            content="string",
            vector_db_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rag_tool = await response.parse()
        assert_matches_type(QueryResult, rag_tool, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_runtime.rag_tool.with_streaming_response.query(
            content="string",
            vector_db_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rag_tool = await response.parse()
            assert_matches_type(QueryResult, rag_tool, path=["response"])

        assert cast(Any, response.is_closed) is True
