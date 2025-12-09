# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ItemListResponse",
    "OpenAIResponseMessageOutput",
    "OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "OpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseOutputMessageFileSearchToolCallResult",
    "OpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseInputFunctionToolCallOutput",
    "OpenAIResponseMcpApprovalRequest",
    "OpenAIResponseMcpApprovalResponse",
    "OpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseOutputMessageMcpListToolsTool",
]


class OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessageOutput(BaseModel):
    """
    Corresponds to the various Message types in the Responses API.
    They are all under one type because the Responses API gives them all
    the same "type" value, and there is no way to tell them apart in certain
    scenarios.
    """

    content: Union[
        str,
        List[
            OpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            OpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class OpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    """Web search tool call output message for OpenAI responses."""

    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class OpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
    """Search results returned by the file search operation."""

    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class OpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    """File search tool call output message for OpenAI responses."""

    id: str

    queries: List[str]

    status: str

    results: Optional[List[OpenAIResponseOutputMessageFileSearchToolCallResult]] = None

    type: Optional[Literal["file_search_call"]] = None


class OpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    """Function tool call output message for OpenAI responses."""

    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class OpenAIResponseInputFunctionToolCallOutput(BaseModel):
    """
    This represents the output of a function call that gets passed back to the model.
    """

    call_id: str

    output: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call_output"]] = None


class OpenAIResponseMcpApprovalRequest(BaseModel):
    """A request for human approval of a tool invocation."""

    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


class OpenAIResponseMcpApprovalResponse(BaseModel):
    """A response to an MCP approval request."""

    approval_request_id: str

    approve: bool

    id: Optional[str] = None

    reason: Optional[str] = None

    type: Optional[Literal["mcp_approval_response"]] = None


class OpenAIResponseOutputMessageMcpCall(BaseModel):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class OpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class OpenAIResponseOutputMessageMcpListTools(BaseModel):
    """MCP list tools output message containing available tools from an MCP server."""

    id: str

    server_label: str

    tools: List[OpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


ItemListResponse: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageOutput,
        OpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseInputFunctionToolCallOutput,
        OpenAIResponseMcpApprovalRequest,
        OpenAIResponseMcpApprovalResponse,
        OpenAIResponseOutputMessageMcpCall,
        OpenAIResponseOutputMessageMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]
