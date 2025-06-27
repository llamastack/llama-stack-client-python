# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileContentResponse", "Content"]


class Content(BaseModel):
    text: str

    type: Literal["text"]


class FileContentResponse(BaseModel):
    attributes: Dict[str, Union[bool, float, str, List[object], object, None]]

    content: List[Content]

    file_id: str

    filename: str
