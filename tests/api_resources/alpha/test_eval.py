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
from llama_stack_client.types.alpha import (
    Job,
    EvaluateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEval:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_evaluate_rows(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    def test_method_evaluate_rows_with_all_params(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    def test_raw_response_evaluate_rows(self, client: LlamaStackClient) -> None:
        response = client.alpha.eval.with_raw_response.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    def test_streaming_response_evaluate_rows(self, client: LlamaStackClient) -> None:
        with client.alpha.eval.with_streaming_response.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvaluateResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_evaluate_rows(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.eval.with_raw_response.evaluate_rows(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
                input_rows=[{"foo": "bar"}],
                scoring_functions=["string"],
            )

    @parametrize
    def test_method_evaluate_rows_alpha(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    def test_method_evaluate_rows_alpha_with_all_params(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    def test_raw_response_evaluate_rows_alpha(self, client: LlamaStackClient) -> None:
        response = client.alpha.eval.with_raw_response.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    def test_streaming_response_evaluate_rows_alpha(self, client: LlamaStackClient) -> None:
        with client.alpha.eval.with_streaming_response.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvaluateResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_evaluate_rows_alpha(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.eval.with_raw_response.evaluate_rows_alpha(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
                input_rows=[{"foo": "bar"}],
                scoring_functions=["string"],
            )

    @parametrize
    def test_method_run_eval(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    def test_method_run_eval_with_all_params(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    def test_raw_response_run_eval(self, client: LlamaStackClient) -> None:
        response = client.alpha.eval.with_raw_response.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    def test_streaming_response_run_eval(self, client: LlamaStackClient) -> None:
        with client.alpha.eval.with_streaming_response.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(Job, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_eval(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.eval.with_raw_response.run_eval(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
            )

    @parametrize
    def test_method_run_eval_alpha(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    def test_method_run_eval_alpha_with_all_params(self, client: LlamaStackClient) -> None:
        eval = client.alpha.eval.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    def test_raw_response_run_eval_alpha(self, client: LlamaStackClient) -> None:
        response = client.alpha.eval.with_raw_response.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    def test_streaming_response_run_eval_alpha(self, client: LlamaStackClient) -> None:
        with client.alpha.eval.with_streaming_response.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(Job, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_eval_alpha(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.eval.with_raw_response.run_eval_alpha(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
            )


class TestAsyncEval:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_evaluate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    async def test_method_evaluate_rows_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    async def test_raw_response_evaluate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.eval.with_raw_response.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.eval.with_streaming_response.evaluate_rows(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvaluateResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_evaluate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.eval.with_raw_response.evaluate_rows(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
                input_rows=[{"foo": "bar"}],
                scoring_functions=["string"],
            )

    @parametrize
    async def test_method_evaluate_rows_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    async def test_method_evaluate_rows_alpha_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    async def test_raw_response_evaluate_rows_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.eval.with_raw_response.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvaluateResponse, eval, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate_rows_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.eval.with_streaming_response.evaluate_rows_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
            input_rows=[{"foo": "bar"}],
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvaluateResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_evaluate_rows_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.eval.with_raw_response.evaluate_rows_alpha(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
                input_rows=[{"foo": "bar"}],
                scoring_functions=["string"],
            )

    @parametrize
    async def test_method_run_eval(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    async def test_method_run_eval_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    async def test_raw_response_run_eval(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.eval.with_raw_response.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    async def test_streaming_response_run_eval(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.eval.with_streaming_response.run_eval(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(Job, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_eval(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.eval.with_raw_response.run_eval(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
            )

    @parametrize
    async def test_method_run_eval_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    async def test_method_run_eval_alpha_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        eval = await async_client.alpha.eval.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {
                        "max_tokens": 0,
                        "repetition_penalty": 0,
                        "stop": ["string"],
                        "strategy": {"type": "greedy"},
                    },
                    "system_message": {
                        "content": "string",
                        "role": "system",
                    },
                    "type": "model",
                },
                "num_examples": 0,
                "scoring_params": {
                    "foo": {
                        "judge_model": "judge_model",
                        "aggregation_functions": ["average"],
                        "judge_score_regexes": ["string"],
                        "prompt_template": "prompt_template",
                        "type": "llm_as_judge",
                    }
                },
            },
        )
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    async def test_raw_response_run_eval_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.eval.with_raw_response.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(Job, eval, path=["response"])

    @parametrize
    async def test_streaming_response_run_eval_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.eval.with_streaming_response.run_eval_alpha(
            benchmark_id="benchmark_id",
            benchmark_config={
                "eval_candidate": {
                    "model": "model",
                    "sampling_params": {},
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(Job, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_eval_alpha(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.eval.with_raw_response.run_eval_alpha(
                benchmark_id="",
                benchmark_config={
                    "eval_candidate": {
                        "model": "model",
                        "sampling_params": {},
                    }
                },
            )
