# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["DatasetIterrowsResponse"]


class DatasetIterrowsResponse(BaseModel):
    """A generic paginated response that follows a simple format."""

    data: List[Dict[str, object]]

    has_more: bool

    url: Optional[str] = None
