# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared_params.agent_config import AgentConfig

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    agent_config: Required[AgentConfig]
    """The configuration for the agent."""
