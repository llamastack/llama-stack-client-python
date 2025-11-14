# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ToolInvocationResult",
    "Content",
    "ContentImageContentItemOutput",
    "ContentImageContentItemOutputImage",
    "ContentImageContentItemOutputImageURL",
    "ContentTextContentItem",
    "ContentListImageContentItemOutputTextContentItem",
    "ContentListImageContentItemOutputTextContentItemImageContentItemOutput",
    "ContentListImageContentItemOutputTextContentItemImageContentItemOutputImage",
    "ContentListImageContentItemOutputTextContentItemImageContentItemOutputImageURL",
    "ContentListImageContentItemOutputTextContentItemTextContentItem",
]


class ContentImageContentItemOutputImageURL(BaseModel):
    uri: str


class ContentImageContentItemOutputImage(BaseModel):
    data: Optional[str] = None

    url: Optional[ContentImageContentItemOutputImageURL] = None
    """A URL reference to external content."""


class ContentImageContentItemOutput(BaseModel):
    image: ContentImageContentItemOutputImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ContentTextContentItem(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentListImageContentItemOutputTextContentItemImageContentItemOutputImageURL(BaseModel):
    uri: str


class ContentListImageContentItemOutputTextContentItemImageContentItemOutputImage(BaseModel):
    data: Optional[str] = None

    url: Optional[ContentListImageContentItemOutputTextContentItemImageContentItemOutputImageURL] = None
    """A URL reference to external content."""


class ContentListImageContentItemOutputTextContentItemImageContentItemOutput(BaseModel):
    image: ContentListImageContentItemOutputTextContentItemImageContentItemOutputImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ContentListImageContentItemOutputTextContentItemTextContentItem(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


ContentListImageContentItemOutputTextContentItem: TypeAlias = Annotated[
    Union[
        ContentListImageContentItemOutputTextContentItemImageContentItemOutput,
        ContentListImageContentItemOutputTextContentItemTextContentItem,
    ],
    PropertyInfo(discriminator="type"),
]

Content: TypeAlias = Union[
    str,
    ContentImageContentItemOutput,
    ContentTextContentItem,
    List[ContentListImageContentItemOutputTextContentItem],
    None,
]


class ToolInvocationResult(BaseModel):
    content: Optional[Content] = None
    """A image content item"""

    error_code: Optional[int] = None

    error_message: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
