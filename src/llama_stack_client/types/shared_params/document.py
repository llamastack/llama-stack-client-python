# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interleaved_content_item import InterleavedContentItem

__all__ = [
    "Document",
    "Content",
    "ContentImageContentItem",
    "ContentImageContentItemImage",
    "ContentImageContentItemImageURL",
    "ContentTextContentItem",
    "ContentURL",
]


class ContentImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]
    """The URL string pointing to the resource"""


class ContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: ContentImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ContentImageContentItem(TypedDict, total=False):
    image: Required[ContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class ContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class ContentURL(TypedDict, total=False):
    uri: Required[str]
    """The URL string pointing to the resource"""


Content: TypeAlias = Union[
    str, ContentImageContentItem, ContentTextContentItem, Iterable[InterleavedContentItem], ContentURL
]


class Document(TypedDict, total=False):
    content: Required[Content]
    """The content of the document."""

    document_id: Required[str]
    """The unique identifier for the document."""

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """Additional metadata for the document."""

    mime_type: str
    """The MIME type of the document."""
