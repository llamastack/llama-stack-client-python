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
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
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
    text: Required[str]

    type: Literal["input_text"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    TypedDict, total=False
):
    detail: Literal["low", "high", "auto"]

    file_id: Optional[str]

    image_url: Optional[str]

    type: Literal["input_image"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    TypedDict, total=False
):
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


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    TypedDict, total=False
):
    file_id: Required[str]

    filename: Required[str]

    index: Required[int]

    type: Literal["file_citation"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    TypedDict, total=False
):
    end_index: Required[int]

    start_index: Required[int]

    title: Required[str]

    url: Required[str]

    type: Literal["url_citation"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    TypedDict, total=False
):
    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Literal["container_file_citation"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    TypedDict, total=False
):
    file_id: Required[str]

    index: Required[int]

    type: Literal["file_path"]


ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Union[
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    TypedDict, total=False
):
    text: Required[str]

    annotations: Iterable[
        ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
    ]

    type: Literal["output_text"]


class ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    TypedDict, total=False
):
    refusal: Required[str]

    type: Literal["refusal"]


ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Union[
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
    ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
]


class ItemOpenAIResponseMessageInput(TypedDict, total=False):
    content: Required[
        Union[
            str,
            Iterable[
                ItemOpenAIResponseMessageInputContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
            ],
            Iterable[
                ItemOpenAIResponseMessageInputContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
            ],
        ]
    ]

    role: Required[Literal["system", "developer", "user", "assistant"]]

    id: Optional[str]

    status: Optional[str]

    type: Literal["message"]


class ItemOpenAIResponseOutputMessageWebSearchToolCall(TypedDict, total=False):
    id: Required[str]

    status: Required[str]

    type: Literal["web_search_call"]


class ItemOpenAIResponseOutputMessageFileSearchToolCallResult(TypedDict, total=False):
    attributes: Required[Dict[str, object]]

    file_id: Required[str]

    filename: Required[str]

    score: Required[float]

    text: Required[str]


class ItemOpenAIResponseOutputMessageFileSearchToolCall(TypedDict, total=False):
    id: Required[str]

    queries: Required[SequenceNotStr[str]]

    status: Required[str]

    results: Optional[Iterable[ItemOpenAIResponseOutputMessageFileSearchToolCallResult]]

    type: Literal["file_search_call"]


class ItemOpenAIResponseOutputMessageFunctionToolCall(TypedDict, total=False):
    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call"]


class ItemOpenAIResponseInputFunctionToolCallOutput(TypedDict, total=False):
    call_id: Required[str]

    output: Required[str]

    id: Optional[str]

    status: Optional[str]

    type: Literal["function_call_output"]


class ItemOpenAIResponseMcpApprovalRequest(TypedDict, total=False):
    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Literal["mcp_approval_request"]


class ItemOpenAIResponseMcpApprovalResponse(TypedDict, total=False):
    approval_request_id: Required[str]

    approve: Required[bool]

    id: Optional[str]

    reason: Optional[str]

    type: Literal["mcp_approval_response"]


class ItemOpenAIResponseOutputMessageMcpCall(TypedDict, total=False):
    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    error: Optional[str]

    output: Optional[str]

    type: Literal["mcp_call"]


class ItemOpenAIResponseOutputMessageMcpListToolsTool(TypedDict, total=False):
    input_schema: Required[Dict[str, object]]

    name: Required[str]

    description: Optional[str]


class ItemOpenAIResponseOutputMessageMcpListTools(TypedDict, total=False):
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
