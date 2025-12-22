# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VectorStoreFileBatches", "FileCounts"]


class FileCounts(BaseModel):
    """File processing status counts for a vector store."""

    cancelled: int

    completed: int

    failed: int

    in_progress: int

    total: int


class VectorStoreFileBatches(BaseModel):
    """OpenAI Vector Store File Batch object."""

    id: str

    created_at: int

    file_counts: FileCounts
    """File processing status counts for a vector store."""

    status: Literal["completed", "in_progress", "cancelled", "failed"]

    vector_store_id: str

    object: Optional[str] = None
