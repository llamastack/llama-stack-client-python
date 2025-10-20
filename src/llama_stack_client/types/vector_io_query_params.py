# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.interleaved_content import InterleavedContent

__all__ = ["VectorIoQueryParams"]


class VectorIoQueryParams(TypedDict, total=False):
    query: Required[InterleavedContent]
    """The query to search for."""

    vector_db_id: Required[str]
    """The identifier of the vector database to query."""

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The parameters of the query."""
