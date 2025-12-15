# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DatasetRegisterParams", "Source", "SourceUriDataSource", "SourceRowsDataSource"]


class DatasetRegisterParams(TypedDict, total=False):
    purpose: Required[Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"]]
    """The purpose of the dataset."""

    source: Required[Source]
    """The data source of the dataset."""

    dataset_id: Optional[str]
    """The ID of the dataset. If not provided, an ID will be generated."""

    metadata: Optional[Dict[str, object]]
    """The metadata for the dataset."""


class SourceUriDataSource(TypedDict, total=False):
    """A dataset that can be obtained from a URI."""

    uri: Required[str]
    """The dataset can be obtained from a URI.

    E.g. "https://mywebsite.com/mydata.jsonl", "lsfs://mydata.jsonl",
    "data:csv;base64,{base64_content}"
    """

    type: Literal["uri"]
    """The type of data source."""


class SourceRowsDataSource(TypedDict, total=False):
    """A dataset stored in rows."""

    rows: Required[Iterable[Dict[str, object]]]
    """The dataset is stored in rows.

    E.g. [{"messages": [{"role": "user", "content": "Hello, world!"}, {"role":
    "assistant", "content": "Hello, world!"}]}]
    """

    type: Literal["rows"]
    """The type of data source."""


Source: TypeAlias = Union[SourceUriDataSource, SourceRowsDataSource]
