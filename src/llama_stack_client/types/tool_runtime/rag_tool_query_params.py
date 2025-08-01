# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..shared_params.query_config import QueryConfig
from ..shared_params.interleaved_content import InterleavedContent

__all__ = ["RagToolQueryParams"]


class RagToolQueryParams(TypedDict, total=False):
    content: Required[InterleavedContent]
    """The query content to search for in the indexed documents"""

    vector_db_ids: Required[List[str]]
    """List of vector database IDs to search within"""

    query_config: QueryConfig
    """(Optional) Configuration parameters for the query operation"""
