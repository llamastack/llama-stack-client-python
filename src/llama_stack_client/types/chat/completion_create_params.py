# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompletionCreateParamsBase",
    "Message",
    "MessageOpenAIUserMessageParam",
    "MessageOpenAIUserMessageParamContentUnionMember1",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "MessageOpenAISystemMessageParam",
    "MessageOpenAISystemMessageParamContentUnionMember1",
    "MessageOpenAIAssistantMessageParam",
    "MessageOpenAIAssistantMessageParamContentUnionMember1",
    "MessageOpenAIAssistantMessageParamToolCall",
    "MessageOpenAIAssistantMessageParamToolCallFunction",
    "MessageOpenAIToolMessageParam",
    "MessageOpenAIToolMessageParamContentUnionMember1",
    "MessageOpenAIDeveloperMessageParam",
    "MessageOpenAIDeveloperMessageParamContentUnionMember1",
    "ResponseFormat",
    "ResponseFormatOpenAIResponseFormatText",
    "ResponseFormatOpenAIResponseFormatJsonSchema",
    "ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema",
    "ResponseFormatOpenAIResponseFormatJsonObject",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """List of messages in the conversation."""

    model: Required[str]
    """The identifier of the model to use.

    The model must be registered with Llama Stack and available via the /models
    endpoint.
    """

    frequency_penalty: float
    """(Optional) The penalty for repeated tokens."""

    function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) The function call to use."""

    functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) List of functions to use."""

    logit_bias: Dict[str, float]
    """(Optional) The logit bias to use."""

    logprobs: bool
    """(Optional) The log probabilities to use."""

    max_completion_tokens: int
    """(Optional) The maximum number of tokens to generate."""

    max_tokens: int
    """(Optional) The maximum number of tokens to generate."""

    n: int
    """(Optional) The number of completions to generate."""

    parallel_tool_calls: bool
    """(Optional) Whether to parallelize tool calls."""

    presence_penalty: float
    """(Optional) The penalty for repeated tokens."""

    response_format: ResponseFormat
    """(Optional) The response format to use."""

    seed: int
    """(Optional) The seed to use."""

    stop: Union[str, List[str]]
    """(Optional) The stop tokens to use."""

    stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) The stream options to use."""

    temperature: float
    """(Optional) The temperature to use."""

    tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) The tool choice to use."""

    tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) The tools to use."""

    top_logprobs: int
    """(Optional) The top log probabilities to use."""

    top_p: float
    """(Optional) The top p to use."""

    user: str
    """(Optional) The user to use."""


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: str


class MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    image_url: Required[
        MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    ]

    type: Required[Literal["image_url"]]


MessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Union[
    MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
    MessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
]


class MessageOpenAIUserMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAIUserMessageParamContentUnionMember1]]]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""

    name: str
    """(Optional) The name of the user message participant."""


class MessageOpenAISystemMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageOpenAISystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAISystemMessageParamContentUnionMember1]]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""

    name: str
    """(Optional) The name of the system message participant."""


class MessageOpenAIAssistantMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageOpenAIAssistantMessageParamToolCallFunction(TypedDict, total=False):
    arguments: str

    name: str


class MessageOpenAIAssistantMessageParamToolCall(TypedDict, total=False):
    type: Required[Literal["function"]]

    id: str

    function: MessageOpenAIAssistantMessageParamToolCallFunction

    index: int


class MessageOpenAIAssistantMessageParam(TypedDict, total=False):
    role: Required[Literal["assistant"]]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, Iterable[MessageOpenAIAssistantMessageParamContentUnionMember1]]
    """The content of the model's response"""

    name: str
    """(Optional) The name of the assistant message participant."""

    tool_calls: Iterable[MessageOpenAIAssistantMessageParamToolCall]
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class MessageOpenAIToolMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageOpenAIToolMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAIToolMessageParamContentUnionMember1]]]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: Required[str]
    """Unique identifier for the tool call this response is for"""


class MessageOpenAIDeveloperMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageOpenAIDeveloperMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageOpenAIDeveloperMessageParamContentUnionMember1]]]
    """The content of the developer message"""

    role: Required[Literal["developer"]]
    """Must be "developer" to identify this as a developer message"""

    name: str
    """(Optional) The name of the developer message participant."""


Message: TypeAlias = Union[
    MessageOpenAIUserMessageParam,
    MessageOpenAISystemMessageParam,
    MessageOpenAIAssistantMessageParam,
    MessageOpenAIToolMessageParam,
    MessageOpenAIDeveloperMessageParam,
]


class ResponseFormatOpenAIResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]


class ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    name: Required[str]

    description: str

    schema: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    strict: bool


class ResponseFormatOpenAIResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema]

    type: Required[Literal["json_schema"]]


class ResponseFormatOpenAIResponseFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]


ResponseFormat: TypeAlias = Union[
    ResponseFormatOpenAIResponseFormatText,
    ResponseFormatOpenAIResponseFormatJsonSchema,
    ResponseFormatOpenAIResponseFormatJsonObject,
]


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Literal[False]
    """(Optional) Whether to stream the response."""


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """(Optional) Whether to stream the response."""


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
