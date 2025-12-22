# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.provider_info import ProviderInfo

__all__ = ["ProviderListResponse"]

ProviderListResponse: TypeAlias = List[ProviderInfo]
