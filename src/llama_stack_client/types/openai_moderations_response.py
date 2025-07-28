# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["OpenAIModerationsResponse", "Result"]


class Result(BaseModel):
    categories: Dict[str, bool]
    """A list of the categories, and whether they are flagged or not."""

    category_applied_input_types: Dict[str, List[str]]

    category_messages: Dict[str, str]

    category_scores: Dict[str, float]
    """A list of the categories along with their scores as predicted by model."""

    flagged: bool
    """Whether any of the below categories are flagged."""


class OpenAIModerationsResponse(BaseModel):
    id: str
    """The unique identifier for the moderation request."""

    model: str
    """The model used to generate the moderation results."""

    results: List[Result]
    """A list of moderation objects"""
