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
from llama_stack_client.types import ToolGroup, ToolgroupListResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolgroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = client.toolgroups.list()

        assert_matches_type(ToolgroupListResponse, toolgroup, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.toolgroups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert_matches_type(ToolgroupListResponse, toolgroup, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.toolgroups.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = response.parse()
                assert_matches_type(ToolgroupListResponse, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = client.toolgroups.get(
                "toolgroup_id",
            )

        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.toolgroups.with_raw_response.get(
                "toolgroup_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.toolgroups.with_streaming_response.get(
                "toolgroup_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = response.parse()
                assert_matches_type(ToolGroup, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `toolgroup_id` but received ''"):
                client.toolgroups.with_raw_response.get(
                    "",
                )

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = client.toolgroups.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
            )

        assert toolgroup is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = client.toolgroups.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
                args={"foo": "bar"},
                mcp_endpoint={"uri": "uri"},
            )

        assert toolgroup is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.toolgroups.with_raw_response.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert toolgroup is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.toolgroups.with_streaming_response.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = response.parse()
                assert toolgroup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = client.toolgroups.unregister(
                "toolgroup_id",
            )

        assert toolgroup is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.toolgroups.with_raw_response.unregister(
                "toolgroup_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert toolgroup is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.toolgroups.with_streaming_response.unregister(
                "toolgroup_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = response.parse()
                assert toolgroup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `toolgroup_id` but received ''"):
                client.toolgroups.with_raw_response.unregister(
                    "",
                )


class TestAsyncToolgroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = await async_client.toolgroups.list()

        assert_matches_type(ToolgroupListResponse, toolgroup, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.toolgroups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert_matches_type(ToolgroupListResponse, toolgroup, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.toolgroups.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = await response.parse()
                assert_matches_type(ToolgroupListResponse, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = await async_client.toolgroups.get(
                "toolgroup_id",
            )

        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.toolgroups.with_raw_response.get(
                "toolgroup_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.toolgroups.with_streaming_response.get(
                "toolgroup_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = await response.parse()
                assert_matches_type(ToolGroup, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `toolgroup_id` but received ''"):
                await async_client.toolgroups.with_raw_response.get(
                    "",
                )

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = await async_client.toolgroups.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
            )

        assert toolgroup is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = await async_client.toolgroups.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
                args={"foo": "bar"},
                mcp_endpoint={"uri": "uri"},
            )

        assert toolgroup is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.toolgroups.with_raw_response.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert toolgroup is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.toolgroups.with_streaming_response.register(
                provider_id="provider_id",
                toolgroup_id="toolgroup_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = await response.parse()
                assert toolgroup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            toolgroup = await async_client.toolgroups.unregister(
                "toolgroup_id",
            )

        assert toolgroup is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.toolgroups.with_raw_response.unregister(
                "toolgroup_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert toolgroup is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.toolgroups.with_streaming_response.unregister(
                "toolgroup_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                toolgroup = await response.parse()
                assert toolgroup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `toolgroup_id` but received ''"):
                await async_client.toolgroups.with_raw_response.unregister(
                    "",
                )
