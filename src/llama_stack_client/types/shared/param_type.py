# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
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
]


class StringType(BaseModel):
    type: Optional[Literal["string"]] = None


class NumberType(BaseModel):
    type: Optional[Literal["number"]] = None


class BooleanType(BaseModel):
    type: Optional[Literal["boolean"]] = None


class ArrayType(BaseModel):
    type: Optional[Literal["array"]] = None


class ObjectType(BaseModel):
    type: Optional[Literal["object"]] = None


class JsonType(BaseModel):
    type: Optional[Literal["json"]] = None


class UnionType(BaseModel):
    type: Optional[Literal["union"]] = None


class ChatCompletionInputType(BaseModel):
    type: Optional[Literal["chat_completion_input"]] = None


class CompletionInputType(BaseModel):
    type: Optional[Literal["completion_input"]] = None


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
    ],
    PropertyInfo(discriminator="type"),
]
