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
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2Annotation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
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
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2Annotation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest",
    "OpenAIResponseObjectStreamResponseOutputTextDelta",
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
    response: ResponseObject
    """The response object that was created"""

    type: Literal["response.created"]
    """Event type identifier, always "response.created" """


class OpenAIResponseObjectStreamResponseInProgress(BaseModel):
    response: ResponseObject
    """Current response state while in progress"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.in_progress"]
    """Event type identifier, always "response.in_progress" """


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(
    BaseModel
):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(
    BaseModel
):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int
    """End position of the citation span in the content"""

    start_index: int
    """Start position of the citation span in the content"""

    title: str
    """Title of the referenced web resource"""

    type: Literal["url_citation"]
    """Annotation type identifier, always "url_citation" """

    url: str
    """URL of the referenced web resource"""


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Literal["file_path"]


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2(BaseModel):
    annotations: List[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2Annotation
    ]

    text: str

    type: Literal["output_text"]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1],
        List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult(
    BaseModel
):
    attributes: Dict[str, Union[bool, float, str, List[object], object, None]]
    """(Optional) Key-value attributes associated with the file"""

    file_id: str
    """Unique identifier of the file containing the result"""

    filename: str
    """Name of the file containing the result"""

    score: float
    """Relevance score for this search result (between 0 and 1)"""

    text: str
    """Text content of the search result"""


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[
        List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult]
    ] = None
    """(Optional) Search results returned by the file search operation"""


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str
    """JSON string containing the function arguments"""

    call_id: str
    """Unique identifier for the function call"""

    name: str
    """Name of the function being called"""

    type: Literal["function_call"]
    """Tool call type identifier, always "function_call" """

    id: Optional[str] = None
    """(Optional) Additional identifier for the tool call"""

    status: Optional[str] = None
    """(Optional) Current status of the function call execution"""


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str
    """Unique identifier for this MCP call"""

    arguments: str
    """JSON string containing the MCP call arguments"""

    name: str
    """Name of the MCP method being called"""

    server_label: str
    """Label identifying the MCP server handling the call"""

    type: Literal["mcp_call"]
    """Tool call type identifier, always "mcp_call" """

    error: Optional[str] = None
    """(Optional) Error message if the MCP call failed"""

    output: Optional[str] = None
    """(Optional) Output result from the successful MCP call"""


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """JSON schema defining the tool's input parameters"""

    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Description of what the tool does"""


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str
    """Unique identifier for this MCP list tools operation"""

    server_label: str
    """Label identifying the MCP server providing the tools"""

    tools: List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool]
    """List of available tools provided by the MCP server"""

    type: Literal["mcp_list_tools"]
    """Tool call type identifier, always "mcp_list_tools" """


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_approval_request"]


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
    item: OpenAIResponseObjectStreamResponseOutputItemAddedItem
    """The output item that was added (message, tool call, etc.)"""

    output_index: int
    """Index position of this item in the output list"""

    response_id: str
    """Unique identifier of the response containing this output"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.output_item.added"]
    """Event type identifier, always "response.output_item.added" """


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(
    BaseModel
):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(
    BaseModel
):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int
    """End position of the citation span in the content"""

    start_index: int
    """Start position of the citation span in the content"""

    title: str
    """Title of the referenced web resource"""

    type: Literal["url_citation"]
    """Annotation type identifier, always "url_citation" """

    url: str
    """URL of the referenced web resource"""


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Literal["file_path"]


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2(BaseModel):
    annotations: List[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2Annotation
    ]

    text: str

    type: Literal["output_text"]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1],
        List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult(
    BaseModel
):
    attributes: Dict[str, Union[bool, float, str, List[object], object, None]]
    """(Optional) Key-value attributes associated with the file"""

    file_id: str
    """Unique identifier of the file containing the result"""

    filename: str
    """Name of the file containing the result"""

    score: float
    """Relevance score for this search result (between 0 and 1)"""

    text: str
    """Text content of the search result"""


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[
        List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult]
    ] = None
    """(Optional) Search results returned by the file search operation"""


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str
    """JSON string containing the function arguments"""

    call_id: str
    """Unique identifier for the function call"""

    name: str
    """Name of the function being called"""

    type: Literal["function_call"]
    """Tool call type identifier, always "function_call" """

    id: Optional[str] = None
    """(Optional) Additional identifier for the tool call"""

    status: Optional[str] = None
    """(Optional) Current status of the function call execution"""


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str
    """Unique identifier for this MCP call"""

    arguments: str
    """JSON string containing the MCP call arguments"""

    name: str
    """Name of the MCP method being called"""

    server_label: str
    """Label identifying the MCP server handling the call"""

    type: Literal["mcp_call"]
    """Tool call type identifier, always "mcp_call" """

    error: Optional[str] = None
    """(Optional) Error message if the MCP call failed"""

    output: Optional[str] = None
    """(Optional) Output result from the successful MCP call"""


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """JSON schema defining the tool's input parameters"""

    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Description of what the tool does"""


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str
    """Unique identifier for this MCP list tools operation"""

    server_label: str
    """Label identifying the MCP server providing the tools"""

    tools: List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool]
    """List of available tools provided by the MCP server"""

    type: Literal["mcp_list_tools"]
    """Tool call type identifier, always "mcp_list_tools" """


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_approval_request"]


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
    item: OpenAIResponseObjectStreamResponseOutputItemDoneItem
    """The completed output item (message, tool call, etc.)"""

    output_index: int
    """Index position of this item in the output list"""

    response_id: str
    """Unique identifier of the response containing this output"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.output_item.done"]
    """Event type identifier, always "response.output_item.done" """


