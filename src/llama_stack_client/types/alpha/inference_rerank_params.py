# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "InferenceRerankParams",
    "Item",
    "ItemOpenAIChatCompletionContentPartTextParam",
    "ItemOpenAIChatCompletionContentPartImageParam",
    "ItemOpenAIChatCompletionContentPartImageParamImageURL",
    "Query",
    "QueryOpenAIChatCompletionContentPartTextParam",
    "QueryOpenAIChatCompletionContentPartImageParam",
    "QueryOpenAIChatCompletionContentPartImageParamImageURL",
]


class InferenceRerankParams(TypedDict, total=False):
    items: Required[SequenceNotStr[Item]]

    model: Required[str]

    query: Required[Query]
    """Text content part for OpenAI-compatible chat completion messages."""

    max_num_results: Optional[int]


class ItemOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]

    type: Literal["text"]


class ItemOpenAIChatCompletionContentPartImageParamImageURL(TypedDict, total=False):
    """Image URL specification for OpenAI-compatible chat completion messages."""

    url: Required[str]

    detail: Optional[str]


class ItemOpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: Required[ItemOpenAIChatCompletionContentPartImageParamImageURL]
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Literal["image_url"]


Item: TypeAlias = Union[
    str, ItemOpenAIChatCompletionContentPartTextParam, ItemOpenAIChatCompletionContentPartImageParam
]


class QueryOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]

    type: Literal["text"]


class QueryOpenAIChatCompletionContentPartImageParamImageURL(TypedDict, total=False):
    """Image URL specification for OpenAI-compatible chat completion messages."""

    url: Required[str]

    detail: Optional[str]


class QueryOpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: Required[QueryOpenAIChatCompletionContentPartImageParamImageURL]
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Literal["image_url"]


Query: TypeAlias = Union[
    str, QueryOpenAIChatCompletionContentPartTextParam, QueryOpenAIChatCompletionContentPartImageParam
]
