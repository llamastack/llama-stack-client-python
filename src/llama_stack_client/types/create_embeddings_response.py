# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreateEmbeddingsResponse", "Data", "Usage"]


class Data(BaseModel):
    embedding: Union[List[float], str]
    """
    The embedding vector as a list of floats (when encoding_format="float") or as a
    base64-encoded string (when encoding_format="base64")
    """

    index: int
    """The index of the embedding in the input list"""

    object: Literal["embedding"]
    """The object type, which will be "embedding" """


class Usage(BaseModel):
    prompt_tokens: int
    """The number of tokens in the input"""

    total_tokens: int
    """The total number of tokens used"""


class CreateEmbeddingsResponse(BaseModel):
    data: List[Data]
    """List of embedding data objects"""

    model: str
    """The model that was used to generate the embeddings"""

    object: Literal["list"]
    """The object type, which will be "list" """

    usage: Usage
    """Usage information"""
