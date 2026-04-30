# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .file import File
from .._models import BaseModel

__all__ = ["ListFilesResponse"]


class ListFilesResponse(BaseModel):
    """Response for listing files in OpenAI Files API."""

    data: List[File]
    """The list of files."""

    first_id: str
    """The ID of the first file in the list for pagination."""

    has_more: bool
    """Whether there are more files available beyond this page."""

    last_id: str
    """The ID of the last file in the list for pagination."""

    object: Optional[Literal["list"]] = None
    """The object type, which is always 'list'."""
