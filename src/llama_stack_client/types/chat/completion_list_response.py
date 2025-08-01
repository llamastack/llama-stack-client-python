# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "CompletionListResponse",
    "Data",
    "DataChoice",
    "DataChoiceMessage",
    "DataChoiceMessageOpenAIUserMessageParam",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile",
    "DataChoiceMessageOpenAISystemMessageParam",
    "DataChoiceMessageOpenAISystemMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIAssistantMessageParam",
    "DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIAssistantMessageParamToolCall",
    "DataChoiceMessageOpenAIAssistantMessageParamToolCallFunction",
    "DataChoiceMessageOpenAIToolMessageParam",
    "DataChoiceMessageOpenAIToolMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIDeveloperMessageParam",
    "DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "DataChoiceLogprobs",
    "DataChoiceLogprobsContent",
    "DataChoiceLogprobsContentTopLogprob",
    "DataChoiceLogprobsRefusal",
    "DataChoiceLogprobsRefusalTopLogprob",
    "DataInputMessage",
    "DataInputMessageOpenAIUserMessageParam",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile",
    "DataInputMessageOpenAISystemMessageParam",
    "DataInputMessageOpenAISystemMessageParamContentUnionMember1",
    "DataInputMessageOpenAIAssistantMessageParam",
    "DataInputMessageOpenAIAssistantMessageParamContentUnionMember1",
    "DataInputMessageOpenAIAssistantMessageParamToolCall",
    "DataInputMessageOpenAIAssistantMessageParamToolCallFunction",
    "DataInputMessageOpenAIToolMessageParam",
    "DataInputMessageOpenAIToolMessageParamContentUnionMember1",
    "DataInputMessageOpenAIDeveloperMessageParam",
    "DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1",
]


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str
    """URL of the image to include in the message"""

    detail: Optional[str] = None
    """(Optional) Level of detail for image processing.

    Can be "low", "high", or "auto"
    """


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )
    """Image URL specification and processing details"""

    type: Literal["image_url"]
    """Must be "image_url" to identify this as image content"""


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile(BaseModel):
    file: DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile

    type: Literal["file"]


DataChoiceMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
        DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class DataChoiceMessageOpenAISystemMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataChoiceMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataChoiceMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None
    """(Optional) Arguments to pass to the function as a JSON string"""

    name: Optional[str] = None
    """(Optional) Name of the function to call"""


class DataChoiceMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]
    """Must be "function" to identify this as a function call"""

    id: Optional[str] = None
    """(Optional) Unique identifier for the tool call"""

    function: Optional[DataChoiceMessageOpenAIAssistantMessageParamToolCallFunction] = None
    """(Optional) Function call details"""

    index: Optional[int] = None
    """(Optional) Index of the tool call in the list"""


class DataChoiceMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[DataChoiceMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class DataChoiceMessageOpenAIToolMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataChoiceMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


DataChoiceMessage: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParam,
        DataChoiceMessageOpenAISystemMessageParam,
        DataChoiceMessageOpenAIAssistantMessageParam,
        DataChoiceMessageOpenAIToolMessageParam,
        DataChoiceMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class DataChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[DataChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[DataChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class DataChoiceLogprobs(BaseModel):
    content: Optional[List[DataChoiceLogprobsContent]] = None
    """(Optional) The log probabilities for the tokens in the message"""

    refusal: Optional[List[DataChoiceLogprobsRefusal]] = None
    """(Optional) The log probabilities for the tokens in the message"""


class DataChoice(BaseModel):
    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    message: DataChoiceMessage
    """The message from the model"""

    logprobs: Optional[DataChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str
    """URL of the image to include in the message"""

    detail: Optional[str] = None
    """(Optional) Level of detail for image processing.

    Can be "low", "high", or "auto"
    """


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )
    """Image URL specification and processing details"""

    type: Literal["image_url"]
    """Must be "image_url" to identify this as image content"""


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile(BaseModel):
    file: DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile

    type: Literal["file"]


DataInputMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
        DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class DataInputMessageOpenAISystemMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataInputMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class DataInputMessageOpenAIAssistantMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataInputMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None
    """(Optional) Arguments to pass to the function as a JSON string"""

    name: Optional[str] = None
    """(Optional) Name of the function to call"""


class DataInputMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]
    """Must be "function" to identify this as a function call"""

    id: Optional[str] = None
    """(Optional) Unique identifier for the tool call"""

    function: Optional[DataInputMessageOpenAIAssistantMessageParamToolCallFunction] = None
    """(Optional) Function call details"""

    index: Optional[int] = None
    """(Optional) Index of the tool call in the list"""


class DataInputMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[DataInputMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[DataInputMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class DataInputMessageOpenAIToolMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataInputMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class DataInputMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


DataInputMessage: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParam,
        DataInputMessageOpenAISystemMessageParam,
        DataInputMessageOpenAIAssistantMessageParam,
        DataInputMessageOpenAIToolMessageParam,
        DataInputMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class Data(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[DataChoice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    input_messages: List[DataInputMessage]

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion"]
    """The object type, which will be "chat.completion" """


class CompletionListResponse(BaseModel):
    data: List[Data]
    """List of chat completion objects with their input messages"""

    first_id: str
    """ID of the first completion in this list"""

    has_more: bool
    """Whether there are more completions available beyond this list"""

    last_id: str
    """ID of the last completion in this list"""

    object: Literal["list"]
    """Must be "list" to identify this as a list response"""
