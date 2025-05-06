# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from .job import (
    JobResource,
    AsyncJobResource,
    JobResourceWithRawResponse,
    AsyncJobResourceWithRawResponse,
    JobResourceWithStreamingResponse,
    AsyncJobResourceWithStreamingResponse,
)
from ...types import (
    post_training_fine_tune_supervised_params,
    post_training_optimize_preferences_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.post_training_job import PostTrainingJob
from ...types.training_config_param import TrainingConfigParam
from ...types.post_training_list_jobs_response import PostTrainingListJobsResponse

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

    def fine_tune_supervised(
        self,
        *,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        training_config: TrainingConfigParam,
        algorithm_config: post_training_fine_tune_supervised_params.AlgorithmConfig | NotGiven = NOT_GIVEN,
        checkpoint_dir: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/post-training/supervised-fine-tune",
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
                post_training_fine_tune_supervised_params.PostTrainingFineTuneSupervisedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )

    def list_jobs(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingListJobsResponse:
        return self._get(
            "/v1/post-training/jobs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingListJobsResponse,
        )

    def optimize_preferences(
        self,
        *,
        algorithm_config: post_training_optimize_preferences_params.AlgorithmConfig,
        finetuned_model: str,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        training_config: TrainingConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/post-training/preference-optimize",
            body=maybe_transform(
                {
                    "algorithm_config": algorithm_config,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                },
                post_training_optimize_preferences_params.PostTrainingOptimizePreferencesParams,
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

    async def fine_tune_supervised(
        self,
        *,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        training_config: TrainingConfigParam,
        algorithm_config: post_training_fine_tune_supervised_params.AlgorithmConfig | NotGiven = NOT_GIVEN,
        checkpoint_dir: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/post-training/supervised-fine-tune",
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
                post_training_fine_tune_supervised_params.PostTrainingFineTuneSupervisedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )

    async def list_jobs(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingListJobsResponse:
        return await self._get(
            "/v1/post-training/jobs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingListJobsResponse,
        )

    async def optimize_preferences(
        self,
        *,
        algorithm_config: post_training_optimize_preferences_params.AlgorithmConfig,
        finetuned_model: str,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        training_config: TrainingConfigParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/post-training/preference-optimize",
            body=await async_maybe_transform(
                {
                    "algorithm_config": algorithm_config,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                },
                post_training_optimize_preferences_params.PostTrainingOptimizePreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )


class PostTrainingResourceWithRawResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.fine_tune_supervised = to_raw_response_wrapper(
            post_training.fine_tune_supervised,
        )
        self.list_jobs = to_raw_response_wrapper(
            post_training.list_jobs,
        )
        self.optimize_preferences = to_raw_response_wrapper(
            post_training.optimize_preferences,
        )

    @cached_property
    def job(self) -> JobResourceWithRawResponse:
        return JobResourceWithRawResponse(self._post_training.job)


class AsyncPostTrainingResourceWithRawResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.fine_tune_supervised = async_to_raw_response_wrapper(
            post_training.fine_tune_supervised,
        )
        self.list_jobs = async_to_raw_response_wrapper(
            post_training.list_jobs,
        )
        self.optimize_preferences = async_to_raw_response_wrapper(
            post_training.optimize_preferences,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithRawResponse:
        return AsyncJobResourceWithRawResponse(self._post_training.job)


class PostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.fine_tune_supervised = to_streamed_response_wrapper(
            post_training.fine_tune_supervised,
        )
        self.list_jobs = to_streamed_response_wrapper(
            post_training.list_jobs,
        )
        self.optimize_preferences = to_streamed_response_wrapper(
            post_training.optimize_preferences,
        )

    @cached_property
    def job(self) -> JobResourceWithStreamingResponse:
        return JobResourceWithStreamingResponse(self._post_training.job)


class AsyncPostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.fine_tune_supervised = async_to_streamed_response_wrapper(
            post_training.fine_tune_supervised,
        )
        self.list_jobs = async_to_streamed_response_wrapper(
            post_training.list_jobs,
        )
        self.optimize_preferences = async_to_streamed_response_wrapper(
            post_training.optimize_preferences,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithStreamingResponse:
        return AsyncJobResourceWithStreamingResponse(self._post_training.job)
