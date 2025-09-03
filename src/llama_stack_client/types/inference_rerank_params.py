# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .shared_params.interleaved_content_item import (
    OpenAIChatCompletionContentPartTextParam,
    OpenAIChatCompletionContentPartImageParam,
)

__all__ = ["InferenceRerankParams"]


class InferenceRerankParams(TypedDict, total=False):
    model: Required[str]
    """The identifier of the reranking model to use. The model must be a reranking model registered with Llama Stack and available via the /models endpoint."""

    query: Required[str | OpenAIChatCompletionContentPartTextParam | OpenAIChatCompletionContentPartImageParam]
    """The search query to rank items against. Can be a string, text content part, or image content part. The input must not exceed the model's max input token length."""

    items: Required[List[str | OpenAIChatCompletionContentPartTextParam | OpenAIChatCompletionContentPartImageParam]]
    """List of items to rerank. Each item can be a string, text content part, or image content part. Each input must not exceed the model's max input token length."""

    max_num_results: int
    """(Optional) Maximum number of results to return. Default: returns all."""
