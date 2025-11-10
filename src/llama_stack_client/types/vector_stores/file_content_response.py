# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileContentResponse", "Data"]


class Data(BaseModel):
    text: str
    """The actual text content"""

    type: Literal["text"]
    """Content type, currently only "text" is supported"""


class FileContentResponse(BaseModel):
    data: List[Data]
    """Parsed content of the file"""

    has_more: bool
    """Indicates if there are more content pages to fetch"""

    object: Literal["vector_store.file_content.page"]
    """The object type, which is always `vector_store.file_content.page`"""

    next_page: Optional[str] = None
    """The token for the next page, if any"""
