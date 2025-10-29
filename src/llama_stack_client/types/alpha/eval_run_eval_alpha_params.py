# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .benchmark_config_param import BenchmarkConfigParam

__all__ = ["EvalRunEvalAlphaParams"]


class EvalRunEvalAlphaParams(TypedDict, total=False):
    benchmark_config: Required[BenchmarkConfigParam]
    """The configuration for the benchmark."""
