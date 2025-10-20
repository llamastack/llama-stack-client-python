# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ModelRegisterParams"]


class ModelRegisterParams(TypedDict, total=False):
    model_id: Required[str]
    """The identifier of the model to register."""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """Any additional metadata for this model."""

    model_type: Literal["llm", "embedding"]
    """The type of model to register."""

    provider_id: str
    """The identifier of the provider."""

    provider_model_id: str
    """The identifier of the model in the provider."""
