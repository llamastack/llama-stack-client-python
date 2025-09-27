# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    expires_after_anchor: Required[Optional[str]]

    expires_after_seconds: Required[Optional[int]]

    file: Required[FileTypes]

    purpose: Required[Literal["assistants", "batch"]]
    """Valid purpose values for OpenAI Files API."""
