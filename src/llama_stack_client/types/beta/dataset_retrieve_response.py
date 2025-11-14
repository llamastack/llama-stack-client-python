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
    uri: str

    type: Optional[Literal["uri"]] = None


class SourceRowsDataSource(BaseModel):
    rows: List[Dict[str, object]]

    type: Optional[Literal["rows"]] = None


Source: TypeAlias = Annotated[Union[SourceUriDataSource, SourceRowsDataSource], PropertyInfo(discriminator="type")]


class DatasetRetrieveResponse(BaseModel):
    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    purpose: Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"]
    """Purpose of the dataset. Each purpose has a required input data schema."""

    source: Source
    """A dataset that can be obtained from a URI."""

    metadata: Optional[Dict[str, object]] = None
    """Any additional metadata for this dataset"""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["dataset"]] = None
