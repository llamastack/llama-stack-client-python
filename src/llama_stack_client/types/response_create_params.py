# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ResponseCreateParamsBase",
    "InputUnionMember1",
    "InputUnionMember1OpenAIResponseOutputMessageWebSearchToolCall",
    "InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCall",
    "InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCallResult",
    "InputUnionMember1OpenAIResponseOutputMessageFunctionToolCall",
    "InputUnionMember1OpenAIResponseInputFunctionToolCallOutput",
    "InputUnionMember1OpenAIResponseMcpApprovalRequest",
    "InputUnionMember1OpenAIResponseMcpApprovalResponse",
    "InputUnionMember1OpenAIResponseMessage",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember1",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember2",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember2Annotation",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
    "Text",
    "TextFormat",
    "Tool",
    "ToolOpenAIResponseInputToolWebSearch",
    "ToolOpenAIResponseInputToolFileSearch",
    "ToolOpenAIResponseInputToolFileSearchRankingOptions",
    "ToolOpenAIResponseInputToolFunction",
    "ToolOpenAIResponseInputToolMcp",
    "ToolOpenAIResponseInputToolMcpRequireApproval",
    "ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter",
    "ToolOpenAIResponseInputToolMcpAllowedTools",
    "ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter",
    "ResponseCreateParamsNonStreaming",
    "ResponseCreateParamsStreaming",
]


class ResponseCreateParamsBase(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputUnionMember1]]]
    """Input message(s) to create the response."""

    model: Required[str]
    """The underlying LLM used for completions."""

    conversation: str
    """(Optional) The ID of a conversation to add the response to.

    Must begin with 'conv\\__'. Input and output messages will be automatically added
    to the conversation.
    """

    include: SequenceNotStr[str]
    """(Optional) Additional fields to include in the response."""

    instructions: str

    max_infer_iters: int

    previous_response_id: str
    """
    (Optional) if specified, the new response will be a continuation of the previous
    response. This can be used to easily fork-off new responses from existing
    responses.
    """

    store: bool

    temperature: float

    text: Text
    """Text response configuration for OpenAI responses."""

    tools: Iterable[Tool]


