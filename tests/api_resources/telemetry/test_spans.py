# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.telemetry import (
    SpanCreateResponse,
    SpanBuildTreeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        span = client.telemetry.spans.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )
        assert_matches_type(SpanCreateResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        span = client.telemetry.spans.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
            max_depth=0,
        )
        assert_matches_type(SpanCreateResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.telemetry.spans.with_raw_response.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanCreateResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.telemetry.spans.with_streaming_response.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanCreateResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_build_tree(self, client: LlamaStackClient) -> None:
        span = client.telemetry.spans.build_tree(
            span_id="span_id",
        )
        assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_build_tree_with_all_params(self, client: LlamaStackClient) -> None:
        span = client.telemetry.spans.build_tree(
            span_id="span_id",
            attributes_to_return=["string"],
            max_depth=0,
        )
        assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_build_tree(self, client: LlamaStackClient) -> None:
        response = client.telemetry.spans.with_raw_response.build_tree(
            span_id="span_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_build_tree(self, client: LlamaStackClient) -> None:
        with client.telemetry.spans.with_streaming_response.build_tree(
            span_id="span_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_build_tree(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            client.telemetry.spans.with_raw_response.build_tree(
                span_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_export(self, client: LlamaStackClient) -> None:
        span = client.telemetry.spans.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )
        assert span is None

    @pytest.mark.skip()
    @parametrize
    def test_method_export_with_all_params(self, client: LlamaStackClient) -> None:
        span = client.telemetry.spans.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
            max_depth=0,
        )
        assert span is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_export(self, client: LlamaStackClient) -> None:
        response = client.telemetry.spans.with_raw_response.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert span is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_export(self, client: LlamaStackClient) -> None:
        with client.telemetry.spans.with_streaming_response.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert span is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        span = await async_client.telemetry.spans.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )
        assert_matches_type(SpanCreateResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        span = await async_client.telemetry.spans.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
            max_depth=0,
        )
        assert_matches_type(SpanCreateResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.spans.with_raw_response.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanCreateResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.spans.with_streaming_response.create(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanCreateResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_build_tree(self, async_client: AsyncLlamaStackClient) -> None:
        span = await async_client.telemetry.spans.build_tree(
            span_id="span_id",
        )
        assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_build_tree_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        span = await async_client.telemetry.spans.build_tree(
            span_id="span_id",
            attributes_to_return=["string"],
            max_depth=0,
        )
        assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_build_tree(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.spans.with_raw_response.build_tree(
            span_id="span_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_build_tree(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.spans.with_streaming_response.build_tree(
            span_id="span_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanBuildTreeResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_build_tree(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            await async_client.telemetry.spans.with_raw_response.build_tree(
                span_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_export(self, async_client: AsyncLlamaStackClient) -> None:
        span = await async_client.telemetry.spans.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )
        assert span is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        span = await async_client.telemetry.spans.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
            max_depth=0,
        )
        assert span is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.spans.with_raw_response.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert span is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.spans.with_streaming_response.export(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert span is None

        assert cast(Any, response.is_closed) is True
