# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .response_object import ResponseObject

__all__ = [
    "ResponseObjectStream",
    "OpenAIResponseObjectStreamResponseCreated",
    "OpenAIResponseObjectStreamResponseInProgress",
    "OpenAIResponseObjectStreamResponseOutputItemAdded",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItem",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprob",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprobTopLogprob",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMcpApprovalRequest",
    "OpenAIResponseObjectStreamResponseOutputItemDone",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItem",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprob",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprobTopLogprob",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest",
    "OpenAIResponseObjectStreamResponseOutputTextDelta",
    "OpenAIResponseObjectStreamResponseOutputTextDeltaLogprob",
    "OpenAIResponseObjectStreamResponseOutputTextDeltaLogprobTopLogprob",
    "OpenAIResponseObjectStreamResponseOutputTextDone",
    "OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta",
    "OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone",
    "OpenAIResponseObjectStreamResponseWebSearchCallInProgress",
    "OpenAIResponseObjectStreamResponseWebSearchCallSearching",
    "OpenAIResponseObjectStreamResponseWebSearchCallCompleted",
    "OpenAIResponseObjectStreamResponseMcpListToolsInProgress",
    "OpenAIResponseObjectStreamResponseMcpListToolsFailed",
    "OpenAIResponseObjectStreamResponseMcpListToolsCompleted",
    "OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta",
    "OpenAIResponseObjectStreamResponseMcpCallArgumentsDone",
    "OpenAIResponseObjectStreamResponseMcpCallInProgress",
    "OpenAIResponseObjectStreamResponseMcpCallFailed",
    "OpenAIResponseObjectStreamResponseMcpCallCompleted",
    "OpenAIResponseObjectStreamResponseContentPartAdded",
    "OpenAIResponseObjectStreamResponseContentPartAddedPart",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextLogprob",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextLogprobTopLogprob",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText",
    "OpenAIResponseObjectStreamResponseContentPartDone",
    "OpenAIResponseObjectStreamResponseContentPartDonePart",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextLogprob",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextLogprobTopLogprob",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText",
    "OpenAIResponseObjectStreamResponseReasoningTextDelta",
    "OpenAIResponseObjectStreamResponseReasoningTextDone",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartAdded",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartDone",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart",
    "OpenAIResponseObjectStreamResponseReasoningSummaryTextDelta",
    "OpenAIResponseObjectStreamResponseReasoningSummaryTextDone",
    "OpenAIResponseObjectStreamResponseRefusalDelta",
    "OpenAIResponseObjectStreamResponseRefusalDone",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAdded",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseFileSearchCallInProgress",
    "OpenAIResponseObjectStreamResponseFileSearchCallSearching",
    "OpenAIResponseObjectStreamResponseFileSearchCallCompleted",
    "OpenAIResponseObjectStreamResponseIncomplete",
    "OpenAIResponseObjectStreamResponseFailed",
    "OpenAIResponseObjectStreamResponseCompleted",
]


class OpenAIResponseObjectStreamResponseCreated(BaseModel):
    """Streaming event indicating a new response has been created."""

    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    type: Optional[Literal["response.created"]] = None