class OpenAIResponseObjectStreamResponseOutputTextDelta(BaseModel):
    content_index: int
    """Index position within the text content"""

    delta: str
    """Incremental text content being added"""

    item_id: str
    """Unique identifier of the output item being updated"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.output_text.delta"]
    """Event type identifier, always "response.output_text.delta" """


class OpenAIResponseObjectStreamResponseOutputTextDone(BaseModel):
    content_index: int
    """Index position within the text content"""

    item_id: str
    """Unique identifier of the completed output item"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    text: str
    """Final complete text content of the output item"""

    type: Literal["response.output_text.done"]
    """Event type identifier, always "response.output_text.done" """


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta(BaseModel):
    delta: str
    """Incremental function call arguments being added"""

    item_id: str
    """Unique identifier of the function call being updated"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.function_call_arguments.delta"]
    """Event type identifier, always "response.function_call_arguments.delta" """


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone(BaseModel):
    arguments: str
    """Final complete arguments JSON string for the function call"""

    item_id: str
    """Unique identifier of the completed function call"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.function_call_arguments.done"]
    """Event type identifier, always "response.function_call_arguments.done" """


class OpenAIResponseObjectStreamResponseWebSearchCallInProgress(BaseModel):
    item_id: str
    """Unique identifier of the web search call"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.web_search_call.in_progress"]
    """Event type identifier, always "response.web_search_call.in_progress" """


class OpenAIResponseObjectStreamResponseWebSearchCallSearching(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.web_search_call.searching"]


class OpenAIResponseObjectStreamResponseWebSearchCallCompleted(BaseModel):
    item_id: str
    """Unique identifier of the completed web search call"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.web_search_call.completed"]
    """Event type identifier, always "response.web_search_call.completed" """


