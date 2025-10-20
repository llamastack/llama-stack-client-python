# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel
from .interleaved_content import InterleavedContent

__all__ = ["QueryResult"]


class QueryResult(BaseModel):
    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Additional metadata about the query result"""

    content: Optional[InterleavedContent] = None
    """(Optional) The retrieved content from the query"""
