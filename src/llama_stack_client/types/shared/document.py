# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
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


class ContentImageContentItemImageURL(BaseModel):
    uri: str
    """The URL string pointing to the resource"""


class ContentImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[ContentImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ContentImageContentItem(BaseModel):
    image: ContentImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class ContentTextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class ContentURL(BaseModel):
    uri: str
    """The URL string pointing to the resource"""


Content: TypeAlias = Union[
    str, ContentImageContentItem, ContentTextContentItem, List[InterleavedContentItem], ContentURL
]


class Document(BaseModel):
    content: Content
    """The content of the document."""

    document_id: str
    """The unique identifier for the document."""

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Additional metadata for the document."""

    mime_type: Optional[str] = None
    """The MIME type of the document."""
