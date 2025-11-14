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
from llama_stack_client.types.alpha import (
    PostTrainingJob,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPostTraining:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_preference_optimize(self, client: LlamaStackClient) -> None:
        post_training = client.alpha.post_training.preference_optimize(
            algorithm_config={"beta": 0},
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_method_preference_optimize_with_all_params(self, client: LlamaStackClient) -> None:
        post_training = client.alpha.post_training.preference_optimize(
            algorithm_config={
                "beta": 0,
                "loss_type": "sigmoid",
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={
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
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
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

    @parametrize
    def test_raw_response_preference_optimize(self, client: LlamaStackClient) -> None:
        response = client.alpha.post_training.with_raw_response.preference_optimize(
            algorithm_config={"beta": 0},
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_streaming_response_preference_optimize(self, client: LlamaStackClient) -> None:
        with client.alpha.post_training.with_streaming_response.preference_optimize(
            algorithm_config={"beta": 0},
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_supervised_fine_tune(self, client: LlamaStackClient) -> None:
        post_training = client.alpha.post_training.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_method_supervised_fine_tune_with_all_params(self, client: LlamaStackClient) -> None:
        post_training = client.alpha.post_training.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={
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
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
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
                "quantize_base": True,
                "type": "LoRA",
                "use_dora": True,
            },
            checkpoint_dir="checkpoint_dir",
            model="model",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_raw_response_supervised_fine_tune(self, client: LlamaStackClient) -> None:
        response = client.alpha.post_training.with_raw_response.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_streaming_response_supervised_fine_tune(self, client: LlamaStackClient) -> None:
        with client.alpha.post_training.with_streaming_response.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
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

    @parametrize
    async def test_method_preference_optimize(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.alpha.post_training.preference_optimize(
            algorithm_config={"beta": 0},
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_method_preference_optimize_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.alpha.post_training.preference_optimize(
            algorithm_config={
                "beta": 0,
                "loss_type": "sigmoid",
            },
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={
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
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
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

    @parametrize
    async def test_raw_response_preference_optimize(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.post_training.with_raw_response.preference_optimize(
            algorithm_config={"beta": 0},
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = await response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_streaming_response_preference_optimize(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.post_training.with_streaming_response.preference_optimize(
            algorithm_config={"beta": 0},
            finetuned_model="finetuned_model",
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = await response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_supervised_fine_tune(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.alpha.post_training.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_method_supervised_fine_tune_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.alpha.post_training.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={
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
                "gradient_accumulation_steps": 0,
                "max_steps_per_epoch": 0,
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
                "quantize_base": True,
                "type": "LoRA",
                "use_dora": True,
            },
            checkpoint_dir="checkpoint_dir",
            model="model",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_raw_response_supervised_fine_tune(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.alpha.post_training.with_raw_response.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = await response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_streaming_response_supervised_fine_tune(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.alpha.post_training.with_streaming_response.supervised_fine_tune(
            hyperparam_search_config={"foo": "bar"},
            job_uuid="job_uuid",
            logger_config={"foo": "bar"},
            training_config={"n_epochs": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = await response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True
