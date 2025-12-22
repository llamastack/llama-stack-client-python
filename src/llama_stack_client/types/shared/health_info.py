# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HealthInfo"]


class HealthInfo(BaseModel):
    """Health status information for the service."""

    status: Literal["OK", "Error", "Not Implemented"]
    """The health status of the service"""
