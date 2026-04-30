# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VectorStoreUpdateParams", "ExpiresAfter"]


class VectorStoreUpdateParams(TypedDict, total=False):
    expires_after: Optional[ExpiresAfter]
    """Expiration policy for a vector store."""

    metadata: Optional[Dict[str, object]]
    """Metadata to associate with the vector store."""

    name: Optional[str]
    """The new name for the vector store."""


class ExpiresAfter(TypedDict, total=False):
    """Expiration policy for a vector store."""

    anchor: Required[Literal["last_active_at"]]
    """Anchor timestamp after which the expiration policy applies."""

    days: Required[int]
    """The number of days after the anchor time that the vector store will expire."""