class OpenAIResponseObjectStreamResponseInProgress(BaseModel):
    """Streaming event indicating the response remains in progress."""

    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    sequence_number: int

    type: Optional[Literal["response.in_progress"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprobTopLogprob(
    BaseModel
):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprob(
    BaseModel
):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    top_logprobs: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprobTopLogprob
        ]
    ] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    logprobs: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprob
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage(BaseModel):
    """
    Corresponds to the various Message types in the Responses API.
    They are all under one type because the Responses API gives them all
    the same "type" value, and there is no way to tell them apart in certain
    scenarios.
    """

    content: Union[
        str,
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    """Web search tool call output message for OpenAI responses."""

    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult(
    BaseModel
):
    """Search results returned by the file search operation."""

    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    """File search tool call output message for OpenAI responses."""

    id: str

    queries: List[str]

    status: str

    results: Optional[
        List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult]
    ] = None

    type: Optional[Literal["file_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    """Function tool call output message for OpenAI responses."""

    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    """MCP list tools output message containing available tools from an MCP server."""

    id: str

    server_label: str

    tools: List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMcpApprovalRequest(BaseModel):
    """A request for human approval of a tool invocation."""

    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItem: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMcpApprovalRequest,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAdded(BaseModel):
    """Streaming event for when a new output item is added to the response."""

    item: OpenAIResponseObjectStreamResponseOutputItemAddedItem
    """
    Corresponds to the various Message types in the Responses API. They are all
    under one type because the Responses API gives them all the same "type" value,
    and there is no way to tell them apart in certain scenarios.
    """

    output_index: int

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.output_item.added"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprobTopLogprob(
    BaseModel
):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprob(
    BaseModel
):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    top_logprobs: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprobTopLogprob
        ]
    ] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    logprobs: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextLogprob
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage(BaseModel):
    """
    Corresponds to the various Message types in the Responses API.
    They are all under one type because the Responses API gives them all
    the same "type" value, and there is no way to tell them apart in certain
    scenarios.
    """

    content: Union[
        str,
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    """Web search tool call output message for OpenAI responses."""

    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult(
    BaseModel
):
    """Search results returned by the file search operation."""

    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    """File search tool call output message for OpenAI responses."""

    id: str

    queries: List[str]

    status: str

    results: Optional[
        List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult]
    ] = None

    type: Optional[Literal["file_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    """Function tool call output message for OpenAI responses."""

    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    """MCP list tools output message containing available tools from an MCP server."""

    id: str

    server_label: str

    tools: List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest(BaseModel):
    """A request for human approval of a tool invocation."""

    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItem: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDone(BaseModel):
    """Streaming event for when an output item is completed."""

    item: OpenAIResponseObjectStreamResponseOutputItemDoneItem
    """
    Corresponds to the various Message types in the Responses API. They are all
    under one type because the Responses API gives them all the same "type" value,
    and there is no way to tell them apart in certain scenarios.
    """

    output_index: int

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.output_item.done"]] = None


class OpenAIResponseObjectStreamResponseOutputTextDeltaLogprobTopLogprob(BaseModel):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class OpenAIResponseObjectStreamResponseOutputTextDeltaLogprob(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    top_logprobs: Optional[List[OpenAIResponseObjectStreamResponseOutputTextDeltaLogprobTopLogprob]] = None


class OpenAIResponseObjectStreamResponseOutputTextDelta(BaseModel):
    """Streaming event for incremental text content updates."""

    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    logprobs: Optional[List[OpenAIResponseObjectStreamResponseOutputTextDeltaLogprob]] = None

    type: Optional[Literal["response.output_text.delta"]] = None


class OpenAIResponseObjectStreamResponseOutputTextDone(BaseModel):
    """Streaming event for when text output is completed."""

    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    text: str

    type: Optional[Literal["response.output_text.done"]] = None


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta(BaseModel):
    """Streaming event for incremental function call argument updates."""

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.function_call_arguments.delta"]] = None


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone(BaseModel):
    """Streaming event for when function call arguments are completed."""

    arguments: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.function_call_arguments.done"]] = None


class OpenAIResponseObjectStreamResponseWebSearchCallInProgress(BaseModel):
    """Streaming event for web search calls in progress."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.web_search_call.in_progress"]] = None


class OpenAIResponseObjectStreamResponseWebSearchCallSearching(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.web_search_call.searching"]] = None


class OpenAIResponseObjectStreamResponseWebSearchCallCompleted(BaseModel):
    """Streaming event for completed web search calls."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.web_search_call.completed"]] = None


class OpenAIResponseObjectStreamResponseMcpListToolsInProgress(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_list_tools.in_progress"]] = None


class OpenAIResponseObjectStreamResponseMcpListToolsFailed(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_list_tools.failed"]] = None


class OpenAIResponseObjectStreamResponseMcpListToolsCompleted(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_list_tools.completed"]] = None


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta(BaseModel):
    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.mcp_call.arguments.delta"]] = None


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDone(BaseModel):
    arguments: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.mcp_call.arguments.done"]] = None


class OpenAIResponseObjectStreamResponseMcpCallInProgress(BaseModel):
    """Streaming event for MCP calls in progress."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.mcp_call.in_progress"]] = None


