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
    ScoringScoreResponse,
    ScoringScoreBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_score(self, client: LlamaStackClient) -> None:
        scoring = client.scoring.score(
            input_rows=[{"foo": "bar"}],
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )
        assert_matches_type(ScoringScoreResponse, scoring, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: LlamaStackClient) -> None:
        response = client.scoring.with_raw_response.score(
            input_rows=[{"foo": "bar"}],
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring = response.parse()
        assert_matches_type(ScoringScoreResponse, scoring, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: LlamaStackClient) -> None:
        with client.scoring.with_streaming_response.score(
            input_rows=[{"foo": "bar"}],
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring = response.parse()
            assert_matches_type(ScoringScoreResponse, scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_score_batch(self, client: LlamaStackClient) -> None:
        scoring = client.scoring.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )
        assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

    @parametrize
    def test_method_score_batch_with_all_params(self, client: LlamaStackClient) -> None:
        scoring = client.scoring.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "aggregation_functions": ["average"],
                    "judge_score_regexes": ["string"],
                    "prompt_template": "prompt_template",
                    "type": "llm_as_judge",
                }
            },
            save_results_dataset=True,
        )
        assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

    @parametrize
    def test_raw_response_score_batch(self, client: LlamaStackClient) -> None:
        response = client.scoring.with_raw_response.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring = response.parse()
        assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

    @parametrize
    def test_streaming_response_score_batch(self, client: LlamaStackClient) -> None:
        with client.scoring.with_streaming_response.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring = response.parse()
            assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScoring:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_score(self, async_client: AsyncLlamaStackClient) -> None:
        scoring = await async_client.scoring.score(
            input_rows=[{"foo": "bar"}],
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )
        assert_matches_type(ScoringScoreResponse, scoring, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring.with_raw_response.score(
            input_rows=[{"foo": "bar"}],
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring = await response.parse()
        assert_matches_type(ScoringScoreResponse, scoring, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring.with_streaming_response.score(
            input_rows=[{"foo": "bar"}],
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring = await response.parse()
            assert_matches_type(ScoringScoreResponse, scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_score_batch(self, async_client: AsyncLlamaStackClient) -> None:
        scoring = await async_client.scoring.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )
        assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

    @parametrize
    async def test_method_score_batch_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        scoring = await async_client.scoring.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "aggregation_functions": ["average"],
                    "judge_score_regexes": ["string"],
                    "prompt_template": "prompt_template",
                    "type": "llm_as_judge",
                }
            },
            save_results_dataset=True,
        )
        assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

    @parametrize
    async def test_raw_response_score_batch(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring.with_raw_response.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring = await response.parse()
        assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

    @parametrize
    async def test_streaming_response_score_batch(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring.with_streaming_response.score_batch(
            dataset_id="dataset_id",
            scoring_functions={
                "foo": {
                    "judge_model": "judge_model",
                    "type": "llm_as_judge",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring = await response.parse()
            assert_matches_type(ScoringScoreBatchResponse, scoring, path=["response"])

        assert cast(Any, response.is_closed) is True
