# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["InferenceRerankResponse", "InferenceRerankResponseItem"]


class InferenceRerankResponseItem(BaseModel):
    """A single rerank result from a reranking response."""

    index: int
    """The original index of the document in the input list."""

    relevance_score: float
    """The relevance score from the model output.

    Higher scores indicate greater relevance.
    """


InferenceRerankResponse: TypeAlias = List[InferenceRerankResponseItem]
