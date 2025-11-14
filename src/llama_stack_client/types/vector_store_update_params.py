# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["VectorStoreUpdateParams"]


class VectorStoreUpdateParams(TypedDict, total=False):
    expires_after: Optional[Dict[str, object]]

    metadata: Optional[Dict[str, object]]

    name: Optional[str]
