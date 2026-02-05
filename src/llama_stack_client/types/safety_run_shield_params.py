# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SafetyRunShieldParams",
    "Message",
    "MessageOpenAIUserMessageParamInput",
    "MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile",
    "MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam",
    "MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam",
    "MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL",
    "MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile",
    "MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile",
    "MessageOpenAISystemMessageParam",
    "MessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "MessageOpenAIAssistantMessageParamInput",
    "MessageOpenAIAssistantMessageParamInputContentListOpenAIChatCompletionContentPartTextParam",
    "MessageOpenAIAssistantMessageParamInputToolCall",
    "MessageOpenAIAssistantMessageParamInputToolCallFunction",
    "MessageOpenAIToolMessageParam",
    "MessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "MessageOpenAIDeveloperMessageParam",
    "MessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam",
]


class SafetyRunShieldParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to run the shield on"""

    shield_id: Required[str]
    """The identifier of the shield to run"""


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """Must be 'text' to identify this as text content."""


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    TypedDict, total=False
):
    """Image URL specification and processing details."""

    url: Required[str]
    """URL of the image to include in the message."""

    detail: Optional[Literal["low", "high", "auto"]]
    """Level of detail for image processing. Can be 'low', 'high', or 'auto'."""


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    TypedDict, total=False
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: Required[
        MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    ]
    """Image URL specification and processing details."""

    type: Literal["image_url"]
    """Must be 'image_url' to identify this as image content."""


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    TypedDict, total=False
):
    """File specification."""

    file_data: Optional[str]
    """Base64-encoded file data."""

    file_id: Optional[str]
    """ID of an uploaded file."""

    filename: Optional[str]
    """Name of the file."""


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    TypedDict, total=False
):
    file: Required[
        MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile
    ]
    """File specification."""

    type: Literal["file"]
    """Must be 'file' to identify this as file content."""


MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile: TypeAlias = Union[
    MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam,
    MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam,
    MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile,
]


class MessageOpenAIUserMessageParamInput(TypedDict, total=False):
    """A message from the user in an OpenAI-compatible chat completion request."""

    content: Required[
        Union[
            str,
            Iterable[
                MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
            ],
        ]
    ]
    """The content of the message, which can include text and other media."""

    name: Optional[str]
    """The name of the user message participant."""

    role: Literal["user"]
    """Must be 'user' to identify this as a user message."""


class MessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """Must be 'text' to identify this as text content."""


class MessageOpenAISystemMessageParam(TypedDict, total=False):
    """A system message providing instructions or context to the model."""

    content: Required[
        Union[str, Iterable[MessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    ]
    """The content of the 'system prompt'.

    If multiple system messages are provided, they are concatenated.
    """

    name: Optional[str]
    """The name of the system message participant."""

    role: Literal["system"]
    """Must be 'system' to identify this as a system message."""


class MessageOpenAIAssistantMessageParamInputContentListOpenAIChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """Must be 'text' to identify this as text content."""


class MessageOpenAIAssistantMessageParamInputToolCallFunction(TypedDict, total=False):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str]
    """Arguments to pass to the function as a JSON string."""

    name: Optional[str]
    """Name of the function to call."""


class MessageOpenAIAssistantMessageParamInputToolCall(TypedDict, total=False):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str]
    """Unique identifier for the tool call."""

    function: Optional[MessageOpenAIAssistantMessageParamInputToolCallFunction]
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int]
    """Index of the tool call in the list."""

    type: Literal["function"]
    """Must be 'function' to identify this as a function call."""


class MessageOpenAIAssistantMessageParamInput(TypedDict, total=False):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str, Iterable[MessageOpenAIAssistantMessageParamInputContentListOpenAIChatCompletionContentPartTextParam], None
    ]
    """The content of the model's response."""

    name: Optional[str]
    """The name of the assistant message participant."""

    role: Literal["assistant"]
    """Must be 'assistant' to identify this as the model's response."""

    tool_calls: Optional[Iterable[MessageOpenAIAssistantMessageParamInputToolCall]]
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class MessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """Must be 'text' to identify this as text content."""


class MessageOpenAIToolMessageParam(TypedDict, total=False):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Required[
        Union[str, Iterable[MessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    ]
    """The response content from the tool."""

    tool_call_id: Required[str]
    """Unique identifier for the tool call this response is for."""

    role: Literal["tool"]
    """Must be 'tool' to identify this as a tool response."""


class MessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """Must be 'text' to identify this as text content."""


class MessageOpenAIDeveloperMessageParam(TypedDict, total=False):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Required[
        Union[str, Iterable[MessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    ]
    """The content of the developer message."""

    name: Optional[str]
    """The name of the developer message participant."""

    role: Literal["developer"]
    """Must be 'developer' to identify this as a developer message."""


Message: TypeAlias = Union[
    MessageOpenAIUserMessageParamInput,
    MessageOpenAISystemMessageParam,
    MessageOpenAIAssistantMessageParamInput,
    MessageOpenAIToolMessageParam,
    MessageOpenAIDeveloperMessageParam,
]
