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
    ToolInvocationResult,
    ToolRuntimeListToolsResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolRuntime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_invoke_tool(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = client.tool_runtime.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
            )

        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    def test_method_invoke_tool_with_all_params(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = client.tool_runtime.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
                authorization="authorization",
            )

        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    def test_raw_response_invoke_tool(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.tool_runtime.with_raw_response.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = response.parse()
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    def test_streaming_response_invoke_tool(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.tool_runtime.with_streaming_response.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool_runtime = response.parse()
                assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_tools(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = client.tool_runtime.list_tools()

        assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

    @parametrize
    def test_method_list_tools_with_all_params(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = client.tool_runtime.list_tools(
                authorization="authorization",
                mcp_endpoint={"uri": "uri"},
                tool_group_id="tool_group_id",
            )

        assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

    @parametrize
    def test_raw_response_list_tools(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.tool_runtime.with_raw_response.list_tools()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = response.parse()
        assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

    @parametrize
    def test_streaming_response_list_tools(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.tool_runtime.with_streaming_response.list_tools() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool_runtime = response.parse()
                assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncToolRuntime:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_invoke_tool(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = await async_client.tool_runtime.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
            )

        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    async def test_method_invoke_tool_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = await async_client.tool_runtime.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
                authorization="authorization",
            )

        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    async def test_raw_response_invoke_tool(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.tool_runtime.with_raw_response.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = await response.parse()
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    async def test_streaming_response_invoke_tool(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.tool_runtime.with_streaming_response.invoke_tool(
                kwargs={"foo": "bar"},
                tool_name="tool_name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool_runtime = await response.parse()
                assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_tools(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = await async_client.tool_runtime.list_tools()

        assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

    @parametrize
    async def test_method_list_tools_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            tool_runtime = await async_client.tool_runtime.list_tools(
                authorization="authorization",
                mcp_endpoint={"uri": "uri"},
                tool_group_id="tool_group_id",
            )

        assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

    @parametrize
    async def test_raw_response_list_tools(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.tool_runtime.with_raw_response.list_tools()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = await response.parse()
        assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

    @parametrize
    async def test_streaming_response_list_tools(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.tool_runtime.with_streaming_response.list_tools() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool_runtime = await response.parse()
                assert_matches_type(ToolRuntimeListToolsResponse, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True