class OpenAIResponseObjectStreamResponseMcpCallFailed(BaseModel):
    """Streaming event for failed MCP calls."""

    sequence_number: int

    type: Optional[Literal["response.mcp_call.failed"]] = None


class OpenAIResponseObjectStreamResponseMcpCallCompleted(BaseModel):
    """Streaming event for completed MCP calls."""

    sequence_number: int

    type: Optional[Literal["response.mcp_call.completed"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextLogprobTopLogprob(
    BaseModel
):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextLogprob(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    top_logprobs: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextLogprobTopLogprob]
    ] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText(BaseModel):
    """Text content within a streamed response part."""

    text: str

    annotations: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation]
    ] = None

    logprobs: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextLogprob]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal(BaseModel):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText(BaseModel):
    """Reasoning text emitted as part of a streamed response."""

    text: str

    type: Optional[Literal["reasoning_text"]] = None


OpenAIResponseObjectStreamResponseContentPartAddedPart: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartAdded(BaseModel):
    """Streaming event for when a new content part is added to a response item."""

    content_index: int

    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseContentPartAddedPart
    """Text content within a streamed response part."""

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.content_part.added"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextLogprobTopLogprob(
    BaseModel
):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextLogprob(BaseModel):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    top_logprobs: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextLogprobTopLogprob]
    ] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText(BaseModel):
    """Text content within a streamed response part."""

    text: str

    annotations: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation]
    ] = None

    logprobs: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextLogprob]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal(BaseModel):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText(BaseModel):
    """Reasoning text emitted as part of a streamed response."""

    text: str

    type: Optional[Literal["reasoning_text"]] = None


OpenAIResponseObjectStreamResponseContentPartDonePart: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartDone(BaseModel):
    """Streaming event for when a content part is completed."""

    content_index: int

    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseContentPartDonePart
    """Text content within a streamed response part."""

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.content_part.done"]] = None


class OpenAIResponseObjectStreamResponseReasoningTextDelta(BaseModel):
    """Streaming event for incremental reasoning text updates."""

    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.reasoning_text.delta"]] = None