class OpenAIResponseObjectStreamResponseMcpListToolsInProgress(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_list_tools.in_progress"]


class OpenAIResponseObjectStreamResponseMcpListToolsFailed(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_list_tools.failed"]


class OpenAIResponseObjectStreamResponseMcpListToolsCompleted(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_list_tools.completed"]


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta(BaseModel):
    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_call.arguments.delta"]


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDone(BaseModel):
    arguments: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_call.arguments.done"]


class OpenAIResponseObjectStreamResponseMcpCallInProgress(BaseModel):
    item_id: str
    """Unique identifier of the MCP call"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.mcp_call.in_progress"]
    """Event type identifier, always "response.mcp_call.in_progress" """


class OpenAIResponseObjectStreamResponseMcpCallFailed(BaseModel):
    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.mcp_call.failed"]
    """Event type identifier, always "response.mcp_call.failed" """


class OpenAIResponseObjectStreamResponseMcpCallCompleted(BaseModel):
    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.mcp_call.completed"]
    """Event type identifier, always "response.mcp_call.completed" """


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int
    """End position of the citation span in the content"""

    start_index: int
    """Start position of the citation span in the content"""

    title: str
    """Title of the referenced web resource"""

    type: Literal["url_citation"]
    """Annotation type identifier, always "url_citation" """

    url: str
    """URL of the referenced web resource"""


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Literal["file_path"]


OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText(BaseModel):
    annotations: List[
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation
    ]
    """Structured annotations associated with the text"""

    text: str
    """Text emitted for this content part"""

    type: Literal["output_text"]
    """Content part type identifier, always "output_text" """

    logprobs: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None
    """(Optional) Token log probability details"""


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal(BaseModel):
    refusal: str
    """Refusal text supplied by the model"""

    type: Literal["refusal"]
    """Content part type identifier, always "refusal" """


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText(BaseModel):
    text: str
    """Reasoning text supplied by the model"""

    type: Literal["reasoning_text"]
    """Content part type identifier, always "reasoning_text" """


OpenAIResponseObjectStreamResponseContentPartAddedPart: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartAdded(BaseModel):
    content_index: int
    """Index position of the part within the content array"""

    item_id: str
    """Unique identifier of the output item containing this content part"""

    output_index: int
    """Index position of the output item in the response"""

    part: OpenAIResponseObjectStreamResponseContentPartAddedPart
    """The content part that was added"""

    response_id: str
    """Unique identifier of the response containing this content"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.content_part.added"]
    """Event type identifier, always "response.content_part.added" """


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int
    """End position of the citation span in the content"""

    start_index: int
    """Start position of the citation span in the content"""

    title: str
    """Title of the referenced web resource"""

    type: Literal["url_citation"]
    """Annotation type identifier, always "url_citation" """

    url: str
    """URL of the referenced web resource"""


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Literal["file_path"]


OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText(BaseModel):
    annotations: List[
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation
    ]
    """Structured annotations associated with the text"""

    text: str
    """Text emitted for this content part"""

    type: Literal["output_text"]
    """Content part type identifier, always "output_text" """

    logprobs: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None
    """(Optional) Token log probability details"""


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal(BaseModel):
    refusal: str
    """Refusal text supplied by the model"""

    type: Literal["refusal"]
    """Content part type identifier, always "refusal" """


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText(BaseModel):
    text: str
    """Reasoning text supplied by the model"""

    type: Literal["reasoning_text"]
    """Content part type identifier, always "reasoning_text" """


OpenAIResponseObjectStreamResponseContentPartDonePart: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartDone(BaseModel):
    content_index: int
    """Index position of the part within the content array"""

    item_id: str
    """Unique identifier of the output item containing this content part"""

    output_index: int
    """Index position of the output item in the response"""

    part: OpenAIResponseObjectStreamResponseContentPartDonePart
    """The completed content part"""

    response_id: str
    """Unique identifier of the response containing this content"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.content_part.done"]
    """Event type identifier, always "response.content_part.done" """


class OpenAIResponseObjectStreamResponseReasoningTextDelta(BaseModel):
    content_index: int
    """Index position of the reasoning content part"""

    delta: str
    """Incremental reasoning text being added"""

    item_id: str
    """Unique identifier of the output item being updated"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.reasoning_text.delta"]
    """Event type identifier, always "response.reasoning_text.delta" """


class OpenAIResponseObjectStreamResponseReasoningTextDone(BaseModel):
    content_index: int
    """Index position of the reasoning content part"""

    item_id: str
    """Unique identifier of the completed output item"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    text: str
    """Final complete reasoning text"""

    type: Literal["response.reasoning_text.done"]
    """Event type identifier, always "response.reasoning_text.done" """


class OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart(BaseModel):
    text: str
    """Summary text"""

    type: Literal["summary_text"]
    """Content part type identifier, always "summary_text" """


class OpenAIResponseObjectStreamResponseReasoningSummaryPartAdded(BaseModel):
    item_id: str
    """Unique identifier of the output item"""

    output_index: int
    """Index position of the output item"""

    part: OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart
    """The summary part that was added"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    summary_index: int
    """Index of the summary part within the reasoning summary"""

    type: Literal["response.reasoning_summary_part.added"]
    """Event type identifier, always "response.reasoning_summary_part.added" """


class OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart(BaseModel):
    text: str
    """Summary text"""

    type: Literal["summary_text"]
    """Content part type identifier, always "summary_text" """


class OpenAIResponseObjectStreamResponseReasoningSummaryPartDone(BaseModel):
    item_id: str
    """Unique identifier of the output item"""

    output_index: int
    """Index position of the output item"""

    part: OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart
    """The completed summary part"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    summary_index: int
    """Index of the summary part within the reasoning summary"""

    type: Literal["response.reasoning_summary_part.done"]
    """Event type identifier, always "response.reasoning_summary_part.done" """


class OpenAIResponseObjectStreamResponseReasoningSummaryTextDelta(BaseModel):
    delta: str
    """Incremental summary text being added"""

    item_id: str
    """Unique identifier of the output item"""

    output_index: int
    """Index position of the output item"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    summary_index: int
    """Index of the summary part within the reasoning summary"""

    type: Literal["response.reasoning_summary_text.delta"]
    """Event type identifier, always "response.reasoning_summary_text.delta" """


class OpenAIResponseObjectStreamResponseReasoningSummaryTextDone(BaseModel):
    item_id: str
    """Unique identifier of the output item"""

    output_index: int
    """Index position of the output item"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    summary_index: int
    """Index of the summary part within the reasoning summary"""

    text: str
    """Final complete summary text"""

    type: Literal["response.reasoning_summary_text.done"]
    """Event type identifier, always "response.reasoning_summary_text.done" """


class OpenAIResponseObjectStreamResponseRefusalDelta(BaseModel):
    content_index: int
    """Index position of the content part"""

    delta: str
    """Incremental refusal text being added"""

    item_id: str
    """Unique identifier of the output item"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.refusal.delta"]
    """Event type identifier, always "response.refusal.delta" """


