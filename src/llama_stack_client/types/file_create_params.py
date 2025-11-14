# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams", "ExpiresAfter"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]

    purpose: Required[Literal["assistants", "batch"]]
    """Valid purpose values for OpenAI Files API."""

    expires_after: Optional[ExpiresAfter]
    """Control expiration of uploaded files.

    Params:

    - anchor, must be "created_at"
    - seconds, must be int between 3600 and 2592000 (1 hour to 30 days)
    """


class ExpiresAfter(TypedDict, total=False):
    anchor: Required[Literal["created_at"]]

    seconds: Required[int]
