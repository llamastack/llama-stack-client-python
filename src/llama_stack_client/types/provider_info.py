# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ProviderInfo"]


class ProviderInfo(BaseModel):
    """
    Information about a registered provider including its configuration and health status.
    """

    api: str

    config: Dict[str, object]

    health: Dict[str, object]

    provider_id: str

    provider_type: str
