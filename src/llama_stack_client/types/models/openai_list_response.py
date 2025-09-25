# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["OpenAIListResponse", "OpenAIListResponseItem"]


class OpenAIListResponseItem(BaseModel):
    id: str

    created: int

    object: Literal["model"]

    owned_by: str


OpenAIListResponse: TypeAlias = List[OpenAIListResponseItem]
