# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    identifier: str
    """Unique identifier for this resource in llama stack"""

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Any additional metadata for this model"""

    api_model_type: Literal["llm", "embedding"] = FieldInfo(alias="model_type")
    """The type of model (LLM or embedding model)"""

    provider_id: str
    """ID of the provider that owns this resource"""

    type: Literal["model"]
    """The resource type, always 'model' for model resources"""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""
