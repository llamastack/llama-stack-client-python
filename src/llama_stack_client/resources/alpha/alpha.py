# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .eval.eval import (
    EvalResource,
    AsyncEvalResource,
    EvalResourceWithRawResponse,
    AsyncEvalResourceWithRawResponse,
    EvalResourceWithStreamingResponse,
    AsyncEvalResourceWithStreamingResponse,
)
from .inference import (
    InferenceResource,
    AsyncInferenceResource,
    InferenceResourceWithRawResponse,
    AsyncInferenceResourceWithRawResponse,
    InferenceResourceWithStreamingResponse,
    AsyncInferenceResourceWithStreamingResponse,
)
from .benchmarks import (
    BenchmarksResource,
    AsyncBenchmarksResource,
    BenchmarksResourceWithRawResponse,
    AsyncBenchmarksResourceWithRawResponse,
    BenchmarksResourceWithStreamingResponse,
    AsyncBenchmarksResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .post_training.post_training import (
    PostTrainingResource,
    AsyncPostTrainingResource,
    PostTrainingResourceWithRawResponse,
    AsyncPostTrainingResourceWithRawResponse,
    PostTrainingResourceWithStreamingResponse,
    AsyncPostTrainingResourceWithStreamingResponse,
)

__all__ = ["AlphaResource", "AsyncAlphaResource"]


class AlphaResource(SyncAPIResource):
    @cached_property
    def inference(self) -> InferenceResource:
        return InferenceResource(self._client)

    @cached_property
    def post_training(self) -> PostTrainingResource:
        return PostTrainingResource(self._client)

    @cached_property
    def benchmarks(self) -> BenchmarksResource:
        return BenchmarksResource(self._client)

    @cached_property
    def eval(self) -> EvalResource:
        return EvalResource(self._client)

    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> AlphaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AlphaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlphaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AlphaResourceWithStreamingResponse(self)


class AsyncAlphaResource(AsyncAPIResource):
    @cached_property
    def inference(self) -> AsyncInferenceResource:
        return AsyncInferenceResource(self._client)

    @cached_property
    def post_training(self) -> AsyncPostTrainingResource:
        return AsyncPostTrainingResource(self._client)

    @cached_property
    def benchmarks(self) -> AsyncBenchmarksResource:
        return AsyncBenchmarksResource(self._client)

    @cached_property
    def eval(self) -> AsyncEvalResource:
        return AsyncEvalResource(self._client)

    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlphaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlphaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlphaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncAlphaResourceWithStreamingResponse(self)


class AlphaResourceWithRawResponse:
    def __init__(self, alpha: AlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def inference(self) -> InferenceResourceWithRawResponse:
        return InferenceResourceWithRawResponse(self._alpha.inference)

    @cached_property
    def post_training(self) -> PostTrainingResourceWithRawResponse:
        return PostTrainingResourceWithRawResponse(self._alpha.post_training)

    @cached_property
    def benchmarks(self) -> BenchmarksResourceWithRawResponse:
        return BenchmarksResourceWithRawResponse(self._alpha.benchmarks)

    @cached_property
    def eval(self) -> EvalResourceWithRawResponse:
        return EvalResourceWithRawResponse(self._alpha.eval)

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._alpha.admin)


class AsyncAlphaResourceWithRawResponse:
    def __init__(self, alpha: AsyncAlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithRawResponse:
        return AsyncInferenceResourceWithRawResponse(self._alpha.inference)

    @cached_property
    def post_training(self) -> AsyncPostTrainingResourceWithRawResponse:
        return AsyncPostTrainingResourceWithRawResponse(self._alpha.post_training)

    @cached_property
    def benchmarks(self) -> AsyncBenchmarksResourceWithRawResponse:
        return AsyncBenchmarksResourceWithRawResponse(self._alpha.benchmarks)

    @cached_property
    def eval(self) -> AsyncEvalResourceWithRawResponse:
        return AsyncEvalResourceWithRawResponse(self._alpha.eval)

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._alpha.admin)


class AlphaResourceWithStreamingResponse:
    def __init__(self, alpha: AlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def inference(self) -> InferenceResourceWithStreamingResponse:
        return InferenceResourceWithStreamingResponse(self._alpha.inference)

    @cached_property
    def post_training(self) -> PostTrainingResourceWithStreamingResponse:
        return PostTrainingResourceWithStreamingResponse(self._alpha.post_training)

    @cached_property
    def benchmarks(self) -> BenchmarksResourceWithStreamingResponse:
        return BenchmarksResourceWithStreamingResponse(self._alpha.benchmarks)

    @cached_property
    def eval(self) -> EvalResourceWithStreamingResponse:
        return EvalResourceWithStreamingResponse(self._alpha.eval)

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._alpha.admin)


class AsyncAlphaResourceWithStreamingResponse:
    def __init__(self, alpha: AsyncAlphaResource) -> None:
        self._alpha = alpha

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithStreamingResponse:
        return AsyncInferenceResourceWithStreamingResponse(self._alpha.inference)

    @cached_property
    def post_training(self) -> AsyncPostTrainingResourceWithStreamingResponse:
        return AsyncPostTrainingResourceWithStreamingResponse(self._alpha.post_training)

    @cached_property
    def benchmarks(self) -> AsyncBenchmarksResourceWithStreamingResponse:
        return AsyncBenchmarksResourceWithStreamingResponse(self._alpha.benchmarks)

    @cached_property
    def eval(self) -> AsyncEvalResourceWithStreamingResponse:
        return AsyncEvalResourceWithStreamingResponse(self._alpha.eval)

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._alpha.admin)
