# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VectorStoreFileBatches", "FileCounts"]


class FileCounts(BaseModel):
    cancelled: int
    """Number of files that had their processing cancelled"""

    completed: int
    """Number of files that have been successfully processed"""

    failed: int
    """Number of files that failed to process"""

    in_progress: int
    """Number of files currently being processed"""

    total: int
    """Total number of files in the vector store"""


class VectorStoreFileBatches(BaseModel):
    id: str
    """Unique identifier for the file batch"""

    created_at: int
    """Timestamp when the file batch was created"""

    file_counts: FileCounts
    """File processing status counts for the batch"""

    object: str
    """Object type identifier, always "vector_store.file_batch" """

    status: Literal["completed", "in_progress", "cancelled", "failed"]
    """Current processing status of the file batch"""

    vector_store_id: str
    """ID of the vector store containing the file batch"""
