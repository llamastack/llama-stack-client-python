# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .vector_store_file import VectorStoreFile

__all__ = ["ListVectorStoreFilesInBatchResponse"]


class ListVectorStoreFilesInBatchResponse(BaseModel):
    data: List[VectorStoreFile]
    """List of vector store file objects in the batch"""

    has_more: bool
    """Whether there are more files available beyond this page"""

    object: str
    """Object type identifier, always "list" """

    first_id: Optional[str] = None
    """(Optional) ID of the first file in the list for pagination"""

    last_id: Optional[str] = None
    """(Optional) ID of the last file in the list for pagination"""
