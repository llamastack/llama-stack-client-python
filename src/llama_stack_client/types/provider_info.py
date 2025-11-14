# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ProviderInfo"]


class ProviderInfo(BaseModel):
    api: str

    config: Dict[str, object]

    health: Dict[str, object]

    provider_id: str

    provider_type: str
