# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .job import (
    JobResource,
    AsyncJobResource,
    JobResourceWithRawResponse,
    AsyncJobResourceWithRawResponse,
    JobResourceWithStreamingResponse,
    AsyncJobResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.alpha import post_training_preference_optimize_params, post_training_supervised_fine_tune_params
from ...._base_client import make_request_options
from ....types.alpha.post_training_job import PostTrainingJob

__all__ = ["PostTrainingResource", "AsyncPostTrainingResource"]


class PostTrainingResource(SyncAPIResource):
    @cached_property
    def job(self) -> JobResource:
        return JobResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return PostTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return PostTrainingResourceWithStreamingResponse(self)

    def preference_optimize(
        self,
        *,
        algorithm_config: post_training_preference_optimize_params.AlgorithmConfig,
        finetuned_model: str,
        hyperparam_search_config: Dict[str, object],
        job_uuid: str,
        logger_config: Dict[str, object],
        training_config: post_training_preference_optimize_params.TrainingConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostTrainingJob:
        """
        Run preference optimization of a model.

        Args:
          algorithm_config: Configuration for Direct Preference Optimization (DPO) alignment.

          training_config: Comprehensive configuration for the training process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1alpha/post-training/preference-optimize",
            body=maybe_transform(
                {
                    "algorithm_config": algorithm_config,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                },
                post_training_preference_optimize_params.PostTrainingPreferenceOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )

    def supervised_fine_tune(
        self,
        *,
        hyperparam_search_config: Dict[str, object],
        job_uuid: str,
        logger_config: Dict[str, object],
        training_config: post_training_supervised_fine_tune_params.TrainingConfig,
        algorithm_config: Optional[post_training_supervised_fine_tune_params.AlgorithmConfig] | Omit = omit,
        checkpoint_dir: Optional[str] | Omit = omit,
        model: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostTrainingJob:
        """
        Run supervised fine-tuning of a model.

        Args:
          training_config: Comprehensive configuration for the training process.

          algorithm_config: Configuration for Low-Rank Adaptation (LoRA) fine-tuning.

          model: Model descriptor for training if not in provider config`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1alpha/post-training/supervised-fine-tune",
            body=maybe_transform(
                {
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                    "algorithm_config": algorithm_config,
                    "checkpoint_dir": checkpoint_dir,
                    "model": model,
                },
                post_training_supervised_fine_tune_params.PostTrainingSupervisedFineTuneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )


class AsyncPostTrainingResource(AsyncAPIResource):
    @cached_property
    def job(self) -> AsyncJobResource:
        return AsyncJobResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncPostTrainingResourceWithStreamingResponse(self)

    async def preference_optimize(
        self,
        *,
        algorithm_config: post_training_preference_optimize_params.AlgorithmConfig,
        finetuned_model: str,
        hyperparam_search_config: Dict[str, object],
        job_uuid: str,
        logger_config: Dict[str, object],
        training_config: post_training_preference_optimize_params.TrainingConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostTrainingJob:
        """
        Run preference optimization of a model.

        Args:
          algorithm_config: Configuration for Direct Preference Optimization (DPO) alignment.

          training_config: Comprehensive configuration for the training process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1alpha/post-training/preference-optimize",
            body=await async_maybe_transform(
                {
                    "algorithm_config": algorithm_config,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                },
                post_training_preference_optimize_params.PostTrainingPreferenceOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )

    async def supervised_fine_tune(
        self,
        *,
        hyperparam_search_config: Dict[str, object],
        job_uuid: str,
        logger_config: Dict[str, object],
        training_config: post_training_supervised_fine_tune_params.TrainingConfig,
        algorithm_config: Optional[post_training_supervised_fine_tune_params.AlgorithmConfig] | Omit = omit,
        checkpoint_dir: Optional[str] | Omit = omit,
        model: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostTrainingJob:
        """
        Run supervised fine-tuning of a model.

        Args:
          training_config: Comprehensive configuration for the training process.

          algorithm_config: Configuration for Low-Rank Adaptation (LoRA) fine-tuning.

          model: Model descriptor for training if not in provider config`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1alpha/post-training/supervised-fine-tune",
            body=await async_maybe_transform(
                {
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                    "algorithm_config": algorithm_config,
                    "checkpoint_dir": checkpoint_dir,
                    "model": model,
                },
                post_training_supervised_fine_tune_params.PostTrainingSupervisedFineTuneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )


class PostTrainingResourceWithRawResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = to_raw_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = to_raw_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> JobResourceWithRawResponse:
        return JobResourceWithRawResponse(self._post_training.job)


class AsyncPostTrainingResourceWithRawResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = async_to_raw_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = async_to_raw_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithRawResponse:
        return AsyncJobResourceWithRawResponse(self._post_training.job)


class PostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = to_streamed_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = to_streamed_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> JobResourceWithStreamingResponse:
        return JobResourceWithStreamingResponse(self._post_training.job)


class AsyncPostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = async_to_streamed_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = async_to_streamed_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithStreamingResponse:
        return AsyncJobResourceWithStreamingResponse(self._post_training.job)
