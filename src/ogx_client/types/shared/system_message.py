# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "SystemMessage",
    "Content",
    "ContentImageContentItem",
    "ContentImageContentItemImage",
    "ContentImageContentItemImageURL",
    "ContentTextContentItem",
    "ContentListImageContentItemTextContentItem",
    "ContentListImageContentItemTextContentItemImageContentItem",
    "ContentListImageContentItemTextContentItemImageContentItemImage",
    "ContentListImageContentItemTextContentItemImageContentItemImageURL",
    "ContentListImageContentItemTextContentItemTextContentItem",
]


class ContentImageContentItemImageURL(BaseModel):
    """A URL reference to external content."""

    uri: str


class ContentImageContentItemImage(BaseModel):
    """A URL or a base64 encoded string"""

    data: Optional[str] = None

    url: Optional[ContentImageContentItemImageURL] = None
    """A URL reference to external content."""


class ContentImageContentItem(BaseModel):
    """A image content item"""

    image: ContentImageContentItemImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ContentTextContentItem(BaseModel):
    """A text content item"""

    text: str

    type: Optional[Literal["text"]] = None


class ContentListImageContentItemTextContentItemImageContentItemImageURL(BaseModel):
    """A URL reference to external content."""

    uri: str


class ContentListImageContentItemTextContentItemImageContentItemImage(BaseModel):
    """A URL or a base64 encoded string"""

    data: Optional[str] = None

    url: Optional[ContentListImageContentItemTextContentItemImageContentItemImageURL] = None
    """A URL reference to external content."""


class ContentListImageContentItemTextContentItemImageContentItem(BaseModel):
    """A image content item"""

    image: ContentListImageContentItemTextContentItemImageContentItemImage
    """A URL or a base64 encoded string"""

    type: Optional[Literal["image"]] = None


class ContentListImageContentItemTextContentItemTextContentItem(BaseModel):
    """A text content item"""

    text: str

    type: Optional[Literal["text"]] = None


ContentListImageContentItemTextContentItem: TypeAlias = Annotated[
    Union[
        ContentListImageContentItemTextContentItemImageContentItem,
        ContentListImageContentItemTextContentItemTextContentItem,
    ],
    PropertyInfo(discriminator="type"),
]

Content: TypeAlias = Union[
    str, ContentImageContentItem, ContentTextContentItem, List[ContentListImageContentItemTextContentItem]
]


class SystemMessage(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Content
    """The content of the 'system prompt'.

    If multiple system messages are provided, they are concatenated. The underlying
    OGX code may also add other system messages.
    """

    role: Optional[Literal["system"]] = None
    """Must be 'system' to identify this as a system message."""
