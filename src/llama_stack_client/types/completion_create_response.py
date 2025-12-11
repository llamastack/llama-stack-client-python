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
    """A choice from an OpenAI-compatible completion response.

    :finish_reason: The reason the model stopped generating
    :text: The text of the choice
    :index: The index of the choice
    :logprobs: (Optional) The log probabilities for the tokens in the choice
    """

    finish_reason: str

    index: int

    text: str

    logprobs: Optional[ChoiceLogprobs] = None
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible
    chat completion response.
    """


class CompletionCreateResponse(BaseModel):
    """Response from an OpenAI-compatible completion request.

    :id: The ID of the completion
    :choices: List of choices
    :created: The Unix timestamp in seconds when the completion was created
    :model: The model that was used to generate the completion
    :object: The object type, which will be "text_completion"
    """

    id: str

    choices: List[Choice]

    created: int

    model: str

    object: Optional[Literal["text_completion"]] = None
