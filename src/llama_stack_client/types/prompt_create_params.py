# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """The prompt text content with variable placeholders."""

    variables: SequenceNotStr[str]
    """List of variable names that can be used in the prompt template."""
