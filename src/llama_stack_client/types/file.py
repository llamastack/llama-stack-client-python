# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str

    bytes: int

    created_at: int

    expires_at: int

    filename: str

    purpose: Literal["assistants", "batch"]
    """Valid purpose values for OpenAI Files API."""

    object: Optional[Literal["file"]] = None
