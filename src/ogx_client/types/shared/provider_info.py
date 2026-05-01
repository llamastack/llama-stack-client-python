# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["ProviderInfo"]


class ProviderInfo(BaseModel):
    """
    Information about a registered provider including its configuration and health status.
    """

    api: str
    """The API name this provider implements"""

    config: Dict[str, object]
    """Configuration parameters for the provider"""

    health: Dict[str, object]
    """Current health status of the provider"""

    provider_id: str
    """Unique identifier for the provider"""

    provider_type: str
    """The type of provider implementation"""
