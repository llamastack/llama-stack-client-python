# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PromptUpdateParams"]


class PromptUpdateParams(TypedDict, total=False):
    prompt: Required[str]
    """The updated prompt text content."""

    version: Required[int]
    """The current version of the prompt being updated."""

    set_as_default: bool
    """Set the new version as the default (default=True)."""

    variables: Optional[SequenceNotStr[str]]
    """Updated list of variable names that can be used in the prompt template."""
