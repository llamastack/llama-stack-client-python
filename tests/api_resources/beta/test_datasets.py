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
from llama_stack_client.types.beta import (
    DatasetListResponse,
    DatasetIterrowsResponse,
    DatasetRegisterResponse,
    DatasetRetrieveResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        dataset = client.beta.datasets.retrieve(
            "dataset_id",
        )
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.beta.datasets.with_raw_response.retrieve(
            "dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.beta.datasets.with_streaming_response.retrieve(
            "dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.beta.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        dataset = client.beta.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.beta.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.beta.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_appendrows(self, client: LlamaStackClient) -> None:
        dataset = client.beta.datasets.appendrows(
            dataset_id="dataset_id",
            rows=[{"foo": "bar"}],
        )
        assert dataset is None

    @parametrize
    def test_raw_response_appendrows(self, client: LlamaStackClient) -> None:
        response = client.beta.datasets.with_raw_response.appendrows(
            dataset_id="dataset_id",
            rows=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_appendrows(self, client: LlamaStackClient) -> None:
        with client.beta.datasets.with_streaming_response.appendrows(
            dataset_id="dataset_id",
            rows=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_appendrows(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.beta.datasets.with_raw_response.appendrows(
                dataset_id="",
                rows=[{"foo": "bar"}],
            )

    @parametrize
    def test_method_iterrows(self, client: LlamaStackClient) -> None:
        dataset = client.beta.datasets.iterrows(
            dataset_id="dataset_id",
        )
        assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

    @parametrize
    def test_method_iterrows_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.beta.datasets.iterrows(
            dataset_id="dataset_id",
            limit=0,
            start_index=0,
        )
        assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_iterrows(self, client: LlamaStackClient) -> None:
        response = client.beta.datasets.with_raw_response.iterrows(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_iterrows(self, client: LlamaStackClient) -> None:
        with client.beta.datasets.with_streaming_response.iterrows(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_iterrows(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.beta.datasets.with_raw_response.iterrows(
                dataset_id="",
            )

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            dataset = client.beta.datasets.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
            )

        assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            dataset = client.beta.datasets.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
                dataset_id="dataset_id",
                metadata={"foo": "bar"},
            )

        assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.beta.datasets.with_raw_response.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.beta.datasets.with_streaming_response.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                dataset = response.parse()
                assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            dataset = client.beta.datasets.unregister(
                "dataset_id",
            )

        assert dataset is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.beta.datasets.with_raw_response.unregister(
                "dataset_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.beta.datasets.with_streaming_response.unregister(
                "dataset_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                dataset = response.parse()
                assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unregister(self, client: LlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
                client.beta.datasets.with_raw_response.unregister(
                    "",
                )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.beta.datasets.retrieve(
            "dataset_id",
        )
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.beta.datasets.with_raw_response.retrieve(
            "dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.beta.datasets.with_streaming_response.retrieve(
            "dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.beta.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.beta.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.beta.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.beta.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_appendrows(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.beta.datasets.appendrows(
            dataset_id="dataset_id",
            rows=[{"foo": "bar"}],
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_appendrows(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.beta.datasets.with_raw_response.appendrows(
            dataset_id="dataset_id",
            rows=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_appendrows(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.beta.datasets.with_streaming_response.appendrows(
            dataset_id="dataset_id",
            rows=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_appendrows(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.beta.datasets.with_raw_response.appendrows(
                dataset_id="",
                rows=[{"foo": "bar"}],
            )

    @parametrize
    async def test_method_iterrows(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.beta.datasets.iterrows(
            dataset_id="dataset_id",
        )
        assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

    @parametrize
    async def test_method_iterrows_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.beta.datasets.iterrows(
            dataset_id="dataset_id",
            limit=0,
            start_index=0,
        )
        assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_iterrows(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.beta.datasets.with_raw_response.iterrows(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_iterrows(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.beta.datasets.with_streaming_response.iterrows(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetIterrowsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_iterrows(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.beta.datasets.with_raw_response.iterrows(
                dataset_id="",
            )

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            dataset = await async_client.beta.datasets.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
            )

        assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            dataset = await async_client.beta.datasets.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
                dataset_id="dataset_id",
                metadata={"foo": "bar"},
            )

        assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.beta.datasets.with_raw_response.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.beta.datasets.with_streaming_response.register(
                purpose="post-training/messages",
                source={
                    "uri": "uri",
                    "type": "uri",
                },
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                dataset = await response.parse()
                assert_matches_type(DatasetRegisterResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            dataset = await async_client.beta.datasets.unregister(
                "dataset_id",
            )

        assert dataset is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.beta.datasets.with_raw_response.unregister(
                "dataset_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.beta.datasets.with_streaming_response.unregister(
                "dataset_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                dataset = await response.parse()
                assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
                await async_client.beta.datasets.with_raw_response.unregister(
                    "",
                )
