# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ModelRegisterParams"]


class ModelRegisterParams(TypedDict, total=False):
    model_id: Required[str]

    metadata: Optional[Dict[str, object]]

    model_type: Optional[Literal["llm", "embedding", "rerank"]]
    """Enumeration of supported model types in Llama Stack."""

    provider_id: Optional[str]

    provider_model_id: Optional[str]
