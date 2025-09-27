# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = ["ToolParamDefinition"]


class ToolParamDefinition(BaseModel):
    param_type: str

    default: Union[bool, float, str, List[object], object, None] = None

    description: Optional[str] = None

    items: Union[bool, float, str, List[object], object, None] = None

    required: Optional[bool] = None

    title: Optional[str] = None
