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
    """List of items to rerank.

    Each item can be a string, text content part, or image content part.
    """

    model: Required[str]
    """The identifier of the reranking model to use."""

    query: Required[Query]
    """The search query to rank items against.

    Can be a string, text content part, or image content part.
    """

    max_num_results: Optional[int]
    """Maximum number of results to return. Default: returns all."""


class ItemOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """Must be 'text' to identify this as text content."""


class ItemOpenAIChatCompletionContentPartImageParamImageURL(TypedDict, total=False):
    """Image URL specification and processing details."""

    url: Required[str]
    """URL of the image to include in the message."""

    detail: Optional[Literal["low", "high", "auto"]]
    """Level of detail for image processing. Can be 'low', 'high', or 'auto'."""


class ItemOpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: Required[ItemOpenAIChatCompletionContentPartImageParamImageURL]
    """Image URL specification and processing details."""

    type: Literal["image_url"]
    """Must be 'image_url' to identify this as image content."""


Item: TypeAlias = Union[
    str, ItemOpenAIChatCompletionContentPartTextParam, ItemOpenAIChatCompletionContentPartImageParam
]


class QueryOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    """Text content part for OpenAI-compatible chat completion messages."""

    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """Must be 'text' to identify this as text content."""


class QueryOpenAIChatCompletionContentPartImageParamImageURL(TypedDict, total=False):
    """Image URL specification and processing details."""

    url: Required[str]
    """URL of the image to include in the message."""

    detail: Optional[Literal["low", "high", "auto"]]
    """Level of detail for image processing. Can be 'low', 'high', or 'auto'."""


class QueryOpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    """Image content part for OpenAI-compatible chat completion messages."""

    image_url: Required[QueryOpenAIChatCompletionContentPartImageParamImageURL]
    """Image URL specification and processing details."""

    type: Literal["image_url"]
    """Must be 'image_url' to identify this as image content."""


Query: TypeAlias = Union[
    str, QueryOpenAIChatCompletionContentPartTextParam, QueryOpenAIChatCompletionContentPartImageParam
]
