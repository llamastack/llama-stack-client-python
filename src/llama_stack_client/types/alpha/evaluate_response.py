# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from ..._models import BaseModel
from ..shared.scoring_result import ScoringResult

__all__ = ["EvaluateResponse"]


class EvaluateResponse(BaseModel):
    generations: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """The generations from the evaluation."""

    scores: Dict[str, ScoringResult]
    """The scores from the evaluation."""
