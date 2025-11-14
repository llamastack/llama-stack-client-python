# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import scoring_score_params, scoring_score_batch_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.scoring_score_response import ScoringScoreResponse
from ..types.scoring_score_batch_response import ScoringScoreBatchResponse

__all__ = ["ScoringResource", "AsyncScoringResource"]


class ScoringResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ScoringResourceWithStreamingResponse(self)

    def score(
        self,
        *,
        input_rows: Iterable[Dict[str, object]],
        scoring_functions: Dict[str, Optional[scoring_score_params.ScoringFunctions]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringScoreResponse:
        """
        Score a list of rows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/scoring/score",
            body=maybe_transform(
                {
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                scoring_score_params.ScoringScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringScoreResponse,
        )

    def score_batch(
        self,
        *,
        dataset_id: str,
        scoring_functions: Dict[str, Optional[scoring_score_batch_params.ScoringFunctions]],
        save_results_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringScoreBatchResponse:
        """
        Score a batch of rows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/scoring/score-batch",
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                    "save_results_dataset": save_results_dataset,
                },
                scoring_score_batch_params.ScoringScoreBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringScoreBatchResponse,
        )


class AsyncScoringResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncScoringResourceWithStreamingResponse(self)

    async def score(
        self,
        *,
        input_rows: Iterable[Dict[str, object]],
        scoring_functions: Dict[str, Optional[scoring_score_params.ScoringFunctions]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringScoreResponse:
        """
        Score a list of rows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/scoring/score",
            body=await async_maybe_transform(
                {
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                scoring_score_params.ScoringScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringScoreResponse,
        )

    async def score_batch(
        self,
        *,
        dataset_id: str,
        scoring_functions: Dict[str, Optional[scoring_score_batch_params.ScoringFunctions]],
        save_results_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringScoreBatchResponse:
        """
        Score a batch of rows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/scoring/score-batch",
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                    "save_results_dataset": save_results_dataset,
                },
                scoring_score_batch_params.ScoringScoreBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringScoreBatchResponse,
        )


class ScoringResourceWithRawResponse:
    def __init__(self, scoring: ScoringResource) -> None:
        self._scoring = scoring

        self.score = to_raw_response_wrapper(
            scoring.score,
        )
        self.score_batch = to_raw_response_wrapper(
            scoring.score_batch,
        )


class AsyncScoringResourceWithRawResponse:
    def __init__(self, scoring: AsyncScoringResource) -> None:
        self._scoring = scoring

        self.score = async_to_raw_response_wrapper(
            scoring.score,
        )
        self.score_batch = async_to_raw_response_wrapper(
            scoring.score_batch,
        )


class ScoringResourceWithStreamingResponse:
    def __init__(self, scoring: ScoringResource) -> None:
        self._scoring = scoring

        self.score = to_streamed_response_wrapper(
            scoring.score,
        )
        self.score_batch = to_streamed_response_wrapper(
            scoring.score_batch,
        )


class AsyncScoringResourceWithStreamingResponse:
    def __init__(self, scoring: AsyncScoringResource) -> None:
        self._scoring = scoring

        self.score = async_to_streamed_response_wrapper(
            scoring.score,
        )
        self.score_batch = async_to_streamed_response_wrapper(
            scoring.score_batch,
        )
