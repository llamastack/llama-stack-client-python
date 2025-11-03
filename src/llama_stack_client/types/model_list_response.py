# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ModelListResponse", "ModelListResponseItem"]


class ModelListResponseItem(BaseModel):
    id: str

    created: int

    object: Literal["model"]

    owned_by: str

    custom_metadata: Optional[Dict[str, Union[bool, float, str, List[builtins.object], builtins.object, None]]] = None


ModelListResponse: TypeAlias = List[ModelListResponseItem]
