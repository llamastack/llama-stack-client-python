# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.system_message import SystemMessage
from ..shared_params.sampling_params import SamplingParams

__all__ = [
    "BenchmarkConfigParam",
    "EvalCandidate",
    "ScoringParams",
    "ScoringParamsLlmAsJudgeScoringFnParams",
    "ScoringParamsRegexParserScoringFnParams",
    "ScoringParamsBasicScoringFnParams",
]


class EvalCandidate(TypedDict, total=False):
    """A model candidate for evaluation."""

    model: Required[str]

    sampling_params: Required[SamplingParams]
    """Sampling parameters."""

    system_message: Optional[SystemMessage]
    """A system message providing instructions or context to the model."""

    type: Literal["model"]


class ScoringParamsLlmAsJudgeScoringFnParams(TypedDict, total=False):
    """Parameters for LLM-as-judge scoring function configuration."""

    judge_model: Required[str]

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    judge_score_regexes: SequenceNotStr[str]
    """Regexes to extract the answer from generated response"""

    prompt_template: Optional[str]

    type: Literal["llm_as_judge"]


class ScoringParamsRegexParserScoringFnParams(TypedDict, total=False):
    """Parameters for regex parser scoring function configuration."""

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    parsing_regexes: SequenceNotStr[str]
    """Regex to extract the answer from generated response"""

    type: Literal["regex_parser"]


class ScoringParamsBasicScoringFnParams(TypedDict, total=False):
    """Parameters for basic scoring function configuration."""

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    type: Literal["basic"]


ScoringParams: TypeAlias = Union[
    ScoringParamsLlmAsJudgeScoringFnParams, ScoringParamsRegexParserScoringFnParams, ScoringParamsBasicScoringFnParams
]


class BenchmarkConfigParam(TypedDict, total=False):
    """A benchmark configuration for evaluation."""

    eval_candidate: Required[EvalCandidate]
    """A model candidate for evaluation."""

    num_examples: Optional[int]
    """
    Number of examples to evaluate (useful for testing), if not provided, all
    examples in the dataset will be evaluated
    """

    scoring_params: Dict[str, ScoringParams]
    """
    Map between scoring function id and parameters for each scoring function you
    want to run
    """
