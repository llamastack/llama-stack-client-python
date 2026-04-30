# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelRetrieveResponse"]


class ModelRetrieveResponse(BaseModel):
    """A model resource representing an AI model registered in OGX."""

    id: str
    """The model identifier (OpenAI-compatible alias for identifier)."""

    identifier: str
    """Unique identifier for this resource in ogx"""

    object: Literal["model"]
    """The object type, always 'model'."""

    provider_id: str
    """ID of the provider that owns this resource"""

    created: Optional[int] = None
    """The Unix timestamp in seconds when the model was created."""

    metadata: Optional[Dict[str, builtins.object]] = None
    """Any additional metadata for this model"""

    api_model_type: Optional[Literal["llm", "embedding", "rerank"]] = FieldInfo(alias="model_type", default=None)
    """Enumeration of supported model types in OGX."""

    api_model_validation: Optional[bool] = FieldInfo(alias="model_validation", default=None)
    """Enable model availability check during registration.

    When false (default), validation is deferred to runtime and model is preserved
    during provider refresh.
    """

    owned_by: Optional[str] = None
    """The owner of the model."""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["model"]] = None
