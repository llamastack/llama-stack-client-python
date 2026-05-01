# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .prompt_list_response import PromptListResponse

__all__ = ["ListPromptsResponse"]


class ListPromptsResponse(BaseModel):
    """Response model to list prompts."""

    data: PromptListResponse
