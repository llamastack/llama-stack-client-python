# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["DatasetRetrieveResponse", "Source", "SourceUriDataSource", "SourceRowsDataSource"]


class SourceUriDataSource(BaseModel):
    """A dataset that can be obtained from a URI."""

    uri: str
    """The dataset can be obtained from a URI.

    E.g. "https://mywebsite.com/mydata.jsonl", "lsfs://mydata.jsonl",
    "data:csv;base64,{base64_content}"
    """

    type: Optional[Literal["uri"]] = None
    """The type of data source."""


class SourceRowsDataSource(BaseModel):
    """A dataset stored in rows."""

    rows: List[Dict[str, object]]
    """The dataset is stored in rows.

    E.g. [{"messages": [{"role": "user", "content": "Hello, world!"}, {"role":
    "assistant", "content": "Hello, world!"}]}]
    """

    type: Optional[Literal["rows"]] = None
    """The type of data source."""


Source: TypeAlias = Annotated[Union[SourceUriDataSource, SourceRowsDataSource], PropertyInfo(discriminator="type")]


class DatasetRetrieveResponse(BaseModel):
    """Dataset resource for storing and accessing training or evaluation data."""

    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    purpose: Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"]
    """Purpose of the dataset indicating its intended use"""

    source: Source
    """Data source configuration for the dataset"""

    metadata: Optional[Dict[str, object]] = None
    """Any additional metadata for this dataset"""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["dataset"]] = None
    """Type of resource, always 'dataset' for datasets"""
