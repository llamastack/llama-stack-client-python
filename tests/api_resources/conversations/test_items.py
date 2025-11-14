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
from llama_stack_client.pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage
from llama_stack_client.types.conversations import (
    ItemGetResponse,
    ItemListResponse,
    ItemCreateResponse,
    ItemDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        item = client.conversations.items.create(
            conversation_id="conversation_id",
            items=[
                {
                    "content": "string",
                    "role": "system",
                    "type": "message",
                }
            ],
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.conversations.items.with_raw_response.create(
            conversation_id="conversation_id",
            items=[
                {
                    "content": "string",
                    "role": "system",
                    "type": "message",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.conversations.items.with_streaming_response.create(
            conversation_id="conversation_id",
            items=[
                {
                    "content": "string",
                    "role": "system",
                    "type": "message",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.items.with_raw_response.create(
                conversation_id="",
                items=[
                    {
                        "content": "string",
                        "role": "system",
                        "type": "message",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        item = client.conversations.items.list(
            conversation_id="conversation_id",
        )
        assert_matches_type(SyncOpenAICursorPage[ItemListResponse], item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        item = client.conversations.items.list(
            conversation_id="conversation_id",
            after="after",
            include=["web_search_call.action.sources"],
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncOpenAICursorPage[ItemListResponse], item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.conversations.items.with_raw_response.list(
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncOpenAICursorPage[ItemListResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.conversations.items.with_streaming_response.list(
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(SyncOpenAICursorPage[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.items.with_raw_response.list(
                conversation_id="",
            )

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        item = client.conversations.items.delete(
            item_id="item_id",
            conversation_id="conversation_id",
        )
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        response = client.conversations.items.with_raw_response.delete(
            item_id="item_id",
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.conversations.items.with_streaming_response.delete(
            item_id="item_id",
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemDeleteResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.items.with_raw_response.delete(
                item_id="item_id",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.conversations.items.with_raw_response.delete(
                item_id="",
                conversation_id="conversation_id",
            )

    @parametrize
    def test_method_get(self, client: LlamaStackClient) -> None:
        item = client.conversations.items.get(
            item_id="item_id",
            conversation_id="conversation_id",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LlamaStackClient) -> None:
        response = client.conversations.items.with_raw_response.get(
            item_id="item_id",
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LlamaStackClient) -> None:
        with client.conversations.items.with_streaming_response.get(
            item_id="item_id",
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.items.with_raw_response.get(
                item_id="item_id",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.conversations.items.with_raw_response.get(
                item_id="",
                conversation_id="conversation_id",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        item = await async_client.conversations.items.create(
            conversation_id="conversation_id",
            items=[
                {
                    "content": "string",
                    "role": "system",
                    "type": "message",
                }
            ],
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.conversations.items.with_raw_response.create(
            conversation_id="conversation_id",
            items=[
                {
                    "content": "string",
                    "role": "system",
                    "type": "message",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.conversations.items.with_streaming_response.create(
            conversation_id="conversation_id",
            items=[
                {
                    "content": "string",
                    "role": "system",
                    "type": "message",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.items.with_raw_response.create(
                conversation_id="",
                items=[
                    {
                        "content": "string",
                        "role": "system",
                        "type": "message",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        item = await async_client.conversations.items.list(
            conversation_id="conversation_id",
        )
        assert_matches_type(AsyncOpenAICursorPage[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        item = await async_client.conversations.items.list(
            conversation_id="conversation_id",
            after="after",
            include=["web_search_call.action.sources"],
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncOpenAICursorPage[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.conversations.items.with_raw_response.list(
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(AsyncOpenAICursorPage[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.conversations.items.with_streaming_response.list(
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AsyncOpenAICursorPage[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.items.with_raw_response.list(
                conversation_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        item = await async_client.conversations.items.delete(
            item_id="item_id",
            conversation_id="conversation_id",
        )
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.conversations.items.with_raw_response.delete(
            item_id="item_id",
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.conversations.items.with_streaming_response.delete(
            item_id="item_id",
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemDeleteResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.items.with_raw_response.delete(
                item_id="item_id",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.conversations.items.with_raw_response.delete(
                item_id="",
                conversation_id="conversation_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaStackClient) -> None:
        item = await async_client.conversations.items.get(
            item_id="item_id",
            conversation_id="conversation_id",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.conversations.items.with_raw_response.get(
            item_id="item_id",
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.conversations.items.with_streaming_response.get(
            item_id="item_id",
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.items.with_raw_response.get(
                item_id="item_id",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.conversations.items.with_raw_response.get(
                item_id="",
                conversation_id="conversation_id",
            )
