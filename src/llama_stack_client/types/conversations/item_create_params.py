# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ItemCreateParams",
    "Item",
    "ItemOpenAIResponseMessageInput",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusal",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInput",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFileCitation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationCitation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFilePath",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprob",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprobTopLogprob",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "ItemOpenAIResponseOutputMessageWebSearchToolCall",
    "ItemOpenAIResponseOutputMessageFileSearchToolCall",
    "ItemOpenAIResponseOutputMessageFileSearchToolCallResult",
    "ItemOpenAIResponseOutputMessageFunctionToolCall",
    "ItemOpenAIResponseInputFunctionToolCallOutput",
    "ItemOpenAIResponseMcpApprovalRequest",
    "ItemOpenAIResponseMcpApprovalResponse",
    "ItemOpenAIResponseOutputMessageMcpCall",
    "ItemOpenAIResponseOutputMessageMcpListTools",
    "ItemOpenAIResponseOutputMessageMcpListToolsTool",
]


class ItemCreateParams(TypedDict, total=False):
    items: Required[Iterable[Item]]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    TypedDict, total=False
):
    """Text content for input messages in OpenAI response format."""

    text: Required[str]

    type: Literal["input_text"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    TypedDict, total=False
):
    """Image content for input messages in OpenAI response format."""

    detail: Literal["low", "high", "auto"]

    file_id: Optional[str]

    image_url: Optional[str]

    type: Literal["input_image"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    TypedDict, total=False
):
    """File content for input messages in OpenAI response format."""

    file_data: Optional[str]

    file_id: Optional[str]

    file_url: Optional[str]

    filename: Optional[str]

    type: Literal["input_file"]


ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Union[
    ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFileCitation(
    TypedDict, total=False
):
    """File citation annotation for referencing specific files in response content."""

    file_id: Required[str]

    filename: Required[str]

    index: Required[int]

    type: Literal["file_citation"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationCitation(
    TypedDict, total=False
):
    """URL citation annotation for referencing external web resources."""

    end_index: Required[int]

    start_index: Required[int]

    title: Required[str]

    url: Required[str]

    type: Literal["url_citation"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationContainerFileCitation(
    TypedDict, total=False
):
    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Literal["container_file_citation"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFilePath(
    TypedDict, total=False
):
    file_id: Required[str]

    index: Required[int]

    type: Literal["file_path"]


ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotation: TypeAlias = Union[
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFileCitation,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationCitation,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationContainerFileCitation,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotationOpenAIResponseAnnotationFilePath,
]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprobTopLogprob(
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


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprob(
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
            ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprobTopLogprob
        ]
    ]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInput(
    TypedDict, total=False
):
    text: Required[str]

    annotations: Iterable[
        ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputAnnotation
    ]

    logprobs: Optional[
        Iterable[
            ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInputLogprob
        ]
    ]

    type: Literal["output_text"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    TypedDict, total=False
):
    """Refusal content within a streamed response part."""

    refusal: Required[str]

    type: Literal["refusal"]


ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusal: TypeAlias = Union[
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextInput,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
]


class ItemOpenAIResponseMessageInput(TypedDict, total=False):
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
                ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
            ],
            Iterable[
                ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextInputOpenAIResponseContentPartRefusal
            ],
        ]
    ]

    role: Required[Literal["system", "developer", "user", "assistant"]]

    id: Optional[str]

    status: Optional[str]

    type: Literal["message"]


class ItemOpenAIResponseOutputMessageWebSearchToolCall(TypedDict, total=False):
    """Web search tool call output message for OpenAI responses."""

    id: Required[str]

    status: Required[str]

    type: Literal["web_search_call"]


class ItemOpenAIResponseOutputMessageFileSearchToolCallResult(TypedDict, total=False):
    """Search results returned by the file search operation."""

    attributes: Required[Dict[str, object]]

    file_id: Required[str]

    filename: Required[str]

    score: Required[float]

    text: Required[str]


class ItemOpenAIResponseOutputMessageFileSearchToolCall(TypedDict, total=False):
    """File search tool call output message for OpenAI responses."""

    id: Required[str]

    queries: Required[SequenceNotStr[str]]

    status: Required[str]

    results: Optional[Iterable[ItemOpenAIResponseOutputMessageFileSearchToolCallResult]]

    type: Literal["file_search_call"]


class ItemOpenAIResponseOutputMessageFunctionToolCall(TypedDict, total=False):
    """Function tool call output message for OpenAI responses."""

    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call"]


class ItemOpenAIResponseInputFunctionToolCallOutput(TypedDict, total=False):
    """
    This represents the output of a function call that gets passed back to the model.
    """

    call_id: Required[str]

    output: Required[str]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call_output"]


class ItemOpenAIResponseMcpApprovalRequest(TypedDict, total=False):
    """A request for human approval of a tool invocation."""

    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Literal["mcp_approval_request"]


class ItemOpenAIResponseMcpApprovalResponse(TypedDict, total=False):
    """A response to an MCP approval request."""

    approval_request_id: Required[str]

    approve: Required[bool]

    id: Optional[str]

    reason: Optional[str]

    type: Literal["mcp_approval_response"]


class ItemOpenAIResponseOutputMessageMcpCall(TypedDict, total=False):
    """Model Context Protocol (MCP) call output message for OpenAI responses."""

    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    error: Optional[str]

    output: Optional[str]

    type: Literal["mcp_call"]


class ItemOpenAIResponseOutputMessageMcpListToolsTool(TypedDict, total=False):
    """Tool definition returned by MCP list tools operation."""

    input_schema: Required[Dict[str, object]]

    name: Required[str]

    description: Optional[str]


class ItemOpenAIResponseOutputMessageMcpListTools(TypedDict, total=False):
    """MCP list tools output message containing available tools from an MCP server."""

    id: Required[str]

    server_label: Required[str]

    tools: Required[Iterable[ItemOpenAIResponseOutputMessageMcpListToolsTool]]

    type: Literal["mcp_list_tools"]


Item: TypeAlias = Union[
    ItemOpenAIResponseMessageInput,
    ItemOpenAIResponseOutputMessageWebSearchToolCall,
    ItemOpenAIResponseOutputMessageFileSearchToolCall,
    ItemOpenAIResponseOutputMessageFunctionToolCall,
    ItemOpenAIResponseInputFunctionToolCallOutput,
    ItemOpenAIResponseMcpApprovalRequest,
    ItemOpenAIResponseMcpApprovalResponse,
    ItemOpenAIResponseOutputMessageMcpCall,
    ItemOpenAIResponseOutputMessageMcpListTools,
]
