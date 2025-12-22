# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Shield"]


class Shield(BaseModel):
    """A safety shield resource that can be used to check content."""

    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    params: Optional[Dict[str, object]] = None

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["shield"]] = None
