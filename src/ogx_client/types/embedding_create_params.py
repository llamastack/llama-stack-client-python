# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]]]
    """Input text to embed, encoded as a string or array of tokens."""

    model: Required[str]
    """The identifier of the model to use."""

    dimensions: int
    """The number of dimensions for output embeddings."""

    encoding_format: Literal["float", "base64"]
    """The format to return the embeddings in."""

    user: str
    """A unique identifier representing your end-user."""
