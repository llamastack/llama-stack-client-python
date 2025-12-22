# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelRetrieveResponse"]


class ModelRetrieveResponse(BaseModel):
    """A model resource representing an AI model registered in Llama Stack."""

    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    metadata: Optional[Dict[str, object]] = None
    """Any additional metadata for this model"""

    api_model_type: Optional[Literal["llm", "embedding", "rerank"]] = FieldInfo(alias="model_type", default=None)
    """Enumeration of supported model types in Llama Stack."""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["model"]] = None
