# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CompletionCreateParamsBase", "CompletionCreateParamsNonStreaming", "CompletionCreateParamsStreaming"]


class CompletionCreateParamsBase(TypedDict, total=False):
    model: Required[str]
    """The identifier of the model to use."""

    prompt: Required[Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]]]
    """The prompt to generate a completion for."""

    best_of: Optional[int]
    """The number of completions to generate."""

    echo: Optional[bool]
    """Whether to echo the prompt."""

    frequency_penalty: Optional[float]
    """The penalty for repeated tokens."""

    logit_bias: Optional[Dict[str, float]]
    """The logit bias to use."""

    logprobs: Optional[bool]
    """The log probabilities to use."""

    max_tokens: Optional[int]
    """The maximum number of tokens to generate."""

    n: Optional[int]
    """The number of completions to generate."""

    presence_penalty: Optional[float]
    """The penalty for repeated tokens."""

    seed: Optional[int]
    """The seed to use."""

    stop: Union[str, SequenceNotStr[str], None]
    """The stop tokens to use."""

    stream_options: Optional[Dict[str, object]]
    """The stream options to use."""

    suffix: Optional[str]
    """The suffix that should be appended to the completion."""

    temperature: Optional[float]
    """The temperature to use."""

    top_p: Optional[float]
    """The top p to use."""

    user: Optional[str]
    """The user to use."""


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Optional[Literal[False]]
    """Whether to stream the response."""


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """Whether to stream the response."""


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
