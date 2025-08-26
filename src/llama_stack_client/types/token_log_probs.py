# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["TokenLogProbs"]


class TokenLogProbs(BaseModel):
    logprobs_by_token: Dict[str, float]
    """Dictionary mapping tokens to their log probabilities"""
