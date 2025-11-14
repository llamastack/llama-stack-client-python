# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BenchmarkRegisterParams"]


class BenchmarkRegisterParams(TypedDict, total=False):
    benchmark_id: Required[str]

    dataset_id: Required[str]

    scoring_functions: Required[SequenceNotStr[str]]

    metadata: Optional[Dict[str, object]]

    provider_benchmark_id: Optional[str]

    provider_id: Optional[str]
