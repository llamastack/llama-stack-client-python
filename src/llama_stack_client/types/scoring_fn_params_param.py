# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["ScoringFnParamsParam", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ]
    """Aggregation functions to apply to the scores of each row"""

    judge_model: Required[str]
    """Identifier of the LLM model to use as a judge for scoring"""

    judge_score_regexes: Required[SequenceNotStr[str]]
    """Regexes to extract the answer from generated response"""

    type: Required[Literal["llm_as_judge"]]
    """The type of scoring function parameters, always llm_as_judge"""

    prompt_template: str
    """(Optional) Custom prompt template for the judge model"""


class RegexParserScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ]
    """Aggregation functions to apply to the scores of each row"""

    parsing_regexes: Required[SequenceNotStr[str]]
    """Regex to extract the answer from generated response"""

    type: Required[Literal["regex_parser"]]
    """The type of scoring function parameters, always regex_parser"""


class BasicScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ]
    """Aggregation functions to apply to the scores of each row"""

    type: Required[Literal["basic"]]
    """The type of scoring function parameters, always basic"""


ScoringFnParamsParam: TypeAlias = Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams]
