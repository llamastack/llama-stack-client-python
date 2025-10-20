# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["VectorStoreSearchParams", "RankingOptions"]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[Union[str, SequenceNotStr[str]]]
    """The query string or array for performing the search."""

    filters: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """Filters based on file attributes to narrow the search results."""

    max_num_results: int
    """Maximum number of results to return (1 to 50 inclusive, default 10)."""

    ranking_options: RankingOptions
    """Ranking options for fine-tuning the search results."""

    rewrite_query: bool
    """Whether to rewrite the natural language query for vector search (default false)"""

    search_mode: str
    """The search mode to use - "keyword", "vector", or "hybrid" (default "vector")"""


class RankingOptions(TypedDict, total=False):
    ranker: str
    """(Optional) Name of the ranking algorithm to use"""

    score_threshold: float
    """(Optional) Minimum relevance score threshold for results"""
