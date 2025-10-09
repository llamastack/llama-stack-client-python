# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .post_training.job_list_response import JobListResponse

__all__ = ["ListPostTrainingJobsResponse"]


class ListPostTrainingJobsResponse(BaseModel):
    data: JobListResponse
