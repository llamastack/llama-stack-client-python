# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseObject",
    "Output",
    "OutputOpenAIResponseMessage",
    "OutputOpenAIResponseMessageContentUnionMember1",
    "OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OutputOpenAIResponseMessageContentUnionMember2",
    "OutputOpenAIResponseMessageContentUnionMember2Annotation",
    "OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation",
    "OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation",
    "OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation",
    "OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath",
    "OutputOpenAIResponseOutputMessageWebSearchToolCall",
    "OutputOpenAIResponseOutputMessageFileSearchToolCall",
    "OutputOpenAIResponseOutputMessageFunctionToolCall",
    "OutputOpenAIResponseOutputMessageMcpCall",
    "OutputOpenAIResponseOutputMessageMcpListTools",
    "OutputOpenAIResponseOutputMessageMcpListToolsTool",
    "Text",
    "TextFormat",
    "Error",
]


class OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str

    type: Literal["input_text"]


class OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]

    type: Literal["input_image"]

    image_url: Optional[str] = None


OutputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation(BaseModel):
    file_id: str

    filename: str

    index: int

    type: Literal["file_citation"]


class OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation(BaseModel):
    end_index: int

    start_index: int

    title: str

    type: Literal["url_citation"]

    url: str


class OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation(BaseModel):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Literal["container_file_citation"]


class OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath(BaseModel):
    file_id: str

    index: int

    type: Literal["file_path"]


OutputOpenAIResponseMessageContentUnionMember2Annotation: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFileCitation,
        OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationCitation,
        OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationContainerFileCitation,
        OutputOpenAIResponseMessageContentUnionMember2AnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageContentUnionMember2(BaseModel):
    annotations: List[OutputOpenAIResponseMessageContentUnionMember2Annotation]

    text: str

    type: Literal["output_text"]


class OutputOpenAIResponseMessage(BaseModel):
    content: Union[
        str, List[OutputOpenAIResponseMessageContentUnionMember1], List[OutputOpenAIResponseMessageContentUnionMember2]
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OutputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


class OutputOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str

    queries: List[str]

    status: str

    type: Literal["file_search_call"]

    results: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None


class OutputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    type: Literal["function_call"]

    id: Optional[str] = None

    status: Optional[str] = None


class OutputOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_call"]

    error: Optional[str] = None

    output: Optional[str] = None


class OutputOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str

    description: Optional[str] = None


class OutputOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str

    server_label: str

    tools: List[OutputOpenAIResponseOutputMessageMcpListToolsTool]

    type: Literal["mcp_list_tools"]


Output: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessage,
        OutputOpenAIResponseOutputMessageWebSearchToolCall,
        OutputOpenAIResponseOutputMessageFileSearchToolCall,
        OutputOpenAIResponseOutputMessageFunctionToolCall,
        OutputOpenAIResponseOutputMessageMcpCall,
        OutputOpenAIResponseOutputMessageMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]


class TextFormat(BaseModel):
    type: Literal["text", "json_schema", "json_object"]
    """Must be "text", "json_schema", or "json_object" to identify the format type"""

    description: Optional[str] = None
    """(Optional) A description of the response format. Only used for json_schema."""

    name: Optional[str] = None
    """The name of the response format. Only used for json_schema."""

    schema_: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = FieldInfo(
        alias="schema", default=None
    )
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model. Only used for json_schema.
    """

    strict: Optional[bool] = None
    """(Optional) Whether to strictly enforce the JSON schema.

    If true, the response must match the schema exactly. Only used for json_schema.
    """


class Text(BaseModel):
    format: Optional[TextFormat] = None
    """Configuration for Responses API text format."""


class Error(BaseModel):
    code: str

    message: str


class ResponseObject(BaseModel):
    @property
    def output_text(self) -> str:
        texts: List[str] = []
        for output in self.output:
            if output.type == "message":
                for content in output.content:
                    if content.type == "output_text":
                        texts.append(content.text)
        return "".join(texts)

    id: str

    created_at: int

    model: str

    object: Literal["response"]

    output: List[Output]

    parallel_tool_calls: bool

    status: str

    text: Text

    error: Optional[Error] = None

    previous_response_id: Optional[str] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    truncation: Optional[str] = None

    user: Optional[str] = None
