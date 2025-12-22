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

    first_id: str

    has_more: bool

    last_id: str

    object: Optional[Literal["list"]] = None
