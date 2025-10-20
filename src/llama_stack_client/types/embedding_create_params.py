# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str]]]
    """Input text to embed, encoded as a string or array of strings.

    To embed multiple inputs in a single request, pass an array of strings.
    """

    model: Required[str]
    """The identifier of the model to use.

    The model must be an embedding model registered with Llama Stack and available
    via the /models endpoint.
    """

    dimensions: int
    """(Optional) The number of dimensions the resulting output embeddings should have.

    Only supported in text-embedding-3 and later models.
    """

    encoding_format: str
    """(Optional) The format to return the embeddings in.

    Can be either "float" or "base64". Defaults to "float".
    """

    user: str
    """
    (Optional) A unique identifier representing your end-user, which can help OpenAI
    to monitor and detect abuse.
    """
