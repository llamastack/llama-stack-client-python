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

    filters: Optional[Dict[str, object]]

    max_num_results: Optional[int]

    ranking_options: Optional[RankingOptions]
    """Options for ranking and filtering search results."""

    rewrite_query: Optional[bool]

    search_mode: Optional[str]


class RankingOptions(TypedDict, total=False):
    """Options for ranking and filtering search results."""

    ranker: Optional[str]

    score_threshold: Optional[float]
