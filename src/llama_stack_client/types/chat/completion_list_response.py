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
    "DataChoiceMessageOpenAIUserMessageParamOutput",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile",
    "DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile",
    "DataChoiceMessageOpenAISystemMessageParam",
    "DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIAssistantMessageParamOutput",
    "DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall",
    "DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction",
    "DataChoiceMessageOpenAIToolMessageParam",
    "DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIDeveloperMessageParam",
    "DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataChoiceLogprobs",
    "DataChoiceLogprobsContent",
    "DataChoiceLogprobsContentTopLogprob",
    "DataChoiceLogprobsRefusal",
    "DataChoiceLogprobsRefusalTopLogprob",
    "DataInputMessage",
    "DataInputMessageOpenAIUserMessageParamOutput",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile",
    "DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile",
    "DataInputMessageOpenAISystemMessageParam",
    "DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIAssistantMessageParamOutput",
    "DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIAssistantMessageParamOutputToolCall",
    "DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction",
    "DataInputMessageOpenAIToolMessageParam",
    "DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIDeveloperMessageParam",
    "DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam",
    "DataUsage",
    "DataUsageCompletionTokensDetails",
    "DataUsagePromptTokensDetails",
]


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Optional[Literal["image_url"]] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile

    type: Optional[Literal["file"]] = None


DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam,
        DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAIUserMessageParamOutput(BaseModel):
    content: Union[
        str,
        List[
            DataChoiceMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
        ],
    ]

    name: Optional[str] = None

    role: Optional[Literal["user"]] = None


class DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAISystemMessageParam(BaseModel):
    content: Union[
        str, List[DataChoiceMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["system"]] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[DataChoiceMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class DataChoiceMessageOpenAIAssistantMessageParamOutput(BaseModel):
    content: Union[
        str,
        List[DataChoiceMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None

    name: Optional[str] = None

    role: Optional[Literal["assistant"]] = None

    tool_calls: Optional[List[DataChoiceMessageOpenAIAssistantMessageParamOutputToolCall]] = None


class DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIToolMessageParam(BaseModel):
    content: Union[
        str, List[DataChoiceMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    tool_call_id: str

    role: Optional[Literal["tool"]] = None


class DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[
        str, List[DataChoiceMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["developer"]] = None


DataChoiceMessage: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParamOutput,
        DataChoiceMessageOpenAISystemMessageParam,
        DataChoiceMessageOpenAIAssistantMessageParamOutput,
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

    refusal: Optional[List[DataChoiceLogprobsRefusal]] = None


class DataChoice(BaseModel):
    finish_reason: str

    index: int

    message: DataChoiceMessage
    """A message from the user in an OpenAI-compatible chat completion request."""

    logprobs: Optional[DataChoiceLogprobs] = None
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible
    chat completion response.
    """


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification for OpenAI-compatible chat completion messages."""

    type: Optional[Literal["image_url"]] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile(
    BaseModel
):
    file: DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFileFile

    type: Optional[Literal["file"]] = None


DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIChatCompletionContentPartImageParam,
        DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFileOpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAIUserMessageParamOutput(BaseModel):
    content: Union[
        str,
        List[
            DataInputMessageOpenAIUserMessageParamOutputContentListOpenAIChatCompletionContentPartTextParamOpenAIChatCompletionContentPartImageParamOpenAIFile
        ],
    ]

    name: Optional[str] = None

    role: Optional[Literal["user"]] = None


class DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAISystemMessageParam(BaseModel):
    content: Union[
        str, List[DataInputMessageOpenAISystemMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["system"]] = None


class DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class DataInputMessageOpenAIAssistantMessageParamOutputToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[DataInputMessageOpenAIAssistantMessageParamOutputToolCallFunction] = None
    """Function call details for OpenAI-compatible tool calls."""

    index: Optional[int] = None

    type: Optional[Literal["function"]] = None


class DataInputMessageOpenAIAssistantMessageParamOutput(BaseModel):
    content: Union[
        str,
        List[DataInputMessageOpenAIAssistantMessageParamOutputContentListOpenAIChatCompletionContentPartTextParam],
        None,
    ] = None

    name: Optional[str] = None

    role: Optional[Literal["assistant"]] = None

    tool_calls: Optional[List[DataInputMessageOpenAIAssistantMessageParamOutputToolCall]] = None


class DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAIToolMessageParamContentListOpenAIChatCompletionContentPartTextParam]]

    tool_call_id: str

    role: Optional[Literal["tool"]] = None


class DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class DataInputMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[
        str, List[DataInputMessageOpenAIDeveloperMessageParamContentListOpenAIChatCompletionContentPartTextParam]
    ]

    name: Optional[str] = None

    role: Optional[Literal["developer"]] = None


DataInputMessage: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParamOutput,
        DataInputMessageOpenAISystemMessageParam,
        DataInputMessageOpenAIAssistantMessageParamOutput,
        DataInputMessageOpenAIToolMessageParam,
        DataInputMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class DataUsageCompletionTokensDetails(BaseModel):
    reasoning_tokens: Optional[int] = None


class DataUsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None


class DataUsage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    completion_tokens_details: Optional[DataUsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[DataUsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class Data(BaseModel):
    id: str

    choices: List[DataChoice]

    created: int

    input_messages: List[DataInputMessage]

    model: str

    object: Optional[Literal["chat.completion"]] = None

    usage: Optional[DataUsage] = None
    """Usage information for OpenAI chat completion."""


class CompletionListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: Optional[Literal["list"]] = None
