# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .response_object import ResponseObject

__all__ = [
    "ResponseObjectStream",
    "OpenAIResponseObjectStreamResponseCreated",
    "OpenAIResponseObjectStreamResponseInProgress",
    "OpenAIResponseObjectStreamResponseOutputItemAdded",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItem",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMcpApprovalRequest",
    "OpenAIResponseObjectStreamResponseOutputItemDone",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItem",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest",
    "OpenAIResponseObjectStreamResponseOutputTextDelta",
    "OpenAIResponseObjectStreamResponseOutputTextDone",
    "OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta",
    "OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone",
    "OpenAIResponseObjectStreamResponseWebSearchCallInProgress",
    "OpenAIResponseObjectStreamResponseWebSearchCallSearching",
    "OpenAIResponseObjectStreamResponseWebSearchCallCompleted",
    "OpenAIResponseObjectStreamResponseMcpListToolsInProgress",
    "OpenAIResponseObjectStreamResponseMcpListToolsFailed",
    "OpenAIResponseObjectStreamResponseMcpListToolsCompleted",
    "OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta",
    "OpenAIResponseObjectStreamResponseMcpCallArgumentsDone",
    "OpenAIResponseObjectStreamResponseMcpCallInProgress",
    "OpenAIResponseObjectStreamResponseMcpCallFailed",
    "OpenAIResponseObjectStreamResponseMcpCallCompleted",
    "OpenAIResponseObjectStreamResponseContentPartAdded",
    "OpenAIResponseObjectStreamResponseContentPartAddedPart",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText",
    "OpenAIResponseObjectStreamResponseContentPartDone",
    "OpenAIResponseObjectStreamResponseContentPartDonePart",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal",
    "OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText",
    "OpenAIResponseObjectStreamResponseReasoningTextDelta",
    "OpenAIResponseObjectStreamResponseReasoningTextDone",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartAdded",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartDone",
    "OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart",
    "OpenAIResponseObjectStreamResponseReasoningSummaryTextDelta",
    "OpenAIResponseObjectStreamResponseReasoningSummaryTextDone",
    "OpenAIResponseObjectStreamResponseRefusalDelta",
    "OpenAIResponseObjectStreamResponseRefusalDone",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAdded",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFileCitation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationCitation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFilePath",
    "OpenAIResponseObjectStreamResponseFileSearchCallInProgress",
    "OpenAIResponseObjectStreamResponseFileSearchCallSearching",
    "OpenAIResponseObjectStreamResponseFileSearchCallCompleted",
    "OpenAIResponseObjectStreamResponseIncomplete",
    "OpenAIResponseObjectStreamResponseFailed",
    "OpenAIResponseObjectStreamResponseCompleted",
]


class OpenAIResponseObjectStreamResponseCreated(BaseModel):
    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    type: Optional[Literal["response.created"]] = None


