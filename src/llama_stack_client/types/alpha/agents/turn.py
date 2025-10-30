# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ..tool_execution_step import ToolExecutionStep
from ...shared.user_message import UserMessage
from ..memory_retrieval_step import MemoryRetrievalStep
from ...shared.completion_message import CompletionMessage
from ...shared.tool_response_message import ToolResponseMessage
from ...shared.interleaved_content_item import InterleavedContentItem

__all__ = [
    "Turn",
    "InputMessage",
    "Step",
    "OutputAttachment",
    "OutputAttachmentContent",
    "OutputAttachmentContentImageContentItem",
    "OutputAttachmentContentImageContentItemImage",
    "OutputAttachmentContentImageContentItemImageURL",
    "OutputAttachmentContentTextContentItem",
    "OutputAttachmentContentURL",
]

InputMessage: TypeAlias = Union[UserMessage, ToolResponseMessage]

Step: TypeAlias = Annotated[
    Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep],
    PropertyInfo(discriminator="step_type"),
]


class OutputAttachmentContentImageContentItemImageURL(BaseModel):
    uri: str
    """The URL string pointing to the resource"""


class OutputAttachmentContentImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[OutputAttachmentContentImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class OutputAttachmentContentImageContentItem(BaseModel):
    image: OutputAttachmentContentImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class OutputAttachmentContentTextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class OutputAttachmentContentURL(BaseModel):
    uri: str
    """The URL string pointing to the resource"""


OutputAttachmentContent: TypeAlias = Union[
    str,
    OutputAttachmentContentImageContentItem,
    OutputAttachmentContentTextContentItem,
    List[InterleavedContentItem],
    OutputAttachmentContentURL,
]


class OutputAttachment(BaseModel):
    content: OutputAttachmentContent
    """The content of the attachment."""

    mime_type: str
    """The MIME type of the attachment."""


class Turn(BaseModel):
    input_messages: List[InputMessage]
    """List of messages that initiated this turn"""

    output_message: CompletionMessage
    """The model's generated response containing content and metadata"""

    session_id: str
    """Unique identifier for the conversation session"""

    started_at: datetime
    """Timestamp when the turn began"""

    steps: List[Step]
    """Ordered list of processing steps executed during this turn"""

    turn_id: str
    """Unique identifier for the turn within a session"""

    completed_at: Optional[datetime] = None
    """(Optional) Timestamp when the turn finished, if completed"""

    output_attachments: Optional[List[OutputAttachment]] = None
    """(Optional) Files or media attached to the agent's response"""
