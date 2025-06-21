# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.eval import (
    Benchmark,
    EvaluateResponse,
    BenchmarkListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBenchmarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        benchmark = client.eval.benchmarks.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
        )
        assert benchmark is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        benchmark = client.eval.benchmarks.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
            metadata={"foo": True},
            provider_benchmark_id="provider_benchmark_id",
            provider_id="provider_id",
        )
        assert benchmark is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.with_raw_response.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert benchmark is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.with_streaming_response.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert benchmark is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        benchmark = client.eval.benchmarks.retrieve(
            "benchmark_id",
        )
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.with_raw_response.retrieve(
            "benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.with_streaming_response.retrieve(
            "benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(Benchmark, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.eval.benchmarks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        benchmark = client.eval.benchmarks.list()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_evaluate(self, client: LlamaStackClient) -> None:
        benchmark = client.eval.benchmarks.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {"strategy": {"type": "greedy"}},
                    "type": "model",
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_evaluate_with_all_params(self, client: LlamaStackClient) -> None:
        benchmark = client.eval.benchmarks.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "strategy": {"type": "greedy"},
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                    },
                    "type": "model",
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                        "prompt_template": "prompt_template",
                    }
                },
                "num_examples": 0,
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_evaluate(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.with_raw_response.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {"strategy": {"type": "greedy"}},
                    "type": "model",
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(EvaluateResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_evaluate(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.with_streaming_response.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {"strategy": {"type": "greedy"}},
                    "type": "model",
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(EvaluateResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_evaluate(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.eval.benchmarks.with_raw_response.evaluate(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {"strategy": {"type": "greedy"}},
                        "type": "model",
                    },
                    "scoring_params": {
                        "foo": {
                            "aggregation_functions": ["average"],
                            "judge_model": "judge_model",
                            "judge_score_regexes": ["string"],
                            "type": "llm_as_judge",
                        }
                    },
                },
                input_rows=[{"foo": True}],
                scoring_functions=["string"],
            )


class TestAsyncBenchmarks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.eval.benchmarks.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
        )
        assert benchmark is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.eval.benchmarks.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
            metadata={"foo": True},
            provider_benchmark_id="provider_benchmark_id",
            provider_id="provider_id",
        )
        assert benchmark is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.with_raw_response.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert benchmark is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.with_streaming_response.create(
            benchmark_id="benchmark_id",
            dataset_id="dataset_id",
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert benchmark is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.eval.benchmarks.retrieve(
            "benchmark_id",
        )
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.with_raw_response.retrieve(
            "benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(Benchmark, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.with_streaming_response.retrieve(
            "benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(Benchmark, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.eval.benchmarks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.eval.benchmarks.list()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkListResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_evaluate(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.eval.benchmarks.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {"strategy": {"type": "greedy"}},
                    "type": "model",
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        benchmark = await async_client.eval.benchmarks.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "strategy": {"type": "greedy"},
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                    },
                    "type": "model",
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                        "prompt_template": "prompt_template",
                    }
                },
                "num_examples": 0,
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.with_raw_response.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {"strategy": {"type": "greedy"}},
                    "type": "model",
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(EvaluateResponse, benchmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.with_streaming_response.evaluate(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {"strategy": {"type": "greedy"}},
                    "type": "model",
                },
                "scoring_params": {
                    "foo": {
                        "aggregation_functions": ["average"],
                        "judge_model": "judge_model",
                        "judge_score_regexes": ["string"],
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": True}],
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(EvaluateResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_evaluate(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.eval.benchmarks.with_raw_response.evaluate(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {"strategy": {"type": "greedy"}},
                        "type": "model",
                    },
                    "scoring_params": {
                        "foo": {
                            "aggregation_functions": ["average"],
                            "judge_model": "judge_model",
                            "judge_score_regexes": ["string"],
                            "type": "llm_as_judge",
                        }
                    },
                },
                input_rows=[{"foo": True}],
                scoring_functions=["string"],
            )
