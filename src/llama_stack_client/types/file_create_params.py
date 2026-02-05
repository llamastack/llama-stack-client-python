# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams", "ExpiresAfter"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to upload."""

    purpose: Required[Literal["assistants", "batch"]]
    """The intended purpose of the uploaded file."""

    expires_after: Optional[ExpiresAfter]
    """Control expiration of uploaded files."""


class ExpiresAfter(TypedDict, total=False):
    """Control expiration of uploaded files."""

    anchor: Required[Literal["created_at"]]
    """The anchor point for expiration, must be 'created_at'."""

    seconds: Required[int]
    """Seconds until expiration, between 3600 (1 hour) and 2592000 (30 days)."""
