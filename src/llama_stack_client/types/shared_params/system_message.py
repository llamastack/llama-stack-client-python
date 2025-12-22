# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SystemMessage",
    "Content",
    "ContentImageContentItemInput",
    "ContentImageContentItemInputImage",
    "ContentImageContentItemInputImageURL",
    "ContentTextContentItem",
    "ContentListImageContentItemInputTextContentItem",
    "ContentListImageContentItemInputTextContentItemImageContentItemInput",
    "ContentListImageContentItemInputTextContentItemImageContentItemInputImage",
    "ContentListImageContentItemInputTextContentItemImageContentItemInputImageURL",
    "ContentListImageContentItemInputTextContentItemTextContentItem",
]


class ContentImageContentItemInputImageURL(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]


class ContentImageContentItemInputImage(TypedDict, total=False):
    """A URL or a base64 encoded string"""

    data: Optional[str]

    url: Optional[ContentImageContentItemInputImageURL]
    """A URL reference to external content."""


class ContentImageContentItemInput(TypedDict, total=False):
    """A image content item"""

    image: Required[ContentImageContentItemInputImage]
    """A URL or a base64 encoded string"""

    type: Literal["image"]


class ContentTextContentItem(TypedDict, total=False):
    """A text content item"""

    text: Required[str]

    type: Literal["text"]


class ContentListImageContentItemInputTextContentItemImageContentItemInputImageURL(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]


class ContentListImageContentItemInputTextContentItemImageContentItemInputImage(TypedDict, total=False):
    """A URL or a base64 encoded string"""

    data: Optional[str]

    url: Optional[ContentListImageContentItemInputTextContentItemImageContentItemInputImageURL]
    """A URL reference to external content."""


class ContentListImageContentItemInputTextContentItemImageContentItemInput(TypedDict, total=False):
    """A image content item"""

    image: Required[ContentListImageContentItemInputTextContentItemImageContentItemInputImage]
    """A URL or a base64 encoded string"""

    type: Literal["image"]


class ContentListImageContentItemInputTextContentItemTextContentItem(TypedDict, total=False):
    """A text content item"""

    text: Required[str]

    type: Literal["text"]


ContentListImageContentItemInputTextContentItem: TypeAlias = Union[
    ContentListImageContentItemInputTextContentItemImageContentItemInput,
    ContentListImageContentItemInputTextContentItemTextContentItem,
]

Content: TypeAlias = Union[
    str, ContentImageContentItemInput, ContentTextContentItem, Iterable[ContentListImageContentItemInputTextContentItem]
]


class SystemMessage(TypedDict, total=False):
    """A system message providing instructions or context to the model."""

    content: Required[Content]
    """A image content item"""

    role: Literal["system"]
