# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ScoringScoreBatchParams",
    "ScoringFunctions",
    "ScoringFunctionsLlmAsJudgeScoringFnParams",
    "ScoringFunctionsRegexParserScoringFnParams",
    "ScoringFunctionsBasicScoringFnParams",
]


class ScoringScoreBatchParams(TypedDict, total=False):
    dataset_id: Required[str]

    scoring_functions: Required[Dict[str, Optional[ScoringFunctions]]]

    save_results_dataset: bool


class ScoringFunctionsLlmAsJudgeScoringFnParams(TypedDict, total=False):
    """Parameters for LLM-as-judge scoring function configuration."""

    judge_model: Required[str]

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    judge_score_regexes: SequenceNotStr[str]
    """Regexes to extract the answer from generated response"""

    prompt_template: Optional[str]

    type: Literal["llm_as_judge"]


class ScoringFunctionsRegexParserScoringFnParams(TypedDict, total=False):
    """Parameters for regex parser scoring function configuration."""

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    parsing_regexes: SequenceNotStr[str]
    """Regex to extract the answer from generated response"""

    type: Literal["regex_parser"]


class ScoringFunctionsBasicScoringFnParams(TypedDict, total=False):
    """Parameters for basic scoring function configuration."""

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    type: Literal["basic"]


ScoringFunctions: TypeAlias = Union[
    ScoringFunctionsLlmAsJudgeScoringFnParams,
    ScoringFunctionsRegexParserScoringFnParams,
    ScoringFunctionsBasicScoringFnParams,
]
