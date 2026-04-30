# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .vector_store import VectorStore

__all__ = ["ListVectorStoresResponse"]


class ListVectorStoresResponse(BaseModel):
    """Response from listing vector stores."""

    data: List[VectorStore]

    first_id: str

    has_more: bool

    last_id: str

    object: Optional[Literal["list"]] = None
