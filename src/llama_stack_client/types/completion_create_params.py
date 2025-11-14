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

    prompt: Required[Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]]]

    best_of: Optional[int]

    echo: Optional[bool]

    frequency_penalty: Optional[float]

    logit_bias: Optional[Dict[str, float]]

    logprobs: Optional[bool]

    max_tokens: Optional[int]

    n: Optional[int]

    presence_penalty: Optional[float]

    seed: Optional[int]

    stop: Union[str, SequenceNotStr[str], None]

    stream_options: Optional[Dict[str, object]]

    suffix: Optional[str]

    temperature: Optional[float]

    top_p: Optional[float]

    user: Optional[str]


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Optional[Literal[False]]


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
