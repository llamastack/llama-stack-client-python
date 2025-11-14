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
from llama_stack_client.types import Shield, ShieldListResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        shield = client.shields.retrieve(
            "identifier",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.retrieve(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Shield, shield, path=["response"])

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

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.shields.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        shield = client.shields.list()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(ShieldListResponse, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            shield = client.shields.delete(
                "identifier",
            )

        assert shield is None

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.shields.with_raw_response.delete(
                "identifier",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert shield is None

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.shields.with_streaming_response.delete(
                "identifier",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                shield = response.parse()
                assert shield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
                client.shields.with_raw_response.delete(
                    "",
                )

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            shield = client.shields.register(
                shield_id="shield_id",
            )

        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            shield = client.shields.register(
                shield_id="shield_id",
                params={"foo": "bar"},
                provider_id="provider_id",
                provider_shield_id="provider_shield_id",
            )

        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.shields.with_raw_response.register(
                shield_id="shield_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.shields.with_streaming_response.register(
                shield_id="shield_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                shield = response.parse()
                assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.retrieve(
            "identifier",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.retrieve(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Shield, shield, path=["response"])

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

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.shields.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.list()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(ShieldListResponse, shield, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(ShieldListResponse, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            shield = await async_client.shields.delete(
                "identifier",
            )

        assert shield is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.shields.with_raw_response.delete(
                "identifier",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert shield is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.shields.with_streaming_response.delete(
                "identifier",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                shield = await response.parse()
                assert shield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
                await async_client.shields.with_raw_response.delete(
                    "",
                )

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            shield = await async_client.shields.register(
                shield_id="shield_id",
            )

        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            shield = await async_client.shields.register(
                shield_id="shield_id",
                params={"foo": "bar"},
                provider_id="provider_id",
                provider_shield_id="provider_shield_id",
            )

        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.shields.with_raw_response.register(
                shield_id="shield_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.shields.with_streaming_response.register(
                shield_id="shield_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                shield = await response.parse()
                assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True
