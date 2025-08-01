# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: str
    """(Optional) A cursor for use in pagination.

    `after` is an object ID that defines your place in the list.
    """

    before: str
    """(Optional) A cursor for use in pagination.

    `before` is an object ID that defines your place in the list.
    """

    filter: Literal["completed", "in_progress", "cancelled", "failed"]
    """
    (Optional) Filter by file status to only return files with the specified status.
    """

    limit: int
    """(Optional) A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """

    order: str
    """(Optional) Sort order by the `created_at` timestamp of the objects.

    `asc` for ascending order and `desc` for descending order.
    """
