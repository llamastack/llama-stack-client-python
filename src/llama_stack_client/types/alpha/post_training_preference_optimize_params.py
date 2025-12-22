# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "PostTrainingPreferenceOptimizeParams",
    "AlgorithmConfig",
    "TrainingConfig",
    "TrainingConfigDataConfig",
    "TrainingConfigEfficiencyConfig",
    "TrainingConfigOptimizerConfig",
]


class PostTrainingPreferenceOptimizeParams(TypedDict, total=False):
    algorithm_config: Required[AlgorithmConfig]
    """Configuration for Direct Preference Optimization (DPO) alignment."""

    finetuned_model: Required[str]

    hyperparam_search_config: Required[Dict[str, object]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, object]]

    training_config: Required[TrainingConfig]
    """Comprehensive configuration for the training process."""


class AlgorithmConfig(TypedDict, total=False):
    """Configuration for Direct Preference Optimization (DPO) alignment."""

    beta: Required[float]

    loss_type: Literal["sigmoid", "hinge", "ipo", "kto_pair"]


class TrainingConfigDataConfig(TypedDict, total=False):
    """Configuration for training data and data loading."""

    batch_size: Required[int]

    data_format: Required[Literal["instruct", "dialog"]]
    """Format of the training dataset."""

    dataset_id: Required[str]

    shuffle: Required[bool]

    packed: Optional[bool]

    train_on_input: Optional[bool]

    validation_dataset_id: Optional[str]


class TrainingConfigEfficiencyConfig(TypedDict, total=False):
    """Configuration for memory and compute efficiency optimizations."""

    enable_activation_checkpointing: Optional[bool]

    enable_activation_offloading: Optional[bool]

    fsdp_cpu_offload: Optional[bool]

    memory_efficient_fsdp_wrap: Optional[bool]


class TrainingConfigOptimizerConfig(TypedDict, total=False):
    """Configuration parameters for the optimization algorithm."""

    lr: Required[float]

    num_warmup_steps: Required[int]

    optimizer_type: Required[Literal["adam", "adamw", "sgd"]]
    """Available optimizer algorithms for training."""

    weight_decay: Required[float]


class TrainingConfig(TypedDict, total=False):
    """Comprehensive configuration for the training process."""

    n_epochs: Required[int]

    data_config: Optional[TrainingConfigDataConfig]
    """Configuration for training data and data loading."""

    dtype: Optional[str]

    efficiency_config: Optional[TrainingConfigEfficiencyConfig]
    """Configuration for memory and compute efficiency optimizations."""

    gradient_accumulation_steps: int

    max_steps_per_epoch: int

    max_validation_steps: Optional[int]

    optimizer_config: Optional[TrainingConfigOptimizerConfig]
    """Configuration parameters for the optimization algorithm."""
