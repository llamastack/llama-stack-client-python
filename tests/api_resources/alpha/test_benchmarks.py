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
from llama_stack_client.types.alpha import Benchmark, BenchmarkListResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBenchmarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        benchmark = client.alpha.benchmarks.retrieve(
            "benchmark_id",
        )
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.alpha.benchmarks.with_raw_response.retrieve(
            "benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.alpha.benchmarks.with_streaming_response.retrieve(
            "benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(Benchmark, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.benchmarks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        benchmark = client.alpha.benchmarks.list()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.alpha.benchmarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.alpha.benchmarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            benchmark = client.alpha.benchmarks.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
            )

        assert benchmark is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            benchmark = client.alpha.benchmarks.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
                metadata={"foo": "bar"},
                provider_benchmark_id="provider_benchmark_id",
                provider_id="provider_id",
            )

        assert benchmark is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.alpha.benchmarks.with_raw_response.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert benchmark is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.alpha.benchmarks.with_streaming_response.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                benchmark = response.parse()
                assert benchmark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            benchmark = client.alpha.benchmarks.unregister(
                "benchmark_id",
            )

        assert benchmark is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.alpha.benchmarks.with_raw_response.unregister(
                "benchmark_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert benchmark is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.alpha.benchmarks.with_streaming_response.unregister(
                "benchmark_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                benchmark = response.parse()
                assert benchmark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
                client.alpha.benchmarks.with_raw_response.unregister(
                    "",
                )


class TestAsyncBenchmarks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.alpha.benchmarks.retrieve(
            "benchmark_id",
        )
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.benchmarks.with_raw_response.retrieve(
            "benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.benchmarks.with_streaming_response.retrieve(
            "benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(Benchmark, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.benchmarks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.alpha.benchmarks.list()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.benchmarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.benchmarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            benchmark = await async_client.alpha.benchmarks.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
            )

        assert benchmark is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            benchmark = await async_client.alpha.benchmarks.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
                metadata={"foo": "bar"},
                provider_benchmark_id="provider_benchmark_id",
                provider_id="provider_id",
            )

        assert benchmark is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.alpha.benchmarks.with_raw_response.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert benchmark is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.alpha.benchmarks.with_streaming_response.register(
                benchmark_id="benchmark_id",
                dataset_id="dataset_id",
                scoring_functions=["string"],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                benchmark = await response.parse()
                assert benchmark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            benchmark = await async_client.alpha.benchmarks.unregister(
                "benchmark_id",
            )

        assert benchmark is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.alpha.benchmarks.with_raw_response.unregister(
                "benchmark_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert benchmark is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.alpha.benchmarks.with_streaming_response.unregister(
                "benchmark_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                benchmark = await response.parse()
                assert benchmark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
                await async_client.alpha.benchmarks.with_raw_response.unregister(
                    "",
                )
