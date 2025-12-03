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
    BatchListResponse,
    BatchCancelResponse,
    BatchCreateResponse,
    BatchRetrieveResponse,
)
from llama_stack_client.pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        batch = client.batches.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        batch = client.batches.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
            idempotency_key="idempotency_key",
            metadata={"foo": "string"},
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.batches.with_raw_response.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.batches.with_streaming_response.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        batch = client.batches.retrieve(
            "batch_id",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.batches.with_raw_response.retrieve(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.batches.with_streaming_response.retrieve(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batches.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        batch = client.batches.list()
        assert_matches_type(SyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        batch = client.batches.list(
            after="after",
            limit=0,
        )
        assert_matches_type(SyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(SyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(SyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: LlamaStackClient) -> None:
        batch = client.batches.cancel(
            "batch_id",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: LlamaStackClient) -> None:
        response = client.batches.with_raw_response.cancel(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: LlamaStackClient) -> None:
        with client.batches.with_streaming_response.cancel(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batches.with_raw_response.cancel(
                "",
            )


class TestAsyncBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        batch = await async_client.batches.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        batch = await async_client.batches.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
            idempotency_key="idempotency_key",
            metadata={"foo": "string"},
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.batches.with_raw_response.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.batches.with_streaming_response.create(
            completion_window="24h",
            endpoint="endpoint",
            input_file_id="input_file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        batch = await async_client.batches.retrieve(
            "batch_id",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.batches.with_raw_response.retrieve(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.batches.with_streaming_response.retrieve(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batches.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        batch = await async_client.batches.list()
        assert_matches_type(AsyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        batch = await async_client.batches.list(
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(AsyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(AsyncOpenAICursorPage[BatchListResponse], batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        batch = await async_client.batches.cancel(
            "batch_id",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.batches.with_raw_response.cancel(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.batches.with_streaming_response.cancel(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batches.with_raw_response.cancel(
                "",
            )
