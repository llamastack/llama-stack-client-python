# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ResponseCreateParamsBase",
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
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutput",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalResponse",
    "Prompt",
    "PromptVariables",
    "PromptVariablesOpenAIResponseInputMessageContentText",
    "PromptVariablesOpenAIResponseInputMessageContentImage",
    "PromptVariablesOpenAIResponseInputMessageContentFile",
    "Text",
    "TextFormat",
    "ToolChoice",
    "ToolChoiceOpenAIResponseInputToolChoiceAllowedTools",
    "ToolChoiceOpenAIResponseInputToolChoiceFileSearch",
    "ToolChoiceOpenAIResponseInputToolChoiceWebSearch",
    "ToolChoiceOpenAIResponseInputToolChoiceFunctionTool",
    "ToolChoiceOpenAIResponseInputToolChoiceMcpTool",
    "ToolChoiceOpenAIResponseInputToolChoiceCustomTool",
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
    "ResponseCreateParamsNonStreaming",
    "ResponseCreateParamsStreaming",
]


class ResponseCreateParamsBase(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput]]]

    model: Required[str]

    conversation: Optional[str]

    include: Optional[
        List[
            Literal[
                "web_search_call.action.sources",
                "code_interpreter_call.outputs",
                "computer_call_output.output.image_url",
                "file_search_call.results",
                "message.input_image.image_url",
                "message.output_text.logprobs",
                "reasoning.encrypted_content",
            ]
        ]
    ]

    instructions: Optional[str]

    max_infer_iters: Optional[int]

    max_tool_calls: Optional[int]

    metadata: Optional[Dict[str, str]]

    parallel_tool_calls: Optional[bool]

    previous_response_id: Optional[str]

    prompt: Optional[Prompt]
    """OpenAI compatible Prompt object that is used in OpenAI responses."""

    store: Optional[bool]

    temperature: Optional[float]

    text: Optional[Text]
    """Text response configuration for OpenAI responses."""

    tool_choice: Optional[ToolChoice]
    """Constrains the tools available to the model to a pre-defined set."""

    tools: Optional[Iterable[Tool]]


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
    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Literal["container_file_citation"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFilePath(
    TypedDict, total=False
):
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

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    """

    token: Required[str]

    logprob: Required[float]

    bytes: Optional[Iterable[int]]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprob(
    TypedDict, total=False
):
    """
    The log probability for a token from an OpenAI-compatible chat completion response.

    :token: The token
    :bytes: (Optional) The bytes for the token
    :logprob: The log probability of the token
    :top_logprobs: The top log probabilities for the token
    """

    token: Required[str]

    logprob: Required[float]

    bytes: Optional[Iterable[int]]

    top_logprobs: Optional[
        Iterable[
            InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprobTopLogprob
        ]
    ]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInput(
    TypedDict, total=False
):
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


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutput(
    TypedDict, total=False
):
    """
    This represents the output of a function call that gets passed back to the model.
    """

    call_id: Required[str]

    output: Required[str]

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


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutput: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInput,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageWebSearchToolCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFunctionToolCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpCall,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListTools,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalRequest,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutput,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalResponse,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInput,
]


class PromptVariablesOpenAIResponseInputMessageContentText(TypedDict, total=False):
    """Text content for input messages in OpenAI response format."""

    text: Required[str]

    type: Literal["input_text"]


class PromptVariablesOpenAIResponseInputMessageContentImage(TypedDict, total=False):
    """Image content for input messages in OpenAI response format."""

    detail: Literal["low", "high", "auto"]

    file_id: Optional[str]

    image_url: Optional[str]

    type: Literal["input_image"]


class PromptVariablesOpenAIResponseInputMessageContentFile(TypedDict, total=False):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str]

    file_id: Optional[str]

    file_url: Optional[str]

    filename: Optional[str]

    type: Literal["input_file"]


PromptVariables: TypeAlias = Union[
    PromptVariablesOpenAIResponseInputMessageContentText,
    PromptVariablesOpenAIResponseInputMessageContentImage,
    PromptVariablesOpenAIResponseInputMessageContentFile,
]


class Prompt(TypedDict, total=False):
    """OpenAI compatible Prompt object that is used in OpenAI responses."""

    id: Required[str]

    variables: Optional[Dict[str, PromptVariables]]

    version: Optional[str]


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


class ToolChoiceOpenAIResponseInputToolChoiceAllowedTools(TypedDict, total=False):
    """Constrains the tools available to the model to a pre-defined set."""

    tools: Required[Iterable[Dict[str, str]]]

    mode: Literal["auto", "required"]

    type: Literal["allowed_tools"]


class ToolChoiceOpenAIResponseInputToolChoiceFileSearch(TypedDict, total=False):
    """Indicates that the model should use file search to generate a response."""

    type: Literal["file_search"]


class ToolChoiceOpenAIResponseInputToolChoiceWebSearch(TypedDict, total=False):
    """Indicates that the model should use web search to generate a response"""

    type: Literal["web_search", "web_search_preview", "web_search_preview_2025_03_11", "web_search_2025_08_26"]


class ToolChoiceOpenAIResponseInputToolChoiceFunctionTool(TypedDict, total=False):
    """Forces the model to call a specific function."""

    name: Required[str]

    type: Literal["function"]


class ToolChoiceOpenAIResponseInputToolChoiceMcpTool(TypedDict, total=False):
    """Forces the model to call a specific tool on a remote MCP server"""

    server_label: Required[str]

    name: Optional[str]

    type: Literal["mcp"]


class ToolChoiceOpenAIResponseInputToolChoiceCustomTool(TypedDict, total=False):
    """Forces the model to call a custom tool."""

    name: Required[str]

    type: Literal["custom"]


ToolChoice: TypeAlias = Union[
    Literal["auto", "required", "none"],
    ToolChoiceOpenAIResponseInputToolChoiceAllowedTools,
    ToolChoiceOpenAIResponseInputToolChoiceFileSearch,
    ToolChoiceOpenAIResponseInputToolChoiceWebSearch,
    ToolChoiceOpenAIResponseInputToolChoiceFunctionTool,
    ToolChoiceOpenAIResponseInputToolChoiceMcpTool,
    ToolChoiceOpenAIResponseInputToolChoiceCustomTool,
]


class ToolOpenAIResponseInputToolWebSearch(TypedDict, total=False):
    """Web search tool configuration for OpenAI response inputs."""

    search_context_size: Optional[str]

    type: Literal["web_search", "web_search_preview", "web_search_preview_2025_03_11", "web_search_2025_08_26"]


class ToolOpenAIResponseInputToolFileSearchRankingOptions(TypedDict, total=False):
    """Options for ranking and filtering search results."""

    ranker: Optional[str]

    score_threshold: Optional[float]


class ToolOpenAIResponseInputToolFileSearch(TypedDict, total=False):
    """File search tool configuration for OpenAI response inputs."""

    vector_store_ids: Required[SequenceNotStr[str]]

    filters: Optional[Dict[str, object]]

    max_num_results: Optional[int]

    ranking_options: Optional[ToolOpenAIResponseInputToolFileSearchRankingOptions]
    """Options for ranking and filtering search results."""

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

    server_url: Required[str]

    allowed_tools: Optional[ToolOpenAIResponseInputToolMcpAllowedTools]
    """Filter configuration for restricting which MCP tools can be used."""

    authorization: Optional[str]

    headers: Optional[Dict[str, object]]

    require_approval: ToolOpenAIResponseInputToolMcpRequireApproval
    """Filter configuration for MCP tool approval requirements."""

    type: Literal["mcp"]


Tool: TypeAlias = Union[
    ToolOpenAIResponseInputToolWebSearch,
    ToolOpenAIResponseInputToolFileSearch,
    ToolOpenAIResponseInputToolFunction,
    ToolOpenAIResponseInputToolMcp,
]


class ResponseCreateParamsNonStreaming(ResponseCreateParamsBase, total=False):
    stream: Optional[Literal[False]]


class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: Required[Literal[True]]


ResponseCreateParams = Union[ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming]
