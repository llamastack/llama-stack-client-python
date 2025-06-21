# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.eval import EvaluateResponse
from llama_stack_client.types.eval.benchmarks import Job

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        job = client.eval.benchmarks.jobs.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.jobs.with_raw_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.jobs.with_streaming_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.eval.benchmarks.jobs.with_raw_response.retrieve(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.eval.benchmarks.jobs.with_raw_response.retrieve(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: LlamaStackClient) -> None:
        job = client.eval.benchmarks.jobs.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert job is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.jobs.with_raw_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.jobs.with_streaming_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.eval.benchmarks.jobs.with_raw_response.cancel(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.eval.benchmarks.jobs.with_raw_response.cancel(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_result(self, client: LlamaStackClient) -> None:
        job = client.eval.benchmarks.jobs.result(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_result(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.jobs.with_raw_response.result(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_result(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.jobs.with_streaming_response.result(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(EvaluateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_result(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.eval.benchmarks.jobs.with_raw_response.result(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.eval.benchmarks.jobs.with_raw_response.result(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: LlamaStackClient) -> None:
        job = client.eval.benchmarks.jobs.run(
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
        )
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.eval.benchmarks.jobs.run(
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
        )
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: LlamaStackClient) -> None:
        response = client.eval.benchmarks.jobs.with_raw_response.run(
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
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: LlamaStackClient) -> None:
        with client.eval.benchmarks.jobs.with_streaming_response.run(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.eval.benchmarks.jobs.with_raw_response.run(
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
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.eval.benchmarks.jobs.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.jobs.with_raw_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.jobs.with_streaming_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.eval.benchmarks.jobs.with_raw_response.retrieve(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.eval.benchmarks.jobs.with_raw_response.retrieve(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.eval.benchmarks.jobs.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert job is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.jobs.with_raw_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.jobs.with_streaming_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.eval.benchmarks.jobs.with_raw_response.cancel(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.eval.benchmarks.jobs.with_raw_response.cancel(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_result(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.eval.benchmarks.jobs.result(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_result(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.jobs.with_raw_response.result(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_result(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.jobs.with_streaming_response.result(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(EvaluateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_result(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.eval.benchmarks.jobs.with_raw_response.result(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.eval.benchmarks.jobs.with_raw_response.result(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.eval.benchmarks.jobs.run(
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
        )
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.eval.benchmarks.jobs.run(
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
        )
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval.benchmarks.jobs.with_raw_response.run(
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
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Job, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval.benchmarks.jobs.with_streaming_response.run(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.eval.benchmarks.jobs.with_raw_response.run(
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
            )
