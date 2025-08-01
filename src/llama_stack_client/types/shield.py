# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Shield"]


class Shield(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["shield"]
    """The resource type, always shield"""

    params: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Configuration parameters for the shield"""

    provider_resource_id: Optional[str] = None
