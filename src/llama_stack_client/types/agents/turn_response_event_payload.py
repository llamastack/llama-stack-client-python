# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .turn import Turn
from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ..tool_execution_step import ToolExecutionStep
from ..shared.content_delta import ContentDelta
from ..memory_retrieval_step import MemoryRetrievalStep

__all__ = [
    "TurnResponseEventPayload",
    "AgentTurnResponseStepStartPayload",
    "AgentTurnResponseStepProgressPayload",
    "AgentTurnResponseStepCompletePayload",
    "AgentTurnResponseStepCompletePayloadStepDetails",
    "AgentTurnResponseTurnStartPayload",
    "AgentTurnResponseTurnCompletePayload",
    "AgentTurnResponseTurnAwaitingInputPayload",
]


class AgentTurnResponseStepStartPayload(BaseModel):
    event_type: Literal["step_start"]
    """Type of event being reported"""

    step_id: str
    """Unique identifier for the step within a turn"""

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]
    """Type of step being executed"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata for the step"""


class AgentTurnResponseStepProgressPayload(BaseModel):
    delta: ContentDelta
    """Incremental content changes during step execution"""

    event_type: Literal["step_progress"]
    """Type of event being reported"""

    step_id: str
    """Unique identifier for the step within a turn"""

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]
    """Type of step being executed"""


AgentTurnResponseStepCompletePayloadStepDetails: TypeAlias = Annotated[
    Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep],
    PropertyInfo(discriminator="step_type"),
]


class AgentTurnResponseStepCompletePayload(BaseModel):
    event_type: Literal["step_complete"]
    """Type of event being reported"""

    step_details: AgentTurnResponseStepCompletePayloadStepDetails
    """Complete details of the executed step"""

    step_id: str
    """Unique identifier for the step within a turn"""

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]
    """Type of step being executed"""


class AgentTurnResponseTurnStartPayload(BaseModel):
    event_type: Literal["turn_start"]
    """Type of event being reported"""

    turn_id: str
    """Unique identifier for the turn within a session"""


class AgentTurnResponseTurnCompletePayload(BaseModel):
    event_type: Literal["turn_complete"]
    """Type of event being reported"""

    turn: Turn
    """Complete turn data including all steps and results"""


class AgentTurnResponseTurnAwaitingInputPayload(BaseModel):
    event_type: Literal["turn_awaiting_input"]
    """Type of event being reported"""

    turn: Turn
    """Turn data when waiting for external tool responses"""


TurnResponseEventPayload: TypeAlias = Annotated[
    Union[
        AgentTurnResponseStepStartPayload,
        AgentTurnResponseStepProgressPayload,
        AgentTurnResponseStepCompletePayload,
        AgentTurnResponseTurnStartPayload,
        AgentTurnResponseTurnCompletePayload,
        AgentTurnResponseTurnAwaitingInputPayload,
    ],
    PropertyInfo(discriminator="event_type"),
]
