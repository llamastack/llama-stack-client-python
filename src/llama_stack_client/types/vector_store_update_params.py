# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import TypedDict

__all__ = ["VectorStoreUpdateParams"]


class VectorStoreUpdateParams(TypedDict, total=False):
    expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The expiration policy for a vector store."""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """Set of 16 key-value pairs that can be attached to an object."""

    name: str
    """The name of the vector store."""
