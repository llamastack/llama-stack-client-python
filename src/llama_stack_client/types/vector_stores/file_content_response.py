# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileContentResponse", "Content"]


class Content(BaseModel):
    text: str
    """The actual text content"""

    type: Literal["text"]
    """Content type, currently only "text" is supported"""


class FileContentResponse(BaseModel):
    attributes: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Key-value attributes associated with the file"""

    content: List[Content]
    """List of content items from the file"""

    file_id: str
    """Unique identifier for the file"""

    filename: str
    """Name of the file"""
