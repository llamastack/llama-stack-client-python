# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ParamType",
    "StringType",
    "NumberType",
    "BooleanType",
    "ArrayType",
    "ObjectType",
    "JsonType",
    "UnionType",
    "ChatCompletionInputType",
    "CompletionInputType",
    "AgentTurnInputType",
]


class StringType(BaseModel):
    type: Literal["string"]
    """Discriminator type. Always "string" """


class NumberType(BaseModel):
    type: Literal["number"]
    """Discriminator type. Always "number" """


class BooleanType(BaseModel):
    type: Literal["boolean"]
    """Discriminator type. Always "boolean" """


class ArrayType(BaseModel):
    type: Literal["array"]
    """Discriminator type. Always "array" """


class ObjectType(BaseModel):
    type: Literal["object"]
    """Discriminator type. Always "object" """


class JsonType(BaseModel):
    type: Literal["json"]
    """Discriminator type. Always "json" """


class UnionType(BaseModel):
    type: Literal["union"]
    """Discriminator type. Always "union" """


class ChatCompletionInputType(BaseModel):
    type: Literal["chat_completion_input"]
    """Discriminator type. Always "chat_completion_input" """


class CompletionInputType(BaseModel):
    type: Literal["completion_input"]
    """Discriminator type. Always "completion_input" """


class AgentTurnInputType(BaseModel):
    type: Literal["agent_turn_input"]
    """Discriminator type. Always "agent_turn_input" """


ParamType: TypeAlias = Annotated[
    Union[
        StringType,
        NumberType,
        BooleanType,
        ArrayType,
        ObjectType,
        JsonType,
        UnionType,
        ChatCompletionInputType,
        CompletionInputType,
        AgentTurnInputType,
    ],
    PropertyInfo(discriminator="type"),
]
