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
    """Function call details."""

    arguments: str
    """Arguments to pass to the function as a JSON string."""

    name: str
    """Name of the function to call."""


class ChoiceDeltaToolCall(BaseModel):
    """Tool call specification for OpenAI-compatible chat completion responses."""

    id: str
    """Unique identifier for the tool call."""

    function: ChoiceDeltaToolCallFunction
    """Function call details."""

    type: Literal["function"]
    """Must be 'function' to identify this as a function call."""


class ChoiceDelta(BaseModel):
    """The delta from the chunk."""

    content: Optional[str] = None
    """The content of the delta."""

    reasoning_content: Optional[str] = None
    """The reasoning content from the model (for o1/o3 models)."""

    refusal: Optional[str] = None
    """The refusal of the delta."""

    role: Optional[Literal["developer", "system", "user", "assistant", "tool"]] = None
    """The role of the delta."""

    tool_calls: Optional[List[ChoiceDeltaToolCall]] = None
    """The tool calls of the delta."""


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
    """The log probabilities for the tokens in the message."""

    content: Optional[List[ChoiceLogprobsContent]] = None
    """The log probabilities for the tokens in the message."""

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None
    """The log probabilities for the refusal tokens."""


class Choice(BaseModel):
    """A chunk choice from an OpenAI-compatible chat completion streaming response."""

    delta: ChoiceDelta
    """The delta from the chunk."""

    index: int
    """The index of the choice."""

    finish_reason: Optional[Literal["stop", "length", "tool_calls", "content_filter", "function_call"]] = None
    """The reason the model stopped generating."""

    logprobs: Optional[ChoiceLogprobs] = None
    """The log probabilities for the tokens in the message."""


class UsageCompletionTokensDetails(BaseModel):
    """Detailed breakdown of output token usage."""

    reasoning_tokens: Optional[int] = None
    """Number of tokens used for reasoning (o1/o3 models)."""


class UsagePromptTokensDetails(BaseModel):
    """Detailed breakdown of input token usage."""

    cached_tokens: Optional[int] = None
    """Number of tokens retrieved from cache."""


class Usage(BaseModel):
    """
    Token usage information (typically included in final chunk with stream_options).
    """

    completion_tokens: Optional[int] = None
    """Number of tokens in the completion."""

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Detailed breakdown of output token usage."""

    prompt_tokens: Optional[int] = None
    """Number of tokens in the prompt."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Detailed breakdown of input token usage."""

    total_tokens: Optional[int] = None
    """Total tokens used (prompt + completion)."""


class ChatCompletionChunk(BaseModel):
    """
    Chunk from a streaming response to an OpenAI-compatible chat completion request.
    """

    id: str
    """The ID of the chat completion."""

    choices: List[Choice]
    """List of choices."""

    created: int
    """The Unix timestamp in seconds when the chat completion was created."""

    model: str
    """The model that was used to generate the chat completion."""

    object: Optional[Literal["chat.completion.chunk"]] = None
    """The object type."""

    service_tier: Optional[str] = None
    """The service tier that was used for this response."""

    system_fingerprint: Optional[str] = None
    """System fingerprint for this completion chunk."""

    usage: Optional[Usage] = None
    """
    Token usage information (typically included in final chunk with stream_options).
    """
