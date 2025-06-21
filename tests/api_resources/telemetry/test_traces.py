# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.telemetry import Span, Trace, TraceCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        trace = client.telemetry.traces.create()
        assert_matches_type(TraceCreateResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        trace = client.telemetry.traces.create(
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
        assert_matches_type(TraceCreateResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.telemetry.traces.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(TraceCreateResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.telemetry.traces.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(TraceCreateResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_span(self, client: LlamaStackClient) -> None:
        trace = client.telemetry.traces.retrieve_span(
            span_id="span_id",
            trace_id="trace_id",
        )
        assert_matches_type(Span, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_span(self, client: LlamaStackClient) -> None:
        response = client.telemetry.traces.with_raw_response.retrieve_span(
            span_id="span_id",
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(Span, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_span(self, client: LlamaStackClient) -> None:
        with client.telemetry.traces.with_streaming_response.retrieve_span(
            span_id="span_id",
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(Span, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_span(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.telemetry.traces.with_raw_response.retrieve_span(
                span_id="span_id",
                trace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            client.telemetry.traces.with_raw_response.retrieve_span(
                span_id="",
                trace_id="trace_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_trace(self, client: LlamaStackClient) -> None:
        trace = client.telemetry.traces.retrieve_trace(
            "trace_id",
        )
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_trace(self, client: LlamaStackClient) -> None:
        response = client.telemetry.traces.with_raw_response.retrieve_trace(
            "trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_trace(self, client: LlamaStackClient) -> None:
        with client.telemetry.traces.with_streaming_response.retrieve_trace(
            "trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(Trace, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_trace(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.telemetry.traces.with_raw_response.retrieve_trace(
                "",
            )


class TestAsyncTraces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        trace = await async_client.telemetry.traces.create()
        assert_matches_type(TraceCreateResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        trace = await async_client.telemetry.traces.create(
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
        assert_matches_type(TraceCreateResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.traces.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(TraceCreateResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.traces.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(TraceCreateResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_span(self, async_client: AsyncLlamaStackClient) -> None:
        trace = await async_client.telemetry.traces.retrieve_span(
            span_id="span_id",
            trace_id="trace_id",
        )
        assert_matches_type(Span, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_span(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.traces.with_raw_response.retrieve_span(
            span_id="span_id",
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(Span, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_span(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.traces.with_streaming_response.retrieve_span(
            span_id="span_id",
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(Span, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_span(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.telemetry.traces.with_raw_response.retrieve_span(
                span_id="span_id",
                trace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            await async_client.telemetry.traces.with_raw_response.retrieve_span(
                span_id="",
                trace_id="trace_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_trace(self, async_client: AsyncLlamaStackClient) -> None:
        trace = await async_client.telemetry.traces.retrieve_trace(
            "trace_id",
        )
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_trace(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.traces.with_raw_response.retrieve_trace(
            "trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_trace(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.traces.with_streaming_response.retrieve_trace(
            "trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(Trace, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_trace(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.telemetry.traces.with_raw_response.retrieve_trace(
                "",
            )
