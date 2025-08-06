# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .query_generator_config import QueryGeneratorConfig

__all__ = ["QueryConfig", "Ranker", "RankerRrfRanker", "RankerWeightedRanker"]


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
