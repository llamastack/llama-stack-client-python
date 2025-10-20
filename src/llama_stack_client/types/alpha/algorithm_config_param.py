# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AlgorithmConfigParam", "LoraFinetuningConfig", "QatFinetuningConfig"]


class LoraFinetuningConfig(TypedDict, total=False):
    alpha: Required[int]
    """LoRA scaling parameter that controls adaptation strength"""

    apply_lora_to_mlp: Required[bool]
    """Whether to apply LoRA to MLP layers"""

    apply_lora_to_output: Required[bool]
    """Whether to apply LoRA to output projection layers"""

    lora_attn_modules: Required[SequenceNotStr[str]]
    """List of attention module names to apply LoRA to"""

    rank: Required[int]
    """Rank of the LoRA adaptation (lower rank = fewer parameters)"""

    type: Required[Literal["LoRA"]]
    """Algorithm type identifier, always "LoRA" """

    quantize_base: bool
    """(Optional) Whether to quantize the base model weights"""

    use_dora: bool
    """(Optional) Whether to use DoRA (Weight-Decomposed Low-Rank Adaptation)"""


class QatFinetuningConfig(TypedDict, total=False):
    group_size: Required[int]
    """Size of groups for grouped quantization"""

    quantizer_name: Required[str]
    """Name of the quantization algorithm to use"""

    type: Required[Literal["QAT"]]
    """Algorithm type identifier, always "QAT" """


AlgorithmConfigParam: TypeAlias = Union[LoraFinetuningConfig, QatFinetuningConfig]
