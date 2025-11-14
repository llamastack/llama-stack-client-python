# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["DatasetIterrowsResponse"]


class DatasetIterrowsResponse(BaseModel):
    data: List[Dict[str, object]]

    has_more: bool

    url: Optional[str] = None
