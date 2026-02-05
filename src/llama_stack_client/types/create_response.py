# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["CreateResponse", "Result"]


class Result(BaseModel):
    """A moderation result object containing flagged status and category information."""

    flagged: bool
    """Whether any of the below categories are flagged"""

    categories: Optional[Dict[str, bool]] = None
    """A dictionary of the categories, and whether they are flagged or not"""

    category_applied_input_types: Optional[Dict[str, List[str]]] = None
    """
    A dictionary of the categories along with the input type(s) that the score
    applies to
    """

    category_scores: Optional[Dict[str, float]] = None
    """A dictionary of the categories along with their scores as predicted by model"""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata about the moderation"""

    user_message: Optional[str] = None
    """A message to convey to the user about the moderation result"""


class CreateResponse(BaseModel):
    """A moderation object containing the results of content classification."""

    id: str
    """The unique identifier for the moderation request"""

    model: str
    """The model used to generate the moderation results"""

    results: List[Result]
    """A list of moderation result objects"""
