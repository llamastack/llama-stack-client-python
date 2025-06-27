# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    limit: int
    """The number of sessions to return."""

    start_index: int
    """The index to start the pagination from."""
