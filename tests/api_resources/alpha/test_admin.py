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
from llama_stack_client.types import RouteListResponse, ProviderListResponse
from llama_stack_client.types.shared import HealthInfo, VersionInfo, ProviderInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_health(self, client: LlamaStackClient) -> None:
        admin = client.alpha.admin.health()
        assert_matches_type(HealthInfo, admin, path=["response"])

    @parametrize
    def test_raw_response_health(self, client: LlamaStackClient) -> None:
        response = client.alpha.admin.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(HealthInfo, admin, path=["response"])

    @parametrize
    def test_streaming_response_health(self, client: LlamaStackClient) -> None:
        with client.alpha.admin.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(HealthInfo, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_inspect_provider(self, client: LlamaStackClient) -> None:
        admin = client.alpha.admin.inspect_provider(
            "provider_id",
        )
        assert_matches_type(ProviderInfo, admin, path=["response"])

    @parametrize
    def test_raw_response_inspect_provider(self, client: LlamaStackClient) -> None:
        response = client.alpha.admin.with_raw_response.inspect_provider(
            "provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ProviderInfo, admin, path=["response"])

    @parametrize
    def test_streaming_response_inspect_provider(self, client: LlamaStackClient) -> None:
        with client.alpha.admin.with_streaming_response.inspect_provider(
            "provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ProviderInfo, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_inspect_provider(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.alpha.admin.with_raw_response.inspect_provider(
                "",
            )

    @parametrize
    def test_method_list_providers(self, client: LlamaStackClient) -> None:
        admin = client.alpha.admin.list_providers()
        assert_matches_type(ProviderListResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_list_providers(self, client: LlamaStackClient) -> None:
        response = client.alpha.admin.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ProviderListResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_list_providers(self, client: LlamaStackClient) -> None:
        with client.alpha.admin.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ProviderListResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_routes(self, client: LlamaStackClient) -> None:
        admin = client.alpha.admin.list_routes()
        assert_matches_type(RouteListResponse, admin, path=["response"])

    @parametrize
    def test_method_list_routes_with_all_params(self, client: LlamaStackClient) -> None:
        admin = client.alpha.admin.list_routes(
            api_filter="v1",
        )
        assert_matches_type(RouteListResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_list_routes(self, client: LlamaStackClient) -> None:
        response = client.alpha.admin.with_raw_response.list_routes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(RouteListResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_list_routes(self, client: LlamaStackClient) -> None:
        with client.alpha.admin.with_streaming_response.list_routes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(RouteListResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_version(self, client: LlamaStackClient) -> None:
        admin = client.alpha.admin.version()
        assert_matches_type(VersionInfo, admin, path=["response"])

    @parametrize
    def test_raw_response_version(self, client: LlamaStackClient) -> None:
        response = client.alpha.admin.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(VersionInfo, admin, path=["response"])

    @parametrize
    def test_streaming_response_version(self, client: LlamaStackClient) -> None:
        with client.alpha.admin.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(VersionInfo, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_health(self, async_client: AsyncLlamaStackClient) -> None:
        admin = await async_client.alpha.admin.health()
        assert_matches_type(HealthInfo, admin, path=["response"])

    @parametrize
    async def test_raw_response_health(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.admin.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(HealthInfo, admin, path=["response"])

    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.admin.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(HealthInfo, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_inspect_provider(self, async_client: AsyncLlamaStackClient) -> None:
        admin = await async_client.alpha.admin.inspect_provider(
            "provider_id",
        )
        assert_matches_type(ProviderInfo, admin, path=["response"])

    @parametrize
    async def test_raw_response_inspect_provider(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.admin.with_raw_response.inspect_provider(
            "provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ProviderInfo, admin, path=["response"])

    @parametrize
    async def test_streaming_response_inspect_provider(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.admin.with_streaming_response.inspect_provider(
            "provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ProviderInfo, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_inspect_provider(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.alpha.admin.with_raw_response.inspect_provider(
                "",
            )

    @parametrize
    async def test_method_list_providers(self, async_client: AsyncLlamaStackClient) -> None:
        admin = await async_client.alpha.admin.list_providers()
        assert_matches_type(ProviderListResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_list_providers(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.admin.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ProviderListResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_list_providers(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.admin.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ProviderListResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_routes(self, async_client: AsyncLlamaStackClient) -> None:
        admin = await async_client.alpha.admin.list_routes()
        assert_matches_type(RouteListResponse, admin, path=["response"])

    @parametrize
    async def test_method_list_routes_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        admin = await async_client.alpha.admin.list_routes(
            api_filter="v1",
        )
        assert_matches_type(RouteListResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_list_routes(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.admin.with_raw_response.list_routes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(RouteListResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_list_routes(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.admin.with_streaming_response.list_routes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(RouteListResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_version(self, async_client: AsyncLlamaStackClient) -> None:
        admin = await async_client.alpha.admin.version()
        assert_matches_type(VersionInfo, admin, path=["response"])

    @parametrize
    async def test_raw_response_version(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.admin.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(VersionInfo, admin, path=["response"])

    @parametrize
    async def test_streaming_response_version(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.admin.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(VersionInfo, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
