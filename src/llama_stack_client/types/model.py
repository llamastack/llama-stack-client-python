# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    """A model from OpenAI.

    :id: The ID of the model
    :object: The object type, which will be "model"
    :created: The Unix timestamp in seconds when the model was created
    :owned_by: The owner of the model
    :custom_metadata: Llama Stack-specific metadata including model_type, provider info, and additional metadata
    """

    id: str

    created: int

    owned_by: str

    custom_metadata: Optional[Dict[str, object]] = None

    object: Optional[Literal["model"]] = None

    @property
    def model_type(self) -> Optional[str]:
        if not self.custom_metadata:
            return None
        value = self.custom_metadata.get("model_type")
        return value if isinstance(value, str) else None

    @property
    def provider_id(self) -> Optional[str]:
        if not self.custom_metadata:
            return None
        value = self.custom_metadata.get("provider_id")
        return value if isinstance(value, str) else None

    @property
    def provider_resource_id(self) -> Optional[str]:
        if not self.custom_metadata:
            return None
        value = self.custom_metadata.get("provider_resource_id")
        return value if isinstance(value, str) else None

    @property
    def identifier(self) -> str:
        return self.id

    @property
    def metadata(self) -> Optional[Dict[str, object]]:
        if not self.custom_metadata:
            return None
        filtered = {
            key: value
            for key, value in self.custom_metadata.items()
            if key
            not in (
                "model_type",
                "provider_id",
                "provider_resource_id",
            )
        }
        return filtered or None
