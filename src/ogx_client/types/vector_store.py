# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStore", "FileCounts", "ExpiresAfter"]


class FileCounts(BaseModel):
    """File processing status counts for a vector store."""

    cancelled: int

    completed: int

    failed: int

    in_progress: int

    total: int


class ExpiresAfter(BaseModel):
    """Expiration policy for a vector store."""

    anchor: Literal["last_active_at"]
    """Anchor timestamp after which the expiration policy applies."""

    days: int
    """The number of days after the anchor time that the vector store will expire."""


class VectorStore(BaseModel):
    """OpenAI Vector Store object."""

    id: str

    created_at: int

    file_counts: FileCounts
    """File processing status counts for a vector store."""

    status: Literal["expired", "in_progress", "completed"]

    expires_after: Optional[ExpiresAfter] = None
    """Expiration policy for a vector store."""

    expires_at: Optional[int] = None

    last_active_at: Optional[int] = None

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    object: Optional[Literal["vector_store"]] = None

    usage_bytes: Optional[int] = None
