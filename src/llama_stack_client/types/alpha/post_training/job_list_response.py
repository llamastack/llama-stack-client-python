# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["JobListResponse", "JobListResponseItem"]


class JobListResponseItem(BaseModel):
    job_uuid: str


JobListResponse: TypeAlias = List[JobListResponseItem]
