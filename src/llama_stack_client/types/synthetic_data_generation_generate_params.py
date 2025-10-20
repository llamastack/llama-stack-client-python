# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .shared_params.message import Message

__all__ = ["SyntheticDataGenerationGenerateParams"]


class SyntheticDataGenerationGenerateParams(TypedDict, total=False):
    dialogs: Required[Iterable[Message]]
    """List of conversation messages to use as input for synthetic data generation"""

    filtering_function: Required[Literal["none", "random", "top_k", "top_p", "top_k_top_p", "sigmoid"]]
    """Type of filtering to apply to generated synthetic data samples"""

    model: str
    """(Optional) The identifier of the model to use.

    The model must be registered with Llama Stack and available via the /models
    endpoint
    """
