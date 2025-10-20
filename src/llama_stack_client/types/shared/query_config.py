# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "QueryConfig",
    "QueryGeneratorConfig",
    "QueryGeneratorConfigDefaultRagQueryGeneratorConfig",
    "QueryGeneratorConfigLlmragQueryGeneratorConfig",
    "Ranker",
    "RankerRrfRanker",
    "RankerWeightedRanker",
]


class QueryGeneratorConfigDefaultRagQueryGeneratorConfig(BaseModel):
    separator: str
    """String separator used to join query terms"""

    type: Literal["default"]
    """Type of query generator, always 'default'"""


class QueryGeneratorConfigLlmragQueryGeneratorConfig(BaseModel):
    model: str
    """Name of the language model to use for query generation"""

    template: str
    """Template string for formatting the query generation prompt"""

    type: Literal["llm"]
    """Type of query generator, always 'llm'"""


QueryGeneratorConfig: TypeAlias = Annotated[
    Union[QueryGeneratorConfigDefaultRagQueryGeneratorConfig, QueryGeneratorConfigLlmragQueryGeneratorConfig],
    PropertyInfo(discriminator="type"),
]


class RankerRrfRanker(BaseModel):
    impact_factor: float
    """The impact factor for RRF scoring.

    Higher values give more weight to higher-ranked results. Must be greater than 0
    """

    type: Literal["rrf"]
    """The type of ranker, always "rrf" """


class RankerWeightedRanker(BaseModel):
    alpha: float
    """Weight factor between 0 and 1.

    0 means only use keyword scores, 1 means only use vector scores, values in
    between blend both scores.
    """

    type: Literal["weighted"]
    """The type of ranker, always "weighted" """


Ranker: TypeAlias = Annotated[Union[RankerRrfRanker, RankerWeightedRanker], PropertyInfo(discriminator="type")]


class QueryConfig(BaseModel):
    chunk_template: str
    """Template for formatting each retrieved chunk in the context.

    Available placeholders: {index} (1-based chunk ordinal), {chunk.content} (chunk
    content string), {metadata} (chunk metadata dict). Default: "Result
    {index}\nContent: {chunk.content}\nMetadata: {metadata}\n"
    """

    max_chunks: int
    """Maximum number of chunks to retrieve."""

    max_tokens_in_context: int
    """Maximum number of tokens in the context."""

    query_generator_config: QueryGeneratorConfig
    """Configuration for the query generator."""

    mode: Optional[Literal["vector", "keyword", "hybrid"]] = None
    """Search mode for retrieval—either "vector", "keyword", or "hybrid".

    Default "vector".
    """

    ranker: Optional[Ranker] = None
    """Configuration for the ranker to use in hybrid search. Defaults to RRF ranker."""
