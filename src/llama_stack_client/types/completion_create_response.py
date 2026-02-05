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
    "CompletionCreateResponse",
    "Choice",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
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
    """A choice from an OpenAI-compatible completion response."""

    finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
    """The reason the model stopped generating."""

    index: int
    """The index of the choice."""

    text: str
    """The text of the choice."""

    logprobs: Optional[ChoiceLogprobs] = None
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible
    chat completion response.
    """


class CompletionCreateResponse(BaseModel):
    """Response from an OpenAI-compatible completion request."""

    id: str
    """The ID of the completion."""

    choices: List[Choice]
    """List of choices."""

    created: int
    """The Unix timestamp in seconds when the completion was created."""

    model: str
    """The model that was used to generate the completion."""

    object: Optional[Literal["text_completion"]] = None
    """The object type."""
