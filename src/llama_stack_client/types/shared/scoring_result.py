# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from ..._models import BaseModel

__all__ = ["ScoringResult"]


class ScoringResult(BaseModel):
    aggregated_results: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Map of metric name to aggregated value"""

    score_rows: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """The scoring result for each row. Each row is a map of column name to value."""
