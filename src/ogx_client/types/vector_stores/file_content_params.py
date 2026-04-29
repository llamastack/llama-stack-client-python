# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileContentParams"]


class FileContentParams(TypedDict, total=False):
    vector_store_id: Required[str]
    """The vector store identifier."""

    include_embeddings: Optional[bool]
    """Include embedding vectors."""

    include_metadata: Optional[bool]
    """Include chunk metadata."""
