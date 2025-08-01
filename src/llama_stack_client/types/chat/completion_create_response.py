# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..chat_completion_chunk import ChatCompletionChunk

__all__ = [
    "CompletionCreateResponse",
    "OpenAIChatCompletion",
    "OpenAIChatCompletionChoice",
    "OpenAIChatCompletionChoiceMessage",
    "OpenAIChatCompletionChoiceMessageOpenAIUserMessageParam",
    "OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1",
    "OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile",
    "OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile",
    "OpenAIChatCompletionChoiceMessageOpenAISystemMessageParam",
    "OpenAIChatCompletionChoiceMessageOpenAISystemMessageParamContentUnionMember1",
    "OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParam",
    "OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamContentUnionMember1",
    "OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamToolCall",
    "OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamToolCallFunction",
    "OpenAIChatCompletionChoiceMessageOpenAIToolMessageParam",
    "OpenAIChatCompletionChoiceMessageOpenAIToolMessageParamContentUnionMember1",
    "OpenAIChatCompletionChoiceMessageOpenAIDeveloperMessageParam",
    "OpenAIChatCompletionChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "OpenAIChatCompletionChoiceLogprobs",
    "OpenAIChatCompletionChoiceLogprobsContent",
    "OpenAIChatCompletionChoiceLogprobsContentTopLogprob",
    "OpenAIChatCompletionChoiceLogprobsRefusal",
    "OpenAIChatCompletionChoiceLogprobsRefusalTopLogprob",
]


class OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


class OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile(BaseModel):
    file: OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile

    type: Literal["file"]


OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
        OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIChatCompletionChoiceMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[OpenAIChatCompletionChoiceMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class OpenAIChatCompletionChoiceMessageOpenAISystemMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class OpenAIChatCompletionChoiceMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[OpenAIChatCompletionChoiceMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]

    id: Optional[str] = None

    function: Optional[OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamToolCallFunction] = None

    index: Optional[int] = None


class OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamContentUnionMember1], None] = (
        None
    )
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class OpenAIChatCompletionChoiceMessageOpenAIToolMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class OpenAIChatCompletionChoiceMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[OpenAIChatCompletionChoiceMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class OpenAIChatCompletionChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class OpenAIChatCompletionChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[OpenAIChatCompletionChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


OpenAIChatCompletionChoiceMessage: TypeAlias = Annotated[
    Union[
        OpenAIChatCompletionChoiceMessageOpenAIUserMessageParam,
        OpenAIChatCompletionChoiceMessageOpenAISystemMessageParam,
        OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParam,
        OpenAIChatCompletionChoiceMessageOpenAIToolMessageParam,
        OpenAIChatCompletionChoiceMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class OpenAIChatCompletionChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class OpenAIChatCompletionChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[OpenAIChatCompletionChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class OpenAIChatCompletionChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class OpenAIChatCompletionChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[OpenAIChatCompletionChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class OpenAIChatCompletionChoiceLogprobs(BaseModel):
    content: Optional[List[OpenAIChatCompletionChoiceLogprobsContent]] = None
    """(Optional) The log probabilities for the tokens in the message"""

    refusal: Optional[List[OpenAIChatCompletionChoiceLogprobsRefusal]] = None
    """(Optional) The log probabilities for the tokens in the message"""


class OpenAIChatCompletionChoice(BaseModel):
    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    message: OpenAIChatCompletionChoiceMessage
    """The message from the model"""

    logprobs: Optional[OpenAIChatCompletionChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class OpenAIChatCompletion(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[OpenAIChatCompletionChoice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion"]
    """The object type, which will be "chat.completion" """


CompletionCreateResponse: TypeAlias = Union[OpenAIChatCompletion, ChatCompletionChunk]
