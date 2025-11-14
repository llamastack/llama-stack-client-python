# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PromptUpdateParams"]


class PromptUpdateParams(TypedDict, total=False):
    prompt: Required[str]

    version: Required[int]

    set_as_default: bool

    variables: Optional[SequenceNotStr[str]]
