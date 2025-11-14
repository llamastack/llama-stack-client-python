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
from llama_stack_client.types import (
    VectorStore,
    VectorStoreDeleteResponse,
    VectorStoreSearchResponse,
)
from llama_stack_client.pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorStores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.create()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.create(
            chunking_strategy={"type": "auto"},
            expires_after={"foo": "bar"},
            file_ids=["string"],
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.vector_stores.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.retrieve(
            "vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.with_raw_response.retrieve(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.vector_stores.with_streaming_response.retrieve(
            "vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.update(
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.update(
            vector_store_id="vector_store_id",
            expires_after={"foo": "bar"},
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.with_raw_response.update(
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LlamaStackClient) -> None:
        with client.vector_stores.with_streaming_response.update(
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.update(
                vector_store_id="",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.list()
        assert_matches_type(SyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.list(
            after="after",
            before="before",
            limit=0,
            order="order",
        )
        assert_matches_type(SyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(SyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.vector_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(SyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.delete(
            "vector_store_id",
        )
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.with_raw_response.delete(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.vector_stores.with_streaming_response.delete(
            "vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_search(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.search(
            vector_store_id="vector_store_id",
            query="string",
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: LlamaStackClient) -> None:
        vector_store = client.vector_stores.search(
            vector_store_id="vector_store_id",
            query="string",
            filters={"foo": "bar"},
            max_num_results=0,
            ranking_options={
                "ranker": "ranker",
                "score_threshold": 0,
            },
            rewrite_query=True,
            search_mode="search_mode",
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.with_raw_response.search(
            vector_store_id="vector_store_id",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: LlamaStackClient) -> None:
        with client.vector_stores.with_streaming_response.search(
            vector_store_id="vector_store_id",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.search(
                vector_store_id="",
                query="string",
            )


class TestAsyncVectorStores:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.create()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.create(
            chunking_strategy={"type": "auto"},
            expires_after={"foo": "bar"},
            file_ids=["string"],
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.retrieve(
            "vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.with_raw_response.retrieve(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.with_streaming_response.retrieve(
            "vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.update(
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.update(
            vector_store_id="vector_store_id",
            expires_after={"foo": "bar"},
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.with_raw_response.update(
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.with_streaming_response.update(
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.update(
                vector_store_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.list()
        assert_matches_type(AsyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.list(
            after="after",
            before="before",
            limit=0,
            order="order",
        )
        assert_matches_type(AsyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(AsyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(AsyncOpenAICursorPage[VectorStore], vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.delete(
            "vector_store_id",
        )
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.with_raw_response.delete(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.with_streaming_response.delete(
            "vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.search(
            vector_store_id="vector_store_id",
            query="string",
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_store = await async_client.vector_stores.search(
            vector_store_id="vector_store_id",
            query="string",
            filters={"foo": "bar"},
            max_num_results=0,
            ranking_options={
                "ranker": "ranker",
                "score_threshold": 0,
            },
            rewrite_query=True,
            search_mode="search_mode",
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.with_raw_response.search(
            vector_store_id="vector_store_id",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.with_streaming_response.search(
            vector_store_id="vector_store_id",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.search(
                vector_store_id="",
                query="string",
            )
