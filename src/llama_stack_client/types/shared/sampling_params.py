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


class StrategyTopPSamplingStrategy(BaseModel):
    """
    Top-p (nucleus) sampling strategy that samples from the smallest set of tokens with cumulative probability >= p.
    """

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    type: Optional[Literal["top_p"]] = None


class StrategyTopKSamplingStrategy(BaseModel):
    """Top-k sampling strategy that restricts sampling to the k most likely tokens."""

    top_k: int

    type: Optional[Literal["top_k"]] = None


Strategy: TypeAlias = Annotated[
    Union[StrategyGreedySamplingStrategy, StrategyTopPSamplingStrategy, StrategyTopKSamplingStrategy],
    PropertyInfo(discriminator="type"),
]


class SamplingParams(BaseModel):
    """Sampling parameters."""

    max_tokens: Optional[int] = None

    repetition_penalty: Optional[float] = None

    stop: Optional[List[str]] = None

    strategy: Optional[Strategy] = None
    """
    Greedy sampling strategy that selects the highest probability token at each
    step.
    """
