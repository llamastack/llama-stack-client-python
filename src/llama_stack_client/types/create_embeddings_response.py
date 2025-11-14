# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreateEmbeddingsResponse", "Data", "Usage"]


class Data(BaseModel):
    embedding: Union[List[float], str]

    index: int

    object: Optional[Literal["embedding"]] = None


class Usage(BaseModel):
    prompt_tokens: int

    total_tokens: int


class CreateEmbeddingsResponse(BaseModel):
    data: List[Data]

    model: str

    usage: Usage
    """Usage information for an OpenAI-compatible embeddings response."""

    object: Optional[Literal["list"]] = None
