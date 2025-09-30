# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeleteFileResponse"]


class DeleteFileResponse(BaseModel):
    id: str
    """The file identifier that was deleted"""

    deleted: bool
    """Whether the file was successfully deleted"""

    object: Literal["file"]
    """The object type, which is always "file" """