class OpenAIResponseObjectStreamResponseRefusalDone(BaseModel):
    content_index: int
    """Index position of the content part"""

    item_id: str
    """Unique identifier of the output item"""

    output_index: int
    """Index position of the item in the output list"""

    refusal: str
    """Final complete refusal text"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.refusal.done"]
    """Event type identifier, always "response.refusal.done" """


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationCitation(BaseModel):
    end_index: int
    """End position of the citation span in the content"""

    start_index: int
    """Start position of the citation span in the content"""

    title: str
    """Title of the referenced web resource"""

    type: Literal["url_citation"]
    """Annotation type identifier, always "url_citation" """

    url: str
    """URL of the referenced web resource"""


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Literal["file_path"]


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
    annotation: OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotation
    """The annotation object being added"""

    annotation_index: int
    """Index of the annotation within the content part"""

    content_index: int
    """Index position of the content part within the output item"""

    item_id: str
    """Unique identifier of the item to which the annotation is being added"""

    output_index: int
    """Index position of the output item in the response's output array"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.output_text.annotation.added"]
    """Event type identifier, always "response.output_text.annotation.added" """


class OpenAIResponseObjectStreamResponseFileSearchCallInProgress(BaseModel):
    item_id: str
    """Unique identifier of the file search call"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.file_search_call.in_progress"]
    """Event type identifier, always "response.file_search_call.in_progress" """


class OpenAIResponseObjectStreamResponseFileSearchCallSearching(BaseModel):
    item_id: str
    """Unique identifier of the file search call"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.file_search_call.searching"]
    """Event type identifier, always "response.file_search_call.searching" """


class OpenAIResponseObjectStreamResponseFileSearchCallCompleted(BaseModel):
    item_id: str
    """Unique identifier of the completed file search call"""

    output_index: int
    """Index position of the item in the output list"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.file_search_call.completed"]
    """Event type identifier, always "response.file_search_call.completed" """


class OpenAIResponseObjectStreamResponseIncomplete(BaseModel):
    response: ResponseObject
    """Response object describing the incomplete state"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.incomplete"]
    """Event type identifier, always "response.incomplete" """


class OpenAIResponseObjectStreamResponseFailed(BaseModel):
    response: ResponseObject
    """Response object describing the failure"""

    sequence_number: int
    """Sequential number for ordering streaming events"""

    type: Literal["response.failed"]
    """Event type identifier, always "response.failed" """


class OpenAIResponseObjectStreamResponseCompleted(BaseModel):
    response: ResponseObject
    """Completed response object"""

    type: Literal["response.completed"]
    """Event type identifier, always "response.completed" """


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
