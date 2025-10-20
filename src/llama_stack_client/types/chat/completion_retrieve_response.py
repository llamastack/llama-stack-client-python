# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "CompletionRetrieveResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceMessageOpenAIUserMessageParam",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile",
    "ChoiceMessageOpenAISystemMessageParam",
    "ChoiceMessageOpenAISystemMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIAssistantMessageParam",
    "ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIAssistantMessageParamToolCall",
    "ChoiceMessageOpenAIAssistantMessageParamToolCallFunction",
    "ChoiceMessageOpenAIToolMessageParam",
    "ChoiceMessageOpenAIToolMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIDeveloperMessageParam",
    "ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
    "InputMessage",
    "InputMessageOpenAIUserMessageParam",
    "InputMessageOpenAIUserMessageParamContentUnionMember1",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile",
    "InputMessageOpenAISystemMessageParam",
    "InputMessageOpenAISystemMessageParamContentUnionMember1",
    "InputMessageOpenAIAssistantMessageParam",
    "InputMessageOpenAIAssistantMessageParamContentUnionMember1",
    "InputMessageOpenAIAssistantMessageParamToolCall",
    "InputMessageOpenAIAssistantMessageParamToolCallFunction",
    "InputMessageOpenAIToolMessageParam",
    "InputMessageOpenAIToolMessageParamContentUnionMember1",
    "InputMessageOpenAIDeveloperMessageParam",
    "InputMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "Usage",
    "UsageCompletionTokensDetails",
    "UsagePromptTokensDetails",
]


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str
    """URL of the image to include in the message"""

    detail: Optional[str] = None
    """(Optional) Level of detail for image processing.

    Can be "low", "high", or "auto"
    """


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification and processing details"""

    type: Literal["image_url"]
    """Must be "image_url" to identify this as image content"""


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile(BaseModel):
    file: ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile

    type: Literal["file"]


ChoiceMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
        ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class ChoiceMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class ChoiceMessageOpenAISystemMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class ChoiceMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class ChoiceMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None
    """(Optional) Arguments to pass to the function as a JSON string"""

    name: Optional[str] = None
    """(Optional) Name of the function to call"""


class ChoiceMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]
    """Must be "function" to identify this as a function call"""

    id: Optional[str] = None
    """(Optional) Unique identifier for the tool call"""

    function: Optional[ChoiceMessageOpenAIAssistantMessageParamToolCallFunction] = None
    """(Optional) Function call details"""

    index: Optional[int] = None
    """(Optional) Index of the tool call in the list"""


class ChoiceMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[ChoiceMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class ChoiceMessageOpenAIToolMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class ChoiceMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class ChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


ChoiceMessage: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIUserMessageParam,
        ChoiceMessageOpenAISystemMessageParam,
        ChoiceMessageOpenAIAssistantMessageParam,
        ChoiceMessageOpenAIToolMessageParam,
        ChoiceMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class ChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobs(BaseModel):
    content: Optional[List[ChoiceLogprobsContent]] = None
    """(Optional) The log probabilities for the tokens in the message"""

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None
    """(Optional) The log probabilities for the tokens in the message"""


class Choice(BaseModel):
    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    message: ChoiceMessage
    """The message from the model"""

    logprobs: Optional[ChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(BaseModel):
    url: str
    """URL of the image to include in the message"""

    detail: Optional[str] = None
    """(Optional) Level of detail for image processing.

    Can be "low", "high", or "auto"
    """


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    """Image URL specification and processing details"""

    type: Literal["image_url"]
    """Must be "image_url" to identify this as image content"""


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile(BaseModel):
    file: InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFileFile

    type: Literal["file"]


InputMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
        InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIFile,
    ],
    PropertyInfo(discriminator="type"),
]


class InputMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class InputMessageOpenAISystemMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class InputMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class InputMessageOpenAIAssistantMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class InputMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None
    """(Optional) Arguments to pass to the function as a JSON string"""

    name: Optional[str] = None
    """(Optional) Name of the function to call"""


class InputMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]
    """Must be "function" to identify this as a function call"""

    id: Optional[str] = None
    """(Optional) Unique identifier for the tool call"""

    function: Optional[InputMessageOpenAIAssistantMessageParamToolCallFunction] = None
    """(Optional) Function call details"""

    index: Optional[int] = None
    """(Optional) Index of the tool call in the list"""


class InputMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[InputMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[InputMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class InputMessageOpenAIToolMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class InputMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class InputMessageOpenAIDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str
    """The text content of the message"""

    type: Literal["text"]
    """Must be "text" to identify this as text content"""


class InputMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


InputMessage: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIUserMessageParam,
        InputMessageOpenAISystemMessageParam,
        InputMessageOpenAIAssistantMessageParam,
        InputMessageOpenAIToolMessageParam,
        InputMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class UsageCompletionTokensDetails(BaseModel):
    reasoning_tokens: Optional[int] = None
    """Number of tokens used for reasoning (o1/o3 models)"""


class UsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None
    """Number of tokens retrieved from cache"""


class Usage(BaseModel):
    completion_tokens: int
    """Number of tokens in the completion"""

    prompt_tokens: int
    """Number of tokens in the prompt"""

    total_tokens: int
    """Total tokens used (prompt + completion)"""

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Token details for output tokens in OpenAI chat completion usage."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Token details for prompt tokens in OpenAI chat completion usage."""


class CompletionRetrieveResponse(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[Choice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    input_messages: List[InputMessage]

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion"]
    """The object type, which will be "chat.completion" """

    usage: Optional[Usage] = None
    """Token usage information for the completion"""
