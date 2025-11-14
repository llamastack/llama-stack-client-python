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
    type: Optional[Literal["greedy"]] = None


class StrategyTopPSamplingStrategy(BaseModel):
    temperature: Optional[float] = None

    top_p: Optional[float] = None

    type: Optional[Literal["top_p"]] = None


class StrategyTopKSamplingStrategy(BaseModel):
    top_k: int

    type: Optional[Literal["top_k"]] = None


Strategy: TypeAlias = Annotated[
    Union[StrategyGreedySamplingStrategy, StrategyTopPSamplingStrategy, StrategyTopKSamplingStrategy],
    PropertyInfo(discriminator="type"),
]


class SamplingParams(BaseModel):
    max_tokens: Optional[int] = None

    repetition_penalty: Optional[float] = None

    stop: Optional[List[str]] = None

    strategy: Optional[Strategy] = None
    """
    Greedy sampling strategy that selects the highest probability token at each
    step.
    """
