# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .file import File
from .._models import BaseModel

__all__ = ["ListFilesResponse"]


class ListFilesResponse(BaseModel):
    data: List[File]

    first_id: str

    has_more: bool

    last_id: str

    object: Optional[Literal["list"]] = None
