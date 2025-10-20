# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["VectorStoreCreateParams"]


class VectorStoreCreateParams(TypedDict, total=False):
    chunking_strategy: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Strategy for splitting files into chunks"""

    expires_after: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Expiration policy for the vector store"""

    file_ids: SequenceNotStr[str]
    """List of file IDs to include in the vector store"""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """Set of key-value pairs that can be attached to the vector store"""

    name: str
    """(Optional) A name for the vector store"""
