# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ModelListResponse", "ModelListResponseItem"]


class ModelListResponseItem(BaseModel):
    id: str

    created: int

    object: Literal["model"]

    owned_by: str


ModelListResponse: TypeAlias = List[ModelListResponseItem]
