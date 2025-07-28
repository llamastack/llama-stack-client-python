# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["JobArtifactsResponse", "Checkpoint", "CheckpointTrainingMetrics"]


class CheckpointTrainingMetrics(BaseModel):
    epoch: int

    perplexity: float

    train_loss: float

    validation_loss: float


class Checkpoint(BaseModel):
    created_at: datetime

    epoch: int

    identifier: str

    path: str

    post_training_job_id: str

    training_metrics: Optional[CheckpointTrainingMetrics] = None


class JobArtifactsResponse(BaseModel):
    checkpoints: List[Checkpoint]

    job_uuid: str
