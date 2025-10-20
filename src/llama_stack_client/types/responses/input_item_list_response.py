# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "InputItemListResponse",
    "Data",
    "DataOpenAIResponseOutputMessageWebSearchToolCall",
    "DataOpenAIResponseOutputMessageFileSearchToolCall",
    "DataOpenAIResponseOutputMessageFileSearchToolCallResult",
    "DataOpenAIResponseOutputMessageFunctionToolCall",
    "DataOpenAIResponseInputFunctionToolCallOutput",
    "DataOpenAIResponseMcpApprovalRequest",
    "DataOpenAIResponseMcpApprovalResponse",
    "DataOpenAIResponseMessage",
    "DataOpenAIResponseMessageContentUnionMember1",
    "DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "DataOpenAIResponseMessageContentUnionMember2",
    "DataOpenAIResponseMessageContentUnionMember2Annotation",
    "DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
]


class DataOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class DataOpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
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


class DataOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[List[DataOpenAIResponseOutputMessageFileSearchToolCallResult]] = None
    """(Optional) Search results returned by the file search operation"""


class DataOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
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


class DataOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    call_id: str

    output: str

    type: Literal["function_call_output"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataOpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_approval_request"]


class DataOpenAIResponseMcpApprovalResponse(BaseModel):
    approval_request_id: str

    approve: bool

    type: Literal["mcp_approval_response"]

    id: Optional[str] = None

    reason: Optional[str] = None


class DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


DataOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(BaseModel):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(BaseModel):
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


class DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(BaseModel):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Literal["file_path"]


DataOpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Annotated[
    Union[
        DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
        DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
        DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
        DataOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOpenAIResponseMessageContentUnionMember2(BaseModel):
    annotations: List[DataOpenAIResponseMessageContentUnionMember2Annotation]

    text: str

    type: Literal["output_text"]


class DataOpenAIResponseMessage(BaseModel):
    content: Union[
        str, List[DataOpenAIResponseMessageContentUnionMember1], List[DataOpenAIResponseMessageContentUnionMember2]
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


Data: TypeAlias = Union[
    DataOpenAIResponseOutputMessageWebSearchToolCall,
    DataOpenAIResponseOutputMessageFileSearchToolCall,
    DataOpenAIResponseOutputMessageFunctionToolCall,
    DataOpenAIResponseInputFunctionToolCallOutput,
    DataOpenAIResponseMcpApprovalRequest,
    DataOpenAIResponseMcpApprovalResponse,
    DataOpenAIResponseMessage,
]


class InputItemListResponse(BaseModel):
    data: List[Data]
    """List of input items"""

    object: Literal["list"]
    """Object type identifier, always "list" """
