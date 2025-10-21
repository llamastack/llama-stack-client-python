# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.document import Document

__all__ = ["RagToolInsertParams"]


class RagToolInsertParams(TypedDict, total=False):
    chunk_size_in_tokens: Required[int]
    """(Optional) Size in tokens for document chunking during indexing"""

    documents: Required[Iterable[Document]]
    """List of documents to index in the RAG system"""

    vector_db_id: Required[str]
    """ID of the vector database to store the document embeddings"""
