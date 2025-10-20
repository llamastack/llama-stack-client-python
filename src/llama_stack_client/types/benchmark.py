# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Benchmark"]


class Benchmark(BaseModel):
    dataset_id: str
    """Identifier of the dataset to use for the benchmark evaluation"""

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Metadata for this evaluation task"""

    provider_id: str

    scoring_functions: List[str]
    """List of scoring function identifiers to apply during evaluation"""

    type: Literal["benchmark"]
    """The resource type, always benchmark"""

    provider_resource_id: Optional[str] = None
