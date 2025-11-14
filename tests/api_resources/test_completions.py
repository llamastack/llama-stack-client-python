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
from llama_stack_client.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: LlamaStackClient) -> None:
        completion = client.completions.create(
            model="model",
            prompt="string",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: LlamaStackClient) -> None:
        completion = client.completions.create(
            model="model",
            prompt="string",
            best_of=0,
            echo=True,
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            seed=0,
            stop="string",
            stream=False,
            stream_options={"foo": "bar"},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: LlamaStackClient) -> None:
        response = client.completions.with_raw_response.create(
            model="model",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: LlamaStackClient) -> None:
        with client.completions.with_streaming_response.create(
            model="model",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: LlamaStackClient) -> None:
        completion_stream = client.completions.create(
            model="model",
            prompt="string",
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: LlamaStackClient) -> None:
        completion_stream = client.completions.create(
            model="model",
            prompt="string",
            stream=True,
            best_of=0,
            echo=True,
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            seed=0,
            stop="string",
            stream_options={"foo": "bar"},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
        )
        completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: LlamaStackClient) -> None:
        response = client.completions.with_raw_response.create(
            model="model",
            prompt="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: LlamaStackClient) -> None:
        with client.completions.with_streaming_response.create(
            model="model",
            prompt="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        completion = await async_client.completions.create(
            model="model",
            prompt="string",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        completion = await async_client.completions.create(
            model="model",
            prompt="string",
            best_of=0,
            echo=True,
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            seed=0,
            stop="string",
            stream=False,
            stream_options={"foo": "bar"},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="model",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="model",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        completion_stream = await async_client.completions.create(
            model="model",
            prompt="string",
            stream=True,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        completion_stream = await async_client.completions.create(
            model="model",
            prompt="string",
            stream=True,
            best_of=0,
            echo=True,
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            seed=0,
            stop="string",
            stream_options={"foo": "bar"},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="model",
            prompt="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="model",
            prompt="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
