# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import Shield, ShieldListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        shield = client.shields.create(
            shield_id="shield_id",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        shield = client.shields.create(
            shield_id="shield_id",
            params={"foo": True},
            provider_id="provider_id",
            provider_shield_id="provider_shield_id",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.create(
            shield_id="shield_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.create(
            shield_id="shield_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        shield = client.shields.retrieve(
            "identifier",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.retrieve(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.retrieve(
            "identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.shields.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        shield = client.shields.list()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(ShieldListResponse, shield, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.create(
            shield_id="shield_id",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.create(
            shield_id="shield_id",
            params={"foo": True},
            provider_id="provider_id",
            provider_shield_id="provider_shield_id",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.create(
            shield_id="shield_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.create(
            shield_id="shield_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.retrieve(
            "identifier",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.retrieve(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.retrieve(
            "identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.shields.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.list()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(ShieldListResponse, shield, path=["response"])

        assert cast(Any, response.is_closed) is True
