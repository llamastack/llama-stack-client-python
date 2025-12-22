# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "PostTrainingSupervisedFineTuneParams",
    "TrainingConfig",
    "TrainingConfigDataConfig",
    "TrainingConfigEfficiencyConfig",
    "TrainingConfigOptimizerConfig",
    "AlgorithmConfig",
    "AlgorithmConfigLoraFinetuningConfig",
    "AlgorithmConfigQatFinetuningConfig",
]


class PostTrainingSupervisedFineTuneParams(TypedDict, total=False):
    hyperparam_search_config: Required[Dict[str, object]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, object]]

    training_config: Required[TrainingConfig]
    """Comprehensive configuration for the training process."""

    algorithm_config: Optional[AlgorithmConfig]
    """Configuration for Low-Rank Adaptation (LoRA) fine-tuning."""

    checkpoint_dir: Optional[str]

    model: Optional[str]
    """Model descriptor for training if not in provider config`"""


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


class AlgorithmConfigLoraFinetuningConfig(TypedDict, total=False):
    """Configuration for Low-Rank Adaptation (LoRA) fine-tuning."""

    alpha: Required[int]

    apply_lora_to_mlp: Required[bool]

    apply_lora_to_output: Required[bool]

    lora_attn_modules: Required[SequenceNotStr[str]]

    rank: Required[int]

    quantize_base: Optional[bool]

    type: Literal["LoRA"]

    use_dora: Optional[bool]


class AlgorithmConfigQatFinetuningConfig(TypedDict, total=False):
    """Configuration for Quantization-Aware Training (QAT) fine-tuning."""

    group_size: Required[int]

    quantizer_name: Required[str]

    type: Literal["QAT"]


AlgorithmConfig: TypeAlias = Union[AlgorithmConfigLoraFinetuningConfig, AlgorithmConfigQatFinetuningConfig]
