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
    "CompletionListResponse",
    "Data",
    "DataChoice",
    "DataChoiceMessage",
    "DataChoiceMessageOpenAIUserMessageParamOutput",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile",
    "DataChoiceMessageOpenAISystemMessageParam",
    "DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIAssistantMessageParamOutput",
    "DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall",
    "DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction",
    "DataChoiceMessageOpenAIToolMessageParam",
    "DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIDeveloperMessageParam",
    "DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceLogprobs",
    "DataChoiceLogprobsContent",
    "DataChoiceLogprobsContentTopLogprob",
    "DataChoiceLogprobsRefusal",
    "DataChoiceLogprobsRefusalTopLogprob",
    "DataInputMessage",
    "DataInputMessageOpenAIUserMessageParamOutput",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile",
    "DataInputMessageOpenAISystemMessageParam",
    "DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIAssistantMessageParamOutput",
    "DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIAssistantMessageParamOutputToolCall",
    "DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction",
    "DataInputMessageOpenAIToolMessageParam",
    "DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIDeveloperMessageParam",
    "DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataUsage",
    "DataUsageCompletionTokensDetails",
    "DataUsagePromptTokensDetails",
]


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification and processing details."""

    url: str
    """URL of the image to include in the message."""

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Level of detail for image processing. Can be 'low', 'high', or 'auto'."""


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification and processing details."""

    type: Optional[Literal["image_url"]] = None
    """Must be 'image_url' to identify this as image content."""


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    """File specification."""

    file_data: Optional[str] = None
    """Base64-encoded file data."""

    file_id: Optional[str] = None
    """ID of an uploaded file."""

    filename: Optional[str] = None
    """Name of the file."""


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile
    """File specification."""

    type: Optional[Literal["file"]] = None
    """Must be 'file' to identify this as file content."""


DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam,
        DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAIUserMessageParamOutput(BaseModel):
    """A message from the user in an OpenAI-compatible chat completion request."""

    content: Union[
        str,
        List[
            DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
        ],
    ]
    """The content of the message, which can include text and other media."""

    name: Optional[str] = None
    """The name of the user message participant."""

    role: Optional[Literal["user"]] = None
    """Must be 'user' to identify this as a user message."""


class DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataChoiceMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[
        str, List[DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]
    """The content of the 'system prompt'.

    If multiple system messages are provided, they are concatenated.
    """

    name: Optional[str] = None
    """The name of the system message participant."""

    role: Optional[Literal["system"]] = None
    """Must be 'system' to identify this as a system message."""


class DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None
    """Arguments to pass to the function as a JSON string."""

    name: Optional[str] = None
    """Name of the function to call."""


class DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None
    """Unique identifier for the tool call."""

    function: Optional[DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None
    """Index of the tool call in the list."""

    type: Optional[Literal["function"]] = None
    """Must be 'function' to identify this as a function call."""


class DataChoiceMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None
    """The content of the model's response."""

    name: Optional[str] = None
    """The name of the assistant message participant."""

    role: Optional[Literal["assistant"]] = None
    """Must be 'assistant' to identify this as the model's response."""

    tool_calls: Optional[List[DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataChoiceMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str, List[DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]
    """The response content from the tool."""

    tool_call_id: str
    """Unique identifier for the tool call this response is for."""

    role: Optional[Literal["tool"]] = None
    """Must be 'tool' to identify this as a tool response."""


class DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]
    """The content of the developer message."""

    name: Optional[str] = None
    """The name of the developer message participant."""

    role: Optional[Literal["developer"]] = None
    """Must be 'developer' to identify this as a developer message."""


DataChoiceMessage: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParamOutput,
        DataChoiceMessageOpenAISystemMessageParam,
        DataChoiceMessageOpenAIAssistantMessageParamOutput,
        DataChoiceMessageOpenAIToolMessageParam,
        DataChoiceMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class DataChoiceLogprobsContentTopLogprob(BaseModel):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""


class DataChoiceLogprobsContent(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""

    top_logprobs: Optional[List[DataChoiceLogprobsContentTopLogprob]] = None
    """The top log probabilities for the token."""


class DataChoiceLogprobsRefusalTopLogprob(BaseModel):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""


class DataChoiceLogprobsRefusal(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""

    top_logprobs: Optional[List[DataChoiceLogprobsRefusalTopLogprob]] = None
    """The top log probabilities for the token."""


class DataChoiceLogprobs(BaseModel):
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible chat completion response.
    """

    content: Optional[List[DataChoiceLogprobsContent]] = None
    """The log probabilities for the tokens in the message."""

    refusal: Optional[List[DataChoiceLogprobsRefusal]] = None
    """The log probabilities for the refusal tokens."""


class DataChoice(BaseModel):
    """A choice from an OpenAI-compatible chat completion response."""

    finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
    """The reason the model stopped generating."""

    index: int
    """The index of the choice."""

    message: DataChoiceMessage
    """The message from the model."""

    logprobs: Optional[DataChoiceLogprobs] = None
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible
    chat completion response.
    """


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification and processing details."""

    url: str
    """URL of the image to include in the message."""

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Level of detail for image processing. Can be 'low', 'high', or 'auto'."""


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification and processing details."""

    type: Optional[Literal["image_url"]] = None
    """Must be 'image_url' to identify this as image content."""


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    """File specification."""

    file_data: Optional[str] = None
    """Base64-encoded file data."""

    file_id: Optional[str] = None
    """ID of an uploaded file."""

    filename: Optional[str] = None
    """Name of the file."""


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile
    """File specification."""

    type: Optional[Literal["file"]] = None
    """Must be 'file' to identify this as file content."""


DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam,
        DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAIUserMessageParamOutput(BaseModel):
    """A message from the user in an OpenAI-compatible chat completion request."""

    content: Union[
        str,
        List[
            DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
        ],
    ]
    """The content of the message, which can include text and other media."""

    name: Optional[str] = None
    """The name of the user message participant."""

    role: Optional[Literal["user"]] = None
    """Must be 'user' to identify this as a user message."""


class DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataInputMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[
        str, List[DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]
    """The content of the 'system prompt'.

    If multiple system messages are provided, they are concatenated.
    """

    name: Optional[str] = None
    """The name of the system message participant."""

    role: Optional[Literal["system"]] = None
    """Must be 'system' to identify this as a system message."""


class DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None
    """Arguments to pass to the function as a JSON string."""

    name: Optional[str] = None
    """Name of the function to call."""


class DataInputMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None
    """Unique identifier for the tool call."""

    function: Optional[DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None
    """Index of the tool call in the list."""

    type: Optional[Literal["function"]] = None
    """Must be 'function' to identify this as a function call."""


class DataInputMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None
    """The content of the model's response."""

    name: Optional[str] = None
    """The name of the assistant message participant."""

    role: Optional[Literal["assistant"]] = None
    """Must be 'assistant' to identify this as the model's response."""

    tool_calls: Optional[List[DataInputMessageOpenAIAssistantMessageParamOutputToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataInputMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[str, List[DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    """The response content from the tool."""

    tool_call_id: str
    """Unique identifier for the tool call this response is for."""

    role: Optional[Literal["tool"]] = None
    """Must be 'tool' to identify this as a tool response."""


class DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class DataInputMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]
    """The content of the developer message."""

    name: Optional[str] = None
    """The name of the developer message participant."""

    role: Optional[Literal["developer"]] = None
    """Must be 'developer' to identify this as a developer message."""


DataInputMessage: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParamOutput,
        DataInputMessageOpenAISystemMessageParam,
        DataInputMessageOpenAIAssistantMessageParamOutput,
        DataInputMessageOpenAIToolMessageParam,
        DataInputMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class DataUsageCompletionTokensDetails(BaseModel):
    """Token details for output tokens in OpenAI chat completion usage."""

    reasoning_tokens: Optional[int] = None
    """Number of tokens used for reasoning (o1/o3 models)."""


class DataUsagePromptTokensDetails(BaseModel):
    """Token details for prompt tokens in OpenAI chat completion usage."""

    cached_tokens: Optional[int] = None
    """Number of tokens retrieved from cache."""


class DataUsage(BaseModel):
    """Usage information for OpenAI chat completion."""

    completion_tokens: int
    """Number of tokens in the completion."""

    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total tokens used (prompt + completion)."""

    completion_tokens_details: Optional[DataUsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[DataUsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class Data(BaseModel):
    id: str
    """The ID of the chat completion."""

    choices: List[DataChoice]
    """List of choices."""

    created: int
    """The Unix timestamp in seconds when the chat completion was created."""

    input_messages: List[DataInputMessage]
    """The input messages used to generate this completion."""

    model: str
    """The model that was used to generate the chat completion."""

    object: Optional[Literal["chat.completion"]] = None
    """The object type."""

    usage: Optional[DataUsage] = None
    """Usage information for OpenAI chat completion."""


class CompletionListResponse(BaseModel):
    """Response from listing OpenAI-compatible chat completions."""

    data: List[Data]
    """List of chat completion objects with their input messages."""

    first_id: str
    """ID of the first completion in this list."""

    has_more: bool
    """Whether there are more completions available beyond this list."""

    last_id: str
    """ID of the last completion in this list."""

    object: Optional[Literal["list"]] = None
    """Must be 'list' to identify this as a list response."""
