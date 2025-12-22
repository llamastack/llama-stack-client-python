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

    index: int

    object: Optional[Literal["embedding"]] = None


class Usage(BaseModel):
    """Usage information for an OpenAI-compatible embeddings response."""

    prompt_tokens: int

    total_tokens: int


class CreateEmbeddingsResponse(BaseModel):
    """Response from an OpenAI-compatible embeddings request."""

    data: List[Data]

    model: str

    usage: Usage
    """Usage information for an OpenAI-compatible embeddings response."""

    object: Optional[Literal["list"]] = None
