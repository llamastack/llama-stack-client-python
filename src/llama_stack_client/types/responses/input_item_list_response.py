# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "InputItemListResponse",
    "Data",
    "DataOpenAIResponseMessageOutput",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusal",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutput",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotation",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFileCitation",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationCitation",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFilePath",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprob",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprobTopLogprob",
    "DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "DataOpenAIResponseOutputMessageWebSearchToolCall",
    "DataOpenAIResponseOutputMessageFileSearchToolCall",
    "DataOpenAIResponseOutputMessageFileSearchToolCallResult",
    "DataOpenAIResponseOutputMessageFunctionToolCall",
    "DataOpenAIResponseOutputMessageMcpCall",
    "DataOpenAIResponseOutputMessageMcpListTools",
    "DataOpenAIResponseOutputMessageMcpListToolsTool",
    "DataOpenAIResponseMcpApprovalRequest",
    "DataOpenAIResponseOutputMessageReasoningItem",
    "DataOpenAIResponseOutputMessageReasoningItemSummary",
    "DataOpenAIResponseOutputMessageReasoningItemContent",
    "DataOpenAIResponseInputFunctionToolCallOutput",
    "DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "DataOpenAIResponseMcpApprovalResponse",
]


class DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    """Container file citation annotation referencing a file within a container."""

    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    """File path annotation referencing a generated file in response content."""

    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotation: TypeAlias = Annotated[
    Union[
        DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFileCitation,
        DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationCitation,
        DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationContainerFileCitation,
        DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprobTopLogprob(
    BaseModel
):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprob(
    BaseModel
):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: str
    """The token."""

    logprob: float
    """The log probability of the token."""

    bytes: Optional[List[int]] = None
    """The bytes for the token."""

    top_logprobs: Optional[
        List[
            DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprobTopLogprob
        ]
    ] = None
    """The top log probabilities for the token."""


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutput(
    BaseModel
):
    """Text content within an output message of an OpenAI response."""

    text: str

    annotations: Optional[
        List[
            DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotation
        ]
    ] = None

    logprobs: Optional[
        List[
            DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprob
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutput,
        DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOpenAIResponseMessageOutput(BaseModel):
    """
    Corresponds to the various Message types in the Responses API.
    They are all under one type because the Responses API gives them all
    the same "type" value, and there is no way to tell them apart in certain
    scenarios.
    """

    content: Union[
        str,
        List[
            DataOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            DataOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class DataOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    """Web search tool call output message for OpenAI responses."""

    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class DataOpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
    """Search results returned by the file search operation."""

    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class DataOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    """File search tool call output message for OpenAI responses."""

    id: str

    queries: List[str]

    status: str

    results: Optional[List[DataOpenAIResponseOutputMessageFileSearchToolCallResult]] = None

    type: Optional[Literal["file_search_call"]] = None


class DataOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    """Function tool call output message for OpenAI responses."""

    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class DataOpenAIResponseOutputMessageMcpCall(BaseModel):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class DataOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class DataOpenAIResponseOutputMessageMcpListTools(BaseModel):
    """MCP list tools output message containing available tools from an MCP server."""

    id: str

    server_label: str

    tools: List[DataOpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


class DataOpenAIResponseMcpApprovalRequest(BaseModel):
    """A request for human approval of a tool invocation."""

    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


class DataOpenAIResponseOutputMessageReasoningItemSummary(BaseModel):
    """A summary of reasoning output from the model."""

    text: str
    """The summary text of the reasoning output."""

    type: Optional[Literal["summary_text"]] = None
    """The type identifier, always 'summary_text'."""


class DataOpenAIResponseOutputMessageReasoningItemContent(BaseModel):
    """Reasoning text from the model."""

    text: str
    """The reasoning text content from the model."""

    type: Optional[Literal["reasoning_text"]] = None
    """The type identifier, always 'reasoning_text'."""


class DataOpenAIResponseOutputMessageReasoningItem(BaseModel):
    """Reasoning output from the model, representing the model's thinking process."""

    id: str
    """Unique identifier for the reasoning output item."""

    summary: List[DataOpenAIResponseOutputMessageReasoningItemSummary]
    """Summary of the reasoning output."""

    content: Optional[List[DataOpenAIResponseOutputMessageReasoningItemContent]] = None
    """The reasoning content from the model."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the reasoning output."""

    type: Optional[Literal["reasoning"]] = None
    """The type identifier, always 'reasoning'."""


class DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    """
    This represents the output of a function call that gets passed back to the model.
    """

    call_id: str

    output: Union[
        str,
        List[
            DataOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
    ]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call_output"]] = None


class DataOpenAIResponseMcpApprovalResponse(BaseModel):
    """A response to an MCP approval request."""

    approval_request_id: str

    approve: bool

    id: Optional[str] = None

    reason: Optional[str] = None

    type: Optional[Literal["mcp_approval_response"]] = None


Data: TypeAlias = Union[
    DataOpenAIResponseMessageOutput,
    DataOpenAIResponseOutputMessageWebSearchToolCall,
    DataOpenAIResponseOutputMessageFileSearchToolCall,
    DataOpenAIResponseOutputMessageFunctionToolCall,
    DataOpenAIResponseOutputMessageMcpCall,
    DataOpenAIResponseOutputMessageMcpListTools,
    DataOpenAIResponseMcpApprovalRequest,
    DataOpenAIResponseOutputMessageReasoningItem,
    DataOpenAIResponseInputFunctionToolCallOutput,
    DataOpenAIResponseMcpApprovalResponse,
    DataOpenAIResponseMessageOutput,
]


class InputItemListResponse(BaseModel):
    """List container for OpenAI response input items."""

    data: List[Data]

    object: Optional[Literal["list"]] = None
