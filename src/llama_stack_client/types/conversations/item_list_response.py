# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ItemListResponse",
    "OpenAIResponseMessage",
    "OpenAIResponseMessageContentUnionMember1",
    "OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile",
    "OpenAIResponseMessageContentUnionMember2",
    "OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText",
    "OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal",
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


class OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    file_id: Optional[str] = None
    """(Optional) The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


class OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile(BaseModel):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The data of the file to be sent to the model."""

    file_id: Optional[str] = None
    """(Optional) The ID of the file to be sent to the model."""

    file_url: Optional[str] = None
    """The URL of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


OpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
        OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
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


class OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
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


class OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Literal["file_path"]


OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText(BaseModel):
    annotations: List[OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation]

    text: str

    type: Literal["output_text"]


class OpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal(BaseModel):
    refusal: str
    """Refusal text supplied by the model"""

    type: Literal["refusal"]
    """Content part type identifier, always "refusal" """


OpenAIResponseMessageContentUnionMember2: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText,
        OpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessage(BaseModel):
    content: Union[str, List[OpenAIResponseMessageContentUnionMember1], List[OpenAIResponseMessageContentUnionMember2]]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class OpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
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


class OpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[List[OpenAIResponseOutputMessageFileSearchToolCallResult]] = None
    """(Optional) Search results returned by the file search operation"""


class OpenAIResponseOutputMessageFunctionToolCall(BaseModel):
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


class OpenAIResponseInputFunctionToolCallOutput(BaseModel):
    call_id: str

    output: str

    type: Literal["function_call_output"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_approval_request"]


class OpenAIResponseMcpApprovalResponse(BaseModel):
    approval_request_id: str

    approve: bool

    type: Literal["mcp_approval_response"]

    id: Optional[str] = None

    reason: Optional[str] = None


class OpenAIResponseOutputMessageMcpCall(BaseModel):
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


class OpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """JSON schema defining the tool's input parameters"""

    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Description of what the tool does"""


class OpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str
    """Unique identifier for this MCP list tools operation"""

    server_label: str
    """Label identifying the MCP server providing the tools"""

    tools: List[OpenAIResponseOutputMessageMcpListToolsTool]
    """List of available tools provided by the MCP server"""

    type: Literal["mcp_list_tools"]
    """Tool call type identifier, always "mcp_list_tools" """


ItemListResponse: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessage,
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
