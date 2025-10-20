# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ChatCompletionChunk",
    "Choice",
    "ChoiceDelta",
    "ChoiceDeltaToolCall",
    "ChoiceDeltaToolCallFunction",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
    "Usage",
    "UsageCompletionTokensDetails",
    "UsagePromptTokensDetails",
]


class ChoiceDeltaToolCallFunction(BaseModel):
    arguments: Optional[str] = None
    """(Optional) Arguments to pass to the function as a JSON string"""

    name: Optional[str] = None
    """(Optional) Name of the function to call"""


class ChoiceDeltaToolCall(BaseModel):
    type: Literal["function"]
    """Must be "function" to identify this as a function call"""

    id: Optional[str] = None
    """(Optional) Unique identifier for the tool call"""

    function: Optional[ChoiceDeltaToolCallFunction] = None
    """(Optional) Function call details"""

    index: Optional[int] = None
    """(Optional) Index of the tool call in the list"""


class ChoiceDelta(BaseModel):
    content: Optional[str] = None
    """(Optional) The content of the delta"""

    reasoning_content: Optional[str] = None
    """
    (Optional) The reasoning content from the model (non-standard, for o1/o3 models)
    """

    refusal: Optional[str] = None
    """(Optional) The refusal of the delta"""

    role: Optional[str] = None
    """(Optional) The role of the delta"""

    tool_calls: Optional[List[ChoiceDeltaToolCall]] = None
    """(Optional) The tool calls of the delta"""


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
    """(Optional) The log probabilities for the tokens in the message"""

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None
    """(Optional) The log probabilities for the tokens in the message"""


class Choice(BaseModel):
    delta: ChoiceDelta
    """The delta from the chunk"""

    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    logprobs: Optional[ChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class UsageCompletionTokensDetails(BaseModel):
    reasoning_tokens: Optional[int] = None
    """Number of tokens used for reasoning (o1/o3 models)"""


class UsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None
    """Number of tokens retrieved from cache"""


class Usage(BaseModel):
    completion_tokens: int
    """Number of tokens in the completion"""

    prompt_tokens: int
    """Number of tokens in the prompt"""

    total_tokens: int
    """Total tokens used (prompt + completion)"""

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class ChatCompletionChunk(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[Choice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion.chunk"]
    """The object type, which will be "chat.completion.chunk" """

    usage: Optional[Usage] = None
    """Token usage information (typically included in final chunk with stream_options)"""
