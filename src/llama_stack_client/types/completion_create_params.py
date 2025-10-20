# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CompletionCreateParamsBase", "CompletionCreateParamsNonStreaming", "CompletionCreateParamsStreaming"]


class CompletionCreateParamsBase(TypedDict, total=False):
    model: Required[str]
    """The identifier of the model to use.

    The model must be registered with Llama Stack and available via the /models
    endpoint.
    """

    prompt: Required[Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]]]
    """The prompt to generate a completion for."""

    best_of: int
    """(Optional) The number of completions to generate."""

    echo: bool
    """(Optional) Whether to echo the prompt."""

    frequency_penalty: float
    """(Optional) The penalty for repeated tokens."""

    logit_bias: Dict[str, float]
    """(Optional) The logit bias to use."""

    logprobs: bool
    """(Optional) The log probabilities to use."""

    max_tokens: int
    """(Optional) The maximum number of tokens to generate."""

    n: int
    """(Optional) The number of completions to generate."""

    presence_penalty: float
    """(Optional) The penalty for repeated tokens."""

    seed: int
    """(Optional) The seed to use."""

    stop: Union[str, SequenceNotStr[str]]
    """(Optional) The stop tokens to use."""

    stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) The stream options to use."""

    suffix: str
    """(Optional) The suffix that should be appended to the completion."""

    temperature: float
    """(Optional) The temperature to use."""

    top_p: float
    """(Optional) The top p to use."""

    user: str
    """(Optional) The user to use."""


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Literal[False]
    """(Optional) Whether to stream the response."""


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """(Optional) Whether to stream the response."""


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
