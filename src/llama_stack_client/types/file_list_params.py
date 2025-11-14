# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: Optional[str]

    limit: Optional[int]

    order: Optional[Literal["asc", "desc"]]
    """Sort order for paginated responses."""

    purpose: Optional[Literal["assistants", "batch"]]
    """Valid purpose values for OpenAI Files API."""
