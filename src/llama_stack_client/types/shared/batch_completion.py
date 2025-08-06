# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..completion_response import CompletionResponse

__all__ = ["BatchCompletion"]


class BatchCompletion(BaseModel):
    batch: List[CompletionResponse]
    """List of completion responses, one for each input in the batch"""
