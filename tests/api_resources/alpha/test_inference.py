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
from llama_stack_client.types.alpha import InferenceRerankResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInference:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_rerank(self, client: LlamaStackClient) -> None:
        inference = client.alpha.inference.rerank(
            items=["string"],
            model="model",
            query="string",
        )
        assert_matches_type(InferenceRerankResponse, inference, path=["response"])

    @parametrize
    def test_method_rerank_with_all_params(self, client: LlamaStackClient) -> None:
        inference = client.alpha.inference.rerank(
            items=["string"],
            model="model",
            query="string",
            max_num_results=0,
        )
        assert_matches_type(InferenceRerankResponse, inference, path=["response"])

    @parametrize
    def test_raw_response_rerank(self, client: LlamaStackClient) -> None:
        response = client.alpha.inference.with_raw_response.rerank(
            items=["string"],
            model="model",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = response.parse()
        assert_matches_type(InferenceRerankResponse, inference, path=["response"])

    @parametrize
    def test_streaming_response_rerank(self, client: LlamaStackClient) -> None:
        with client.alpha.inference.with_streaming_response.rerank(
            items=["string"],
            model="model",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = response.parse()
            assert_matches_type(InferenceRerankResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInference:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_rerank(self, async_client: AsyncLlamaStackClient) -> None:
        inference = await async_client.alpha.inference.rerank(
            items=["string"],
            model="model",
            query="string",
        )
        assert_matches_type(InferenceRerankResponse, inference, path=["response"])

    @parametrize
    async def test_method_rerank_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        inference = await async_client.alpha.inference.rerank(
            items=["string"],
            model="model",
            query="string",
            max_num_results=0,
        )
        assert_matches_type(InferenceRerankResponse, inference, path=["response"])

    @parametrize
    async def test_raw_response_rerank(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.inference.with_raw_response.rerank(
            items=["string"],
            model="model",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = await response.parse()
        assert_matches_type(InferenceRerankResponse, inference, path=["response"])

    @parametrize
    async def test_streaming_response_rerank(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.inference.with_streaming_response.rerank(
            items=["string"],
            model="model",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = await response.parse()
            assert_matches_type(InferenceRerankResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True
