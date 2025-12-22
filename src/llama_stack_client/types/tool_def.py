# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolDef"]


class ToolDef(BaseModel):
    """Tool definition used in runtime contexts."""

    name: str

    description: Optional[str] = None

    input_schema: Optional[Dict[str, object]] = None

    metadata: Optional[Dict[str, object]] = None

    output_schema: Optional[Dict[str, object]] = None

    toolgroup_id: Optional[str] = None
