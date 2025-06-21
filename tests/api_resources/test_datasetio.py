# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    DatasetioIterateRowsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasetio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_append_rows(self, client: LlamaStackClient) -> None:
        datasetio = client.datasetio.append_rows(
            dataset_id="dataset_id",
            rows=[{"foo": True}],
        )
        assert datasetio is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_append_rows(self, client: LlamaStackClient) -> None:
        response = client.datasetio.with_raw_response.append_rows(
            dataset_id="dataset_id",
            rows=[{"foo": True}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasetio = response.parse()
        assert datasetio is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_append_rows(self, client: LlamaStackClient) -> None:
        with client.datasetio.with_streaming_response.append_rows(
            dataset_id="dataset_id",
            rows=[{"foo": True}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasetio = response.parse()
            assert datasetio is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_append_rows(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasetio.with_raw_response.append_rows(
                dataset_id="",
                rows=[{"foo": True}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_iterate_rows(self, client: LlamaStackClient) -> None:
        datasetio = client.datasetio.iterate_rows(
            dataset_id="dataset_id",
        )
        assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_iterate_rows_with_all_params(self, client: LlamaStackClient) -> None:
        datasetio = client.datasetio.iterate_rows(
            dataset_id="dataset_id",
            limit=0,
            start_index=0,
        )
        assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_iterate_rows(self, client: LlamaStackClient) -> None:
        response = client.datasetio.with_raw_response.iterate_rows(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasetio = response.parse()
        assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_iterate_rows(self, client: LlamaStackClient) -> None:
        with client.datasetio.with_streaming_response.iterate_rows(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasetio = response.parse()
            assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_iterate_rows(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasetio.with_raw_response.iterate_rows(
                dataset_id="",
            )


class TestAsyncDatasetio:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_append_rows(self, async_client: AsyncLlamaStackClient) -> None:
        datasetio = await async_client.datasetio.append_rows(
            dataset_id="dataset_id",
            rows=[{"foo": True}],
        )
        assert datasetio is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_append_rows(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasetio.with_raw_response.append_rows(
            dataset_id="dataset_id",
            rows=[{"foo": True}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasetio = await response.parse()
        assert datasetio is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_append_rows(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasetio.with_streaming_response.append_rows(
            dataset_id="dataset_id",
            rows=[{"foo": True}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasetio = await response.parse()
            assert datasetio is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_append_rows(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasetio.with_raw_response.append_rows(
                dataset_id="",
                rows=[{"foo": True}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_iterate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        datasetio = await async_client.datasetio.iterate_rows(
            dataset_id="dataset_id",
        )
        assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_iterate_rows_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        datasetio = await async_client.datasetio.iterate_rows(
            dataset_id="dataset_id",
            limit=0,
            start_index=0,
        )
        assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_iterate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasetio.with_raw_response.iterate_rows(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasetio = await response.parse()
        assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_iterate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasetio.with_streaming_response.iterate_rows(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasetio = await response.parse()
            assert_matches_type(DatasetioIterateRowsResponse, datasetio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_iterate_rows(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasetio.with_raw_response.iterate_rows(
                dataset_id="",
            )
