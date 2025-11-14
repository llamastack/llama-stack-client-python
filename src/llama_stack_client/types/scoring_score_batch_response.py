# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .shared.scoring_result import ScoringResult

__all__ = ["ScoringScoreBatchResponse"]


class ScoringScoreBatchResponse(BaseModel):
    results: Dict[str, ScoringResult]

    dataset_id: Optional[str] = None
