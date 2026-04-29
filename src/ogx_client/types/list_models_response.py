# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .model import Model
from .._models import BaseModel

__all__ = ["ListModelsResponse"]


class ListModelsResponse(BaseModel):
    """Response containing a list of OpenAI model objects."""

    data: List[Model]
    """List of OpenAI model objects."""

    object: Optional[Literal["list"]] = None
