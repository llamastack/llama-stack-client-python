# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ItemCreateParams",
    "Item",
    "ItemOpenAIResponseMessage",
    "ItemOpenAIResponseMessageContentUnionMember1",
    "ItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "ItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "ItemOpenAIResponseMessageContentUnionMember2",
    "ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText",
    "ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation",
    "ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal",
    "ItemOpenAIResponseOutputMessageWebSearchToolCall",
    "ItemOpenAIResponseOutputMessageFileSearchToolCall",
    "ItemOpenAIResponseOutputMessageFileSearchToolCallResult",
    "ItemOpenAIResponseOutputMessageFunctionToolCall",
    "ItemOpenAIResponseInputFunctionToolCallOutput",
    "ItemOpenAIResponseMcpApprovalRequest",
    "ItemOpenAIResponseMcpApprovalResponse",
    "ItemOpenAIResponseOutputMessageMcpCall",
    "ItemOpenAIResponseOutputMessageMcpListTools",
    "ItemOpenAIResponseOutputMessageMcpListToolsTool",
]


class ItemCreateParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """Items to include in the conversation context."""


class ItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(TypedDict, total=False):
    text: Required[str]
    """The text content of the input message"""

    type: Required[Literal["input_text"]]
    """Content type identifier, always "input_text" """


class ItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(TypedDict, total=False):
    detail: Required[Literal["low", "high", "auto"]]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Required[Literal["input_image"]]
    """Content type identifier, always "input_image" """

    image_url: str
    """(Optional) URL of the image content"""


ItemOpenAIResponseMessageContentUnionMember1: TypeAlias = Union[
    ItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
    ItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
]


class ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    TypedDict, total=False
):
    file_id: Required[str]
    """Unique identifier of the referenced file"""

    filename: Required[str]
    """Name of the referenced file"""

    index: Required[int]
    """Position index of the citation within the content"""

    type: Required[Literal["file_citation"]]
    """Annotation type identifier, always "file_citation" """


class ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    TypedDict, total=False
):
    end_index: Required[int]
    """End position of the citation span in the content"""

    start_index: Required[int]
    """Start position of the citation span in the content"""

    title: Required[str]
    """Title of the referenced web resource"""

    type: Required[Literal["url_citation"]]
    """Annotation type identifier, always "url_citation" """

    url: Required[str]
    """URL of the referenced web resource"""


class ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    TypedDict, total=False
):
    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Required[Literal["container_file_citation"]]


class ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    TypedDict, total=False
):
    file_id: Required[str]

    index: Required[int]

    type: Required[Literal["file_path"]]


ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Union[
    ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
    ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
    ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
    ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
]


class ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText(TypedDict, total=False):
    annotations: Required[
        Iterable[ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation]
    ]

    text: Required[str]

    type: Required[Literal["output_text"]]


class ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal(TypedDict, total=False):
    refusal: Required[str]
    """Refusal text supplied by the model"""

    type: Required[Literal["refusal"]]
    """Content part type identifier, always "refusal" """


ItemOpenAIResponseMessageContentUnionMember2: TypeAlias = Union[
    ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText,
    ItemOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal,
]


class ItemOpenAIResponseMessage(TypedDict, total=False):
    content: Required[
        Union[
            str,
            Iterable[ItemOpenAIResponseMessageContentUnionMember1],
            Iterable[ItemOpenAIResponseMessageContentUnionMember2],
        ]
    ]

    role: Required[Literal["system", "developer", "user", "assistant"]]

    type: Required[Literal["message"]]

    id: str

    status: str


class ItemOpenAIResponseOutputMessageWebSearchToolCall(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this tool call"""

    status: Required[str]
    """Current status of the web search operation"""

    type: Required[Literal["web_search_call"]]
    """Tool call type identifier, always "web_search_call" """


class ItemOpenAIResponseOutputMessageFileSearchToolCallResult(TypedDict, total=False):
    attributes: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) Key-value attributes associated with the file"""

    file_id: Required[str]
    """Unique identifier of the file containing the result"""

    filename: Required[str]
    """Name of the file containing the result"""

    score: Required[float]
    """Relevance score for this search result (between 0 and 1)"""

    text: Required[str]
    """Text content of the search result"""


class ItemOpenAIResponseOutputMessageFileSearchToolCall(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this tool call"""

    queries: Required[SequenceNotStr[str]]
    """List of search queries executed"""

    status: Required[str]
    """Current status of the file search operation"""

    type: Required[Literal["file_search_call"]]
    """Tool call type identifier, always "file_search_call" """

    results: Iterable[ItemOpenAIResponseOutputMessageFileSearchToolCallResult]
    """(Optional) Search results returned by the file search operation"""


class ItemOpenAIResponseOutputMessageFunctionToolCall(TypedDict, total=False):
    arguments: Required[str]
    """JSON string containing the function arguments"""

    call_id: Required[str]
    """Unique identifier for the function call"""

    name: Required[str]
    """Name of the function being called"""

    type: Required[Literal["function_call"]]
    """Tool call type identifier, always "function_call" """

    id: str
    """(Optional) Additional identifier for the tool call"""

    status: str
    """(Optional) Current status of the function call execution"""


class ItemOpenAIResponseInputFunctionToolCallOutput(TypedDict, total=False):
    call_id: Required[str]

    output: Required[str]

    type: Required[Literal["function_call_output"]]

    id: str

    status: str


class ItemOpenAIResponseMcpApprovalRequest(TypedDict, total=False):
    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Required[Literal["mcp_approval_request"]]


class ItemOpenAIResponseMcpApprovalResponse(TypedDict, total=False):
    approval_request_id: Required[str]

    approve: Required[bool]

    type: Required[Literal["mcp_approval_response"]]

    id: str

    reason: str


class ItemOpenAIResponseOutputMessageMcpCall(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this MCP call"""

    arguments: Required[str]
    """JSON string containing the MCP call arguments"""

    name: Required[str]
    """Name of the MCP method being called"""

    server_label: Required[str]
    """Label identifying the MCP server handling the call"""

    type: Required[Literal["mcp_call"]]
    """Tool call type identifier, always "mcp_call" """

    error: str
    """(Optional) Error message if the MCP call failed"""

    output: str
    """(Optional) Output result from the successful MCP call"""


class ItemOpenAIResponseOutputMessageMcpListToolsTool(TypedDict, total=False):
    input_schema: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """JSON schema defining the tool's input parameters"""

    name: Required[str]
    """Name of the tool"""

    description: str
    """(Optional) Description of what the tool does"""


class ItemOpenAIResponseOutputMessageMcpListTools(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this MCP list tools operation"""

    server_label: Required[str]
    """Label identifying the MCP server providing the tools"""

    tools: Required[Iterable[ItemOpenAIResponseOutputMessageMcpListToolsTool]]
    """List of available tools provided by the MCP server"""

    type: Required[Literal["mcp_list_tools"]]
    """Tool call type identifier, always "mcp_list_tools" """


Item: TypeAlias = Union[
    ItemOpenAIResponseMessage,
    ItemOpenAIResponseOutputMessageWebSearchToolCall,
    ItemOpenAIResponseOutputMessageFileSearchToolCall,
    ItemOpenAIResponseOutputMessageFunctionToolCall,
    ItemOpenAIResponseInputFunctionToolCallOutput,
    ItemOpenAIResponseMcpApprovalRequest,
    ItemOpenAIResponseMcpApprovalResponse,
    ItemOpenAIResponseOutputMessageMcpCall,
    ItemOpenAIResponseOutputMessageMcpListTools,
]
