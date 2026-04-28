# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResponseDeleteResponse"]


class ResponseDeleteResponse(BaseModel):
    """Response object confirming deletion of an OpenAI response."""

    id: str

    deleted: Optional[bool] = None

    object: Optional[Literal["response"]] = None
