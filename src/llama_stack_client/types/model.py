# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    id: str

    created: int

    owned_by: str

    custom_metadata: Optional[Dict[str, object]] = None

    object: Optional[Literal["model"]] = None
