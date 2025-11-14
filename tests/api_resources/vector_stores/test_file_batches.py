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
from llama_stack_client.types.vector_stores import (
    VectorStoreFile,
    VectorStoreFileBatches,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        file_batch = client.vector_stores.file_batches.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        file_batch = client.vector_stores.file_batches.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
            attributes={"foo": "bar"},
            chunking_strategy={"type": "auto"},
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.file_batches.with_raw_response.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.vector_stores.file_batches.with_streaming_response.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.file_batches.with_raw_response.create(
                vector_store_id="",
                file_ids=["string"],
            )

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        file_batch = client.vector_stores.file_batches.retrieve(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.file_batches.with_raw_response.retrieve(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.vector_stores.file_batches.with_streaming_response.retrieve(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.file_batches.with_raw_response.retrieve(
                batch_id="batch_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.vector_stores.file_batches.with_raw_response.retrieve(
                batch_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    def test_method_cancel(self, client: LlamaStackClient) -> None:
        file_batch = client.vector_stores.file_batches.cancel(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.file_batches.with_raw_response.cancel(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: LlamaStackClient) -> None:
        with client.vector_stores.file_batches.with_streaming_response.cancel(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.file_batches.with_raw_response.cancel(
                batch_id="batch_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.vector_stores.file_batches.with_raw_response.cancel(
                batch_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    def test_method_list_files(self, client: LlamaStackClient) -> None:
        file_batch = client.vector_stores.file_batches.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(SyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    def test_method_list_files_with_all_params(self, client: LlamaStackClient) -> None:
        file_batch = client.vector_stores.file_batches.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
            after="after",
            before="before",
            filter="filter",
            limit=0,
            order="order",
        )
        assert_matches_type(SyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    def test_raw_response_list_files(self, client: LlamaStackClient) -> None:
        response = client.vector_stores.file_batches.with_raw_response.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(SyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    def test_streaming_response_list_files(self, client: LlamaStackClient) -> None:
        with client.vector_stores.file_batches.with_streaming_response.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(SyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_files(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.file_batches.with_raw_response.list_files(
                batch_id="batch_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.vector_stores.file_batches.with_raw_response.list_files(
                batch_id="",
                vector_store_id="vector_store_id",
            )


class TestAsyncFileBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        file_batch = await async_client.vector_stores.file_batches.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        file_batch = await async_client.vector_stores.file_batches.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
            attributes={"foo": "bar"},
            chunking_strategy={"type": "auto"},
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.file_batches.with_raw_response.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = await response.parse()
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.file_batches.with_streaming_response.create(
            vector_store_id="vector_store_id",
            file_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.file_batches.with_raw_response.create(
                vector_store_id="",
                file_ids=["string"],
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        file_batch = await async_client.vector_stores.file_batches.retrieve(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.file_batches.with_raw_response.retrieve(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = await response.parse()
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.file_batches.with_streaming_response.retrieve(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.file_batches.with_raw_response.retrieve(
                batch_id="batch_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.vector_stores.file_batches.with_raw_response.retrieve(
                batch_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        file_batch = await async_client.vector_stores.file_batches.cancel(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.file_batches.with_raw_response.cancel(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = await response.parse()
        assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.file_batches.with_streaming_response.cancel(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(VectorStoreFileBatches, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.file_batches.with_raw_response.cancel(
                batch_id="batch_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.vector_stores.file_batches.with_raw_response.cancel(
                batch_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    async def test_method_list_files(self, async_client: AsyncLlamaStackClient) -> None:
        file_batch = await async_client.vector_stores.file_batches.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(AsyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    async def test_method_list_files_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        file_batch = await async_client.vector_stores.file_batches.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
            after="after",
            before="before",
            filter="filter",
            limit=0,
            order="order",
        )
        assert_matches_type(AsyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_stores.file_batches.with_raw_response.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = await response.parse()
        assert_matches_type(AsyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_stores.file_batches.with_streaming_response.list_files(
            batch_id="batch_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(AsyncOpenAICursorPage[VectorStoreFile], file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_files(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.file_batches.with_raw_response.list_files(
                batch_id="batch_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.vector_stores.file_batches.with_raw_response.list_files(
                batch_id="",
                vector_store_id="vector_store_id",
            )
