# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseListResponse",
    "Input",
    "InputOpenAIResponseMessage",
    "InputOpenAIResponseMessageContentUnionMember1",
    "InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile",
    "InputOpenAIResponseMessageContentUnionMember2",
    "InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText",
    "InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation",
    "InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "InputOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal",
    "InputOpenAIResponseOutputMessageWebSearchToolCall",
    "InputOpenAIResponseOutputMessageFileSearchToolCall",
    "InputOpenAIResponseOutputMessageFileSearchToolCallResult",
    "InputOpenAIResponseOutputMessageFunctionToolCall",
    "InputOpenAIResponseOutputMessageMcpCall",
    "InputOpenAIResponseOutputMessageMcpListTools",
    "InputOpenAIResponseOutputMessageMcpListToolsTool",
    "InputOpenAIResponseMcpApprovalRequest",
    "InputOpenAIResponseInputFunctionToolCallOutput",
    "InputOpenAIResponseMcpApprovalResponse",
    "Output",
    "OutputOpenAIResponseMessage",
    "OutputOpenAIResponseMessageContentUnionMember1",
    "OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile",
    "OutputOpenAIResponseMessageContentUnionMember2",
    "OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText",
    "OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal",
    "OutputOpenAIResponseOutputMessageWebSearchToolCall",
    "OutputOpenAIResponseOutputMessageFileSearchToolCall",
    "OutputOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OutputOpenAIResponseOutputMessageFunctionToolCall",
    "OutputOpenAIResponseOutputMessageMcpCall",
    "OutputOpenAIResponseOutputMessageMcpListTools",
    "OutputOpenAIResponseOutputMessageMcpListToolsTool",
    "OutputOpenAIResponseMcpApprovalRequest",
    "Text",
    "TextFormat",
    "Error",
    "Prompt",
    "PromptVariables",
    "PromptVariablesOpenAIResponseInputMessageContentText",
    "PromptVariablesOpenAIResponseInputMessageContentImage",
    "PromptVariablesOpenAIResponseInputMessageContentFile",
    "Tool",
    "ToolOpenAIResponseInputToolWebSearch",
    "ToolOpenAIResponseInputToolFileSearch",
    "ToolOpenAIResponseInputToolFileSearchRankingOptions",
    "ToolOpenAIResponseInputToolFunction",
    "ToolOpenAIResponseToolMcp",
    "ToolOpenAIResponseToolMcpAllowedTools",
    "ToolOpenAIResponseToolMcpAllowedToolsAllowedToolsFilter",
    "Usage",
    "UsageInputTokensDetails",
    "UsageOutputTokensDetails",
]


class InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    file_id: Optional[str] = None
    """(Optional) The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


class InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile(BaseModel):
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


InputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
        InputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
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


class InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
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


class InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Literal["file_path"]


InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText(BaseModel):
    annotations: List[
        InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation
    ]

    text: str

    type: Literal["output_text"]


class InputOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal(BaseModel):
    refusal: str
    """Refusal text supplied by the model"""

    type: Literal["refusal"]
    """Content part type identifier, always "refusal" """


InputOpenAIResponseMessageContentUnionMember2: TypeAlias = Annotated[
    Union[
        InputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText,
        InputOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class InputOpenAIResponseMessage(BaseModel):
    content: Union[
        str, List[InputOpenAIResponseMessageContentUnionMember1], List[InputOpenAIResponseMessageContentUnionMember2]
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class InputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class InputOpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
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


class InputOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[List[InputOpenAIResponseOutputMessageFileSearchToolCallResult]] = None
    """(Optional) Search results returned by the file search operation"""


class InputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
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


class InputOpenAIResponseOutputMessageMcpCall(BaseModel):
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


class InputOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """JSON schema defining the tool's input parameters"""

    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Description of what the tool does"""


class InputOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str
    """Unique identifier for this MCP list tools operation"""

    server_label: str
    """Label identifying the MCP server providing the tools"""

    tools: List[InputOpenAIResponseOutputMessageMcpListToolsTool]
    """List of available tools provided by the MCP server"""

    type: Literal["mcp_list_tools"]
    """Tool call type identifier, always "mcp_list_tools" """


class InputOpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_approval_request"]


class InputOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    call_id: str

    output: str

    type: Literal["function_call_output"]

    id: Optional[str] = None

    status: Optional[str] = None


class InputOpenAIResponseMcpApprovalResponse(BaseModel):
    approval_request_id: str

    approve: bool

    type: Literal["mcp_approval_response"]

    id: Optional[str] = None

    reason: Optional[str] = None


Input: TypeAlias = Union[
    InputOpenAIResponseMessage,
    InputOpenAIResponseOutputMessageWebSearchToolCall,
    InputOpenAIResponseOutputMessageFileSearchToolCall,
    InputOpenAIResponseOutputMessageFunctionToolCall,
    InputOpenAIResponseOutputMessageMcpCall,
    InputOpenAIResponseOutputMessageMcpListTools,
    InputOpenAIResponseMcpApprovalRequest,
    InputOpenAIResponseInputFunctionToolCallOutput,
    InputOpenAIResponseMcpApprovalResponse,
    InputOpenAIResponseMessage,
]


class OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    file_id: Optional[str] = None
    """(Optional) The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


class OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile(BaseModel):
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


OutputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
        OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
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


class OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
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


class OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Literal["file_path"]


OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText(BaseModel):
    annotations: List[
        OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputTextAnnotation
    ]

    text: str

    type: Literal["output_text"]


class OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal(BaseModel):
    refusal: str
    """Refusal text supplied by the model"""

    type: Literal["refusal"]
    """Content part type identifier, always "refusal" """


OutputOpenAIResponseMessageContentUnionMember2: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseOutputMessageContentOutputText,
        OutputOpenAIResponseMessageContentUnionMember2OpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessage(BaseModel):
    content: Union[
        str, List[OutputOpenAIResponseMessageContentUnionMember1], List[OutputOpenAIResponseMessageContentUnionMember2]
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OutputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class OutputOpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
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


class OutputOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[List[OutputOpenAIResponseOutputMessageFileSearchToolCallResult]] = None
    """(Optional) Search results returned by the file search operation"""


class OutputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
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


class OutputOpenAIResponseOutputMessageMcpCall(BaseModel):
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


class OutputOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """JSON schema defining the tool's input parameters"""

    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Description of what the tool does"""


class OutputOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str
    """Unique identifier for this MCP list tools operation"""

    server_label: str
    """Label identifying the MCP server providing the tools"""

    tools: List[OutputOpenAIResponseOutputMessageMcpListToolsTool]
    """List of available tools provided by the MCP server"""

    type: Literal["mcp_list_tools"]
    """Tool call type identifier, always "mcp_list_tools" """


class OutputOpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_approval_request"]


Output: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessage,
        OutputOpenAIResponseOutputMessageWebSearchToolCall,
        OutputOpenAIResponseOutputMessageFileSearchToolCall,
        OutputOpenAIResponseOutputMessageFunctionToolCall,
        OutputOpenAIResponseOutputMessageMcpCall,
        OutputOpenAIResponseOutputMessageMcpListTools,
        OutputOpenAIResponseMcpApprovalRequest,
    ],
    PropertyInfo(discriminator="type"),
]


class TextFormat(BaseModel):
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


class Text(BaseModel):
    format: Optional[TextFormat] = None
    """(Optional) Text format configuration specifying output format requirements"""


class Error(BaseModel):
    code: str
    """Error code identifying the type of failure"""

    message: str
    """Human-readable error message describing the failure"""


class PromptVariablesOpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class PromptVariablesOpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    file_id: Optional[str] = None
    """(Optional) The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


class PromptVariablesOpenAIResponseInputMessageContentFile(BaseModel):
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


PromptVariables: TypeAlias = Annotated[
    Union[
        PromptVariablesOpenAIResponseInputMessageContentText,
        PromptVariablesOpenAIResponseInputMessageContentImage,
        PromptVariablesOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class Prompt(BaseModel):
    id: str
    """Unique identifier of the prompt template"""

    variables: Optional[Dict[str, PromptVariables]] = None
    """
    Dictionary of variable names to OpenAIResponseInputMessageContent structure for
    template substitution. The substitution values can either be strings, or other
    Response input types like images or files.
    """

    version: Optional[str] = None
    """Version number of the prompt to use (defaults to latest if not specified)"""


class ToolOpenAIResponseInputToolWebSearch(BaseModel):
    type: Literal["web_search", "web_search_preview", "web_search_preview_2025_03_11"]
    """Web search tool type variant to use"""

    search_context_size: Optional[str] = None
    """(Optional) Size of search context, must be "low", "medium", or "high" """


class ToolOpenAIResponseInputToolFileSearchRankingOptions(BaseModel):
    ranker: Optional[str] = None
    """(Optional) Name of the ranking algorithm to use"""

    score_threshold: Optional[float] = None
    """(Optional) Minimum relevance score threshold for results"""


class ToolOpenAIResponseInputToolFileSearch(BaseModel):
    type: Literal["file_search"]
    """Tool type identifier, always "file_search" """

    vector_store_ids: List[str]
    """List of vector store identifiers to search within"""

    filters: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) Additional filters to apply to the search"""

    max_num_results: Optional[int] = None
    """(Optional) Maximum number of search results to return (1-50)"""

    ranking_options: Optional[ToolOpenAIResponseInputToolFileSearchRankingOptions] = None
    """(Optional) Options for ranking and scoring search results"""


class ToolOpenAIResponseInputToolFunction(BaseModel):
    name: str
    """Name of the function that can be called"""

    type: Literal["function"]
    """Tool type identifier, always "function" """

    description: Optional[str] = None
    """(Optional) Description of what the function does"""

    parameters: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """(Optional) JSON schema defining the function's parameters"""

    strict: Optional[bool] = None
    """(Optional) Whether to enforce strict parameter validation"""


class ToolOpenAIResponseToolMcpAllowedToolsAllowedToolsFilter(BaseModel):
    tool_names: Optional[List[str]] = None
    """(Optional) List of specific tool names that are allowed"""


ToolOpenAIResponseToolMcpAllowedTools: TypeAlias = Union[
    List[str], ToolOpenAIResponseToolMcpAllowedToolsAllowedToolsFilter
]


class ToolOpenAIResponseToolMcp(BaseModel):
    server_label: str
    """Label to identify this MCP server"""

    type: Literal["mcp"]
    """Tool type identifier, always "mcp" """

    allowed_tools: Optional[ToolOpenAIResponseToolMcpAllowedTools] = None
    """(Optional) Restriction on which tools can be used from this server"""


Tool: TypeAlias = Union[
    ToolOpenAIResponseInputToolWebSearch,
    ToolOpenAIResponseInputToolFileSearch,
    ToolOpenAIResponseInputToolFunction,
    ToolOpenAIResponseToolMcp,
]


class UsageInputTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None
    """Number of tokens retrieved from cache"""


class UsageOutputTokensDetails(BaseModel):
    reasoning_tokens: Optional[int] = None
    """Number of tokens used for reasoning (o1/o3 models)"""


class Usage(BaseModel):
    input_tokens: int
    """Number of tokens in the input"""

    output_tokens: int
    """Number of tokens in the output"""

    total_tokens: int
    """Total tokens used (input + output)"""

    input_tokens_details: Optional[UsageInputTokensDetails] = None
    """Detailed breakdown of input token usage"""

    output_tokens_details: Optional[UsageOutputTokensDetails] = None
    """Detailed breakdown of output token usage"""


class ResponseListResponse(BaseModel):
    id: str
    """Unique identifier for this response"""

    created_at: int
    """Unix timestamp when the response was created"""

    input: List[Input]
    """List of input items that led to this response"""

    model: str
    """Model identifier used for generation"""

    object: Literal["response"]
    """Object type identifier, always "response" """

    output: List[Output]
    """List of generated output items (messages, tool calls, etc.)"""

    parallel_tool_calls: bool
    """Whether tool calls can be executed in parallel"""

    status: str
    """Current status of the response generation"""

    text: Text
    """Text formatting configuration for the response"""

    error: Optional[Error] = None
    """(Optional) Error details if the response generation failed"""

    instructions: Optional[str] = None
    """(Optional) System message inserted into the model's context"""

    previous_response_id: Optional[str] = None
    """(Optional) ID of the previous response in a conversation"""

    prompt: Optional[Prompt] = None
    """(Optional) Reference to a prompt template and its variables."""

    temperature: Optional[float] = None
    """(Optional) Sampling temperature used for generation"""

    tools: Optional[List[Tool]] = None
    """(Optional) An array of tools the model may call while generating a response."""

    top_p: Optional[float] = None
    """(Optional) Nucleus sampling parameter used for generation"""

    truncation: Optional[str] = None
    """(Optional) Truncation strategy applied to the response"""

    usage: Optional[Usage] = None
    """(Optional) Token usage information for the response"""