class OpenAIResponseObjectStreamResponseReasoningTextDone(BaseModel):
    """Streaming event for when reasoning text is completed."""

    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    text: str

    type: Optional[Literal["response.reasoning_text.done"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart(BaseModel):
    """Reasoning summary part in a streamed response."""

    text: str

    type: Optional[Literal["summary_text"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartAdded(BaseModel):
    """Streaming event for when a new reasoning summary part is added."""

    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart
    """Reasoning summary part in a streamed response."""

    sequence_number: int

    summary_index: int

    type: Optional[Literal["response.reasoning_summary_part.added"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart(BaseModel):
    """Reasoning summary part in a streamed response."""

    text: str

    type: Optional[Literal["summary_text"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartDone(BaseModel):
    """Streaming event for when a reasoning summary part is completed."""

    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart
    """Reasoning summary part in a streamed response."""

    sequence_number: int

    summary_index: int

    type: Optional[Literal["response.reasoning_summary_part.done"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryTextDelta(BaseModel):
    """Streaming event for incremental reasoning summary text updates."""

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    summary_index: int

    type: Optional[Literal["response.reasoning_summary_text.delta"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryTextDone(BaseModel):
    """Streaming event for when reasoning summary text is completed."""

    item_id: str

    output_index: int

    sequence_number: int

    summary_index: int

    text: str

    type: Optional[Literal["response.reasoning_summary_text.done"]] = None


class OpenAIResponseObjectStreamResponseRefusalDelta(BaseModel):
    """Streaming event for incremental refusal text updates."""

    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.refusal.delta"]] = None


class OpenAIResponseObjectStreamResponseRefusalDone(BaseModel):
    """Streaming event for when refusal text is completed."""

    content_index: int

    item_id: str

    output_index: int

    refusal: str

    sequence_number: int

    type: Optional[Literal["response.refusal.done"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationCitation(BaseModel):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAdded(BaseModel):
    """Streaming event for when an annotation is added to output text."""

    annotation: OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotation
    """File citation annotation for referencing specific files in response content."""

    annotation_index: int

    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.output_text.annotation.added"]] = None


class OpenAIResponseObjectStreamResponseFileSearchCallInProgress(BaseModel):
    """Streaming event for file search calls in progress."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.file_search_call.in_progress"]] = None


class OpenAIResponseObjectStreamResponseFileSearchCallSearching(BaseModel):
    """Streaming event for file search currently searching."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.file_search_call.searching"]] = None


class OpenAIResponseObjectStreamResponseFileSearchCallCompleted(BaseModel):
    """Streaming event for completed file search calls."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.file_search_call.completed"]] = None


class OpenAIResponseObjectStreamResponseIncomplete(BaseModel):
    """Streaming event emitted when a response ends in an incomplete state."""

    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    sequence_number: int

    type: Optional[Literal["response.incomplete"]] = None


class OpenAIResponseObjectStreamResponseFailed(BaseModel):
    """Streaming event emitted when a response fails."""

    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    sequence_number: int

    type: Optional[Literal["response.failed"]] = None


class OpenAIResponseObjectStreamResponseCompleted(BaseModel):
    """Streaming event indicating a response has been completed."""

    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    type: Optional[Literal["response.completed"]] = None


ResponseObjectStream: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseCreated,
        OpenAIResponseObjectStreamResponseInProgress,
        OpenAIResponseObjectStreamResponseOutputItemAdded,
        OpenAIResponseObjectStreamResponseOutputItemDone,
        OpenAIResponseObjectStreamResponseOutputTextDelta,
        OpenAIResponseObjectStreamResponseOutputTextDone,
        OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta,
        OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone,
        OpenAIResponseObjectStreamResponseWebSearchCallInProgress,
        OpenAIResponseObjectStreamResponseWebSearchCallSearching,
        OpenAIResponseObjectStreamResponseWebSearchCallCompleted,
        OpenAIResponseObjectStreamResponseMcpListToolsInProgress,
        OpenAIResponseObjectStreamResponseMcpListToolsFailed,
        OpenAIResponseObjectStreamResponseMcpListToolsCompleted,
        OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta,
        OpenAIResponseObjectStreamResponseMcpCallArgumentsDone,
        OpenAIResponseObjectStreamResponseMcpCallInProgress,
        OpenAIResponseObjectStreamResponseMcpCallFailed,
        OpenAIResponseObjectStreamResponseMcpCallCompleted,
        OpenAIResponseObjectStreamResponseContentPartAdded,
        OpenAIResponseObjectStreamResponseContentPartDone,
        OpenAIResponseObjectStreamResponseReasoningTextDelta,
        OpenAIResponseObjectStreamResponseReasoningTextDone,
        OpenAIResponseObjectStreamResponseReasoningSummaryPartAdded,
        OpenAIResponseObjectStreamResponseReasoningSummaryPartDone,
        OpenAIResponseObjectStreamResponseReasoningSummaryTextDelta,
        OpenAIResponseObjectStreamResponseReasoningSummaryTextDone,
        OpenAIResponseObjectStreamResponseRefusalDelta,
        OpenAIResponseObjectStreamResponseRefusalDone,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAdded,
        OpenAIResponseObjectStreamResponseFileSearchCallInProgress,
        OpenAIResponseObjectStreamResponseFileSearchCallSearching,
        OpenAIResponseObjectStreamResponseFileSearchCallCompleted,
        OpenAIResponseObjectStreamResponseIncomplete,
        OpenAIResponseObjectStreamResponseFailed,
        OpenAIResponseObjectStreamResponseCompleted,
    ],
    PropertyInfo(discriminator="type"),
]
