# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "QueryConfig",
    "QueryGeneratorConfig",
    "QueryGeneratorConfigDefaultRagQueryGeneratorConfig",
    "QueryGeneratorConfigLlmragQueryGeneratorConfig",
    "Ranker",
    "RankerRrfRanker",
    "RankerWeightedRanker",
]


class QueryGeneratorConfigDefaultRagQueryGeneratorConfig(TypedDict, total=False):
    separator: Required[str]
    """String separator used to join query terms"""

    type: Required[Literal["default"]]
    """Type of query generator, always 'default'"""


class QueryGeneratorConfigLlmragQueryGeneratorConfig(TypedDict, total=False):
    model: Required[str]
    """Name of the language model to use for query generation"""

    template: Required[str]
    """Template string for formatting the query generation prompt"""

    type: Required[Literal["llm"]]
    """Type of query generator, always 'llm'"""


QueryGeneratorConfig: TypeAlias = Union[
    QueryGeneratorConfigDefaultRagQueryGeneratorConfig, QueryGeneratorConfigLlmragQueryGeneratorConfig
]


class RankerRrfRanker(TypedDict, total=False):
    impact_factor: Required[float]
    """The impact factor for RRF scoring.

    Higher values give more weight to higher-ranked results. Must be greater than 0
    """

    type: Required[Literal["rrf"]]
    """The type of ranker, always "rrf" """


class RankerWeightedRanker(TypedDict, total=False):
    alpha: Required[float]
    """Weight factor between 0 and 1.

    0 means only use keyword scores, 1 means only use vector scores, values in
    between blend both scores.
    """

    type: Required[Literal["weighted"]]
    """The type of ranker, always "weighted" """


Ranker: TypeAlias = Union[RankerRrfRanker, RankerWeightedRanker]


class QueryConfig(TypedDict, total=False):
    chunk_template: Required[str]
    """Template for formatting each retrieved chunk in the context.

    Available placeholders: {index} (1-based chunk ordinal), {chunk.content} (chunk
    content string), {metadata} (chunk metadata dict). Default: "Result
    {index}\nContent: {chunk.content}\nMetadata: {metadata}\n"
    """

    max_chunks: Required[int]
    """Maximum number of chunks to retrieve."""

    max_tokens_in_context: Required[int]
    """Maximum number of tokens in the context."""

    query_generator_config: Required[QueryGeneratorConfig]
    """Configuration for the query generator."""

    mode: Literal["vector", "keyword", "hybrid"]
    """Search mode for retrieval—either "vector", "keyword", or "hybrid".

    Default "vector".
    """

    ranker: Ranker
    """Configuration for the ranker to use in hybrid search. Defaults to RRF ranker."""