class OpenAIResponseObjectStreamResponseInProgress(BaseModel):
    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    sequence_number: int

    type: Optional[Literal["response.in_progress"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    text: str

    type: Optional[Literal["input_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    refusal: str

    type: Optional[Literal["refusal"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult(
    BaseModel
):
    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str

    queries: List[str]

    status: str

    results: Optional[
        List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCallResult]
    ] = None

    type: Optional[Literal["file_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str

    server_label: str

    tools: List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItem: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMcpApprovalRequest,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAdded(BaseModel):
    item: OpenAIResponseObjectStreamResponseOutputItemAddedItem
    """
    Corresponds to the various Message types in the Responses API. They are all
    under one type because the Responses API gives them all the same "type" value,
    and there is no way to tell them apart in certain scenarios.
    """

    output_index: int

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.output_item.added"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    text: str

    type: Optional[Literal["input_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    refusal: str

    type: Optional[Literal["refusal"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[
            OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal
        ],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Optional[Literal["web_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult(
    BaseModel
):
    attributes: Dict[str, object]

    file_id: str

    filename: str

    score: float

    text: str


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str

    queries: List[str]

    status: str

    results: Optional[
        List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCallResult]
    ] = None

    type: Optional[Literal["file_search_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["function_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    error: Optional[str] = None

    output: Optional[str] = None

    type: Optional[Literal["mcp_call"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, object]

    name: str

    description: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str

    server_label: str

    tools: List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool]

    type: Optional[Literal["mcp_list_tools"]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Optional[Literal["mcp_approval_request"]] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItem: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMcpApprovalRequest,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDone(BaseModel):
    item: OpenAIResponseObjectStreamResponseOutputItemDoneItem
    """
    Corresponds to the various Message types in the Responses API. They are all
    under one type because the Responses API gives them all the same "type" value,
    and there is no way to tell them apart in certain scenarios.
    """

    output_index: int

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.output_item.done"]] = None


class OpenAIResponseObjectStreamResponseOutputTextDelta(BaseModel):
    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.output_text.delta"]] = None


class OpenAIResponseObjectStreamResponseOutputTextDone(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    text: str

    type: Optional[Literal["response.output_text.done"]] = None


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta(BaseModel):
    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.function_call_arguments.delta"]] = None


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone(BaseModel):
    arguments: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.function_call_arguments.done"]] = None


class OpenAIResponseObjectStreamResponseWebSearchCallInProgress(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.web_search_call.in_progress"]] = None


class OpenAIResponseObjectStreamResponseWebSearchCallSearching(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.web_search_call.searching"]] = None


class OpenAIResponseObjectStreamResponseWebSearchCallCompleted(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.web_search_call.completed"]] = None


class OpenAIResponseObjectStreamResponseMcpListToolsInProgress(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_list_tools.in_progress"]] = None


class OpenAIResponseObjectStreamResponseMcpListToolsFailed(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_list_tools.failed"]] = None


class OpenAIResponseObjectStreamResponseMcpListToolsCompleted(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_list_tools.completed"]] = None


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta(BaseModel):
    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.mcp_call.arguments.delta"]] = None


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDone(BaseModel):
    arguments: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.mcp_call.arguments.done"]] = None


class OpenAIResponseObjectStreamResponseMcpCallInProgress(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.mcp_call.in_progress"]] = None


class OpenAIResponseObjectStreamResponseMcpCallFailed(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_call.failed"]] = None


class OpenAIResponseObjectStreamResponseMcpCallCompleted(BaseModel):
    sequence_number: int

    type: Optional[Literal["response.mcp_call.completed"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText(BaseModel):
    text: str

    annotations: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputTextAnnotation]
    ] = None

    logprobs: Optional[List[Dict[str, object]]] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal(BaseModel):
    refusal: str

    type: Optional[Literal["refusal"]] = None


class OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText(BaseModel):
    text: str

    type: Optional[Literal["reasoning_text"]] = None


OpenAIResponseObjectStreamResponseContentPartAddedPart: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartOutputText,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartRefusal,
        OpenAIResponseObjectStreamResponseContentPartAddedPartOpenAIResponseContentPartReasoningText,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartAdded(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseContentPartAddedPart
    """Text content within a streamed response part."""

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.content_part.added"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText(BaseModel):
    text: str

    annotations: Optional[
        List[OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputTextAnnotation]
    ] = None

    logprobs: Optional[List[Dict[str, object]]] = None

    type: Optional[Literal["output_text"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal(BaseModel):
    refusal: str

    type: Optional[Literal["refusal"]] = None


class OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText(BaseModel):
    text: str

    type: Optional[Literal["reasoning_text"]] = None


OpenAIResponseObjectStreamResponseContentPartDonePart: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartOutputText,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartRefusal,
        OpenAIResponseObjectStreamResponseContentPartDonePartOpenAIResponseContentPartReasoningText,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseContentPartDone(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseContentPartDonePart
    """Text content within a streamed response part."""

    response_id: str

    sequence_number: int

    type: Optional[Literal["response.content_part.done"]] = None


class OpenAIResponseObjectStreamResponseReasoningTextDelta(BaseModel):
    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.reasoning_text.delta"]] = None


class OpenAIResponseObjectStreamResponseReasoningTextDone(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    text: str

    type: Optional[Literal["response.reasoning_text.done"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart(BaseModel):
    text: str

    type: Optional[Literal["summary_text"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartAdded(BaseModel):
    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseReasoningSummaryPartAddedPart
    """Reasoning summary part in a streamed response."""

    sequence_number: int

    summary_index: int

    type: Optional[Literal["response.reasoning_summary_part.added"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart(BaseModel):
    text: str

    type: Optional[Literal["summary_text"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryPartDone(BaseModel):
    item_id: str

    output_index: int

    part: OpenAIResponseObjectStreamResponseReasoningSummaryPartDonePart
    """Reasoning summary part in a streamed response."""

    sequence_number: int

    summary_index: int

    type: Optional[Literal["response.reasoning_summary_part.done"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryTextDelta(BaseModel):
    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    summary_index: int

    type: Optional[Literal["response.reasoning_summary_text.delta"]] = None


class OpenAIResponseObjectStreamResponseReasoningSummaryTextDone(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    summary_index: int

    text: str

    type: Optional[Literal["response.reasoning_summary_text.done"]] = None


class OpenAIResponseObjectStreamResponseRefusalDelta(BaseModel):
    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.refusal.delta"]] = None


class OpenAIResponseObjectStreamResponseRefusalDone(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    refusal: str

    sequence_number: int

    type: Optional[Literal["response.refusal.done"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationCitation(BaseModel):
    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotation: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFileCitation,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationCitation,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationContainerFileCitation,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputTextAnnotationAdded(BaseModel):
    annotation: OpenAIResponseObjectStreamResponseOutputTextAnnotationAddedAnnotation
    """File citation annotation for referencing specific files in response content."""

    annotation_index: int

    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.output_text.annotation.added"]] = None


class OpenAIResponseObjectStreamResponseFileSearchCallInProgress(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.file_search_call.in_progress"]] = None


class OpenAIResponseObjectStreamResponseFileSearchCallSearching(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.file_search_call.searching"]] = None


class OpenAIResponseObjectStreamResponseFileSearchCallCompleted(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Optional[Literal["response.file_search_call.completed"]] = None


class OpenAIResponseObjectStreamResponseIncomplete(BaseModel):
    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    sequence_number: int

    type: Optional[Literal["response.incomplete"]] = None


class OpenAIResponseObjectStreamResponseFailed(BaseModel):
    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    sequence_number: int

    type: Optional[Literal["response.failed"]] = None


class OpenAIResponseObjectStreamResponseCompleted(BaseModel):
    response: ResponseObject
    """Complete OpenAI response object containing generation results and metadata."""

    type: Optional[Literal["response.completed"]] = None


ResponseObjectStream: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseCreated,
        OpenAIResponseObjectStreamResponseInProgress,
        OpenAIResponseObjectStreamResponseOutputItemAdded,
        OpenAIResponseObjectStreamResponseOutputItemDone,
        OpenAIResponseObjectStreamResponseOutputTextDelta,
        OpenAIResponseObjectStreamResponseOutputTextDone,
        OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta,
        OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone,
        OpenAIResponseObjectStreamResponseWebSearchCallInProgress,
        OpenAIResponseObjectStreamResponseWebSearchCallSearching,
        OpenAIResponseObjectStreamResponseWebSearchCallCompleted,
        OpenAIResponseObjectStreamResponseMcpListToolsInProgress,
        OpenAIResponseObjectStreamResponseMcpListToolsFailed,
        OpenAIResponseObjectStreamResponseMcpListToolsCompleted,
        OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta,
        OpenAIResponseObjectStreamResponseMcpCallArgumentsDone,
        OpenAIResponseObjectStreamResponseMcpCallInProgress,
        OpenAIResponseObjectStreamResponseMcpCallFailed,
        OpenAIResponseObjectStreamResponseMcpCallCompleted,
        OpenAIResponseObjectStreamResponseContentPartAdded,
        OpenAIResponseObjectStreamResponseContentPartDone,
        OpenAIResponseObjectStreamResponseReasoningTextDelta,
        OpenAIResponseObjectStreamResponseReasoningTextDone,
        OpenAIResponseObjectStreamResponseReasoningSummaryPartAdded,
        OpenAIResponseObjectStreamResponseReasoningSummaryPartDone,
        OpenAIResponseObjectStreamResponseReasoningSummaryTextDelta,
        OpenAIResponseObjectStreamResponseReasoningSummaryTextDone,
        OpenAIResponseObjectStreamResponseRefusalDelta,
        OpenAIResponseObjectStreamResponseRefusalDone,
        OpenAIResponseObjectStreamResponseOutputTextAnnotationAdded,
        OpenAIResponseObjectStreamResponseFileSearchCallInProgress,
        OpenAIResponseObjectStreamResponseFileSearchCallSearching,
        OpenAIResponseObjectStreamResponseFileSearchCallCompleted,
        OpenAIResponseObjectStreamResponseIncomplete,
        OpenAIResponseObjectStreamResponseFailed,
        OpenAIResponseObjectStreamResponseCompleted,
    ],
    PropertyInfo(discriminator="type"),
]
