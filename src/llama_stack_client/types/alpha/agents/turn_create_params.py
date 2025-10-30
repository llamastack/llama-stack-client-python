# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...shared_params.user_message import UserMessage
from ...shared_params.tool_response_message import ToolResponseMessage
from ...shared_params.interleaved_content_item import InterleavedContentItem

__all__ = [
    "TurnCreateParamsBase",
    "Message",
    "Document",
    "DocumentContent",
    "DocumentContentImageContentItem",
    "DocumentContentImageContentItemImage",
    "DocumentContentImageContentItemImageURL",
    "DocumentContentTextContentItem",
    "DocumentContentURL",
    "ToolConfig",
    "Toolgroup",
    "ToolgroupAgentToolGroupWithArgs",
    "TurnCreateParamsNonStreaming",
    "TurnCreateParamsStreaming",
]


class TurnCreateParamsBase(TypedDict, total=False):
    agent_id: Required[str]

    messages: Required[Iterable[Message]]
    """List of messages to start the turn with."""

    documents: Iterable[Document]
    """(Optional) List of documents to create the turn with."""

    tool_config: ToolConfig
    """
    (Optional) The tool configuration to create the turn with, will be used to
    override the agent's tool_config.
    """

    toolgroups: SequenceNotStr[Toolgroup]
    """
    (Optional) List of toolgroups to create the turn with, will be used in addition
    to the agent's config toolgroups for the request.
    """


Message: TypeAlias = Union[UserMessage, ToolResponseMessage]


class DocumentContentImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]
    """The URL string pointing to the resource"""


class DocumentContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: DocumentContentImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class DocumentContentImageContentItem(TypedDict, total=False):
    image: Required[DocumentContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class DocumentContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class DocumentContentURL(TypedDict, total=False):
    uri: Required[str]
    """The URL string pointing to the resource"""


DocumentContent: TypeAlias = Union[
    str,
    DocumentContentImageContentItem,
    DocumentContentTextContentItem,
    Iterable[InterleavedContentItem],
    DocumentContentURL,
]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]
    """The content of the document."""

    mime_type: Required[str]
    """The MIME type of the document."""


class ToolConfig(TypedDict, total=False):
    system_message_behavior: Literal["append", "replace"]
    """(Optional) Config for how to override the default system prompt.

    - `SystemMessageBehavior.append`: Appends the provided system message to the
      default system prompt. - `SystemMessageBehavior.replace`: Replaces the default
      system prompt with the provided system message. The system message can include
      the string '{{function_definitions}}' to indicate where the function
      definitions should be inserted.
    """

    tool_choice: Union[Literal["auto", "required", "none"], str]
    """(Optional) Whether tool use is automatic, required, or none.

    Can also specify a tool name to use a specific tool. Defaults to
    ToolChoice.auto.
    """

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """(Optional) Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls.
    """


class ToolgroupAgentToolGroupWithArgs(TypedDict, total=False):
    args: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]


Toolgroup: TypeAlias = Union[str, ToolgroupAgentToolGroupWithArgs]


class TurnCreateParamsNonStreaming(TurnCreateParamsBase, total=False):
    stream: Literal[False]
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """


class TurnCreateParamsStreaming(TurnCreateParamsBase):
    stream: Required[Literal[True]]
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """


TurnCreateParams = Union[TurnCreateParamsNonStreaming, TurnCreateParamsStreaming]
