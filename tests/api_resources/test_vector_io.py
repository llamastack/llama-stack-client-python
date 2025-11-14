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
from llama_stack_client.types import QueryChunksResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorIo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_insert(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                }
            ],
            vector_store_id="vector_store_id",
        )
        assert vector_io is None

    @parametrize
    def test_method_insert_with_all_params(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                    "chunk_metadata": {
                        "chunk_embedding_dimension": 0,
                        "chunk_embedding_model": "chunk_embedding_model",
                        "chunk_id": "chunk_id",
                        "chunk_tokenizer": "chunk_tokenizer",
                        "chunk_window": "chunk_window",
                        "content_token_count": 0,
                        "created_timestamp": 0,
                        "document_id": "document_id",
                        "metadata_token_count": 0,
                        "source": "source",
                        "updated_timestamp": 0,
                    },
                    "embedding": [0],
                    "metadata": {"foo": "bar"},
                }
            ],
            vector_store_id="vector_store_id",
            ttl_seconds=0,
        )
        assert vector_io is None

    @parametrize
    def test_raw_response_insert(self, client: LlamaStackClient) -> None:
        response = client.vector_io.with_raw_response.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                }
            ],
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = response.parse()
        assert vector_io is None

    @parametrize
    def test_streaming_response_insert(self, client: LlamaStackClient) -> None:
        with client.vector_io.with_streaming_response.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                }
            ],
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = response.parse()
            assert vector_io is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.query(
            query="string",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: LlamaStackClient) -> None:
        vector_io = client.vector_io.query(
            query="string",
            vector_store_id="vector_store_id",
            params={"foo": "bar"},
        )
        assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: LlamaStackClient) -> None:
        response = client.vector_io.with_raw_response.query(
            query="string",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = response.parse()
        assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: LlamaStackClient) -> None:
        with client.vector_io.with_streaming_response.query(
            query="string",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = response.parse()
            assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVectorIo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_insert(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                }
            ],
            vector_store_id="vector_store_id",
        )
        assert vector_io is None

    @parametrize
    async def test_method_insert_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                    "chunk_metadata": {
                        "chunk_embedding_dimension": 0,
                        "chunk_embedding_model": "chunk_embedding_model",
                        "chunk_id": "chunk_id",
                        "chunk_tokenizer": "chunk_tokenizer",
                        "chunk_window": "chunk_window",
                        "content_token_count": 0,
                        "created_timestamp": 0,
                        "document_id": "document_id",
                        "metadata_token_count": 0,
                        "source": "source",
                        "updated_timestamp": 0,
                    },
                    "embedding": [0],
                    "metadata": {"foo": "bar"},
                }
            ],
            vector_store_id="vector_store_id",
            ttl_seconds=0,
        )
        assert vector_io is None

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_io.with_raw_response.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                }
            ],
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = await response.parse()
        assert vector_io is None

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_io.with_streaming_response.insert(
            chunks=[
                {
                    "chunk_id": "chunk_id",
                    "content": "string",
                }
            ],
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = await response.parse()
            assert vector_io is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.query(
            query="string",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_io = await async_client.vector_io.query(
            query="string",
            vector_store_id="vector_store_id",
            params={"foo": "bar"},
        )
        assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_io.with_raw_response.query(
            query="string",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_io = await response.parse()
        assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_io.with_streaming_response.query(
            query="string",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_io = await response.parse()
            assert_matches_type(QueryChunksResponse, vector_io, path=["response"])

        assert cast(Any, response.is_closed) is True
