# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """The file identifier, which can be referenced in the API endpoints"""

    bytes: int
    """The size of the file, in bytes"""

    created_at: int
    """The Unix timestamp (in seconds) for when the file was created"""

    expires_at: int
    """The Unix timestamp (in seconds) for when the file expires"""

    filename: str
    """The name of the file"""

    object: Literal["file"]
    """The object type, which is always "file" """

    purpose: Literal["assistants", "batch"]
    """The intended purpose of the file"""
