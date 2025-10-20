# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "DatasetListResponse",
    "DatasetListResponseItem",
    "DatasetListResponseItemSource",
    "DatasetListResponseItemSourceUriDataSource",
    "DatasetListResponseItemSourceRowsDataSource",
]


class DatasetListResponseItemSourceUriDataSource(BaseModel):
    type: Literal["uri"]

    uri: str
    """The dataset can be obtained from a URI.

    E.g. - "https://mywebsite.com/mydata.jsonl" - "lsfs://mydata.jsonl" -
    "data:csv;base64,{base64_content}"
    """


class DatasetListResponseItemSourceRowsDataSource(BaseModel):
    rows: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """The dataset is stored in rows.

    E.g. - [ {"messages": [{"role": "user", "content": "Hello, world!"}, {"role":
    "assistant", "content": "Hello, world!"}]} ]
    """

    type: Literal["rows"]


DatasetListResponseItemSource: TypeAlias = Annotated[
    Union[DatasetListResponseItemSourceUriDataSource, DatasetListResponseItemSourceRowsDataSource],
    PropertyInfo(discriminator="type"),
]


class DatasetListResponseItem(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Additional metadata for the dataset"""

    provider_id: str

    purpose: Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"]
    """Purpose of the dataset indicating its intended use"""

    source: DatasetListResponseItemSource
    """Data source configuration for the dataset"""

    type: Literal["dataset"]
    """Type of resource, always 'dataset' for datasets"""

    provider_resource_id: Optional[str] = None


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
