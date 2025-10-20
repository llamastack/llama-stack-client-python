# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConversationObject"]


class ConversationObject(BaseModel):
    id: str

    created_at: int

    object: Literal["conversation"]

    items: Optional[List[builtins.object]] = None

    metadata: Optional[Dict[str, str]] = None
