# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["VectorStoreSearchParams", "RankingOptions"]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[Union[str, SequenceNotStr[str]]]
    """The search query string or list of query strings."""

    filters: Optional[Dict[str, object]]
    """Filters to apply to the search."""

    max_num_results: Optional[int]
    """Maximum number of results to return."""

    ranking_options: Optional[RankingOptions]
    """Options for ranking and filtering search results.

    This class configures how search results are ranked and filtered. You can use
    algorithm-based rerankers (weighted, RRF) or neural rerankers. Defaults from
    VectorStoresConfig are used when parameters are not provided.

    Examples: # Weighted ranker with custom alpha
    SearchRankingOptions(ranker="weighted", alpha=0.7)

        # RRF ranker with custom impact factor
        SearchRankingOptions(ranker="rrf", impact_factor=50.0)

        # Use config defaults (just specify ranker type)
        SearchRankingOptions(ranker="weighted")  # Uses alpha from VectorStoresConfig

        # Score threshold filtering
        SearchRankingOptions(ranker="weighted", score_threshold=0.5)
    """

    rewrite_query: Optional[bool]
    """Whether to rewrite the query for better results."""

    search_mode: Optional[str]
    """The search mode to use (e.g., 'vector', 'keyword')."""


class RankingOptions(TypedDict, total=False):
    """Options for ranking and filtering search results.

    This class configures how search results are ranked and filtered. You can use algorithm-based
    rerankers (weighted, RRF) or neural rerankers. Defaults from VectorStoresConfig are
    used when parameters are not provided.

    Examples:
        # Weighted ranker with custom alpha
        SearchRankingOptions(ranker="weighted", alpha=0.7)

        # RRF ranker with custom impact factor
        SearchRankingOptions(ranker="rrf", impact_factor=50.0)

        # Use config defaults (just specify ranker type)
        SearchRankingOptions(ranker="weighted")  # Uses alpha from VectorStoresConfig

        # Score threshold filtering
        SearchRankingOptions(ranker="weighted", score_threshold=0.5)
    """

    alpha: Optional[float]
    """Weight factor for weighted ranker"""

    impact_factor: Optional[float]
    """Impact factor for RRF algorithm"""

    model: Optional[str]
    """Model identifier for neural reranker"""

    ranker: Optional[str]

    score_threshold: Optional[float]

    weights: Optional[Dict[str, float]]
    """Weights for combining vector, keyword, and neural scores.

    Keys: 'vector', 'keyword', 'neural'
    """
