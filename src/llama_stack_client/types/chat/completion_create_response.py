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
    "CompletionCreateResponse",
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
    "Usage",
    "UsageCompletionTokensDetails",
    "UsagePromptTokensDetails",
]


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
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
    content: Union[
        str,
        List[
            ChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
        ],
    ]

    name: Optional[str] = None

    role: Optional[Literal["user"]] = None


class ChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    name: Optional[str] = None

    role: Optional[Literal["system"]] = None


class ChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ChoiceMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class ChoiceMessageOpenAIAssistantMessageParamOutput(BaseModel):
    content: Union[
        str,
        List[ChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None

    name: Optional[str] = None

    role: Optional[Literal["assistant"]] = None

    tool_calls: Optional[List[ChoiceMessageOpenAIAssistantMessageParamOutputToolCall]] = None


class ChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    tool_call_id: str

    role: Optional[Literal["tool"]] = None


class ChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
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
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobs(BaseModel):
    content: Optional[List[ChoiceLogprobsContent]] = None

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None


class Choice(BaseModel):
    finish_reason: str

    index: int

    message: ChoiceMessage
    """A message from the user in an OpenAI-compatible chat completion request."""

    logprobs: Optional[ChoiceLogprobs] = None
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible
    chat completion response.
    """


class UsageCompletionTokensDetails(BaseModel):
    reasoning_tokens: Optional[int] = None


class UsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None


class Usage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class CompletionCreateResponse(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    object: Optional[Literal["chat.completion"]] = None

    usage: Optional[Usage] = None
    """Usage information for OpenAI chat completion."""
