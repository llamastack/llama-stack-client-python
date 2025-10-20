# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .vector_store import VectorStore

__all__ = ["ListVectorStoresResponse"]


class ListVectorStoresResponse(BaseModel):
    data: List[VectorStore]
    """List of vector store objects"""

    has_more: bool
    """Whether there are more vector stores available beyond this page"""

    object: str
    """Object type identifier, always "list" """

    first_id: Optional[str] = None
    """(Optional) ID of the first vector store in the list for pagination"""

    last_id: Optional[str] = None
    """(Optional) ID of the last vector store in the list for pagination"""
