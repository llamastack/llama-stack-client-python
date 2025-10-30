# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PromptUpdateParams"]


class PromptUpdateParams(TypedDict, total=False):
    prompt: Required[str]
    """The updated prompt text content."""

    set_as_default: Required[bool]
    """Set the new version as the default (default=True)."""

    version: Required[int]
    """The current version of the prompt being updated."""

    variables: SequenceNotStr[str]
    """Updated list of variable names that can be used in the prompt template."""
