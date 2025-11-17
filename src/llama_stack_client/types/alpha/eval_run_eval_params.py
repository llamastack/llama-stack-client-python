# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .benchmark_config_param import BenchmarkConfigParam

__all__ = ["EvalRunEvalParams"]


class EvalRunEvalParams(TypedDict, total=False):
    benchmark_config: Required[BenchmarkConfigParam]
    """A benchmark configuration for evaluation."""
