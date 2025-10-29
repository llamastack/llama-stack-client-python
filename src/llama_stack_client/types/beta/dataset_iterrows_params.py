# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DatasetIterrowsParams"]


class DatasetIterrowsParams(TypedDict, total=False):
    limit: int
    """The number of rows to get."""

    start_index: int
    """Index into dataset for the first row to get. Get all rows if None."""
