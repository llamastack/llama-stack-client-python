# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeleteFileResponse"]


class DeleteFileResponse(BaseModel):
    """Response for deleting a file in OpenAI Files API."""

    id: str
    """The file identifier that was deleted."""

    deleted: bool
    """Whether the file was successfully deleted."""

    object: Optional[Literal["file"]] = None
    """The object type, which is always 'file'."""
