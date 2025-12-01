# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
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
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
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

    include: Optional[SequenceNotStr[str]]

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

    tools: Optional[Iterable[Tool]]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    TypedDict, total=False
):
    text: Required[str]

    type: Literal["input_text"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    TypedDict, total=False
):
    detail: Literal["low", "high", "auto"]

    file_id: Optional[str]

    image_url: Optional[str]

    type: Literal["input_image"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    TypedDict, total=False
):
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


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    TypedDict, total=False
):
    file_id: Required[str]

    filename: Required[str]

    index: Required[int]

    type: Literal["file_citation"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    TypedDict, total=False
):
    end_index: Required[int]

    start_index: Required[int]

    title: Required[str]

    url: Required[str]

    type: Literal["url_citation"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    TypedDict, total=False
):
    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Literal["container_file_citation"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    TypedDict, total=False
):
    file_id: Required[str]

    index: Required[int]

    type: Literal["file_path"]


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    TypedDict, total=False
):
    text: Required[str]

    annotations: Iterable[
        InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
    ]

    type: Literal["output_text"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    TypedDict, total=False
):
    refusal: Required[str]

    type: Literal["refusal"]


InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Union[
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
    InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInput(
    TypedDict, total=False
):
    content: Required[
        Union[
            str,
            Iterable[
                InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
            ],
            Iterable[
                InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
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
    id: Required[str]

    status: Required[str]

    type: Literal["web_search_call"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCallResult(
    TypedDict, total=False
):
    attributes: Required[Dict[str, object]]

    file_id: Required[str]

    filename: Required[str]

    score: Required[float]

    text: Required[str]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageFileSearchToolCall(
    TypedDict, total=False
):
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
    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpCall(
    TypedDict, total=False
):
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
    input_schema: Required[Dict[str, object]]

    name: Required[str]

    description: Optional[str]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseOutputMessageMcpListTools(
    TypedDict, total=False
):
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
    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Literal["mcp_approval_request"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseInputFunctionToolCallOutput(
    TypedDict, total=False
):
    call_id: Required[str]

    output: Required[str]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call_output"]


class InputListOpenAIResponseMessageUnionOpenAIResponseInputFunctionToolCallOutputOpenAIResponseMcpApprovalResponse(
    TypedDict, total=False
):
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
    text: Required[str]

    type: Literal["input_text"]


class PromptVariablesOpenAIResponseInputMessageContentImage(TypedDict, total=False):
    detail: Literal["low", "high", "auto"]

    file_id: Optional[str]

    image_url: Optional[str]

    type: Literal["input_image"]


class PromptVariablesOpenAIResponseInputMessageContentFile(TypedDict, total=False):
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
    id: Required[str]

    variables: Optional[Dict[str, PromptVariables]]

    version: Optional[str]


class TextFormat(TypedDict, total=False):
    description: Optional[str]

    name: Optional[str]

    schema: Optional[Dict[str, object]]

    strict: Optional[bool]

    type: Literal["text", "json_schema", "json_object"]


class Text(TypedDict, total=False):
    format: Optional[TextFormat]
    """Configuration for Responses API text format."""


class ToolOpenAIResponseInputToolWebSearch(TypedDict, total=False):
    search_context_size: Optional[str]

    type: Literal["web_search", "web_search_preview", "web_search_preview_2025_03_11", "web_search_2025_08_26"]


class ToolOpenAIResponseInputToolFileSearchRankingOptions(TypedDict, total=False):
    ranker: Optional[str]

    score_threshold: Optional[float]


class ToolOpenAIResponseInputToolFileSearch(TypedDict, total=False):
    vector_store_ids: Required[SequenceNotStr[str]]

    filters: Optional[Dict[str, object]]

    max_num_results: Optional[int]

    ranking_options: Optional[ToolOpenAIResponseInputToolFileSearchRankingOptions]
    """Options for ranking and filtering search results."""

    type: Literal["file_search"]


class ToolOpenAIResponseInputToolFunction(TypedDict, total=False):
    name: Required[str]

    parameters: Required[Optional[Dict[str, object]]]

    description: Optional[str]

    strict: Optional[bool]

    type: Literal["function"]


class ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter(TypedDict, total=False):
    tool_names: Optional[SequenceNotStr[str]]


ToolOpenAIResponseInputToolMcpAllowedTools: TypeAlias = Union[
    SequenceNotStr[str], ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter
]


class ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter(TypedDict, total=False):
    always: Optional[SequenceNotStr[str]]

    never: Optional[SequenceNotStr[str]]


ToolOpenAIResponseInputToolMcpRequireApproval: TypeAlias = Union[
    Literal["always", "never"], ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter
]


class ToolOpenAIResponseInputToolMcp(TypedDict, total=False):
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
