# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    completion_window: Required[Literal["24h"]]
    """The time window within which the batch should be processed."""

    endpoint: Required[str]
    """The endpoint to be used for all requests in the batch."""

    input_file_id: Required[str]
    """The ID of an uploaded file containing requests for the batch."""

    idempotency_key: Optional[str]
    """Optional idempotency key. When provided, enables idempotent behavior."""

    metadata: Optional[Dict[str, str]]
    """Optional metadata for the batch."""
