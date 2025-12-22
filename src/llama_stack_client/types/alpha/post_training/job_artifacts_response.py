# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["JobArtifactsResponse", "Checkpoint", "CheckpointTrainingMetrics"]


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


class JobArtifactsResponse(BaseModel):
    """Artifacts of a finetuning job."""

    job_uuid: str

    checkpoints: Optional[List[Checkpoint]] = None
