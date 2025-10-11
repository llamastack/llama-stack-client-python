"""Streaming event primitives for the responses-backed Agent API."""

from dataclasses import dataclass
from typing import Iterable, Optional

from llama_stack_client.types.response_object_stream import (
    OpenAIResponseObjectStreamResponseCompleted,
    OpenAIResponseObjectStreamResponseFailed,
    OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta,
    OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone,
    OpenAIResponseObjectStreamResponseInProgress,
    OpenAIResponseObjectStreamResponseOutputItemAdded,
    OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage,
    OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2,
    OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall,
    OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall,
    OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools,
    OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall,
    OpenAIResponseObjectStreamResponseOutputTextDelta,
    OpenAIResponseObjectStreamResponseOutputTextDone,
    ResponseObjectStream,
)


@dataclass
class AgentStreamEvent:
    type: str


@dataclass
class AgentResponseStarted(AgentStreamEvent):
    response_id: str


@dataclass
class AgentTextDelta(AgentStreamEvent):
    text: str
    response_id: str
    output_index: int


@dataclass
class AgentTextCompleted(AgentStreamEvent):
    text: str
    response_id: str
    output_index: int


@dataclass
class AgentToolCallIssued(AgentStreamEvent):
    response_id: str
    output_index: int
    call_id: str
    name: str
    arguments_json: str


@dataclass
class AgentToolCallDelta(AgentStreamEvent):
    response_id: str
    output_index: int
    call_id: str
    arguments_delta: Optional[str]


@dataclass
class AgentToolCallCompleted(AgentStreamEvent):
    response_id: str
    output_index: int
    call_id: str
    arguments_json: str


@dataclass
class AgentResponseCompleted(AgentStreamEvent):
    response_id: str


@dataclass
class AgentResponseFailed(AgentStreamEvent):
    response_id: str
    error_message: str


def iter_agent_events(events: Iterable[ResponseObjectStream]) -> Iterable[AgentStreamEvent]:
    for event in events:
        if isinstance(event, OpenAIResponseObjectStreamResponseInProgress):
            yield AgentResponseStarted(type="response_started", response_id=event.response.id)
        elif isinstance(event, OpenAIResponseObjectStreamResponseOutputTextDelta):
            yield AgentTextDelta(
                type="text_delta",
                text=event.delta,
                response_id=event.response_id,
                output_index=event.output_index,
            )
        elif isinstance(event, OpenAIResponseObjectStreamResponseOutputTextDone):
            yield AgentTextCompleted(
                type="text_completed",
                text=event.text,
                response_id=event.response_id,
                output_index=event.output_index,
            )
        elif isinstance(event, OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta):
            yield AgentToolCallDelta(
                type="tool_call_delta",
                response_id=event.response_id,
                output_index=event.output_index,
                call_id=event.item_id,
                arguments_delta=event.delta,
            )
        elif isinstance(event, OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone):
            yield AgentToolCallCompleted(
                type="tool_call_completed",
                response_id=event.response_id,
                output_index=event.output_index,
                call_id=event.item_id,
                arguments_json=event.arguments,
            )
        elif isinstance(event, OpenAIResponseObjectStreamResponseOutputItemAdded):
            item = event.item
            if isinstance(
                item,
                OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall,
            ):
                yield AgentToolCallIssued(
                    type="tool_call_issued",
                    response_id=event.response_id,
                    output_index=event.output_index,
                    call_id=item.call_id,
                    name=item.name,
                    arguments_json=item.arguments,
                )
            elif isinstance(
                item,
                OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall,
            ):
                yield AgentToolCallIssued(
                    type="tool_call_issued",
                    response_id=event.response_id,
                    output_index=event.output_index,
                    call_id=item.id,
                    name=item.type,
                    arguments_json="{}",
                )
            elif isinstance(
                item,
                OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall,
            ):
                yield AgentToolCallIssued(
                    type="tool_call_issued",
                    response_id=event.response_id,
                    output_index=event.output_index,
                    call_id=item.id,
                    name=item.name,
                    arguments_json=item.arguments,
                )
            elif isinstance(
                item,
                OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools,
            ):
                yield AgentToolCallIssued(
                    type="tool_call_issued",
                    response_id=event.response_id,
                    output_index=event.output_index,
                    call_id=item.id,
                    name=item.type,
                    arguments_json="{}",
                )
            elif isinstance(item, OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage):
                yield AgentTextCompleted(
                    type="text_completed",
                    text=str(item.content),
                    response_id=event.response_id,
                    output_index=event.output_index,
                )
            elif isinstance(
                item,
                OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2,
            ):
                yield AgentTextCompleted(
                    type="text_completed",
                    text=item.text,
                    response_id=event.response_id,
                    output_index=event.output_index,
                )
        elif isinstance(event, OpenAIResponseObjectStreamResponseCompleted):
            yield AgentResponseCompleted(type="response_completed", response_id=event.response.id)
        elif isinstance(event, OpenAIResponseObjectStreamResponseFailed):
            yield AgentResponseFailed(
                type="response_failed",
                response_id=event.response.id,
                error_message=event.response.error.message if event.response.error else "Unknown error",
            )
