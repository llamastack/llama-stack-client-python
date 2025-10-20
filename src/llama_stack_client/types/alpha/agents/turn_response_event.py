# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .turn import Turn
from ...._utils import PropertyInfo
from ...._models import BaseModel
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ...shared.tool_call import ToolCall
from ..tool_execution_step import ToolExecutionStep
from ..memory_retrieval_step import MemoryRetrievalStep

__all__ = [
    "TurnResponseEvent",
    "Payload",
    "PayloadAgentTurnResponseStepStartPayload",
    "PayloadAgentTurnResponseStepProgressPayload",
    "PayloadAgentTurnResponseStepProgressPayloadDelta",
    "PayloadAgentTurnResponseStepProgressPayloadDeltaTextDelta",
    "PayloadAgentTurnResponseStepProgressPayloadDeltaImageDelta",
    "PayloadAgentTurnResponseStepProgressPayloadDeltaToolCallDelta",
    "PayloadAgentTurnResponseStepProgressPayloadDeltaToolCallDeltaToolCall",
    "PayloadAgentTurnResponseStepCompletePayload",
    "PayloadAgentTurnResponseStepCompletePayloadStepDetails",
    "PayloadAgentTurnResponseTurnStartPayload",
    "PayloadAgentTurnResponseTurnCompletePayload",
    "PayloadAgentTurnResponseTurnAwaitingInputPayload",
]


class PayloadAgentTurnResponseStepStartPayload(BaseModel):
    event_type: Literal["step_start"]
    """Type of event being reported"""

    step_id: str
    """Unique identifier for the step within a turn"""

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]
    """Type of step being executed"""

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional metadata for the step"""


class PayloadAgentTurnResponseStepProgressPayloadDeltaTextDelta(BaseModel):
    text: str
    """The incremental text content"""

    type: Literal["text"]
    """Discriminator type of the delta. Always "text" """


class PayloadAgentTurnResponseStepProgressPayloadDeltaImageDelta(BaseModel):
    image: str
    """The incremental image data as bytes"""

    type: Literal["image"]
    """Discriminator type of the delta. Always "image" """


PayloadAgentTurnResponseStepProgressPayloadDeltaToolCallDeltaToolCall: TypeAlias = Union[str, ToolCall]


class PayloadAgentTurnResponseStepProgressPayloadDeltaToolCallDelta(BaseModel):
    parse_status: Literal["started", "in_progress", "failed", "succeeded"]
    """Current parsing status of the tool call"""

    tool_call: PayloadAgentTurnResponseStepProgressPayloadDeltaToolCallDeltaToolCall
    """Either an in-progress tool call string or the final parsed tool call"""

    type: Literal["tool_call"]
    """Discriminator type of the delta. Always "tool_call" """


PayloadAgentTurnResponseStepProgressPayloadDelta: TypeAlias = Annotated[
    Union[
        PayloadAgentTurnResponseStepProgressPayloadDeltaTextDelta,
        PayloadAgentTurnResponseStepProgressPayloadDeltaImageDelta,
        PayloadAgentTurnResponseStepProgressPayloadDeltaToolCallDelta,
    ],
    PropertyInfo(discriminator="type"),
]


class PayloadAgentTurnResponseStepProgressPayload(BaseModel):
    delta: PayloadAgentTurnResponseStepProgressPayloadDelta
    """Incremental content changes during step execution"""

    event_type: Literal["step_progress"]
    """Type of event being reported"""

    step_id: str
    """Unique identifier for the step within a turn"""

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]
    """Type of step being executed"""


PayloadAgentTurnResponseStepCompletePayloadStepDetails: TypeAlias = Annotated[
    Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep],
    PropertyInfo(discriminator="step_type"),
]


class PayloadAgentTurnResponseStepCompletePayload(BaseModel):
    event_type: Literal["step_complete"]
    """Type of event being reported"""

    step_details: PayloadAgentTurnResponseStepCompletePayloadStepDetails
    """Complete details of the executed step"""

    step_id: str
    """Unique identifier for the step within a turn"""

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]
    """Type of step being executed"""


class PayloadAgentTurnResponseTurnStartPayload(BaseModel):
    event_type: Literal["turn_start"]
    """Type of event being reported"""

    turn_id: str
    """Unique identifier for the turn within a session"""


class PayloadAgentTurnResponseTurnCompletePayload(BaseModel):
    event_type: Literal["turn_complete"]
    """Type of event being reported"""

    turn: Turn
    """Complete turn data including all steps and results"""


class PayloadAgentTurnResponseTurnAwaitingInputPayload(BaseModel):
    event_type: Literal["turn_awaiting_input"]
    """Type of event being reported"""

    turn: Turn
    """Turn data when waiting for external tool responses"""


Payload: TypeAlias = Annotated[
    Union[
        PayloadAgentTurnResponseStepStartPayload,
        PayloadAgentTurnResponseStepProgressPayload,
        PayloadAgentTurnResponseStepCompletePayload,
        PayloadAgentTurnResponseTurnStartPayload,
        PayloadAgentTurnResponseTurnCompletePayload,
        PayloadAgentTurnResponseTurnAwaitingInputPayload,
    ],
    PropertyInfo(discriminator="event_type"),
]


class TurnResponseEvent(BaseModel):
    payload: Payload
    """Event-specific payload containing event data"""
