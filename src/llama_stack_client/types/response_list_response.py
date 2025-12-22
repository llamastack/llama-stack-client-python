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
    "InputOpenAIResponseMessageOutput",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
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
    "OutputOpenAIResponseMessageOutput",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "OutputOpenAIResponseOutputMessageWebSearchToolCall",
    "OutputOpenAIResponseOutputMessageFileSearchToolCall",
    "OutputOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OutputOpenAIResponseOutputMessageFunctionToolCall",
    "OutputOpenAIResponseOutputMessageMcpCall",
    "OutputOpenAIResponseOutputMessageMcpListTools",
    "OutputOpenAIResponseOutputMessageMcpListToolsTool",
    "OutputOpenAIResponseMcpApprovalRequest",
    "Error",
    "Prompt",
    "PromptVariables",
    "PromptVariablesOpenAIResponseInputMessageContentText",
    "PromptVariablesOpenAIResponseInputMessageContentImage",
    "PromptVariablesOpenAIResponseInputMessageContentFile",
    "Text",
    "TextFormat",
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


class InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class InputOpenAIResponseMessageOutput(BaseModel):
    """
    Corresponds to the various Message types in the Responses API.
    They are all under one type because the Responses API gives them all
    the same "type" value, and there is no way to tell them apart in certain
    scenarios.
    """

    content: Union[
        str,
        List[
            InputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            InputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class InputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    """Web search tool call output message for OpenAI responses."""

    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class InputOpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
    """Search results returned by the file search operation."""

    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class InputOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    """File search tool call output message for OpenAI responses."""

    id: str

    queries: List[str]

    status: str

    results: Optional[List[InputOpenAIResponseOutputMessageFileSearchToolCallResult]] = None

    type: Optional[Literal["file_search_call"]] = None


class InputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    """Function tool call output message for OpenAI responses."""

    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class InputOpenAIResponseOutputMessageMcpCall(BaseModel):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class InputOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class InputOpenAIResponseOutputMessageMcpListTools(BaseModel):
    """MCP list tools output message containing available tools from an MCP server."""

    id: str

    server_label: str

    tools: List[InputOpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


class InputOpenAIResponseMcpApprovalRequest(BaseModel):
    """A request for human approval of a tool invocation."""

    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


class InputOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    """
    This represents the output of a function call that gets passed back to the model.
    """

    call_id: str

    output: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call_output"]] = None


class InputOpenAIResponseMcpApprovalResponse(BaseModel):
    """A response to an MCP approval request."""

    approval_request_id: str

    approve: bool

    id: Optional[str] = None

    reason: Optional[str] = None

    type: Optional[Literal["mcp_approval_response"]] = None


Input: TypeAlias = Union[
    InputOpenAIResponseMessageOutput,
    InputOpenAIResponseOutputMessageWebSearchToolCall,
    InputOpenAIResponseOutputMessageFileSearchToolCall,
    InputOpenAIResponseOutputMessageFunctionToolCall,
    InputOpenAIResponseOutputMessageMcpCall,
    InputOpenAIResponseOutputMessageMcpListTools,
    InputOpenAIResponseMcpApprovalRequest,
    InputOpenAIResponseInputFunctionToolCallOutput,
    InputOpenAIResponseMcpApprovalResponse,
    InputOpenAIResponseMessageOutput,
]


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageOutput(BaseModel):
    """
    Corresponds to the various Message types in the Responses API.
    They are all under one type because the Responses API gives them all
    the same "type" value, and there is no way to tell them apart in certain
    scenarios.
    """

    content: Union[
        str,
        List[
            OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class OutputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    """Web search tool call output message for OpenAI responses."""

    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class OutputOpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
    """Search results returned by the file search operation."""

    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class OutputOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    """File search tool call output message for OpenAI responses."""

    id: str

    queries: List[str]

    status: str

    results: Optional[List[OutputOpenAIResponseOutputMessageFileSearchToolCallResult]] = None

    type: Optional[Literal["file_search_call"]] = None


class OutputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    """Function tool call output message for OpenAI responses."""

    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class OutputOpenAIResponseOutputMessageMcpCall(BaseModel):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class OutputOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class OutputOpenAIResponseOutputMessageMcpListTools(BaseModel):
    """MCP list tools output message containing available tools from an MCP server."""

    id: str

    server_label: str

    tools: List[OutputOpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


class OutputOpenAIResponseMcpApprovalRequest(BaseModel):
    """A request for human approval of a tool invocation."""

    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


Output: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageOutput,
        OutputOpenAIResponseOutputMessageWebSearchToolCall,
        OutputOpenAIResponseOutputMessageFileSearchToolCall,
        OutputOpenAIResponseOutputMessageFunctionToolCall,
        OutputOpenAIResponseOutputMessageMcpCall,
        OutputOpenAIResponseOutputMessageMcpListTools,
        OutputOpenAIResponseMcpApprovalRequest,
    ],
    PropertyInfo(discriminator="type"),
]


class Error(BaseModel):
    """Error details for failed OpenAI response requests."""

    code: str

    message: str


class PromptVariablesOpenAIResponseInputMessageContentText(BaseModel):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class PromptVariablesOpenAIResponseInputMessageContentImage(BaseModel):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class PromptVariablesOpenAIResponseInputMessageContentFile(BaseModel):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


PromptVariables: TypeAlias = Annotated[
    Union[
        PromptVariablesOpenAIResponseInputMessageContentText,
        PromptVariablesOpenAIResponseInputMessageContentImage,
        PromptVariablesOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class Prompt(BaseModel):
    """OpenAI compatible Prompt object that is used in OpenAI responses."""

    id: str

    variables: Optional[Dict[str, PromptVariables]] = None

    version: Optional[str] = None


class TextFormat(BaseModel):
    """Configuration for Responses API text format."""

    description: Optional[str] = None

    name: Optional[str] = None

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)

    strict: Optional[bool] = None

    type: Optional[Literal["text", "json_schema", "json_object"]] = None


class Text(BaseModel):
    """Text response configuration for OpenAI responses."""

    format: Optional[TextFormat] = None
    """Configuration for Responses API text format."""


class ToolOpenAIResponseInputToolWebSearch(BaseModel):
    """Web search tool configuration for OpenAI response inputs."""

    search_context_size: Optional[str] = None

    type: Optional[
        Literal["web_search", "web_search_preview", "web_search_preview_2025_03_11", "web_search_2025_08_26"]
    ] = None


class ToolOpenAIResponseInputToolFileSearchRankingOptions(BaseModel):
    """Options for ranking and filtering search results."""

    ranker: Optional[str] = None

    score_threshold: Optional[float] = None


class ToolOpenAIResponseInputToolFileSearch(BaseModel):
    """File search tool configuration for OpenAI response inputs."""

    vector_store_ids: List[str]

    filters: Optional[Dict[str, object]] = None

    max_num_results: Optional[int] = None

    ranking_options: Optional[ToolOpenAIResponseInputToolFileSearchRankingOptions] = None
    """Options for ranking and filtering search results."""

    type: Optional[Literal["file_search"]] = None


class ToolOpenAIResponseInputToolFunction(BaseModel):
    """Function tool configuration for OpenAI response inputs."""

    name: str

    parameters: Optional[Dict[str, object]] = None

    description: Optional[str] = None

    strict: Optional[bool] = None

    type: Optional[Literal["function"]] = None


class ToolOpenAIResponseToolMcpAllowedToolsAllowedToolsFilter(BaseModel):
    """Filter configuration for restricting which MCP tools can be used."""

    tool_names: Optional[List[str]] = None


ToolOpenAIResponseToolMcpAllowedTools: TypeAlias = Union[
    List[str], ToolOpenAIResponseToolMcpAllowedToolsAllowedToolsFilter, None
]


class ToolOpenAIResponseToolMcp(BaseModel):
    """Model Context Protocol (MCP) tool configuration for OpenAI response object."""

    server_label: str

    allowed_tools: Optional[ToolOpenAIResponseToolMcpAllowedTools] = None
    """Filter configuration for restricting which MCP tools can be used."""

    type: Optional[Literal["mcp"]] = None


Tool: TypeAlias = Union[
    ToolOpenAIResponseInputToolWebSearch,
    ToolOpenAIResponseInputToolFileSearch,
    ToolOpenAIResponseInputToolFunction,
    ToolOpenAIResponseToolMcp,
]


class UsageInputTokensDetails(BaseModel):
    """Token details for input tokens in OpenAI response usage."""

    cached_tokens: Optional[int] = None


class UsageOutputTokensDetails(BaseModel):
    """Token details for output tokens in OpenAI response usage."""

    reasoning_tokens: Optional[int] = None


class Usage(BaseModel):
    """Usage information for OpenAI response."""

    input_tokens: int

    output_tokens: int

    total_tokens: int

    input_tokens_details: Optional[UsageInputTokensDetails] = None
    """Token details for input tokens in OpenAI response usage."""

    output_tokens_details: Optional[UsageOutputTokensDetails] = None
    """Token details for output tokens in OpenAI response usage."""


class ResponseListResponse(BaseModel):
    """OpenAI response object extended with input context information."""

    id: str

    created_at: int

    input: List[Input]

    model: str

    output: List[Output]

    status: str

    error: Optional[Error] = None
    """Error details for failed OpenAI response requests."""

    instructions: Optional[str] = None

    max_tool_calls: Optional[int] = None

    metadata: Optional[Dict[str, str]] = None

    object: Optional[Literal["response"]] = None

    parallel_tool_calls: Optional[bool] = None

    previous_response_id: Optional[str] = None

    prompt: Optional[Prompt] = None
    """OpenAI compatible Prompt object that is used in OpenAI responses."""

    temperature: Optional[float] = None

    text: Optional[Text] = None
    """Text response configuration for OpenAI responses."""

    tools: Optional[List[Tool]] = None

    top_p: Optional[float] = None

    truncation: Optional[str] = None

    usage: Optional[Usage] = None
    """Usage information for OpenAI response."""
