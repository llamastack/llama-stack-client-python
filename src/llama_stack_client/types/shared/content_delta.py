# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .tool_call import ToolCall

__all__ = ["ContentDelta", "TextDelta", "ImageDelta", "ToolCallDelta", "ToolCallDeltaToolCall"]


class TextDelta(BaseModel):
    text: str
    """The incremental text content"""

    type: Literal["text"]
    """Discriminator type of the delta. Always "text" """


class ImageDelta(BaseModel):
    image: str
    """The incremental image data as bytes"""

    type: Literal["image"]
    """Discriminator type of the delta. Always "image" """


ToolCallDeltaToolCall: TypeAlias = Union[str, ToolCall]


class ToolCallDelta(BaseModel):
    parse_status: Literal["started", "in_progress", "failed", "succeeded"]
    """Current parsing status of the tool call"""

    tool_call: ToolCallDeltaToolCall
    """Either an in-progress tool call string or the final parsed tool call"""

    type: Literal["tool_call"]
    """Discriminator type of the delta. Always "tool_call" """


ContentDelta: TypeAlias = Annotated[Union[TextDelta, ImageDelta, ToolCallDelta], PropertyInfo(discriminator="type")]
