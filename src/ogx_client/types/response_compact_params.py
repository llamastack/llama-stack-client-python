# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ResponseCompactParams",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInput",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusal",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInput",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFileCitation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationCitation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFilePath",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprob",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprobTopLogprob",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageWebSearchToolCall",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCall",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCallResult",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFunctionToolCall",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpCall",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListTools",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListToolsTool",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalRequest",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItem",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItemSummary",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItemContent",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutput",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalResponse",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseCompaction",
    "Reasoning",
    "Text",
    "TextFormat",
    "Tool",
    "ToolOpenAIResponseInputToolWebSearch",
    "ToolOpenAIResponseInputToolFileSearch",
    "ToolOpenAIResponseInputToolFileSearchRankingOptions",
    "ToolOpenAIResponseInputToolFunction",
    "ToolOpenAIResponseInputToolMcp",
    "ToolOpenAIResponseInputToolMcpAllowedTools",
    "ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter",
    "ToolOpenAIResponseInputToolMcpRequireApproval",
    "ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter",
]


class ResponseCompactParams(TypedDict, total=False):
    model: Required[str]
    """The model to use for generating the compacted summary."""

    input: Union[str, Iterable[InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput], None]
    """Input message(s) to compact."""

    instructions: Optional[str]
    """Instructions to guide the compaction."""

    parallel_tool_calls: Optional[bool]
    """Whether to enable parallel tool calls.

    Accepted for compatibility but not used during compaction.
    """

    previous_response_id: Optional[str]
    """ID of a previous response whose history to compact."""

    prompt_cache_key: Optional[str]
    """A key to use when reading from or writing to the prompt cache."""

    reasoning: Optional[Reasoning]
    """Configuration for reasoning effort in OpenAI responses.

    Controls how much reasoning the model performs before generating a response.
    """

    text: Optional[Text]
    """Text response configuration for OpenAI responses."""

    tools: Optional[Iterable[Tool]]
    """List of tools available to the model.

    Accepted for compatibility but not used during compaction.
    """


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    TypedDict, total=False
):
    """Text content for input messages in OpenAI response format."""

    text: Required[str]

    type: Literal["input_text"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    TypedDict, total=False
):
    """Image content for input messages in OpenAI response format."""

    detail: Literal["low", "high", "auto"]

    file_id: Optional[str]

    image_url: Optional[str]

    type: Literal["input_image"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    TypedDict, total=False
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str]

    file_id: Optional[str]

    file_url: Optional[str]

    filename: Optional[str]

    type: Literal["input_file"]


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFileCitation(
    TypedDict, total=False
):
    """File citation annotation for referencing specific files in response content."""

    file_id: Required[str]

    filename: Required[str]

    index: Required[int]

    type: Literal["file_citation"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationCitation(
    TypedDict, total=False
):
    """URL citation annotation for referencing external web resources."""

    end_index: Required[int]

    start_index: Required[int]

    title: Required[str]

    url: Required[str]

    type: Literal["url_citation"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationContainerFileCitation(
    TypedDict, total=False
):
    """Container file citation annotation referencing a file within a container."""

    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Literal["container_file_citation"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFilePath(
    TypedDict, total=False
):
    """File path annotation referencing a generated file in response content."""

    file_id: Required[str]

    index: Required[int]

    type: Literal["file_path"]


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotation: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFileCitation,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationCitation,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationContainerFileCitation,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFilePath,
]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprobTopLogprob(
    TypedDict, total=False
):
    """
    The top log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: Required[str]
    """The token."""

    logprob: Required[float]
    """The log probability of the token."""

    bytes: Optional[Iterable[int]]
    """The bytes for the token."""


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprob(
    TypedDict, total=False
):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.
    """

    token: Required[str]
    """The token."""

    logprob: Required[float]
    """The log probability of the token."""

    bytes: Optional[Iterable[int]]
    """The bytes for the token."""

    top_logprobs: Optional[
        Iterable[
            InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprobTopLogprob
        ]
    ]
    """The top log probabilities for the token."""


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInput(
    TypedDict, total=False
):
    """Text content within an output message of an OpenAI response."""

    text: Required[str]

    annotations: Iterable[
        InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotation
    ]

    logprobs: Optional[
        Iterable[
            InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprob
        ]
    ]

    type: Literal["output_text"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    TypedDict, total=False
):
    """Refusal content within a streamed response part."""

    refusal: Required[str]

    type: Literal["refusal"]


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusal: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInput,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInput(
    TypedDict, total=False
):
    """
    Corresponds to the various Message types in the Responses API.
    They are all under one type because the Responses API gives them all
    the same "type" value, and there is no way to tell them apart in certain
    scenarios.
    """

    content: Required[
        Union[
            str,
            Iterable[
                InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
            ],
            Iterable[
                InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusal
            ],
        ]
    ]

    role: Required[Literal["system", "developer", "user", "assistant"]]

    id: Optional[str]

    status: Optional[str]

    type: Literal["message"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageWebSearchToolCall(
    TypedDict, total=False
):
    """Web search tool call output message for OpenAI responses."""

    id: Required[str]

    status: Required[str]

    type: Literal["web_search_call"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCallResult(
    TypedDict, total=False
):
    """Search results returned by the file search operation."""

    attributes: Required[Dict[str, object]]

    file_id: Required[str]

    filename: Required[str]

    score: Required[float]

    text: Required[str]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCall(
    TypedDict, total=False
):
    """File search tool call output message for OpenAI responses."""

    id: Required[str]

    queries: Required[SequenceNotStr[str]]

    status: Required[str]

    results: Optional[
        Iterable[
            InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCallResult
        ]
    ]

    type: Literal["file_search_call"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFunctionToolCall(
    TypedDict, total=False
):
    """Function tool call output message for OpenAI responses."""

    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpCall(
    TypedDict, total=False
):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    error: Optional[str]

    output: Optional[str]

    type: Literal["mcp_call"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListToolsTool(
    TypedDict, total=False
):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Required[Dict[str, object]]

    name: Required[str]

    description: Optional[str]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListTools(
    TypedDict, total=False
):
    """MCP list tools output message containing available tools from an MCP server."""

    id: Required[str]

    server_label: Required[str]

    tools: Required[
        Iterable[
            InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListToolsTool
        ]
    ]

    type: Literal["mcp_list_tools"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalRequest(
    TypedDict, total=False
):
    """A request for human approval of a tool invocation."""

    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Literal["mcp_approval_request"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItemSummary(
    TypedDict, total=False
):
    """A summary of reasoning output from the model."""

    text: Required[str]
    """The summary text of the reasoning output."""

    type: Literal["summary_text"]
    """The type identifier, always 'summary_text'."""


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItemContent(
    TypedDict, total=False
):
    """Reasoning text from the model."""

    text: Required[str]
    """The reasoning text content from the model."""

    type: Literal["reasoning_text"]
    """The type identifier, always 'reasoning_text'."""


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItem(
    TypedDict, total=False
):
    """Reasoning output from the model, representing the model's thinking process."""

    id: Required[str]
    """Unique identifier for the reasoning output item."""

    summary: Required[
        Iterable[
            InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItemSummary
        ]
    ]
    """Summary of the reasoning output."""

    content: Optional[
        Iterable[
            InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItemContent
        ]
    ]
    """The reasoning content from the model."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the reasoning output."""

    type: Literal["reasoning"]
    """The type identifier, always 'reasoning'."""


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    TypedDict, total=False
):
    """Text content for input messages in OpenAI response format."""

    text: Required[str]

    type: Literal["input_text"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    TypedDict, total=False
):
    """Image content for input messages in OpenAI response format."""

    detail: Literal["low", "high", "auto"]

    file_id: Optional[str]

    image_url: Optional[str]

    type: Literal["input_image"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    TypedDict, total=False
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str]

    file_id: Optional[str]

    file_url: Optional[str]

    filename: Optional[str]

    type: Literal["input_file"]


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutput(
    TypedDict, total=False
):
    """
    This represents the output of a function call that gets passed back to the model.
    """

    call_id: Required[str]

    output: Required[
        Union[
            str,
            Iterable[
                InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutputOutputListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
            ],
        ]
    ]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call_output"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalResponse(
    TypedDict, total=False
):
    """A response to an MCP approval request."""

    approval_request_id: Required[str]

    approve: Required[bool]

    id: Optional[str]

    reason: Optional[str]

    type: Literal["mcp_approval_response"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseCompaction(
    TypedDict, total=False
):
    """A compaction item that summarizes prior conversation context."""

    encrypted_content: Required[str]

    id: Optional[str]

    type: Literal["compaction"]


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInput,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageWebSearchToolCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFunctionToolCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListTools,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalRequest,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageReasoningItem,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutput,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalResponse,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseCompaction,
]


class Reasoning(TypedDict, total=False):
    """Configuration for reasoning effort in OpenAI responses.

    Controls how much reasoning the model performs before generating a response.
    """

    effort: Optional[Literal["none", "minimal", "low", "medium", "high", "xhigh"]]

    summary: Optional[Literal["auto", "concise", "detailed"]]
    """Summary mode for reasoning output. One of 'auto', 'concise', or 'detailed'."""


class TextFormat(TypedDict, total=False):
    """Configuration for Responses API text format."""

    description: Optional[str]

    name: Optional[str]

    schema: Optional[Dict[str, object]]

    strict: Optional[bool]

    type: Literal["text", "json_schema", "json_object"]


class Text(TypedDict, total=False):
    """Text response configuration for OpenAI responses."""

    format: Optional[TextFormat]
    """Configuration for Responses API text format."""

    verbosity: Optional[Literal["low", "medium", "high"]]


class ToolOpenAIResponseInputToolWebSearch(TypedDict, total=False):
    """Web search tool configuration for OpenAI response inputs."""

    search_context_size: Optional[str]

    type: Literal["web_search", "web_search_preview", "web_search_preview_2025_03_11", "web_search_2025_08_26"]


class ToolOpenAIResponseInputToolFileSearchRankingOptions(TypedDict, total=False):
    """Options for ranking and filtering search results.

    This class configures how search results are ranked and filtered. You can use algorithm-based
    rerankers (weighted, RRF) or neural rerankers. Defaults from VectorStoresConfig are
    used when parameters are not provided.

    Examples:
        # Weighted ranker with custom alpha
        SearchRankingOptions(ranker="weighted", alpha=0.7)

        # RRF ranker with custom impact factor
        SearchRankingOptions(ranker="rrf", impact_factor=50.0)

        # Use config defaults (just specify ranker type)
        SearchRankingOptions(ranker="weighted")  # Uses alpha from VectorStoresConfig

        # Score threshold filtering
        SearchRankingOptions(ranker="weighted", score_threshold=0.5)
    """

    alpha: Optional[float]
    """Weight factor for weighted ranker"""

    impact_factor: Optional[float]
    """Impact factor for RRF algorithm"""

    model: Optional[str]
    """Model identifier for neural reranker"""

    ranker: Optional[str]

    score_threshold: Optional[float]

    weights: Optional[Dict[str, float]]
    """Weights for combining vector, keyword, and neural scores.

    Keys: 'vector', 'keyword', 'neural'
    """


class ToolOpenAIResponseInputToolFileSearch(TypedDict, total=False):
    """File search tool configuration for OpenAI response inputs."""

    vector_store_ids: Required[SequenceNotStr[str]]

    filters: Optional[Dict[str, object]]

    max_num_results: Optional[int]

    ranking_options: Optional[ToolOpenAIResponseInputToolFileSearchRankingOptions]
    """Options for ranking and filtering search results.

    This class configures how search results are ranked and filtered. You can use
    algorithm-based rerankers (weighted, RRF) or neural rerankers. Defaults from
    VectorStoresConfig are used when parameters are not provided.

    Examples: # Weighted ranker with custom alpha
    SearchRankingOptions(ranker="weighted", alpha=0.7)

        # RRF ranker with custom impact factor
        SearchRankingOptions(ranker="rrf", impact_factor=50.0)

        # Use config defaults (just specify ranker type)
        SearchRankingOptions(ranker="weighted")  # Uses alpha from VectorStoresConfig

        # Score threshold filtering
        SearchRankingOptions(ranker="weighted", score_threshold=0.5)
    """

    type: Literal["file_search"]


class ToolOpenAIResponseInputToolFunction(TypedDict, total=False):
    """Function tool configuration for OpenAI response inputs."""

    name: Required[str]

    parameters: Required[Optional[Dict[str, object]]]

    description: Optional[str]

    strict: Optional[bool]

    type: Literal["function"]


class ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter(TypedDict, total=False):
    """Filter configuration for restricting which MCP tools can be used."""

    tool_names: Optional[SequenceNotStr[str]]


ToolOpenAIResponseInputToolMcpAllowedTools: TypeAlias = Union[
    SequenceNotStr[str], ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter
]


class ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter(TypedDict, total=False):
    """Filter configuration for MCP tool approval requirements."""

    always: Optional[SequenceNotStr[str]]

    never: Optional[SequenceNotStr[str]]


ToolOpenAIResponseInputToolMcpRequireApproval: TypeAlias = Union[
    Literal["always", "never"], ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter
]


class ToolOpenAIResponseInputToolMcp(TypedDict, total=False):
    """Model Context Protocol (MCP) tool configuration for OpenAI response inputs."""

    server_label: Required[str]

    allowed_tools: Optional[ToolOpenAIResponseInputToolMcpAllowedTools]
    """Filter configuration for restricting which MCP tools can be used."""

    authorization: Optional[str]

    connector_id: Optional[str]

    headers: Optional[Dict[str, object]]

    require_approval: ToolOpenAIResponseInputToolMcpRequireApproval
    """Filter configuration for MCP tool approval requirements."""

    server_url: Optional[str]

    type: Literal["mcp"]


Tool: TypeAlias = Union[
    ToolOpenAIResponseInputToolWebSearch,
    ToolOpenAIResponseInputToolFileSearch,
    ToolOpenAIResponseInputToolFunction,
    ToolOpenAIResponseInputToolMcp,
]
