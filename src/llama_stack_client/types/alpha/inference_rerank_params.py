# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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

    Each item can be a string, text content part, or image content part. Each input
    must not exceed the model's max input token length.
    """

    model: Required[str]
    """The identifier of the reranking model to use."""

    query: Required[Query]
    """The search query to rank items against.

    Can be a string, text content part, or image content part. The input must not
    exceed the model's max input token length.
    """

    max_num_results: int
    """(Optional) Maximum number of results to return. Default: returns all."""


class ItemOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    text: Required[str]
    """The text content of the message"""

    type: Required[Literal["text"]]
    """Must be "text" to identify this as text content"""


class ItemOpenAIChatCompletionContentPartImageParamImageURL(TypedDict, total=False):
    url: Required[str]
    """URL of the image to include in the message"""

    detail: str
    """(Optional) Level of detail for image processing.

    Can be "low", "high", or "auto"
    """


class ItemOpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    image_url: Required[ItemOpenAIChatCompletionContentPartImageParamImageURL]
    """Image URL specification and processing details"""

    type: Required[Literal["image_url"]]
    """Must be "image_url" to identify this as image content"""


Item: TypeAlias = Union[
    str, ItemOpenAIChatCompletionContentPartTextParam, ItemOpenAIChatCompletionContentPartImageParam
]


class QueryOpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    text: Required[str]
    """The text content of the message"""

    type: Required[Literal["text"]]
    """Must be "text" to identify this as text content"""


class QueryOpenAIChatCompletionContentPartImageParamImageURL(TypedDict, total=False):
    url: Required[str]
    """URL of the image to include in the message"""

    detail: str
    """(Optional) Level of detail for image processing.

    Can be "low", "high", or "auto"
    """


class QueryOpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    image_url: Required[QueryOpenAIChatCompletionContentPartImageParamImageURL]
    """Image URL specification and processing details"""

    type: Required[Literal["image_url"]]
    """Must be "image_url" to identify this as image content"""


Query: TypeAlias = Union[
    str, QueryOpenAIChatCompletionContentPartTextParam, QueryOpenAIChatCompletionContentPartImageParam
]
