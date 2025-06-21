# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    PostTrainingJob,
    PostTrainingListJobsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPostTraining:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_fine_tune_supervised(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_fine_tune_supervised_with_all_params(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
                "data_config": {
                    "batch_size": 0,
                    "data_format": "instruct",
                    "dataset_id": "dataset_id",
                    "shuffle": True,
                    "packed": True,
                    "train_on_input": True,
                    "validation_dataset_id": "validation_dataset_id",
                },
                "dtype": "dtype",
                "efficiency_config": {
                    "enable_activation_checkpointing": True,
                    "enable_activation_offloading": True,
                    "fsdp_cpu_offload": True,
                    "memory_efficient_fsdp_wrap": True,
                },
                "max_validation_steps": 0,
                "optimizer_config": {
                    "lr": 0,
                    "num_warmup_steps": 0,
                    "optimizer_type": "adam",
                    "weight_decay": 0,
                },
            },
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
                "type": "LoRA",
                "quantize_base": True,
                "use_dora": True,
            },
            checkpoint_dir="checkpoint_dir",
            model="model",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_fine_tune_supervised(self, client: LlamaStackClient) -> None:
        response = client.post_training.with_raw_response.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_fine_tune_supervised(self, client: LlamaStackClient) -> None:
        with client.post_training.with_streaming_response.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_jobs(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.list_jobs()
        assert_matches_type(PostTrainingListJobsResponse, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_jobs(self, client: LlamaStackClient) -> None:
        response = client.post_training.with_raw_response.list_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = response.parse()
        assert_matches_type(PostTrainingListJobsResponse, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_jobs(self, client: LlamaStackClient) -> None:
        with client.post_training.with_streaming_response.list_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = response.parse()
            assert_matches_type(PostTrainingListJobsResponse, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_optimize_preferences(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_optimize_preferences_with_all_params(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
                "data_config": {
                    "batch_size": 0,
                    "data_format": "instruct",
                    "dataset_id": "dataset_id",
                    "shuffle": True,
                    "packed": True,
                    "train_on_input": True,
                    "validation_dataset_id": "validation_dataset_id",
                },
                "dtype": "dtype",
                "efficiency_config": {
                    "enable_activation_checkpointing": True,
                    "enable_activation_offloading": True,
                    "fsdp_cpu_offload": True,
                    "memory_efficient_fsdp_wrap": True,
                },
                "max_validation_steps": 0,
                "optimizer_config": {
                    "lr": 0,
                    "num_warmup_steps": 0,
                    "optimizer_type": "adam",
                    "weight_decay": 0,
                },
            },
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_optimize_preferences(self, client: LlamaStackClient) -> None:
        response = client.post_training.with_raw_response.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_optimize_preferences(self, client: LlamaStackClient) -> None:
        with client.post_training.with_streaming_response.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPostTraining:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_fine_tune_supervised(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_fine_tune_supervised_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
                "data_config": {
                    "batch_size": 0,
                    "data_format": "instruct",
                    "dataset_id": "dataset_id",
                    "shuffle": True,
                    "packed": True,
                    "train_on_input": True,
                    "validation_dataset_id": "validation_dataset_id",
                },
                "dtype": "dtype",
                "efficiency_config": {
                    "enable_activation_checkpointing": True,
                    "enable_activation_offloading": True,
                    "fsdp_cpu_offload": True,
                    "memory_efficient_fsdp_wrap": True,
                },
                "max_validation_steps": 0,
                "optimizer_config": {
                    "lr": 0,
                    "num_warmup_steps": 0,
                    "optimizer_type": "adam",
                    "weight_decay": 0,
                },
            },
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
                "type": "LoRA",
                "quantize_base": True,
                "use_dora": True,
            },
            checkpoint_dir="checkpoint_dir",
            model="model",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_fine_tune_supervised(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.with_raw_response.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = await response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_fine_tune_supervised(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.with_streaming_response.fine_tune_supervised(
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = await response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_jobs(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.list_jobs()
        assert_matches_type(PostTrainingListJobsResponse, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_jobs(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.with_raw_response.list_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = await response.parse()
        assert_matches_type(PostTrainingListJobsResponse, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_jobs(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.with_streaming_response.list_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = await response.parse()
            assert_matches_type(PostTrainingListJobsResponse, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_optimize_preferences(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_optimize_preferences_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
                "data_config": {
                    "batch_size": 0,
                    "data_format": "instruct",
                    "dataset_id": "dataset_id",
                    "shuffle": True,
                    "packed": True,
                    "train_on_input": True,
                    "validation_dataset_id": "validation_dataset_id",
                },
                "dtype": "dtype",
                "efficiency_config": {
                    "enable_activation_checkpointing": True,
                    "enable_activation_offloading": True,
                    "fsdp_cpu_offload": True,
                    "memory_efficient_fsdp_wrap": True,
                },
                "max_validation_steps": 0,
                "optimizer_config": {
                    "lr": 0,
                    "num_warmup_steps": 0,
                    "optimizer_type": "adam",
                    "weight_decay": 0,
                },
            },
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_optimize_preferences(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.with_raw_response.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = await response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_optimize_preferences(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.with_streaming_response.optimize_preferences(
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            training_config={
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
                "n_epochs": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = await response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True
