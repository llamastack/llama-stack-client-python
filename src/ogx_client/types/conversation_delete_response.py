# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConversationDeleteResponse"]


class ConversationDeleteResponse(BaseModel):
    """Response for deleted conversation."""

    id: str
    """The deleted conversation identifier"""

    deleted: Optional[bool] = None
    """Whether the object was deleted"""

    object: Optional[str] = None
    """Object type"""
