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
    "ItemGetResponse",
    "ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile",
    "ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText",
    "ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage",
    "ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath",
    "ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal",
]


class ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText(
    BaseModel
):
    text: str

    type: Optional[Literal["input_text"]] = None


class ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage(
    BaseModel
):
    detail: Optional[Literal["low", "high", "auto"]] = None

    file_id: Optional[str] = None

    image_url: Optional[str] = None

    type: Optional[Literal["input_image"]] = None


class ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile(
    BaseModel
):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    type: Optional[Literal["input_file"]] = None


ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile: TypeAlias = Annotated[
    Union[
        ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentText,
        ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentImage,
        ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFileOpenAIResponseInputMessageContentFile,
    ],
    PropertyInfo(discriminator="type"),
]


class ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation(
    BaseModel
):
    file_id: str

    filename: str

    index: int

    type: Optional[Literal["file_citation"]] = None


class ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation(
    BaseModel
):
    end_index: int

    start_index: int

    title: str

    url: str

    type: Optional[Literal["url_citation"]] = None


class ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation(
    BaseModel
):
    container_id: str

    end_index: int

    file_id: str

    filename: str

    start_index: int

    type: Optional[Literal["container_file_citation"]] = None


class ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath(
    BaseModel
):
    file_id: str

    index: int

    type: Optional[Literal["file_path"]] = None


ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFileCitation,
        ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationCitation,
        ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationContainerFileCitation,
        ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotationOpenAIResponseAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText(
    BaseModel
):
    text: str

    annotations: Optional[
        List[
            ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputTextAnnotation
        ]
    ] = None

    type: Optional[Literal["output_text"]] = None


class ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal(
    BaseModel
):
    refusal: str

    type: Optional[Literal["refusal"]] = None


ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal: TypeAlias = Annotated[
    Union[
        ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseOutputMessageContentOutputText,
        ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusalOpenAIResponseContentPartRefusal,
    ],
    PropertyInfo(discriminator="type"),
]


class ItemGetResponse(BaseModel):
    content: Union[
        str,
        List[
            ContentListOpenAIResponseInputMessageContentTextOpenAIResponseInputMessageContentImageOpenAIResponseInputMessageContentFile
        ],
        List[ContentListOpenAIResponseOutputMessageContentOutputTextOpenAIResponseContentPartRefusal],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[Literal["message"]] = None
