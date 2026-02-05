# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreateEmbeddingsResponse", "Data", "Usage"]


class Data(BaseModel):
    """A single embedding data object from an OpenAI-compatible embeddings response."""

    embedding: Union[List[float], str]
    """
    The embedding vector as a list of floats (when encoding_format='float') or as a
    base64-encoded string.
    """

    index: int
    """The index of the embedding in the input list."""

    object: Optional[Literal["embedding"]] = None
    """The object type."""


class Usage(BaseModel):
    """Usage information."""

    prompt_tokens: int
    """The number of tokens in the input."""

    total_tokens: int
    """The total number of tokens used."""


class CreateEmbeddingsResponse(BaseModel):
    """Response from an OpenAI-compatible embeddings request."""

    data: List[Data]
    """List of embedding data objects."""

    model: str
    """The model that was used to generate the embeddings."""

    usage: Usage
    """Usage information."""

    object: Optional[Literal["list"]] = None
    """The object type."""
