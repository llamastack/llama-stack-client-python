# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ItemDeleteResponse"]


class ItemDeleteResponse(BaseModel):
    id: str
    """The deleted item identifier"""

    deleted: Optional[bool] = None
    """Whether the object was deleted"""

    object: Optional[str] = None
    """Object type"""
