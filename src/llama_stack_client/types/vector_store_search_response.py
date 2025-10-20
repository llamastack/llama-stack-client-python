# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreSearchResponse", "Data", "DataContent"]


class DataContent(BaseModel):
    text: str
    """The actual text content"""

    type: Literal["text"]
    """Content type, currently only "text" is supported"""


class Data(BaseModel):
    content: List[DataContent]
    """List of content items matching the search query"""

    file_id: str
    """Unique identifier of the file containing the result"""

    filename: str
    """Name of the file containing the result"""

    score: float
    """Relevance score for this search result"""

    attributes: Optional[Dict[str, Union[str, float, bool]]] = None
    """(Optional) Key-value attributes associated with the file"""


class VectorStoreSearchResponse(BaseModel):
    data: List[Data]
    """List of search result objects"""

    has_more: bool
    """Whether there are more results available beyond this page"""

    object: str
    """Object type identifier for the search results page"""

    search_query: str
    """The original search query that was executed"""

    next_page: Optional[str] = None
    """(Optional) Token for retrieving the next page of results"""
