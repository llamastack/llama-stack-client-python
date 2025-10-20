# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .scoring_fn_params import ScoringFnParams

__all__ = ["ScoringFn", "ReturnType"]


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


class ScoringFn(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    return_type: ReturnType

    type: Literal["scoring_function"]
    """The resource type, always scoring_function"""

    description: Optional[str] = None

    params: Optional[ScoringFnParams] = None
    """Parameters for LLM-as-judge scoring function configuration."""

    provider_resource_id: Optional[str] = None
