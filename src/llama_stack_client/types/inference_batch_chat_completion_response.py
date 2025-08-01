# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.chat_completion_response import ChatCompletionResponse

__all__ = ["InferenceBatchChatCompletionResponse"]


class InferenceBatchChatCompletionResponse(BaseModel):
    batch: List[ChatCompletionResponse]
    """List of chat completion responses, one for each conversation in the batch"""
