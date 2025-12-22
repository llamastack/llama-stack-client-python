# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ScoringFunctionRegisterParams",
    "ReturnType",
    "Params",
    "ParamsLlmAsJudgeScoringFnParams",
    "ParamsRegexParserScoringFnParams",
    "ParamsBasicScoringFnParams",
]


class ScoringFunctionRegisterParams(TypedDict, total=False):
    description: Required[str]

    return_type: Required[ReturnType]

    scoring_fn_id: Required[str]

    params: Optional[Params]
    """Parameters for LLM-as-judge scoring function configuration."""

    provider_id: Optional[str]

    provider_scoring_fn_id: Optional[str]


class ReturnType(TypedDict, total=False):
    type: Required[
        Literal[
            "string",
            "number",
            "boolean",
            "array",
            "object",
            "json",
            "union",
            "chat_completion_input",
            "completion_input",
            "agent_turn_input",
        ]
    ]


class ParamsLlmAsJudgeScoringFnParams(TypedDict, total=False):
    """Parameters for LLM-as-judge scoring function configuration."""

    judge_model: Required[str]

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    judge_score_regexes: SequenceNotStr[str]
    """Regexes to extract the answer from generated response"""

    prompt_template: Optional[str]

    type: Literal["llm_as_judge"]


class ParamsRegexParserScoringFnParams(TypedDict, total=False):
    """Parameters for regex parser scoring function configuration."""

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    parsing_regexes: SequenceNotStr[str]
    """Regex to extract the answer from generated response"""

    type: Literal["regex_parser"]


class ParamsBasicScoringFnParams(TypedDict, total=False):
    """Parameters for basic scoring function configuration."""

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    type: Literal["basic"]


Params: TypeAlias = Union[ParamsLlmAsJudgeScoringFnParams, ParamsRegexParserScoringFnParams, ParamsBasicScoringFnParams]
