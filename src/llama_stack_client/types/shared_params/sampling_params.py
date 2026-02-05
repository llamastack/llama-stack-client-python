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
    """Must be 'greedy' to identify this sampling strategy."""


class StrategyTopPSamplingStrategy(TypedDict, total=False):
    """
    Top-p (nucleus) sampling strategy that samples from the smallest set of tokens with cumulative probability >= p.
    """

    temperature: Required[float]
    """Controls randomness in sampling. Higher values increase randomness."""

    top_p: float
    """Cumulative probability threshold for nucleus sampling."""

    type: Literal["top_p"]
    """Must be 'top_p' to identify this sampling strategy."""


class StrategyTopKSamplingStrategy(TypedDict, total=False):
    """Top-k sampling strategy that restricts sampling to the k most likely tokens."""

    top_k: Required[int]
    """Number of top tokens to consider for sampling. Must be at least 1."""

    type: Literal["top_k"]
    """Must be 'top_k' to identify this sampling strategy."""


Strategy: TypeAlias = Union[StrategyGreedySamplingStrategy, StrategyTopPSamplingStrategy, StrategyTopKSamplingStrategy]


class SamplingParams(TypedDict, total=False):
    """Sampling parameters for text generation."""

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the completion.

    The token count of your prompt plus max_tokens cannot exceed the model's context
    length.
    """

    repetition_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far.
    """

    stop: Optional[SequenceNotStr[str]]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    strategy: Strategy
    """The sampling strategy to use."""
