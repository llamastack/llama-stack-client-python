# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolDef"]


class ToolDef(BaseModel):
    name: str

    description: Optional[str] = None

    input_schema: Optional[Dict[str, object]] = None

    metadata: Optional[Dict[str, object]] = None

    output_schema: Optional[Dict[str, object]] = None

    toolgroup_id: Optional[str] = None
