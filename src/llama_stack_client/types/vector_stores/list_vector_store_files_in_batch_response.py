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
    """Response from listing files in a vector store file batch."""

    data: List[VectorStoreFile]

    first_id: Optional[str] = None

    has_more: Optional[bool] = None

    last_id: Optional[str] = None

    object: Optional[str] = None
