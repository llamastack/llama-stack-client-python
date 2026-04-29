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
    """Parameter type for string values."""

    type: Optional[Literal["string"]] = None


class NumberType(BaseModel):
    """Parameter type for numeric values."""

    type: Optional[Literal["number"]] = None


class BooleanType(BaseModel):
    """Parameter type for boolean values."""

    type: Optional[Literal["boolean"]] = None


class ArrayType(BaseModel):
    """Parameter type for array values."""

    type: Optional[Literal["array"]] = None


class ObjectType(BaseModel):
    """Parameter type for object values."""

    type: Optional[Literal["object"]] = None


class JsonType(BaseModel):
    """Parameter type for JSON values."""

    type: Optional[Literal["json"]] = None


class UnionType(BaseModel):
    """Parameter type for union values."""

    type: Optional[Literal["union"]] = None


class ChatCompletionInputType(BaseModel):
    """Parameter type for chat completion input."""

    type: Optional[Literal["chat_completion_input"]] = None


class CompletionInputType(BaseModel):
    """Parameter type for completion input."""

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
