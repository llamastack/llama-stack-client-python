# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .algorithm_config_param import AlgorithmConfigParam

__all__ = [
    "PostTrainingSupervisedFineTuneParams",
    "TrainingConfig",
    "TrainingConfigDataConfig",
    "TrainingConfigEfficiencyConfig",
    "TrainingConfigOptimizerConfig",
]


class PostTrainingSupervisedFineTuneParams(TypedDict, total=False):
    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The hyperparam search configuration."""

    job_uuid: Required[str]
    """The UUID of the job to create."""

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The logger configuration."""

    training_config: Required[TrainingConfig]
    """The training configuration."""

    algorithm_config: AlgorithmConfigParam
    """The algorithm configuration."""

    checkpoint_dir: str
    """The directory to save checkpoint(s) to."""

    model: str
    """The model to fine-tune."""


class TrainingConfigDataConfig(TypedDict, total=False):
    batch_size: Required[int]
    """Number of samples per training batch"""

    data_format: Required[Literal["instruct", "dialog"]]
    """Format of the dataset (instruct or dialog)"""

    dataset_id: Required[str]
    """Unique identifier for the training dataset"""

    shuffle: Required[bool]
    """Whether to shuffle the dataset during training"""

    packed: bool
    """
    (Optional) Whether to pack multiple samples into a single sequence for
    efficiency
    """

    train_on_input: bool
    """(Optional) Whether to compute loss on input tokens as well as output tokens"""

    validation_dataset_id: str
    """(Optional) Unique identifier for the validation dataset"""


class TrainingConfigEfficiencyConfig(TypedDict, total=False):
    enable_activation_checkpointing: bool
    """(Optional) Whether to use activation checkpointing to reduce memory usage"""

    enable_activation_offloading: bool
    """(Optional) Whether to offload activations to CPU to save GPU memory"""

    fsdp_cpu_offload: bool
    """(Optional) Whether to offload FSDP parameters to CPU"""

    memory_efficient_fsdp_wrap: bool
    """(Optional) Whether to use memory-efficient FSDP wrapping"""


class TrainingConfigOptimizerConfig(TypedDict, total=False):
    lr: Required[float]
    """Learning rate for the optimizer"""

    num_warmup_steps: Required[int]
    """Number of steps for learning rate warmup"""

    optimizer_type: Required[Literal["adam", "adamw", "sgd"]]
    """Type of optimizer to use (adam, adamw, or sgd)"""

    weight_decay: Required[float]
    """Weight decay coefficient for regularization"""


class TrainingConfig(TypedDict, total=False):
    gradient_accumulation_steps: Required[int]
    """Number of steps to accumulate gradients before updating"""

    max_steps_per_epoch: Required[int]
    """Maximum number of steps to run per epoch"""

    n_epochs: Required[int]
    """Number of training epochs to run"""

    data_config: TrainingConfigDataConfig
    """(Optional) Configuration for data loading and formatting"""

    dtype: str
    """(Optional) Data type for model parameters (bf16, fp16, fp32)"""

    efficiency_config: TrainingConfigEfficiencyConfig
    """(Optional) Configuration for memory and compute optimizations"""

    max_validation_steps: int
    """(Optional) Maximum number of validation steps per epoch"""

    optimizer_config: TrainingConfigOptimizerConfig
    """(Optional) Configuration for the optimization algorithm"""
