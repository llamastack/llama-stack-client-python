# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ShieldRegisterParams"]


class ShieldRegisterParams(TypedDict, total=False):
    shield_id: Required[str]
    """The identifier of the shield to register."""

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The parameters of the shield."""

    provider_id: str
    """The identifier of the provider."""

    provider_shield_id: str
    """The identifier of the shield in the provider."""
