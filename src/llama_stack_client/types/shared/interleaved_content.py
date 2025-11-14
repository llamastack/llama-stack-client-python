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
    "InterleavedContent",
    "ImageContentItem",
    "ImageContentItemImage",
    "ImageContentItemImageURL",
    "TextContentItem",
    "ListImageContentItemTextContentItem",
    "ListImageContentItemTextContentItemImageContentItem",
    "ListImageContentItemTextContentItemImageContentItemImage",
    "ListImageContentItemTextContentItemImageContentItemImageURL",
    "ListImageContentItemTextContentItemTextContentItem",
]


class ImageContentItemImageURL(BaseModel):
    uri: str


class ImageContentItemImage(BaseModel):
    data: Optional[str] = None

    url: Optional[ImageContentItemImageURL] = None
    """A URL reference to external content."""


class ImageContentItem(BaseModel):
    image: ImageContentItemImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class TextContentItem(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ListImageContentItemTextContentItemImageContentItemImageURL(BaseModel):
    uri: str


class ListImageContentItemTextContentItemImageContentItemImage(BaseModel):
    data: Optional[str] = None

    url: Optional[ListImageContentItemTextContentItemImageContentItemImageURL] = None
    """A URL reference to external content."""


class ListImageContentItemTextContentItemImageContentItem(BaseModel):
    image: ListImageContentItemTextContentItemImageContentItemImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ListImageContentItemTextContentItemTextContentItem(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


ListImageContentItemTextContentItem: TypeAlias = Annotated[
    Union[ListImageContentItemTextContentItemImageContentItem, ListImageContentItemTextContentItemTextContentItem],
    PropertyInfo(discriminator="type"),
]

InterleavedContent: TypeAlias = Union[str, ImageContentItem, TextContentItem, List[ListImageContentItemTextContentItem]]
