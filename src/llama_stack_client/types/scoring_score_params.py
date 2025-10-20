# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["ScoringScoreParams"]


class ScoringScoreParams(TypedDict, total=False):
    input_rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]
    """The rows to score."""

    scoring_functions: Required[Dict[str, Optional[ScoringFnParamsParam]]]
    """The scoring functions to use for the scoring."""
