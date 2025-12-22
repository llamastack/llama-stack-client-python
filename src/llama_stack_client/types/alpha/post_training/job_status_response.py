# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["JobStatusResponse", "Checkpoint", "CheckpointTrainingMetrics"]


class CheckpointTrainingMetrics(BaseModel):
    """Training metrics captured during post-training jobs."""

    epoch: int

    perplexity: float

    train_loss: float

    validation_loss: float


class Checkpoint(BaseModel):
    """Checkpoint created during training runs."""

    created_at: datetime

    epoch: int

    identifier: str

    path: str

    post_training_job_id: str

    training_metrics: Optional[CheckpointTrainingMetrics] = None
    """Training metrics captured during post-training jobs."""


class JobStatusResponse(BaseModel):
    """Status of a finetuning job."""

    job_uuid: str

    status: Literal["completed", "in_progress", "failed", "scheduled", "cancelled"]
    """Status of a job execution."""

    checkpoints: Optional[List[Checkpoint]] = None

    completed_at: Optional[datetime] = None

    resources_allocated: Optional[Dict[str, object]] = None

    scheduled_at: Optional[datetime] = None

    started_at: Optional[datetime] = None
