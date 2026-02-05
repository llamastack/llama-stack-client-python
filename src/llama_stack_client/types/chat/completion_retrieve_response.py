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
    "CompletionRetrieveResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceMessageOpenAIUserMessageParamOutput",
    "ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile",
    "ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam",
    "ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL",
    "ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile",
    "ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile",
    "ChoiceMessageOpenAISystemMessageParam",
    "ChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIAssistantMessageParamOutput",
    "ChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIAssistantMessageParamOutputToolCall",
    "ChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction",
    "ChoiceMessageOpenAIToolMessageParam",
    "ChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIDeveloperMessageParam",
    "ChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
    "InputMessage",
    "InputMessageOpenAIUserMessageParamOutput",
    "InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile",
    "InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam",
    "InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL",
    "InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile",
    "InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile",
    "InputMessageOpenAISystemMessageParam",
    "InputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIAssistantMessageParamOutput",
    "InputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIAssistantMessageParamOutputToolCall",
    "InputMessageOpenAIAssistantMessageParamOutputToolCallFunction",
    "InputMessageOpenAIToolMessageParam",
    "InputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIDeveloperMessageParam",
    "InputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "Usage",
    "UsageCompletionTokensDetails",
    "UsagePromptTokensDetails",
]


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification and processing details."""

    url: str
    """URL of the image to include in the message."""

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Level of detail for image processing. Can be 'low', 'high', or 'auto'."""


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification and processing details."""

    type: Optional[Literal["image_url"]] = None
    """Must be 'image_url' to identify this as image content."""


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    """File specification."""

    file_data: Optional[str] = None
    """Base64-encoded file data."""

    file_id: Optional[str] = None
    """ID of an uploaded file."""

    filename: Optional[str] = None
    """Name of the file."""


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile
    """File specification."""

    type: Optional[Literal["file"]] = None
    """Must be 'file' to identify this as file content."""


ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam,
        ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam,
        ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class ChoiceMessageOpenAIUserMessageParamOutput(BaseModel):
    """A message from the user in an OpenAI-compatible chat completion request."""

    content: Union[
        str,
        List[
            ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
        ],
    ]
    """The content of the message, which can include text and other media."""

    name: Optional[str] = None
    """The name of the user message participant."""

    role: Optional[Literal["user"]] = None
    """Must be 'user' to identify this as a user message."""


class ChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class ChoiceMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[str, List[ChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    """The content of the 'system prompt'.

    If multiple system messages are provided, they are concatenated.
    """

    name: Optional[str] = None
    """The name of the system message participant."""

    role: Optional[Literal["system"]] = None
    """Must be 'system' to identify this as a system message."""


class ChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class ChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None
    """Arguments to pass to the function as a JSON string."""

    name: Optional[str] = None
    """Name of the function to call."""


class ChoiceMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None
    """Unique identifier for the tool call."""

    function: Optional[ChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None
    """Index of the tool call in the list."""

    type: Optional[Literal["function"]] = None
    """Must be 'function' to identify this as a function call."""


class ChoiceMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[ChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None
    """The content of the model's response."""

    name: Optional[str] = None
    """The name of the assistant message participant."""

    role: Optional[Literal["assistant"]] = None
    """Must be 'assistant' to identify this as the model's response."""

    tool_calls: Optional[List[ChoiceMessageOpenAIAssistantMessageParamOutputToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class ChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class ChoiceMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[str, List[ChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    """The response content from the tool."""

    tool_call_id: str
    """Unique identifier for the tool call this response is for."""

    role: Optional[Literal["tool"]] = None
    """Must be 'tool' to identify this as a tool response."""


class ChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class ChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[ChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]
    """The content of the developer message."""

    name: Optional[str] = None
    """The name of the developer message participant."""

    role: Optional[Literal["developer"]] = None
    """Must be 'developer' to identify this as a developer message."""


ChoiceMessage: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIUserMessageParamOutput,
        ChoiceMessageOpenAISystemMessageParam,
        ChoiceMessageOpenAIAssistantMessageParamOutput,
        ChoiceMessageOpenAIToolMessageParam,
        ChoiceMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class ChoiceLogprobsContentTopLogprob(BaseModel):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""


class ChoiceLogprobsContent(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""

    top_logprobs: Optional[List[ChoiceLogprobsContentTopLogprob]] = None
    """The top log probabilities for the token."""


class ChoiceLogprobsRefusalTopLogprob(BaseModel):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""


class ChoiceLogprobsRefusal(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""

    top_logprobs: Optional[List[ChoiceLogprobsRefusalTopLogprob]] = None
    """The top log probabilities for the token."""


class ChoiceLogprobs(BaseModel):
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible chat completion response.
    """

    content: Optional[List[ChoiceLogprobsContent]] = None
    """The log probabilities for the tokens in the message."""

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None
    """The log probabilities for the refusal tokens."""


class Choice(BaseModel):
    """A choice from an OpenAI-compatible chat completion response."""

    finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
    """The reason the model stopped generating."""

    index: int
    """The index of the choice."""

    message: ChoiceMessage
    """The message from the model."""

    logprobs: Optional[ChoiceLogprobs] = None
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible
    chat completion response.
    """


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification and processing details."""

    url: str
    """URL of the image to include in the message."""

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Level of detail for image processing. Can be 'low', 'high', or 'auto'."""


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification and processing details."""

    type: Optional[Literal["image_url"]] = None
    """Must be 'image_url' to identify this as image content."""


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    """File specification."""

    file_data: Optional[str] = None
    """Base64-encoded file data."""

    file_id: Optional[str] = None
    """ID of an uploaded file."""

    filename: Optional[str] = None
    """Name of the file."""


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile
    """File specification."""

    type: Optional[Literal["file"]] = None
    """Must be 'file' to identify this as file content."""


InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam,
        InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam,
        InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class InputMessageOpenAIUserMessageParamOutput(BaseModel):
    """A message from the user in an OpenAI-compatible chat completion request."""

    content: Union[
        str,
        List[
            InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
        ],
    ]
    """The content of the message, which can include text and other media."""

    name: Optional[str] = None
    """The name of the user message participant."""

    role: Optional[Literal["user"]] = None
    """Must be 'user' to identify this as a user message."""


class InputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class InputMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[str, List[InputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    """The content of the 'system prompt'.

    If multiple system messages are provided, they are concatenated.
    """

    name: Optional[str] = None
    """The name of the system message participant."""

    role: Optional[Literal["system"]] = None
    """Must be 'system' to identify this as a system message."""


class InputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class InputMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None
    """Arguments to pass to the function as a JSON string."""

    name: Optional[str] = None
    """Name of the function to call."""


class InputMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None
    """Unique identifier for the tool call."""

    function: Optional[InputMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None
    """Index of the tool call in the list."""

    type: Optional[Literal["function"]] = None
    """Must be 'function' to identify this as a function call."""


class InputMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[InputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None
    """The content of the model's response."""

    name: Optional[str] = None
    """The name of the assistant message participant."""

    role: Optional[Literal["assistant"]] = None
    """Must be 'assistant' to identify this as the model's response."""

    tool_calls: Optional[List[InputMessageOpenAIAssistantMessageParamOutputToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class InputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class InputMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[str, List[InputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]
    """The response content from the tool."""

    tool_call_id: str
    """Unique identifier for the tool call this response is for."""

    role: Optional[Literal["tool"]] = None
    """Must be 'tool' to identify this as a tool response."""


class InputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """Must be 'text' to identify this as text content."""


class InputMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[InputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]
    """The content of the developer message."""

    name: Optional[str] = None
    """The name of the developer message participant."""

    role: Optional[Literal["developer"]] = None
    """Must be 'developer' to identify this as a developer message."""


InputMessage: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIUserMessageParamOutput,
        InputMessageOpenAISystemMessageParam,
        InputMessageOpenAIAssistantMessageParamOutput,
        InputMessageOpenAIToolMessageParam,
        InputMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class UsageCompletionTokensDetails(BaseModel):
    """Token details for output tokens in OpenAI chat completion usage."""

    reasoning_tokens: Optional[int] = None
    """Number of tokens used for reasoning (o1/o3 models)."""


class UsagePromptTokensDetails(BaseModel):
    """Token details for prompt tokens in OpenAI chat completion usage."""

    cached_tokens: Optional[int] = None
    """Number of tokens retrieved from cache."""


class Usage(BaseModel):
    """Usage information for OpenAI chat completion."""

    completion_tokens: int
    """Number of tokens in the completion."""

    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total tokens used (prompt + completion)."""

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class CompletionRetrieveResponse(BaseModel):
    id: str
    """The ID of the chat completion."""

    choices: List[Choice]
    """List of choices."""

    created: int
    """The Unix timestamp in seconds when the chat completion was created."""

    input_messages: List[InputMessage]
    """The input messages used to generate this completion."""

    model: str
    """The model that was used to generate the chat completion."""

    object: Optional[Literal["chat.completion"]] = None
    """The object type."""

    usage: Optional[Usage] = None
    """Usage information for OpenAI chat completion."""
