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
    ResponseObject,
    ResponseListResponse,
    ResponseDeleteResponse,
)
from llama_stack_client.pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: LlamaStackClient) -> None:
        response = client.responses.create(
            input="string",
            model="model",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: LlamaStackClient) -> None:
        response = client.responses.create(
            input="string",
            model="model",
            conversation="conversation",
            include=["web_search_call.action.sources"],
            instructions="instructions",
            max_infer_iters=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {
                    "foo": {
                        "text": "text",
                        "type": "input_text",
                    }
                },
                "version": "version",
            },
            store=True,
            stream=False,
            temperature=0,
            text={
                "format": {
                    "description": "description",
                    "name": "name",
                    "schema": {"foo": "bar"},
                    "strict": True,
                    "type": "text",
                }
            },
            tool_choice="auto",
            tools=[
                {
                    "search_context_size": 'S?oC"high',
                    "type": "web_search",
                }
            ],
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: LlamaStackClient) -> None:
        http_response = client.responses.with_raw_response.create(
            input="string",
            model="model",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: LlamaStackClient) -> None:
        with client.responses.with_streaming_response.create(
            input="string",
            model="model",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: LlamaStackClient) -> None:
        response_stream = client.responses.create(
            input="string",
            model="model",
            stream=True,
        )
        response_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: LlamaStackClient) -> None:
        response_stream = client.responses.create(
            input="string",
            model="model",
            stream=True,
            conversation="conversation",
            include=["web_search_call.action.sources"],
            instructions="instructions",
            max_infer_iters=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {
                    "foo": {
                        "text": "text",
                        "type": "input_text",
                    }
                },
                "version": "version",
            },
            store=True,
            temperature=0,
            text={
                "format": {
                    "description": "description",
                    "name": "name",
                    "schema": {"foo": "bar"},
                    "strict": True,
                    "type": "text",
                }
            },
            tool_choice="auto",
            tools=[
                {
                    "search_context_size": 'S?oC"high',
                    "type": "web_search",
                }
            ],
        )
        response_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: LlamaStackClient) -> None:
        response = client.responses.with_raw_response.create(
            input="string",
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: LlamaStackClient) -> None:
        with client.responses.with_streaming_response.create(
            input="string",
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        response = client.responses.retrieve(
            "response_id",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        http_response = client.responses.with_raw_response.retrieve(
            "response_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.responses.with_streaming_response.retrieve(
            "response_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        response = client.responses.list()
        assert_matches_type(SyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        response = client.responses.list(
            after="after",
            limit=0,
            model="model",
            order="asc",
        )
        assert_matches_type(SyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        http_response = client.responses.with_raw_response.list()

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(SyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.responses.with_streaming_response.list() as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(SyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        response = client.responses.delete(
            "response_id",
        )
        assert_matches_type(ResponseDeleteResponse, response, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        http_response = client.responses.with_raw_response.delete(
            "response_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseDeleteResponse, response, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.responses.with_streaming_response.delete(
            "response_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseDeleteResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.with_raw_response.delete(
                "",
            )


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.responses.create(
            input="string",
            model="model",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.responses.create(
            input="string",
            model="model",
            conversation="conversation",
            include=["web_search_call.action.sources"],
            instructions="instructions",
            max_infer_iters=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {
                    "foo": {
                        "text": "text",
                        "type": "input_text",
                    }
                },
                "version": "version",
            },
            store=True,
            stream=False,
            temperature=0,
            text={
                "format": {
                    "description": "description",
                    "name": "name",
                    "schema": {"foo": "bar"},
                    "strict": True,
                    "type": "text",
                }
            },
            tool_choice="auto",
            tools=[
                {
                    "search_context_size": 'S?oC"high',
                    "type": "web_search",
                }
            ],
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        http_response = await async_client.responses.with_raw_response.create(
            input="string",
            model="model",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="string",
            model="model",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        response_stream = await async_client.responses.create(
            input="string",
            model="model",
            stream=True,
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        response_stream = await async_client.responses.create(
            input="string",
            model="model",
            stream=True,
            conversation="conversation",
            include=["web_search_call.action.sources"],
            instructions="instructions",
            max_infer_iters=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {
                    "foo": {
                        "text": "text",
                        "type": "input_text",
                    }
                },
                "version": "version",
            },
            store=True,
            temperature=0,
            text={
                "format": {
                    "description": "description",
                    "name": "name",
                    "schema": {"foo": "bar"},
                    "strict": True,
                    "type": "text",
                }
            },
            tool_choice="auto",
            tools=[
                {
                    "search_context_size": 'S?oC"high',
                    "type": "web_search",
                }
            ],
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.responses.with_raw_response.create(
            input="string",
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="string",
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.responses.retrieve(
            "response_id",
        )
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        http_response = await async_client.responses.with_raw_response.retrieve(
            "response_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseObject, response, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.responses.with_streaming_response.retrieve(
            "response_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseObject, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.responses.list()
        assert_matches_type(AsyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.responses.list(
            after="after",
            limit=0,
            model="model",
            order="asc",
        )
        assert_matches_type(AsyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        http_response = await async_client.responses.with_raw_response.list()

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(AsyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.responses.with_streaming_response.list() as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(AsyncOpenAICursorPage[ResponseListResponse], response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.responses.delete(
            "response_id",
        )
        assert_matches_type(ResponseDeleteResponse, response, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        http_response = await async_client.responses.with_raw_response.delete(
            "response_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseDeleteResponse, response, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.responses.with_streaming_response.delete(
            "response_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseDeleteResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.with_raw_response.delete(
                "",
            )
