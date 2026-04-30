# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["ScoringFnParams", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(BaseModel):
    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    judge_model: str
    """Identifier of the LLM model to use as a judge for scoring"""

    judge_score_regexes: List[str]
    """Regexes to extract the answer from generated response"""

    type: Literal["llm_as_judge"]
    """The type of scoring function parameters, always llm_as_judge"""

    prompt_template: Optional[str] = None
    """(Optional) Custom prompt template for the judge model"""


class RegexParserScoringFnParams(BaseModel):
    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    parsing_regexes: List[str]
    """Regex to extract the answer from generated response"""

    type: Literal["regex_parser"]
    """The type of scoring function parameters, always regex_parser"""


class BasicScoringFnParams(BaseModel):
    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    """Aggregation functions to apply to the scores of each row"""

    type: Literal["basic"]
    """The type of scoring function parameters, always basic"""


ScoringFnParams: TypeAlias = Annotated[
    Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams],
    PropertyInfo(discriminator="type"),
]
