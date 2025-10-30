# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..scoring_fn_params_param import ScoringFnParamsParam
from ..shared_params.agent_config import AgentConfig
from ..shared_params.system_message import SystemMessage
from ..shared_params.sampling_params import SamplingParams

__all__ = ["BenchmarkConfigParam", "EvalCandidate", "EvalCandidateModelCandidate", "EvalCandidateAgentCandidate"]


class EvalCandidateModelCandidate(TypedDict, total=False):
    model: Required[str]
    """The model ID to evaluate."""

    sampling_params: Required[SamplingParams]
    """The sampling parameters for the model."""

    type: Required[Literal["model"]]

    system_message: SystemMessage
    """(Optional) The system message providing instructions or context to the model."""


class EvalCandidateAgentCandidate(TypedDict, total=False):
    config: Required[AgentConfig]
    """The configuration for the agent candidate."""

    type: Required[Literal["agent"]]


EvalCandidate: TypeAlias = Union[EvalCandidateModelCandidate, EvalCandidateAgentCandidate]


class BenchmarkConfigParam(TypedDict, total=False):
    eval_candidate: Required[EvalCandidate]
    """The candidate to evaluate."""

    scoring_params: Required[Dict[str, ScoringFnParamsParam]]
    """
    Map between scoring function id and parameters for each scoring function you
    want to run
    """

    num_examples: int
    """(Optional) The number of examples to evaluate.

    If not provided, all examples in the dataset will be evaluated
    """
