# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CompletionCreateParamsBase",
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
    "ResponseFormat",
    "ResponseFormatOpenAIResponseFormatText",
    "ResponseFormatOpenAIResponseFormatJsonSchema",
    "ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema",
    "ResponseFormatOpenAIResponseFormatJsonObject",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]

    frequency_penalty: Optional[float]

    function_call: Union[str, Dict[str, object], None]

    functions: Optional[Iterable[Dict[str, object]]]

    logit_bias: Optional[Dict[str, float]]

    logprobs: Optional[bool]

    max_completion_tokens: Optional[int]

    max_tokens: Optional[int]

    n: Optional[int]

    parallel_tool_calls: Optional[bool]

    presence_penalty: Optional[float]

    response_format: Optional[ResponseFormat]
    """Text response format for OpenAI-compatible chat completion requests."""

    seed: Optional[int]

    stop: Union[str, SequenceNotStr[str], None]

    stream_options: Optional[Dict[str, object]]

    temperature: Optional[float]

    tool_choice: Union[str, Dict[str, object], None]

    tools: Optional[Iterable[Dict[str, object]]]

    top_logprobs: Optional[int]

    top_p: Optional[float]

    user: Optional[str]


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]

    type: Literal["text"]


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    TypedDict, total=False
):
    """Image URL specification for OpenAI-compatible chat completion messages."""

    url: Required[str]

    detail: Optional[str]


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    TypedDict, total=False
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: Required[
        MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    ]
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Literal["image_url"]


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    TypedDict, total=False
):
    file_data: Optional[str]

    file_id: Optional[str]

    filename: Optional[str]


class MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    TypedDict, total=False
):
    file: Required[
        MessageOpenAIUserMessageParamInputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile
    ]

    type: Literal["file"]


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

    name: Optional[str]

    role: Literal["user"]


class MessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]

    type: Literal["text"]


class MessageOpenAISystemMessageParam(TypedDict, total=False):
    """A system message providing instructions or context to the model."""

    content: Required[
        Union[str, Iterable[MessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    ]

    name: Optional[str]

    role: Literal["system"]


class MessageOpenAIAssistantMessageParamInputContentListOpenAIChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]

    type: Literal["text"]


class MessageOpenAIAssistantMessageParamInputToolCallFunction(TypedDict, total=False):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str]

    name: Optional[str]


class MessageOpenAIAssistantMessageParamInputToolCall(TypedDict, total=False):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str]

    function: Optional[MessageOpenAIAssistantMessageParamInputToolCallFunction]
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int]

    type: Literal["function"]


class MessageOpenAIAssistantMessageParamInput(TypedDict, total=False):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str, Iterable[MessageOpenAIAssistantMessageParamInputContentListOpenAIChatCompletionContentPartTextParam], None
    ]

    name: Optional[str]

    role: Literal["assistant"]

    tool_calls: Optional[Iterable[MessageOpenAIAssistantMessageParamInputToolCall]]


class MessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]

    type: Literal["text"]


class MessageOpenAIToolMessageParam(TypedDict, total=False):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Required[
        Union[str, Iterable[MessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    ]

    tool_call_id: Required[str]

    role: Literal["tool"]


class MessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]

    type: Literal["text"]


class MessageOpenAIDeveloperMessageParam(TypedDict, total=False):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Required[
        Union[str, Iterable[MessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    ]

    name: Optional[str]

    role: Literal["developer"]


Message: TypeAlias = Union[
    MessageOpenAIUserMessageParamInput,
    MessageOpenAISystemMessageParam,
    MessageOpenAIAssistantMessageParamInput,
    MessageOpenAIToolMessageParam,
    MessageOpenAIDeveloperMessageParam,
]


class ResponseFormatOpenAIResponseFormatText(TypedDict, total=False):
    """Text response format for OpenAI-compatible chat completion requests."""

    type: Literal["text"]


class ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    """JSON schema specification for OpenAI-compatible structured response format."""

    description: Optional[str]

    name: str

    schema: Optional[Dict[str, object]]

    strict: Optional[bool]


class ResponseFormatOpenAIResponseFormatJsonSchema(TypedDict, total=False):
    """JSON schema response format for OpenAI-compatible chat completion requests."""

    json_schema: Required[ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema]
    """JSON schema specification for OpenAI-compatible structured response format."""

    type: Literal["json_schema"]


class ResponseFormatOpenAIResponseFormatJsonObject(TypedDict, total=False):
    """JSON object response format for OpenAI-compatible chat completion requests."""

    type: Literal["json_object"]


ResponseFormat: TypeAlias = Union[
    ResponseFormatOpenAIResponseFormatText,
    ResponseFormatOpenAIResponseFormatJsonSchema,
    ResponseFormatOpenAIResponseFormatJsonObject,
]


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Optional[Literal[False]]


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
