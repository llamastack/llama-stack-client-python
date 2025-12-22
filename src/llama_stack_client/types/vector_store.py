# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["VectorStore", "FileCounts"]


class FileCounts(BaseModel):
    """File processing status counts for a vector store."""

    cancelled: int

    completed: int

    failed: int

    in_progress: int

    total: int


class VectorStore(BaseModel):
    """OpenAI Vector Store object."""

    id: str

    created_at: int

    file_counts: FileCounts
    """File processing status counts for a vector store."""

    expires_after: Optional[Dict[str, object]] = None

    expires_at: Optional[int] = None

    last_active_at: Optional[int] = None

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    object: Optional[str] = None

    status: Optional[str] = None

    usage_bytes: Optional[int] = None
