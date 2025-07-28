# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
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
    """The algorithm configuration."""

    finetuned_model: Required[str]
    """The model to fine-tune."""

    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The hyperparam search configuration."""

    job_uuid: Required[str]
    """The UUID of the job to create."""

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The logger configuration."""

    training_config: Required[TrainingConfig]
    """The training configuration."""


class AlgorithmConfig(TypedDict, total=False):
    beta: Required[float]

    loss_type: Required[Literal["sigmoid", "hinge", "ipo", "kto_pair"]]


class TrainingConfigDataConfig(TypedDict, total=False):
    batch_size: Required[int]

    data_format: Required[Literal["instruct", "dialog"]]

    dataset_id: Required[str]

    shuffle: Required[bool]

    packed: bool

    train_on_input: bool

    validation_dataset_id: str


class TrainingConfigEfficiencyConfig(TypedDict, total=False):
    enable_activation_checkpointing: bool

    enable_activation_offloading: bool

    fsdp_cpu_offload: bool

    memory_efficient_fsdp_wrap: bool


class TrainingConfigOptimizerConfig(TypedDict, total=False):
    lr: Required[float]

    num_warmup_steps: Required[int]

    optimizer_type: Required[Literal["adam", "adamw", "sgd"]]

    weight_decay: Required[float]


class TrainingConfig(TypedDict, total=False):
    gradient_accumulation_steps: Required[int]

    max_steps_per_epoch: Required[int]

    n_epochs: Required[int]

    data_config: TrainingConfigDataConfig

    dtype: str

    efficiency_config: TrainingConfigEfficiencyConfig

    max_validation_steps: int

    optimizer_config: TrainingConfigOptimizerConfig
