# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ModelRegisterParams"]


class ModelRegisterParams(TypedDict, total=False):
    model_id: Required[str]
    """The identifier of the model to register."""

    metadata: Optional[Dict[str, object]]
    """Any additional metadata for this model."""

    model_type: Optional[Literal["llm", "embedding", "rerank"]]
    """Enumeration of supported model types in Llama Stack."""

    model_validation: Optional[bool]
    """Enable model availability check during registration.

    When false (default), validation is deferred to runtime and model is preserved
    during provider refresh.
    """

    provider_id: Optional[str]
    """The identifier of the provider."""

    provider_model_id: Optional[str]
    """The identifier of the model in the provider."""
