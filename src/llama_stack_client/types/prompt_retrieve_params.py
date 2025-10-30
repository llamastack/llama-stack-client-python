# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PromptRetrieveParams"]


class PromptRetrieveParams(TypedDict, total=False):
    version: int
    """The version of the prompt to get (defaults to latest)."""
