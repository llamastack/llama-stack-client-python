# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Job"]


class Job(BaseModel):
    """A job execution instance with status tracking."""

    job_id: str

    status: Literal["completed", "in_progress", "failed", "scheduled", "cancelled"]
    """Status of a job execution."""
