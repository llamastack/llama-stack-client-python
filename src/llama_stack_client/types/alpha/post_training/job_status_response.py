# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["JobStatusResponse", "Checkpoint", "CheckpointTrainingMetrics"]


class CheckpointTrainingMetrics(BaseModel):
    epoch: int
    """Training epoch number"""

    perplexity: float
    """Perplexity metric indicating model confidence"""

    train_loss: float
    """Loss value on the training dataset"""

    validation_loss: float
    """Loss value on the validation dataset"""


class Checkpoint(BaseModel):
    created_at: datetime
    """Timestamp when the checkpoint was created"""

    epoch: int
    """Training epoch when the checkpoint was saved"""

    identifier: str
    """Unique identifier for the checkpoint"""

    path: str
    """File system path where the checkpoint is stored"""

    post_training_job_id: str
    """Identifier of the training job that created this checkpoint"""

    training_metrics: Optional[CheckpointTrainingMetrics] = None
    """(Optional) Training metrics associated with this checkpoint"""


class JobStatusResponse(BaseModel):
    checkpoints: List[Checkpoint]
    """List of model checkpoints created during training"""

    job_uuid: str
    """Unique identifier for the training job"""

    status: Literal["completed", "in_progress", "failed", "scheduled", "cancelled"]
    """Current status of the training job"""

    completed_at: Optional[datetime] = None
    """(Optional) Timestamp when the job finished, if completed"""

    resources_allocated: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Information about computational resources allocated to the job"""

    scheduled_at: Optional[datetime] = None
    """(Optional) Timestamp when the job was scheduled"""

    started_at: Optional[datetime] = None
    """(Optional) Timestamp when the job execution began"""
