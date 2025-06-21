# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    ScoringFn,
    ScoringFunctionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScoringFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
        )
        assert scoring_function is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
            params={
                "aggregation_functions": ["average"],
                "judge_model": "judge_model",
                "judge_score_regexes": ["string"],
                "type": "llm_as_judge",
                "prompt_template": "prompt_template",
            },
            provider_id="provider_id",
            provider_scoring_fn_id="provider_scoring_fn_id",
        )
        assert scoring_function is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.scoring_functions.with_raw_response.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = response.parse()
        assert scoring_function is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.scoring_functions.with_streaming_response.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = response.parse()
            assert scoring_function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.retrieve(
            "scoring_fn_id",
        )
        assert_matches_type(ScoringFn, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.scoring_functions.with_raw_response.retrieve(
            "scoring_fn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = response.parse()
        assert_matches_type(ScoringFn, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.scoring_functions.with_streaming_response.retrieve(
            "scoring_fn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = response.parse()
            assert_matches_type(ScoringFn, scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scoring_fn_id` but received ''"):
            client.scoring_functions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.list()
        assert_matches_type(ScoringFunctionListResponse, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.scoring_functions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = response.parse()
        assert_matches_type(ScoringFunctionListResponse, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.scoring_functions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = response.parse()
            assert_matches_type(ScoringFunctionListResponse, scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScoringFunctions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
        )
        assert scoring_function is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
            params={
                "aggregation_functions": ["average"],
                "judge_model": "judge_model",
                "judge_score_regexes": ["string"],
                "type": "llm_as_judge",
                "prompt_template": "prompt_template",
            },
            provider_id="provider_id",
            provider_scoring_fn_id="provider_scoring_fn_id",
        )
        assert scoring_function is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring_functions.with_raw_response.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = await response.parse()
        assert scoring_function is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring_functions.with_streaming_response.create(
            description="description",
            return_type={"type": "string"},
            scoring_fn_id="scoring_fn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = await response.parse()
            assert scoring_function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.retrieve(
            "scoring_fn_id",
        )
        assert_matches_type(ScoringFn, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring_functions.with_raw_response.retrieve(
            "scoring_fn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = await response.parse()
        assert_matches_type(ScoringFn, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring_functions.with_streaming_response.retrieve(
            "scoring_fn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = await response.parse()
            assert_matches_type(ScoringFn, scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scoring_fn_id` but received ''"):
            await async_client.scoring_functions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.list()
        assert_matches_type(ScoringFunctionListResponse, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring_functions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = await response.parse()
        assert_matches_type(ScoringFunctionListResponse, scoring_function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring_functions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = await response.parse()
            assert_matches_type(ScoringFunctionListResponse, scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True
