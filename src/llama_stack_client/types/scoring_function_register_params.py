# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["ScoringFunctionRegisterParams", "ReturnType"]


class ScoringFunctionRegisterParams(TypedDict, total=False):
    description: Required[str]
    """The description of the scoring function."""

    return_type: Required[ReturnType]

    scoring_fn_id: Required[str]
    """The ID of the scoring function to register."""

    params: ScoringFnParamsParam
    """
    The parameters for the scoring function for benchmark eval, these can be
    overridden for app eval.
    """

    provider_id: str
    """The ID of the provider to use for the scoring function."""

    provider_scoring_fn_id: str
    """The ID of the provider scoring function to use for the scoring function."""


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
