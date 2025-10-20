# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["VectorStore", "FileCounts"]


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


class VectorStore(BaseModel):
    id: str
    """Unique identifier for the vector store"""

    created_at: int
    """Timestamp when the vector store was created"""

    file_counts: FileCounts
    """File processing status counts for the vector store"""

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Set of key-value pairs that can be attached to the vector store"""

    object: str
    """Object type identifier, always "vector_store" """

    status: str
    """Current status of the vector store"""

    usage_bytes: int
    """Storage space used by the vector store in bytes"""

    expires_after: Optional[Dict[str, Union[bool, float, str, List[builtins.object], builtins.object, None]]] = None
    """(Optional) Expiration policy for the vector store"""

    expires_at: Optional[int] = None
    """(Optional) Timestamp when the vector store will expire"""

    last_active_at: Optional[int] = None
    """(Optional) Timestamp of last activity on the vector store"""

    name: Optional[str] = None
    """(Optional) Name of the vector store"""
