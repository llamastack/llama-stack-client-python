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

    name: Optional[str] = None


class ChoiceDeltaToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ChoiceDeltaToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class ChoiceDelta(BaseModel):
    content: Optional[str] = None

    reasoning_content: Optional[str] = None

    refusal: Optional[str] = None

    role: Optional[str] = None

    tool_calls: Optional[List[ChoiceDeltaToolCall]] = None


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
    delta: ChoiceDelta
    """A delta from an OpenAI-compatible chat completion streaming response."""

    finish_reason: str

    index: int

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


class ChatCompletionChunk(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    object: Optional[Literal["chat.completion.chunk"]] = None

    usage: Optional[Usage] = None
    """Usage information for OpenAI chat completion."""
