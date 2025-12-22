# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ScoringFn",
    "ReturnType",
    "Params",
    "ParamsLlmAsJudgeScoringFnParams",
    "ParamsRegexParserScoringFnParams",
    "ParamsBasicScoringFnParams",
]


class ReturnType(BaseModel):
    type: Literal[
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


class ParamsLlmAsJudgeScoringFnParams(BaseModel):
    """Parameters for LLM-as-judge scoring function configuration."""

    judge_model: str

    aggregation_functions: Optional[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ] = None
    """Aggregation functions to apply to the scores of each row"""

    judge_score_regexes: Optional[List[str]] = None
    """Regexes to extract the answer from generated response"""

    prompt_template: Optional[str] = None

    type: Optional[Literal["llm_as_judge"]] = None


class ParamsRegexParserScoringFnParams(BaseModel):
    """Parameters for regex parser scoring function configuration."""

    aggregation_functions: Optional[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ] = None
    """Aggregation functions to apply to the scores of each row"""

    parsing_regexes: Optional[List[str]] = None
    """Regex to extract the answer from generated response"""

    type: Optional[Literal["regex_parser"]] = None


class ParamsBasicScoringFnParams(BaseModel):
    """Parameters for basic scoring function configuration."""

    aggregation_functions: Optional[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ] = None
    """Aggregation functions to apply to the scores of each row"""

    type: Optional[Literal["basic"]] = None


Params: TypeAlias = Annotated[
    Union[ParamsLlmAsJudgeScoringFnParams, ParamsRegexParserScoringFnParams, ParamsBasicScoringFnParams, None],
    PropertyInfo(discriminator="type"),
]


class ScoringFn(BaseModel):
    """A scoring function resource for evaluating model outputs."""

    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    return_type: ReturnType

    description: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Any additional metadata for this definition"""

    params: Optional[Params] = None
    """
    The parameters for the scoring function for benchmark eval, these can be
    overridden for app eval
    """

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["scoring_function"]] = None
