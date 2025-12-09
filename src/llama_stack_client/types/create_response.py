# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["CreateResponse", "Result"]


class Result(BaseModel):
    """A moderation object."""

    flagged: bool

    categories: Optional[Dict[str, bool]] = None

    category_applied_input_types: Optional[Dict[str, List[str]]] = None

    category_scores: Optional[Dict[str, float]] = None

    metadata: Optional[Dict[str, object]] = None

    user_message: Optional[str] = None


class CreateResponse(BaseModel):
    """A moderation object."""

    id: str

    model: str

    results: List[Result]
