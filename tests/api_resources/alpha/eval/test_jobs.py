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
from llama_stack_client.types.alpha import Job, EvaluateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        job = client.alpha.eval.jobs.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.alpha.eval.jobs.with_raw_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.alpha.eval.jobs.with_streaming_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(EvaluateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.eval.jobs.with_raw_response.retrieve(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.alpha.eval.jobs.with_raw_response.retrieve(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @parametrize
    def test_method_cancel(self, client: LlamaStackClient) -> None:
        job = client.alpha.eval.jobs.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert job is None

    @parametrize
    def test_raw_response_cancel(self, client: LlamaStackClient) -> None:
        response = client.alpha.eval.jobs.with_raw_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @parametrize
    def test_streaming_response_cancel(self, client: LlamaStackClient) -> None:
        with client.alpha.eval.jobs.with_streaming_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.eval.jobs.with_raw_response.cancel(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.alpha.eval.jobs.with_raw_response.cancel(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @parametrize
    def test_method_status(self, client: LlamaStackClient) -> None:
        job = client.alpha.eval.jobs.status(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: LlamaStackClient) -> None:
        response = client.alpha.eval.jobs.with_raw_response.status(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: LlamaStackClient) -> None:
        with client.alpha.eval.jobs.with_streaming_response.status(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            client.alpha.eval.jobs.with_raw_response.status(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.alpha.eval.jobs.with_raw_response.status(
                job_id="",
                benchmark_id="benchmark_id",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.alpha.eval.jobs.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.eval.jobs.with_raw_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.eval.jobs.with_streaming_response.retrieve(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(EvaluateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.eval.jobs.with_raw_response.retrieve(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.alpha.eval.jobs.with_raw_response.retrieve(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.alpha.eval.jobs.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert job is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.eval.jobs.with_raw_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.eval.jobs.with_streaming_response.cancel(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.eval.jobs.with_raw_response.cancel(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.alpha.eval.jobs.with_raw_response.cancel(
                job_id="",
                benchmark_id="benchmark_id",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.alpha.eval.jobs.status(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.eval.jobs.with_raw_response.status(
            job_id="job_id",
            benchmark_id="benchmark_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.eval.jobs.with_streaming_response.status(
            job_id="job_id",
            benchmark_id="benchmark_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benchmark_id` but received ''"):
            await async_client.alpha.eval.jobs.with_raw_response.status(
                job_id="job_id",
                benchmark_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.alpha.eval.jobs.with_raw_response.status(
                job_id="",
                benchmark_id="benchmark_id",
            )
