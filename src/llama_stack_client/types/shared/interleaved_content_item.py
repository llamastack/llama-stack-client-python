# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "InterleavedContentItem",
    "ImageContentItem",
    "ImageContentItemImage",
    "ImageContentItemImageURL",
    "TextContentItem",
]


class ImageContentItemImageURL(BaseModel):
    uri: str
    """The URL string pointing to the resource"""


class ImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[ImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ImageContentItem(BaseModel):
    image: ImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class TextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


InterleavedContentItem: TypeAlias = Annotated[
    Union[ImageContentItem, TextContentItem], PropertyInfo(discriminator="type")
]
