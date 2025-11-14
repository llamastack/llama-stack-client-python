# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = ["ScoringResult"]


class ScoringResult(BaseModel):
    aggregated_results: Dict[str, object]

    score_rows: List[Dict[str, object]]
