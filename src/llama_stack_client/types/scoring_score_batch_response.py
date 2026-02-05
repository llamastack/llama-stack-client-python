# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .shared.scoring_result import ScoringResult

__all__ = ["ScoringScoreBatchResponse"]


class ScoringScoreBatchResponse(BaseModel):
    """Response from batch scoring operations on datasets."""

    results: Dict[str, ScoringResult]
    """A map of scoring function name to ScoringResult"""

    dataset_id: Optional[str] = None
    """(Optional) The identifier of the dataset that was scored"""
