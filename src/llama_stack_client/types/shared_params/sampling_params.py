# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "SamplingParams",
    "Strategy",
    "StrategyGreedySamplingStrategy",
    "StrategyTopPSamplingStrategy",
    "StrategyTopKSamplingStrategy",
]


class StrategyGreedySamplingStrategy(TypedDict, total=False):
    """
    Greedy sampling strategy that selects the highest probability token at each step.
    """

    type: Literal["greedy"]


class StrategyTopPSamplingStrategy(TypedDict, total=False):
    """
    Top-p (nucleus) sampling strategy that samples from the smallest set of tokens with cumulative probability >= p.
    """

    temperature: Required[Optional[float]]

    top_p: Optional[float]

    type: Literal["top_p"]


class StrategyTopKSamplingStrategy(TypedDict, total=False):
    """Top-k sampling strategy that restricts sampling to the k most likely tokens."""

    top_k: Required[int]

    type: Literal["top_k"]


Strategy: TypeAlias = Union[StrategyGreedySamplingStrategy, StrategyTopPSamplingStrategy, StrategyTopKSamplingStrategy]


class SamplingParams(TypedDict, total=False):
    """Sampling parameters."""

    max_tokens: Optional[int]

    repetition_penalty: Optional[float]

    stop: Optional[SequenceNotStr[str]]

    strategy: Strategy
    """
    Greedy sampling strategy that selects the highest probability token at each
    step.
    """
