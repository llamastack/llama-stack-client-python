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

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification for OpenAI-compatible chat completion messages."""

    url: str

    detail: Optional[str] = None


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Optional[Literal["image_url"]] = None


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile

    type: Optional[Literal["file"]] = None


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

    name: Optional[str] = None

    role: Optional[Literal["user"]] = None


class ChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[str, List[ChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    name: Optional[str] = None

    role: Optional[Literal["system"]] = None


class ChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None

    name: Optional[str] = None


class ChoiceMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None

    function: Optional[ChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class ChoiceMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[ChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None

    name: Optional[str] = None

    role: Optional[Literal["assistant"]] = None

    tool_calls: Optional[List[ChoiceMessageOpenAIAssistantMessageParamOutputToolCall]] = None


class ChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[str, List[ChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    tool_call_id: str

    role: Optional[Literal["tool"]] = None


class ChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[ChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["developer"]] = None


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

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsContent(BaseModel):
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

    top_logprobs: Optional[List[ChoiceLogprobsContentTopLogprob]] = None


class ChoiceLogprobsRefusalTopLogprob(BaseModel):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusal(BaseModel):
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

    top_logprobs: Optional[List[ChoiceLogprobsRefusalTopLogprob]] = None


class ChoiceLogprobs(BaseModel):
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible chat completion response.
    """

    content: Optional[List[ChoiceLogprobsContent]] = None

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None


class Choice(BaseModel):
    """A choice from an OpenAI-compatible chat completion response."""

    finish_reason: str

    index: int

    message: ChoiceMessage
    """A message from the user in an OpenAI-compatible chat completion request."""

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

    type: Optional[Literal["text"]] = None


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    """Image URL specification for OpenAI-compatible chat completion messages."""

    url: str

    detail: Optional[str] = None


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Optional[Literal["image_url"]] = None


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: InputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile

    type: Optional[Literal["file"]] = None


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

    name: Optional[str] = None

    role: Optional[Literal["user"]] = None


class InputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class InputMessageOpenAISystemMessageParam(BaseModel):
    """A system message providing instructions or context to the model."""

    content: Union[str, List[InputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    name: Optional[str] = None

    role: Optional[Literal["system"]] = None


class InputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class InputMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    """Function call details for OpenAI-compatible tool calls."""

    arguments: Optional[str] = None

    name: Optional[str] = None


class InputMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: Optional[str] = None

    function: Optional[InputMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class InputMessageOpenAIAssistantMessageParamOutput(BaseModel):
    """
    A message containing the model's (assistant) response in an OpenAI-compatible chat completion request.
    """

    content: Union[
        str,
        List[InputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None

    name: Optional[str] = None

    role: Optional[Literal["assistant"]] = None

    tool_calls: Optional[List[InputMessageOpenAIAssistantMessageParamOutputToolCall]] = None


class InputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class InputMessageOpenAIToolMessageParam(BaseModel):
    """
    A message representing the result of a tool invocation in an OpenAI-compatible chat completion request.
    """

    content: Union[str, List[InputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    tool_call_id: str

    role: Optional[Literal["tool"]] = None


class InputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: str

    type: Optional[Literal["text"]] = None


class InputMessageOpenAIDeveloperMessageParam(BaseModel):
    """A message from the developer in an OpenAI-compatible chat completion request."""

    content: Union[
        str, List[InputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["developer"]] = None


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


class UsagePromptTokensDetails(BaseModel):
    """Token details for prompt tokens in OpenAI chat completion usage."""

    cached_tokens: Optional[int] = None


class Usage(BaseModel):
    """Usage information for OpenAI chat completion."""

    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class CompletionRetrieveResponse(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    input_messages: List[InputMessage]

    model: str

    object: Optional[Literal["chat.completion"]] = None

    usage: Optional[Usage] = None
    """Usage information for OpenAI chat completion."""
