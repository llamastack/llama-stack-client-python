# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConversationObject"]


class ConversationObject(BaseModel):
    """OpenAI-compatible conversation object."""

    id: str
    """The unique ID of the conversation."""

    created_at: int
    """
    The time at which the conversation was created, measured in seconds since the
    Unix epoch.
    """

    items: Optional[List[Dict[str, object]]] = None
    """Initial items to include in the conversation context.

    You may add up to 20 items at a time.
    """

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.
    """

    object: Optional[Literal["conversation"]] = None
    """The object type, which is always conversation."""
