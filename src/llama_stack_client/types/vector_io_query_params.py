# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VectorIoQueryParams",
    "Query",
    "QueryImageContentItemInput",
    "QueryImageContentItemInputImage",
    "QueryImageContentItemInputImageURL",
    "QueryTextContentItem",
    "QueryListImageContentItemInputTextContentItem",
    "QueryListImageContentItemInputTextContentItemImageContentItemInput",
    "QueryListImageContentItemInputTextContentItemImageContentItemInputImage",
    "QueryListImageContentItemInputTextContentItemImageContentItemInputImageURL",
    "QueryListImageContentItemInputTextContentItemTextContentItem",
]


class VectorIoQueryParams(TypedDict, total=False):
    query: Required[Query]
    """A image content item"""

    vector_store_id: Required[str]

    params: Optional[Dict[str, object]]


class QueryImageContentItemInputImageURL(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]


class QueryImageContentItemInputImage(TypedDict, total=False):
    """A URL or a base64 encoded string"""

    data: Optional[str]

    url: Optional[QueryImageContentItemInputImageURL]
    """A URL reference to external content."""


class QueryImageContentItemInput(TypedDict, total=False):
    """A image content item"""

    image: Required[QueryImageContentItemInputImage]
    """A URL or a base64 encoded string"""

    type: Literal["image"]


class QueryTextContentItem(TypedDict, total=False):
    """A text content item"""

    text: Required[str]

    type: Literal["text"]


class QueryListImageContentItemInputTextContentItemImageContentItemInputImageURL(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]


class QueryListImageContentItemInputTextContentItemImageContentItemInputImage(TypedDict, total=False):
    """A URL or a base64 encoded string"""

    data: Optional[str]

    url: Optional[QueryListImageContentItemInputTextContentItemImageContentItemInputImageURL]
    """A URL reference to external content."""


class QueryListImageContentItemInputTextContentItemImageContentItemInput(TypedDict, total=False):
    """A image content item"""

    image: Required[QueryListImageContentItemInputTextContentItemImageContentItemInputImage]
    """A URL or a base64 encoded string"""

    type: Literal["image"]


class QueryListImageContentItemInputTextContentItemTextContentItem(TypedDict, total=False):
    """A text content item"""

    text: Required[str]

    type: Literal["text"]


QueryListImageContentItemInputTextContentItem: TypeAlias = Union[
    QueryListImageContentItemInputTextContentItemImageContentItemInput,
    QueryListImageContentItemInputTextContentItemTextContentItem,
]

Query: TypeAlias = Union[
    str, QueryImageContentItemInput, QueryTextContentItem, Iterable[QueryListImageContentItemInputTextContentItem]
]
