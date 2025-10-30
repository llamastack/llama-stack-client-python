# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel
from ..shared.agent_config import AgentConfig

__all__ = ["AgentRetrieveResponse"]


class AgentRetrieveResponse(BaseModel):
    agent_config: AgentConfig
    """Configuration settings for the agent"""

    agent_id: str
    """Unique identifier for the agent"""

    created_at: datetime
    """Timestamp when the agent was created"""
