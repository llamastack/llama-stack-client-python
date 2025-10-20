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
    "ItemGetResponse",
    "OpenAIResponseMessage",
    "OpenAIResponseMessageContentUnionMember1",
    "OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OpenAIResponseMessageContentUnionMember2",
    "OpenAIResponseMessageContentUnionMember2Annotation",
    "OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseOutputMessageFileSearchToolCallResult",
    "OpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseOutputMessageMcpListToolsTool",
]


class OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str
    """The text content of the input message"""

    type: Literal["input_text"]
    """Content type identifier, always "input_text" """


class OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """Level of detail for image processing, can be "low", "high", or "auto" """

    type: Literal["input_image"]
    """Content type identifier, always "input_image" """

    image_url: Optional[str] = None
    """(Optional) URL of the image content"""


OpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(BaseModel):
    file_id: str
    """Unique identifier of the referenced file"""

    filename: str
    """Name of the referenced file"""

    index: int
    """Position index of the citation within the content"""

    type: Literal["file_citation"]
    """Annotation type identifier, always "file_citation" """


class OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(BaseModel):
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


class OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(BaseModel):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Literal["file_path"]


OpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseMessageContentUnionMember2(BaseModel):
    annotations: List[OpenAIResponseMessageContentUnionMember2Annotation]

    text: str

    type: Literal["output_text"]


class OpenAIResponseMessage(BaseModel):
    content: Union[str, List[OpenAIResponseMessageContentUnionMember1], List[OpenAIResponseMessageContentUnionMember2]]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseOutputMessageFunctionToolCall(BaseModel):
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


class OpenAIResponseOutputMessageFileSearchToolCallResult(BaseModel):
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


class OpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    queries: List[str]
    """List of search queries executed"""

    status: str
    """Current status of the file search operation"""

    type: Literal["file_search_call"]
    """Tool call type identifier, always "file_search_call" """

    results: Optional[List[OpenAIResponseOutputMessageFileSearchToolCallResult]] = None
    """(Optional) Search results returned by the file search operation"""


class OpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str
    """Unique identifier for this tool call"""

    status: str
    """Current status of the web search operation"""

    type: Literal["web_search_call"]
    """Tool call type identifier, always "web_search_call" """


class OpenAIResponseOutputMessageMcpCall(BaseModel):
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


class OpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """JSON schema defining the tool's input parameters"""

    name: str
    """Name of the tool"""

    description: Optional[str] = None
    """(Optional) Description of what the tool does"""


class OpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str
    """Unique identifier for this MCP list tools operation"""

    server_label: str
    """Label identifying the MCP server providing the tools"""

    tools: List[OpenAIResponseOutputMessageMcpListToolsTool]
    """List of available tools provided by the MCP server"""

    type: Literal["mcp_list_tools"]
    """Tool call type identifier, always "mcp_list_tools" """


ItemGetResponse: TypeAlias = Annotated[
    Union[
        OpenAIResponseMessage,
        OpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseOutputMessageMcpCall,
        OpenAIResponseOutputMessageMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]
