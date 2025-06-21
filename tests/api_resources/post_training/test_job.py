# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.post_training import (
    JobRetrieveStatusResponse,
    JobRetrieveArtifactsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.cancel(
            job_uuid="job_uuid",
        )
        assert job is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: LlamaStackClient) -> None:
        response = client.post_training.job.with_raw_response.cancel(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: LlamaStackClient) -> None:
        with client.post_training.job.with_streaming_response.cancel(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_artifacts(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.retrieve_artifacts(
            job_uuid="job_uuid",
        )
        assert_matches_type(JobRetrieveArtifactsResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_artifacts(self, client: LlamaStackClient) -> None:
        response = client.post_training.job.with_raw_response.retrieve_artifacts(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobRetrieveArtifactsResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_artifacts(self, client: LlamaStackClient) -> None:
        with client.post_training.job.with_streaming_response.retrieve_artifacts(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobRetrieveArtifactsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_status(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.retrieve_status(
            job_uuid="job_uuid",
        )
        assert_matches_type(JobRetrieveStatusResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_status(self, client: LlamaStackClient) -> None:
        response = client.post_training.job.with_raw_response.retrieve_status(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobRetrieveStatusResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_status(self, client: LlamaStackClient) -> None:
        with client.post_training.job.with_streaming_response.retrieve_status(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobRetrieveStatusResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJob:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.cancel(
            job_uuid="job_uuid",
        )
        assert job is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.job.with_raw_response.cancel(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.job.with_streaming_response.cancel(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_artifacts(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.retrieve_artifacts(
            job_uuid="job_uuid",
        )
        assert_matches_type(JobRetrieveArtifactsResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_artifacts(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.job.with_raw_response.retrieve_artifacts(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobRetrieveArtifactsResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_artifacts(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.job.with_streaming_response.retrieve_artifacts(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobRetrieveArtifactsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.retrieve_status(
            job_uuid="job_uuid",
        )
        assert_matches_type(JobRetrieveStatusResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.job.with_raw_response.retrieve_status(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobRetrieveStatusResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.job.with_streaming_response.retrieve_status(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobRetrieveStatusResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True
