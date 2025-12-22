# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

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


class ContentImageContentItemInputImageURL(BaseModel):
    """A URL reference to external content."""

    uri: str


class ContentImageContentItemInputImage(BaseModel):
    """A URL or a base64 encoded string"""

    data: Optional[str] = None

    url: Optional[ContentImageContentItemInputImageURL] = None
    """A URL reference to external content."""


class ContentImageContentItemInput(BaseModel):
    """A image content item"""

    image: ContentImageContentItemInputImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ContentTextContentItem(BaseModel):
    """A text content item"""

    text: str

    type: Optional[Literal["text"]] = None


class ContentListImageContentItemInputTextContentItemImageContentItemInputImageURL(BaseModel):
    """A URL reference to external content."""

    uri: str


class ContentListImageContentItemInputTextContentItemImageContentItemInputImage(BaseModel):
    """A URL or a base64 encoded string"""

    data: Optional[str] = None

    url: Optional[ContentListImageContentItemInputTextContentItemImageContentItemInputImageURL] = None
    """A URL reference to external content."""


class ContentListImageContentItemInputTextContentItemImageContentItemInput(BaseModel):
    """A image content item"""

    image: ContentListImageContentItemInputTextContentItemImageContentItemInputImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ContentListImageContentItemInputTextContentItemTextContentItem(BaseModel):
    """A text content item"""

    text: str

    type: Optional[Literal["text"]] = None


ContentListImageContentItemInputTextContentItem: TypeAlias = Annotated[
    Union[
        ContentListImageContentItemInputTextContentItemImageContentItemInput,
        ContentListImageContentItemInputTextContentItemTextContentItem,
    ],
    PropertyInfo(discriminator="type"),
]

Content: TypeAlias = Union[
    str, ContentImageContentItemInput, ContentTextContentItem, List[ContentListImageContentItemInputTextContentItem]
]


class SystemMessage(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Content
    """A image content item"""

    role: Optional[Literal["system"]] = None
