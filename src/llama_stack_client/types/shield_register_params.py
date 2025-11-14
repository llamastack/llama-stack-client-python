# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ShieldRegisterParams"]


class ShieldRegisterParams(TypedDict, total=False):
    shield_id: Required[str]

    params: Optional[Dict[str, object]]

    provider_id: Optional[str]

    provider_shield_id: Optional[str]
