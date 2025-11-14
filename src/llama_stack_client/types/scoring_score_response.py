# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel
from .shared.scoring_result import ScoringResult

__all__ = ["ScoringScoreResponse"]


class ScoringScoreResponse(BaseModel):
    results: Dict[str, ScoringResult]
