# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["ScoringScoreBatchParams"]


class ScoringScoreBatchParams(TypedDict, total=False):
    dataset_id: Required[str]
    """The ID of the dataset to score."""

    save_results_dataset: Required[bool]
    """Whether to save the results to a dataset."""

    scoring_functions: Required[Dict[str, Optional[ScoringFnParamsParam]]]
    """The scoring functions to use for the scoring."""
