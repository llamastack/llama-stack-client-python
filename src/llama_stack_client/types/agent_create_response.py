# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AgentCreateResponse"]


class AgentCreateResponse(BaseModel):
    agent_id: str
    """Unique identifier for the created agent"""
