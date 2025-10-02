# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["DatasetIterrowsResponse"]


class DatasetIterrowsResponse(BaseModel):
    data: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """The list of items for the current page"""

    has_more: bool
    """Whether there are more items available after this set"""

    url: Optional[str] = None
    """The URL for accessing this list"""
