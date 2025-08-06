# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["ModerationCreateParams"]


class ModerationCreateParams(TypedDict, total=False):
    input: Required[Union[str, List[str]]]
    """Input (or inputs) to classify.

    Can be a single string, an array of strings, or an array of multi-modal input
    objects similar to other models.
    """

    model: Required[str]
    """The content moderation model you would like to use."""
