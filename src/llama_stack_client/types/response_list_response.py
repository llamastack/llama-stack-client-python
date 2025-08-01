# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseListResponse",
    "Data",
    "DataInput",
    "DataInputOpenAIResponseOutputMessageWebSearchToolCall",
    "DataInputOpenAIResponseOutputMessageFileSearchToolCall",
    "DataInputOpenAIResponseOutputMessageFunctionToolCall",
    "DataInputOpenAIResponseInputFunctionToolCallOutput",
    "DataInputOpenAIResponseMessage",
    "DataInputOpenAIResponseMessageContentUnionMember1",
    "DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "DataInputOpenAIResponseMessageContentUnionMember2",
    "DataInputOpenAIResponseMessageContentUnionMember2Annotation",
    "DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
    "DataOutput",
    "DataOutputOpenAIResponseMessage",
    "DataOutputOpenAIResponseMessageContentUnionMember1",
    "DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "DataOutputOpenAIResponseMessageContentUnionMember2",
    "DataOutputOpenAIResponseMessageContentUnionMember2Annotation",
    "DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
    "DataOutputOpenAIResponseOutputMessageWebSearchToolCall",
    "DataOutputOpenAIResponseOutputMessageFileSearchToolCall",
    "DataOutputOpenAIResponseOutputMessageFunctionToolCall",
    "DataOutputOpenAIResponseOutputMessageMcpCall",
    "DataOutputOpenAIResponseOutputMessageMcpListTools",
    "DataOutputOpenAIResponseOutputMessageMcpListToolsTool",
    "DataText",
    "DataTextFormat",
    "DataError",
]


class DataInputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class DataInputOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None
    """(Optional) Search results returned by the file search operation"""


class DataInputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
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


class DataInputOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    call_id: str

    output: str

    type: Literal["function_call_output"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


DataInputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(BaseModel):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(BaseModel):
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


class DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Literal["file_path"]


DataInputOpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Annotated[
    Union[
        DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
        DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
        DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
        DataInputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputOpenAIResponseMessageContentUnionMember2(BaseModel):
    annotations: List[DataInputOpenAIResponseMessageContentUnionMember2Annotation]

    text: str

    type: Literal["output_text"]


class DataInputOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[DataInputOpenAIResponseMessageContentUnionMember1],
        List[DataInputOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


DataInput: TypeAlias = Union[
    DataInputOpenAIResponseOutputMessageWebSearchToolCall,
    DataInputOpenAIResponseOutputMessageFileSearchToolCall,
    DataInputOpenAIResponseOutputMessageFunctionToolCall,
    DataInputOpenAIResponseInputFunctionToolCallOutput,
    DataInputOpenAIResponseMessage,
]


class DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


DataOutputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(BaseModel):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(BaseModel):
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


class DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Literal["file_path"]


DataOutputOpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Annotated[
    Union[
        DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
        DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
        DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
        DataOutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOutputOpenAIResponseMessageContentUnionMember2(BaseModel):
    annotations: List[DataOutputOpenAIResponseMessageContentUnionMember2Annotation]

    text: str

    type: Literal["output_text"]


class DataOutputOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[DataOutputOpenAIResponseMessageContentUnionMember1],
        List[DataOutputOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataOutputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class DataOutputOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None
    """(Optional) Search results returned by the file search operation"""


class DataOutputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
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


class DataOutputOpenAIResponseOutputMessageMcpCall(BaseModel):
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


class DataOutputOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """JSON schema defining the tool's input parameters"""

    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Description of what the tool does"""


class DataOutputOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str
    """Unique identifier for this MCP list tools operation"""

    server_label: str
    """Label identifying the MCP server providing the tools"""

    tools: List[DataOutputOpenAIResponseOutputMessageMcpListToolsTool]
    """List of available tools provided by the MCP server"""

    type: Literal["mcp_list_tools"]
    """Tool call type identifier, always "mcp_list_tools" """


DataOutput: TypeAlias = Annotated[
    Union[
        DataOutputOpenAIResponseMessage,
        DataOutputOpenAIResponseOutputMessageWebSearchToolCall,
        DataOutputOpenAIResponseOutputMessageFileSearchToolCall,
        DataOutputOpenAIResponseOutputMessageFunctionToolCall,
        DataOutputOpenAIResponseOutputMessageMcpCall,
        DataOutputOpenAIResponseOutputMessageMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]


class DataTextFormat(BaseModel):
    type: Literal["text", "json_schema", "json_object"]
    """Must be "text", "json_schema", or "json_object" to identify the format type"""

    description: Optional[str] = None
    """(Optional) A description of the response format. Only used for json_schema."""

    name: Optional[str] = None
    """The name of the response format. Only used for json_schema."""

    schema_: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = FieldInfo(
        alias="schema", default=None
    )
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model. Only used for json_schema.
    """

    strict: Optional[bool] = None
    """(Optional) Whether to strictly enforce the JSON schema.

    If true, the response must match the schema exactly. Only used for json_schema.
    """


class DataText(BaseModel):
    format: Optional[DataTextFormat] = None
    """(Optional) Text format configuration specifying output format requirements"""


class DataError(BaseModel):
    code: str
    """Error code identifying the type of failure"""

    message: str
    """Human-readable error message describing the failure"""


class Data(BaseModel):
    id: str
    """Unique identifier for this response"""

    created_at: int
    """Unix timestamp when the response was created"""

    input: List[DataInput]
    """List of input items that led to this response"""

    model: str
    """Model identifier used for generation"""

    object: Literal["response"]
    """Object type identifier, always "response" """

    output: List[DataOutput]
    """List of generated output items (messages, tool calls, etc.)"""

    parallel_tool_calls: bool
    """Whether tool calls can be executed in parallel"""

    status: str
    """Current status of the response generation"""

    text: DataText
    """Text formatting configuration for the response"""

    error: Optional[DataError] = None
    """(Optional) Error details if the response generation failed"""

    previous_response_id: Optional[str] = None
    """(Optional) ID of the previous response in a conversation"""

    temperature: Optional[float] = None
    """(Optional) Sampling temperature used for generation"""

    top_p: Optional[float] = None
    """(Optional) Nucleus sampling parameter used for generation"""

    truncation: Optional[str] = None
    """(Optional) Truncation strategy applied to the response"""

    user: Optional[str] = None
    """(Optional) User identifier associated with the request"""


class ResponseListResponse(BaseModel):
    data: List[Data]
    """List of response objects with their input context"""

    first_id: str
    """Identifier of the first item in this page"""

    has_more: bool
    """Whether there are more results available beyond this page"""

    last_id: str
    """Identifier of the last item in this page"""

    object: Literal["list"]
    """Object type identifier, always "list" """
