# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeleteFileResponse"]


class DeleteFileResponse(BaseModel):
    """Response for deleting a file in OpenAI Files API."""

    id: str

    deleted: bool

    object: Optional[Literal["file"]] = None
