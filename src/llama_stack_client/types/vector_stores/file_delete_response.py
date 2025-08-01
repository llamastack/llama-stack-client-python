# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["FileDeleteResponse"]


class FileDeleteResponse(BaseModel):
    id: str
    """Unique identifier of the deleted file"""

    deleted: bool
    """Whether the deletion operation was successful"""

    object: str
    """Object type identifier for the deletion response"""
