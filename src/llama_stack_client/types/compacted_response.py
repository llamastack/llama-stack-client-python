# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "CompactedResponse",
    "Output",
    "OutputOpenAIResponseMessageOutput",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusal",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutput",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFileCitation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationCitation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFilePath",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprob",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprobTopLogprob",
    "OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "OutputOpenAIResponseOutputMessageWebSearchToolCall",
    "OutputOpenAIResponseOutputMessageFileSearchToolCall",
    "OutputOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OutputOpenAIResponseOutputMessageFunctionToolCall",
    "OutputOpenAIResponseOutputMessageMcpCall",
    "OutputOpenAIResponseOutputMessageMcpListTools",
    "OutputOpenAIResponseOutputMessageMcpListToolsTool",
    "OutputOpenAIResponseMcpApprovalRequest",
    "OutputOpenAIResponseOutputMessageReasoningItem",
    "OutputOpenAIResponseOutputMessageReasoningItemSummary",
    "OutputOpenAIResponseOutputMessageReasoningItemContent",
    "OutputOpenAIResponseInputFunctionToolCallOutput",
    "OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OutputOpenAIResponseMcpApprovalResponse",
    "OutputOpenAIResponseCompaction",
    "Usage",
    "UsageInputTokensDetails",
    "UsageOutputTokensDetails",
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


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    """File citation annotation for referencing specific files in response content."""

    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    """URL citation annotation for referencing external web resources."""

    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    """Container file citation annotation referencing a file within a container."""

    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    """File path annotation referencing a generated file in response content."""

    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotation: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFileCitation,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationCitation,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprobTopLogprob(
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


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprob(
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
            OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprobTopLogprob
        ]
    ] = None
    """The top log probabilities for the token."""


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutput(
    BaseModel
):
    """Text content within an output message of an OpenAI response."""

    text: str

    annotations: Optional[
        List[
            OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputAnnotation
        ]
    ] = None

    logprobs: Optional[
        List[
            OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutputLogprob
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    """Refusal content within a streamed response part."""

    refusal: str

    type: Optional[Literal["refusal"]] = None


OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextOutput,
        OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
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
            OutputOpenAIResponseMessageOutputContentListOpenAIResponseOutputMessageContentOutputTextOutputOpenAIResponseContentPartRefusal
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


class OutputOpenAIResponseOutputMessageReasoningItemSummary(BaseModel):
    """A summary of reasoning output from the model."""

    text: str
    """The summary text of the reasoning output."""

    type: Optional[Literal["summary_text"]] = None
    """The type identifier, always 'summary_text'."""


class OutputOpenAIResponseOutputMessageReasoningItemContent(BaseModel):
    """Reasoning text from the model."""

    text: str
    """The reasoning text content from the model."""

    type: Optional[Literal["reasoning_text"]] = None
    """The type identifier, always 'reasoning_text'."""


class OutputOpenAIResponseOutputMessageReasoningItem(BaseModel):
    """Reasoning output from the model, representing the model's thinking process."""

    id: str
    """Unique identifier for the reasoning output item."""

    summary: List[OutputOpenAIResponseOutputMessageReasoningItemSummary]
    """Summary of the reasoning output."""

    content: Optional[List[OutputOpenAIResponseOutputMessageReasoningItemContent]] = None
    """The reasoning content from the model."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the reasoning output."""

    type: Optional[Literal["reasoning"]] = None
    """The type identifier, always 'reasoning'."""


class OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    """Text content for input messages in OpenAI response format."""

    text: str

    type: Optional[Literal["input_text"]] = None


class OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    """Image content for input messages in OpenAI response format."""

    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    """
    This represents the output of a function call that gets passed back to the model.
    """

    call_id: str

    output: Union[
        str,
        List[
            OutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
    ]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call_output"]] = None


class OutputOpenAIResponseMcpApprovalResponse(BaseModel):
    """A response to an MCP approval request."""

    approval_request_id: str

    approve: bool

    id: Optional[str] = None

    reason: Optional[str] = None

    type: Optional[Literal["mcp_approval_response"]] = None


class OutputOpenAIResponseCompaction(BaseModel):
    """A compaction item that summarizes prior conversation context."""

    encrypted_content: str

    id: Optional[str] = None

    type: Optional[Literal["compaction"]] = None


Output: TypeAlias = Union[
    OutputOpenAIResponseMessageOutput,
    OutputOpenAIResponseOutputMessageWebSearchToolCall,
    OutputOpenAIResponseOutputMessageFileSearchToolCall,
    OutputOpenAIResponseOutputMessageFunctionToolCall,
    OutputOpenAIResponseOutputMessageMcpCall,
    OutputOpenAIResponseOutputMessageMcpListTools,
    OutputOpenAIResponseMcpApprovalRequest,
    OutputOpenAIResponseOutputMessageReasoningItem,
    OutputOpenAIResponseInputFunctionToolCallOutput,
    OutputOpenAIResponseMcpApprovalResponse,
    OutputOpenAIResponseCompaction,
]


class UsageInputTokensDetails(BaseModel):
    """Token details for input tokens in OpenAI response usage."""

    cached_tokens: int


class UsageOutputTokensDetails(BaseModel):
    """Token details for output tokens in OpenAI response usage."""

    reasoning_tokens: int


class Usage(BaseModel):
    """Usage information for OpenAI response."""

    input_tokens: int

    input_tokens_details: UsageInputTokensDetails
    """Token details for input tokens in OpenAI response usage."""

    output_tokens: int

    output_tokens_details: UsageOutputTokensDetails
    """Token details for output tokens in OpenAI response usage."""

    total_tokens: int


class CompactedResponse(BaseModel):
    """Response from compacting a conversation."""

    id: str

    created_at: int

    output: List[Output]

    usage: Usage
    """Usage information for OpenAI response."""

    object: Optional[Literal["response.compaction"]] = None
