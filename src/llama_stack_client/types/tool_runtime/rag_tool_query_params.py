# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.query_config import QueryConfig
from ..shared_params.interleaved_content import InterleavedContent

__all__ = ["RagToolQueryParams"]


class RagToolQueryParams(TypedDict, total=False):
    content: Required[InterleavedContent]
    """The query content to search for in the indexed documents"""

    vector_db_ids: Required[SequenceNotStr[str]]
    """List of vector database IDs to search within"""

    query_config: QueryConfig
    """(Optional) Configuration parameters for the query operation"""
