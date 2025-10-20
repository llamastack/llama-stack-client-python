# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileBatchListFilesParams"]


class FileBatchListFilesParams(TypedDict, total=False):
    vector_store_id: Required[str]

    after: str
    """A cursor for use in pagination.

    `after` is an object ID that defines your place in the list.
    """

    before: str
    """A cursor for use in pagination.

    `before` is an object ID that defines your place in the list.
    """

    filter: str
    """Filter by file status. One of in_progress, completed, failed, cancelled."""

    limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """

    order: str
    """Sort order by the `created_at` timestamp of the objects.

    `asc` for ascending order and `desc` for descending order.
    """
