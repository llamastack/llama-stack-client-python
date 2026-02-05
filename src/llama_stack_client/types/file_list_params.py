# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: Optional[str]
    """A cursor for pagination. Returns files after this ID."""

    limit: Optional[int]
    """Maximum number of files to return (1-10,000)."""

    order: Optional[Literal["asc", "desc"]]
    """Sort order for paginated responses."""

    purpose: Optional[Literal["assistants", "batch"]]
    """Valid purpose values for OpenAI Files API."""
