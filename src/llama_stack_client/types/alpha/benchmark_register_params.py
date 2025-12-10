# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BenchmarkRegisterParams"]


class BenchmarkRegisterParams(TypedDict, total=False):
    benchmark_id: Required[str]
    """The ID of the benchmark to register."""

    dataset_id: Required[str]
    """The ID of the dataset to use for the benchmark."""

    scoring_functions: Required[SequenceNotStr[str]]
    """The scoring functions to use for the benchmark."""

    metadata: Optional[Dict[str, object]]
    """The metadata to use for the benchmark."""

    provider_benchmark_id: Optional[str]
    """The ID of the provider benchmark to use for the benchmark."""

    provider_id: Optional[str]
    """The ID of the provider to use for the benchmark."""
