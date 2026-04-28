# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ogx_client import OgxClient, AsyncOgxClient
from tests.utils import assert_matches_type
from ogx_client.types import RunShieldResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSafety:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run_shield(self, client: OgxClient) -> None:
        safety = client.safety.run_shield(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            shield_id="x",
        )
        assert_matches_type(RunShieldResponse, safety, path=["response"])

    @parametrize
    def test_raw_response_run_shield(self, client: OgxClient) -> None:
        response = client.safety.with_raw_response.run_shield(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            shield_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        safety = response.parse()
        assert_matches_type(RunShieldResponse, safety, path=["response"])

    @parametrize
    def test_streaming_response_run_shield(self, client: OgxClient) -> None:
        with client.safety.with_streaming_response.run_shield(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            shield_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            safety = response.parse()
            assert_matches_type(RunShieldResponse, safety, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSafety:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_run_shield(self, async_client: AsyncOgxClient) -> None:
        safety = await async_client.safety.run_shield(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            shield_id="x",
        )
        assert_matches_type(RunShieldResponse, safety, path=["response"])

    @parametrize
    async def test_raw_response_run_shield(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.safety.with_raw_response.run_shield(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            shield_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        safety = await response.parse()
        assert_matches_type(RunShieldResponse, safety, path=["response"])

    @parametrize
    async def test_streaming_response_run_shield(self, async_client: AsyncOgxClient) -> None:
        async with async_client.safety.with_streaming_response.run_shield(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            shield_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            safety = await response.parse()
            assert_matches_type(RunShieldResponse, safety, path=["response"])

        assert cast(Any, response.is_closed) is True
