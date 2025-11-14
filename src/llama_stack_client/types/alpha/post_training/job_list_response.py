# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..post_training_job import PostTrainingJob

__all__ = ["JobListResponse"]

JobListResponse: TypeAlias = List[PostTrainingJob]
