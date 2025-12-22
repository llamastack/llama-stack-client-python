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
from llama_stack_client.types.shared import HealthInfo, VersionInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInspect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_health(self, client: LlamaStackClient) -> None:
        inspect = client.inspect.health()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    def test_raw_response_health(self, client: LlamaStackClient) -> None:
        response = client.inspect.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inspect = response.parse()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    def test_streaming_response_health(self, client: LlamaStackClient) -> None:
        with client.inspect.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inspect = response.parse()
            assert_matches_type(HealthInfo, inspect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_version(self, client: LlamaStackClient) -> None:
        inspect = client.inspect.version()
        assert_matches_type(VersionInfo, inspect, path=["response"])

    @parametrize
    def test_raw_response_version(self, client: LlamaStackClient) -> None:
        response = client.inspect.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inspect = response.parse()
        assert_matches_type(VersionInfo, inspect, path=["response"])

    @parametrize
    def test_streaming_response_version(self, client: LlamaStackClient) -> None:
        with client.inspect.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inspect = response.parse()
            assert_matches_type(VersionInfo, inspect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInspect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_health(self, async_client: AsyncLlamaStackClient) -> None:
        inspect = await async_client.inspect.health()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    async def test_raw_response_health(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.inspect.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inspect = await response.parse()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.inspect.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inspect = await response.parse()
            assert_matches_type(HealthInfo, inspect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_version(self, async_client: AsyncLlamaStackClient) -> None:
        inspect = await async_client.inspect.version()
        assert_matches_type(VersionInfo, inspect, path=["response"])

    @parametrize
    async def test_raw_response_version(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.inspect.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inspect = await response.parse()
        assert_matches_type(VersionInfo, inspect, path=["response"])

    @parametrize
    async def test_streaming_response_version(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.inspect.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inspect = await response.parse()
            assert_matches_type(VersionInfo, inspect, path=["response"])

        assert cast(Any, response.is_closed) is True
