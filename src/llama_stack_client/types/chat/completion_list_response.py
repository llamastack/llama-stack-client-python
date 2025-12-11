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

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification for OpenAI-compatible chat completion messages."""

    url: str

    detail: Optional[str] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Optional[Literal["image_url"]] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile

    type: Optional[Literal["file"]] = None


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

    name: Optional[str] = None

    role: Optional[Literal["user"]] = None


class DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[
        str, List[DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["system"]] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None

    name: Optional[str] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None

    function: Optional[DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None

    name: Optional[str] = None

    role: Optional[Literal["assistant"]] = None

    tool_calls: Optional[List[DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall]] = None


class DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str, List[DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    tool_call_id: str

    role: Optional[Literal["tool"]] = None


class DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["developer"]] = None


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

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsContent(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    top_logprobs: Optional[List[DataChoiceLogprobsContentTopLogprob]] = None


class DataChoiceLogprobsRefusalTopLogprob(BaseModel):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsRefusal(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    top_logprobs: Optional[List[DataChoiceLogprobsRefusalTopLogprob]] = None


class DataChoiceLogprobs(BaseModel):
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible chat completion response.
    """

    content: Optional[List[DataChoiceLogprobsContent]] = None

    refusal: Optional[List[DataChoiceLogprobsRefusal]] = None


class DataChoice(BaseModel):
    """A choice from an OpenAI-compatible chat completion response."""

    finish_reason: str

    index: int

    message: DataChoiceMessage
    """A message from the user in an OpenAI-compatible chat completion request."""

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

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification for OpenAI-compatible chat completion messages."""

    url: str

    detail: Optional[str] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Optional[Literal["image_url"]] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile

    type: Optional[Literal["file"]] = None


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

    name: Optional[str] = None

    role: Optional[Literal["user"]] = None


class DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[
        str, List[DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["system"]] = None


class DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None

    name: Optional[str] = None


class DataInputMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None

    function: Optional[DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class DataInputMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None

    name: Optional[str] = None

    role: Optional[Literal["assistant"]] = None

    tool_calls: Optional[List[DataInputMessageOpenAIAssistantMessageParamOutputToolCall]] = None


class DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[str, List[DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    tool_call_id: str

    role: Optional[Literal["tool"]] = None


class DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["developer"]] = None


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


class DataUsagePromptTokensDetails(BaseModel):
    """Token details for prompt tokens in OpenAI chat completion usage."""

    cached_tokens: Optional[int] = None


class DataUsage(BaseModel):
    """Usage information for OpenAI chat completion."""

    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    completion_tokens_details: Optional[DataUsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[DataUsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class Data(BaseModel):
    id: str

    choices: List[DataChoice]

    created: int

    input_messages: List[DataInputMessage]

    model: str

    object: Optional[Literal["chat.completion"]] = None

    usage: Optional[DataUsage] = None
    """Usage information for OpenAI chat completion."""


class CompletionListResponse(BaseModel):
    """Response from listing OpenAI-compatible chat completions."""

    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: Optional[Literal["list"]] = None