class InputUnionMember1OpenAIResponseOutputMessageWebSearchToolCall(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this tool call"""

    status: Required[str]
    """Current status of the web search operation"""

    type: Required[Literal["web_search_call"]]
    """Tool call type identifier, always "web_search_call" """


class InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCallResult(TypedDict, total=False):
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


class InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCall(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this tool call"""

    queries: Required[SequenceNotStr[str]]
    """List of search queries executed"""

    status: Required[str]
    """Current status of the file search operation"""

    type: Required[Literal["file_search_call"]]
    """Tool call type identifier, always "file_search_call" """

    results: Iterable[InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCallResult]
    """(Optional) Search results returned by the file search operation"""


class InputUnionMember1OpenAIResponseOutputMessageFunctionToolCall(TypedDict, total=False):
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


class InputUnionMember1OpenAIResponseInputFunctionToolCallOutput(TypedDict, total=False):
    call_id: Required[str]

    output: Required[str]

    type: Required[Literal["function_call_output"]]

    id: str

    status: str


class InputUnionMember1OpenAIResponseMcpApprovalRequest(TypedDict, total=False):
    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Required[Literal["mcp_approval_request"]]


class InputUnionMember1OpenAIResponseMcpApprovalResponse(TypedDict, total=False):
    approval_request_id: Required[str]

    approve: Required[bool]

    type: Required[Literal["mcp_approval_response"]]

    id: str

    reason: str


class InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(
    TypedDict, total=False
):
    text: Required[str]
    """The text content of the input message"""

    type: Required[Literal["input_text"]]
    """Content type identifier, always "input_text" """


class InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(
    TypedDict, total=False
):
    detail: Required[Literal["low", "high", "auto"]]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Required[Literal["input_image"]]
    """Content type identifier, always "input_image" """

    image_url: str
    """(Optional) URL of the image content"""


InputUnionMember1OpenAIResponseMessageContentUnionMember1: TypeAlias = Union[
    InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
    InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
]


class InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(
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


class InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(
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


class InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(
    TypedDict, total=False
):
    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Required[Literal["container_file_citation"]]


class InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(
    TypedDict, total=False
):
    file_id: Required[str]

    index: Required[int]

    type: Required[Literal["file_path"]]


InputUnionMember1OpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Union[
    InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
    InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
    InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
    InputUnionMember1OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
]


class InputUnionMember1OpenAIResponseMessageContentUnionMember2(TypedDict, total=False):
    annotations: Required[Iterable[InputUnionMember1OpenAIResponseMessageContentUnionMember2Annotation]]

    text: Required[str]

    type: Required[Literal["output_text"]]


class InputUnionMember1OpenAIResponseMessage(TypedDict, total=False):
    content: Required[
        Union[
            str,
            Iterable[InputUnionMember1OpenAIResponseMessageContentUnionMember1],
            Iterable[InputUnionMember1OpenAIResponseMessageContentUnionMember2],
        ]
    ]

    role: Required[Literal["system", "developer", "user", "assistant"]]

    type: Required[Literal["message"]]

    id: str

    status: str


InputUnionMember1: TypeAlias = Union[
    InputUnionMember1OpenAIResponseOutputMessageWebSearchToolCall,
    InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCall,
    InputUnionMember1OpenAIResponseOutputMessageFunctionToolCall,
    InputUnionMember1OpenAIResponseInputFunctionToolCallOutput,
    InputUnionMember1OpenAIResponseMcpApprovalRequest,
    InputUnionMember1OpenAIResponseMcpApprovalResponse,
    InputUnionMember1OpenAIResponseMessage,
]


class TextFormat(TypedDict, total=False):
    type: Required[Literal["text", "json_schema", "json_object"]]
    """Must be "text", "json_schema", or "json_object" to identify the format type"""

    description: str
    """(Optional) A description of the response format. Only used for json_schema."""

    name: str
    """The name of the response format. Only used for json_schema."""

    schema: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model. Only used for json_schema.
    """

    strict: bool
    """(Optional) Whether to strictly enforce the JSON schema.

    If true, the response must match the schema exactly. Only used for json_schema.
    """


class Text(TypedDict, total=False):
    format: TextFormat
    """(Optional) Text format configuration specifying output format requirements"""


class ToolOpenAIResponseInputToolWebSearch(TypedDict, total=False):
    type: Required[Literal["web_search", "web_search_preview", "web_search_preview_2025_03_11"]]
    """Web search tool type variant to use"""

    search_context_size: str
    """(Optional) Size of search context, must be "low", "medium", or "high" """


class ToolOpenAIResponseInputToolFileSearchRankingOptions(TypedDict, total=False):
    ranker: str
    """(Optional) Name of the ranking algorithm to use"""

    score_threshold: float
    """(Optional) Minimum relevance score threshold for results"""


class ToolOpenAIResponseInputToolFileSearch(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """Tool type identifier, always "file_search" """

    vector_store_ids: Required[SequenceNotStr[str]]
    """List of vector store identifiers to search within"""

    filters: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) Additional filters to apply to the search"""

    max_num_results: int
    """(Optional) Maximum number of search results to return (1-50)"""

    ranking_options: ToolOpenAIResponseInputToolFileSearchRankingOptions
    """(Optional) Options for ranking and scoring search results"""


class ToolOpenAIResponseInputToolFunction(TypedDict, total=False):
    name: Required[str]
    """Name of the function that can be called"""

    type: Required[Literal["function"]]
    """Tool type identifier, always "function" """

    description: str
    """(Optional) Description of what the function does"""

    parameters: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) JSON schema defining the function's parameters"""

    strict: bool
    """(Optional) Whether to enforce strict parameter validation"""


class ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter(TypedDict, total=False):
    always: SequenceNotStr[str]
    """(Optional) List of tool names that always require approval"""

    never: SequenceNotStr[str]
    """(Optional) List of tool names that never require approval"""


ToolOpenAIResponseInputToolMcpRequireApproval: TypeAlias = Union[
    Literal["always", "never"], ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter
]


class ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter(TypedDict, total=False):
    tool_names: SequenceNotStr[str]
    """(Optional) List of specific tool names that are allowed"""


ToolOpenAIResponseInputToolMcpAllowedTools: TypeAlias = Union[
    SequenceNotStr[str], ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter
]


class ToolOpenAIResponseInputToolMcp(TypedDict, total=False):
    require_approval: Required[ToolOpenAIResponseInputToolMcpRequireApproval]
    """Approval requirement for tool calls ("always", "never", or filter)"""

    server_label: Required[str]
    """Label to identify this MCP server"""

    server_url: Required[str]
    """URL endpoint of the MCP server"""

    type: Required[Literal["mcp"]]
    """Tool type identifier, always "mcp" """

    allowed_tools: ToolOpenAIResponseInputToolMcpAllowedTools
    """(Optional) Restriction on which tools can be used from this server"""

    headers: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) HTTP headers to include when connecting to the server"""


Tool: TypeAlias = Union[
    ToolOpenAIResponseInputToolWebSearch,
    ToolOpenAIResponseInputToolFileSearch,
    ToolOpenAIResponseInputToolFunction,
    ToolOpenAIResponseInputToolMcp,
]


class ResponseCreateParamsNonStreaming(ResponseCreateParamsBase, total=False):
    stream: Literal[False]


class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: Required[Literal[True]]


ResponseCreateParams = Union[ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming]
