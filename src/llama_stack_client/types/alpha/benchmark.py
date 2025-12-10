# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Benchmark"]


class Benchmark(BaseModel):
    """A benchmark resource for evaluating model performance."""

    dataset_id: str
    """Identifier of the dataset to use for the benchmark evaluation."""

    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    scoring_functions: List[str]
    """List of scoring function identifiers to apply during evaluation."""

    metadata: Optional[Dict[str, object]] = None
    """Metadata for this evaluation task."""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["benchmark"]] = None
    """The resource type, always benchmark."""
