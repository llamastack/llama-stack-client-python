# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.safety_violation import SafetyViolation

__all__ = ["RunShieldResponse"]


class RunShieldResponse(BaseModel):
    violation: Optional[SafetyViolation] = None
    """(Optional) Safety violation detected by the shield, if any"""
