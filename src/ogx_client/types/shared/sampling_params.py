# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "SamplingParams",
    "Strategy",
    "StrategyGreedySamplingStrategy",
    "StrategyTopPSamplingStrategy",
    "StrategyTopKSamplingStrategy",
]


class StrategyGreedySamplingStrategy(BaseModel):
    """
    Greedy sampling strategy that selects the highest probability token at each step.
    """

    type: Optional[Literal["greedy"]] = None
    """Must be 'greedy' to identify this sampling strategy."""


class StrategyTopPSamplingStrategy(BaseModel):
    """
    Top-p (nucleus) sampling strategy that samples from the smallest set of tokens with cumulative probability >= p.
    """

    temperature: float
    """Controls randomness in sampling. Higher values increase randomness."""

    top_p: Optional[float] = None
    """Cumulative probability threshold for nucleus sampling."""

    type: Optional[Literal["top_p"]] = None
    """Must be 'top_p' to identify this sampling strategy."""


class StrategyTopKSamplingStrategy(BaseModel):
    """Top-k sampling strategy that restricts sampling to the k most likely tokens."""

    top_k: int
    """Number of top tokens to consider for sampling. Must be at least 1."""

    type: Optional[Literal["top_k"]] = None
    """Must be 'top_k' to identify this sampling strategy."""


Strategy: TypeAlias = Annotated[
    Union[StrategyGreedySamplingStrategy, StrategyTopPSamplingStrategy, StrategyTopKSamplingStrategy],
    PropertyInfo(discriminator="type"),
]


class SamplingParams(BaseModel):
    """Sampling parameters for text generation."""

    max_tokens: Optional[int] = None
    """The maximum number of tokens that can be generated in the completion.

    The token count of your prompt plus max_tokens cannot exceed the model's context
    length.
    """

    repetition_penalty: Optional[float] = None
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far.
    """

    stop: Optional[List[str]] = None
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    strategy: Optional[Strategy] = None
    """The sampling strategy to use."""
