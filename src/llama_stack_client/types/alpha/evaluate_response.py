# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel
from ..shared.scoring_result import ScoringResult

__all__ = ["EvaluateResponse"]


class EvaluateResponse(BaseModel):
    """The response from an evaluation."""

    generations: List[Dict[str, object]]

    scores: Dict[str, ScoringResult]
