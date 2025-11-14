# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ToolRuntimeInvokeToolParams"]


class ToolRuntimeInvokeToolParams(TypedDict, total=False):
    kwargs: Required[Dict[str, object]]

    tool_name: Required[str]

    authorization: Optional[str]
