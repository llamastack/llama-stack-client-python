# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SafetyRunShieldParams",
    "Message",
    "MessageOpenAIUserMessageParam",
    "MessageOpenAIUserMessageParamContentUnionMember1",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIFile",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile",
    "MessageOpenAISystemMessageParam",
    "MessageOpenAISystemMessageParamContentUnionMember1",
    "MessageOpenAIAssistantMessageParam",
    "MessageOpenAIAssistantMessageParamContentUnionMember1",
    "MessageOpenAIAssistantMessageParamToolCall",
    "MessageOpenAIAssistantMessageParamToolCallFunction",
    "MessageOpenAIToolMessageParam",
    "MessageOpenAIToolMessageParamContentUnionMember1",
    "MessageOpenAIDeveloperMessageParam",
    "MessageOpenAIDeveloperMessageParamContentUnionMember1",
]


class SafetyRunShieldParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to run the shield on."""

    params: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The parameters of the shield."""

    shield_id: Required[str]
    """The identifier of the shield to run."""


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    text: Required[str]
    """The text content of the message"""

    type: Required[Literal["text"]]
    """Must be "text" to identify this as text content"""


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    TypedDict, total=False
):
    url: Required[str]
    """URL of the image to include in the message"""

    detail: str
    """(Optional) Level of detail for image processing.

    Can be "low", "high", or "auto"
    """


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    image_url: Required[
        MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    ]
    """Image URL specification and processing details"""

    type: Required[Literal["image_url"]]
    """Must be "image_url" to identify this as image content"""


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile(TypedDict, total=False):
    file_data: str

    file_id: str

    filename: str


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIFile(TypedDict, total=False):
    file: Required[MessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile]

    type: Required[Literal["file"]]


MessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Union[
    MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
    MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    MessageOpenAIUserMessageParamContentUnionMember1OpenAIFile,
]


class MessageOpenAIUserMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAIUserMessageParamContentUnionMember1]]]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""

    name: str
    """(Optional) The name of the user message participant."""


class MessageOpenAISystemMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]
    """The text content of the message"""

    type: Required[Literal["text"]]
    """Must be "text" to identify this as text content"""


class MessageOpenAISystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAISystemMessageParamContentUnionMember1]]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""

    name: str
    """(Optional) The name of the system message participant."""


class MessageOpenAIAssistantMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]
    """The text content of the message"""

    type: Required[Literal["text"]]
    """Must be "text" to identify this as text content"""


class MessageOpenAIAssistantMessageParamToolCallFunction(TypedDict, total=False):
    arguments: str
    """(Optional) Arguments to pass to the function as a JSON string"""

    name: str
    """(Optional) Name of the function to call"""


class MessageOpenAIAssistantMessageParamToolCall(TypedDict, total=False):
    type: Required[Literal["function"]]
    """Must be "function" to identify this as a function call"""

    id: str
    """(Optional) Unique identifier for the tool call"""

    function: MessageOpenAIAssistantMessageParamToolCallFunction
    """(Optional) Function call details"""

    index: int
    """(Optional) Index of the tool call in the list"""


class MessageOpenAIAssistantMessageParam(TypedDict, total=False):
    role: Required[Literal["assistant"]]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, Iterable[MessageOpenAIAssistantMessageParamContentUnionMember1]]
    """The content of the model's response"""

    name: str
    """(Optional) The name of the assistant message participant."""

    tool_calls: Iterable[MessageOpenAIAssistantMessageParamToolCall]
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class MessageOpenAIToolMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]
    """The text content of the message"""

    type: Required[Literal["text"]]
    """Must be "text" to identify this as text content"""


class MessageOpenAIToolMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAIToolMessageParamContentUnionMember1]]]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: Required[str]
    """Unique identifier for the tool call this response is for"""


class MessageOpenAIDeveloperMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]
    """The text content of the message"""

    type: Required[Literal["text"]]
    """Must be "text" to identify this as text content"""


class MessageOpenAIDeveloperMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAIDeveloperMessageParamContentUnionMember1]]]
    """The content of the developer message"""

    role: Required[Literal["developer"]]
    """Must be "developer" to identify this as a developer message"""

    name: str
    """(Optional) The name of the developer message participant."""


Message: TypeAlias = Union[
    MessageOpenAIUserMessageParam,
    MessageOpenAISystemMessageParam,
    MessageOpenAIAssistantMessageParam,
    MessageOpenAIToolMessageParam,
    MessageOpenAIDeveloperMessageParam,
]
