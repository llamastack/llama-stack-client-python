# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AdminListRoutesParams"]


class AdminListRoutesParams(TypedDict, total=False):
    api_filter: Optional[Literal["v1", "v1alpha", "v1beta", "deprecated"]]
    """Filter to control which routes are returned.

    Can be an API level ('v1', 'v1alpha', 'v1beta') to show non-deprecated routes at
    that level, or 'deprecated' to show deprecated routes across all levels. If not
    specified, returns all non-deprecated routes.
    """
