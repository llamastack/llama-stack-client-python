# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    VectorDBListResponse,
    VectorDBRegisterResponse,
    VectorDBRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorDBs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        vector_db = client.vector_dbs.retrieve(
            "vector_db_id",
        )
        assert_matches_type(VectorDBRetrieveResponse, vector_db, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.vector_dbs.with_raw_response.retrieve(
            "vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = response.parse()
        assert_matches_type(VectorDBRetrieveResponse, vector_db, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.vector_dbs.with_streaming_response.retrieve(
            "vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = response.parse()
            assert_matches_type(VectorDBRetrieveResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_db_id` but received ''"):
            client.vector_dbs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        vector_db = client.vector_dbs.list()
        assert_matches_type(VectorDBListResponse, vector_db, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.vector_dbs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = response.parse()
        assert_matches_type(VectorDBListResponse, vector_db, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.vector_dbs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = response.parse()
            assert_matches_type(VectorDBListResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        vector_db = client.vector_dbs.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
        )
        assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        vector_db = client.vector_dbs.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
            embedding_dimension=0,
            provider_id="provider_id",
            provider_vector_db_id="provider_vector_db_id",
            vector_db_name="vector_db_name",
        )
        assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.vector_dbs.with_raw_response.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = response.parse()
        assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.vector_dbs.with_streaming_response.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = response.parse()
            assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        vector_db = client.vector_dbs.unregister(
            "vector_db_id",
        )
        assert vector_db is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        response = client.vector_dbs.with_raw_response.unregister(
            "vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = response.parse()
        assert vector_db is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with client.vector_dbs.with_streaming_response.unregister(
            "vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = response.parse()
            assert vector_db is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unregister(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_db_id` but received ''"):
            client.vector_dbs.with_raw_response.unregister(
                "",
            )


class TestAsyncVectorDBs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        vector_db = await async_client.vector_dbs.retrieve(
            "vector_db_id",
        )
        assert_matches_type(VectorDBRetrieveResponse, vector_db, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_dbs.with_raw_response.retrieve(
            "vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = await response.parse()
        assert_matches_type(VectorDBRetrieveResponse, vector_db, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_dbs.with_streaming_response.retrieve(
            "vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = await response.parse()
            assert_matches_type(VectorDBRetrieveResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_db_id` but received ''"):
            await async_client.vector_dbs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        vector_db = await async_client.vector_dbs.list()
        assert_matches_type(VectorDBListResponse, vector_db, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_dbs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = await response.parse()
        assert_matches_type(VectorDBListResponse, vector_db, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_dbs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = await response.parse()
            assert_matches_type(VectorDBListResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        vector_db = await async_client.vector_dbs.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
        )
        assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        vector_db = await async_client.vector_dbs.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
            embedding_dimension=0,
            provider_id="provider_id",
            provider_vector_db_id="provider_vector_db_id",
            vector_db_name="vector_db_name",
        )
        assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_dbs.with_raw_response.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = await response.parse()
        assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_dbs.with_streaming_response.register(
            embedding_model="embedding_model",
            vector_db_id="vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = await response.parse()
            assert_matches_type(VectorDBRegisterResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        vector_db = await async_client.vector_dbs.unregister(
            "vector_db_id",
        )
        assert vector_db is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.vector_dbs.with_raw_response.unregister(
            "vector_db_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = await response.parse()
        assert vector_db is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.vector_dbs.with_streaming_response.unregister(
            "vector_db_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = await response.parse()
            assert vector_db is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_db_id` but received ''"):
            await async_client.vector_dbs.with_raw_response.unregister(
                "",
            )
