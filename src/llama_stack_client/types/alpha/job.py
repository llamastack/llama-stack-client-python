# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Job"]


class Job(BaseModel):
    job_id: str

    status: Literal["completed", "in_progress", "failed", "scheduled", "cancelled"]
    """Status of a job execution."""
