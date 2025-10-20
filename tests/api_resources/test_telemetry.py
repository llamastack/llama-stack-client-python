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
    Trace,
    TelemetryGetSpanResponse,
    TelemetryQuerySpansResponse,
    TelemetryGetSpanTreeResponse,
    TelemetryQueryTracesResponse,
    TelemetryQueryMetricsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelemetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_span(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_span(
            span_id="span_id",
            trace_id="trace_id",
        )
        assert_matches_type(TelemetryGetSpanResponse, telemetry, path=["response"])

    @parametrize
    def test_raw_response_get_span(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.get_span(
            span_id="span_id",
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(TelemetryGetSpanResponse, telemetry, path=["response"])

    @parametrize
    def test_streaming_response_get_span(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.get_span(
            span_id="span_id",
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(TelemetryGetSpanResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_span(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.telemetry.with_raw_response.get_span(
                span_id="span_id",
                trace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            client.telemetry.with_raw_response.get_span(
                span_id="",
                trace_id="trace_id",
            )

    @parametrize
    def test_method_get_span_tree(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_span_tree(
            span_id="span_id",
        )
        assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

    @parametrize
    def test_method_get_span_tree_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_span_tree(
            span_id="span_id",
            attributes_to_return=["string"],
            max_depth=0,
        )
        assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

    @parametrize
    def test_raw_response_get_span_tree(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.get_span_tree(
            span_id="span_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

    @parametrize
    def test_streaming_response_get_span_tree(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.get_span_tree(
            span_id="span_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_span_tree(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            client.telemetry.with_raw_response.get_span_tree(
                span_id="",
            )

    @parametrize
    def test_method_get_trace(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_trace(
            "trace_id",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    def test_raw_response_get_trace(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.get_trace(
            "trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    def test_streaming_response_get_trace(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.get_trace(
            "trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(Trace, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_trace(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.telemetry.with_raw_response.get_trace(
                "",
            )

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_method_query_metrics(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
        )
        assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_method_query_metrics_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
            end_time=0,
            granularity="granularity",
            label_matchers=[
                {
                    "name": "name",
                    "operator": "=",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_raw_response_query_metrics(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_streaming_response_query_metrics(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_path_params_query_metrics(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_name` but received ''"):
            client.telemetry.with_raw_response.query_metrics(
                metric_name="",
                query_type="range",
                start_time=0,
            )

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_method_query_spans(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_method_query_spans_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_spans(
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
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_raw_response_query_spans(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.query_spans(
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
        telemetry = response.parse()
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_streaming_response_query_spans(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.query_spans(
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

            telemetry = response.parse()
            assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_method_query_traces(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_traces()
        assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_method_query_traces_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_traces(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            limit=0,
            offset=0,
            order_by=["string"],
        )
        assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_raw_response_query_traces(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.query_traces()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    def test_streaming_response_query_traces(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.query_traces() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_save_spans_to_dataset(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.save_spans_to_dataset(
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
        assert telemetry is None

    @parametrize
    def test_method_save_spans_to_dataset_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.save_spans_to_dataset(
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
        assert telemetry is None

    @parametrize
    def test_raw_response_save_spans_to_dataset(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.save_spans_to_dataset(
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
        telemetry = response.parse()
        assert telemetry is None

    @parametrize
    def test_streaming_response_save_spans_to_dataset(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.save_spans_to_dataset(
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

            telemetry = response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTelemetry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_span(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_span(
            span_id="span_id",
            trace_id="trace_id",
        )
        assert_matches_type(TelemetryGetSpanResponse, telemetry, path=["response"])

    @parametrize
    async def test_raw_response_get_span(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.get_span(
            span_id="span_id",
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(TelemetryGetSpanResponse, telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_get_span(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.get_span(
            span_id="span_id",
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(TelemetryGetSpanResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_span(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.telemetry.with_raw_response.get_span(
                span_id="span_id",
                trace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            await async_client.telemetry.with_raw_response.get_span(
                span_id="",
                trace_id="trace_id",
            )

    @parametrize
    async def test_method_get_span_tree(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_span_tree(
            span_id="span_id",
        )
        assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

    @parametrize
    async def test_method_get_span_tree_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_span_tree(
            span_id="span_id",
            attributes_to_return=["string"],
            max_depth=0,
        )
        assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

    @parametrize
    async def test_raw_response_get_span_tree(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.get_span_tree(
            span_id="span_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_get_span_tree(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.get_span_tree(
            span_id="span_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(TelemetryGetSpanTreeResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_span_tree(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            await async_client.telemetry.with_raw_response.get_span_tree(
                span_id="",
            )

    @parametrize
    async def test_method_get_trace(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_trace(
            "trace_id",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    async def test_raw_response_get_trace(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.get_trace(
            "trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_get_trace(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.get_trace(
            "trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(Trace, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_trace(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.telemetry.with_raw_response.get_trace(
                "",
            )

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_method_query_metrics(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
        )
        assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_method_query_metrics_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
            end_time=0,
            granularity="granularity",
            label_matchers=[
                {
                    "name": "name",
                    "operator": "=",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_raw_response_query_metrics(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_streaming_response_query_metrics(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.query_metrics(
            metric_name="metric_name",
            query_type="range",
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(TelemetryQueryMetricsResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_path_params_query_metrics(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_name` but received ''"):
            await async_client.telemetry.with_raw_response.query_metrics(
                metric_name="",
                query_type="range",
                start_time=0,
            )

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_method_query_spans(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_method_query_spans_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_spans(
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
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_raw_response_query_spans(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.query_spans(
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
        telemetry = await response.parse()
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_streaming_response_query_spans(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.query_spans(
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

            telemetry = await response.parse()
            assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_method_query_traces(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_traces()
        assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_method_query_traces_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_traces(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            limit=0,
            offset=0,
            order_by=["string"],
        )
        assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_raw_response_query_traces(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.query_traces()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="unsupported query params in java / kotlin")
    @parametrize
    async def test_streaming_response_query_traces(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.query_traces() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(TelemetryQueryTracesResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_save_spans_to_dataset(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.save_spans_to_dataset(
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
        assert telemetry is None

    @parametrize
    async def test_method_save_spans_to_dataset_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.save_spans_to_dataset(
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
        assert telemetry is None

    @parametrize
    async def test_raw_response_save_spans_to_dataset(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.save_spans_to_dataset(
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
        telemetry = await response.parse()
        assert telemetry is None

    @parametrize
    async def test_streaming_response_save_spans_to_dataset(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.save_spans_to_dataset(
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

            telemetry = await response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True
