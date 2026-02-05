# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = ["ScoringResult"]


class ScoringResult(BaseModel):
    """A scoring result for a single row."""

    aggregated_results: Dict[str, object]
    """Map of metric name to aggregated value"""

    score_rows: List[Dict[str, object]]
    """The scoring result for each row. Each row is a map of column name to value."""
