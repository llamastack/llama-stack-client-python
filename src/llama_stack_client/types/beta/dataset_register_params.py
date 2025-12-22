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
    """Purpose of the dataset. Each purpose has a required input data schema."""

    source: Required[Source]
    """A dataset that can be obtained from a URI."""

    dataset_id: Optional[str]

    metadata: Optional[Dict[str, object]]


class SourceUriDataSource(TypedDict, total=False):
    """A dataset that can be obtained from a URI."""

    uri: Required[str]

    type: Literal["uri"]


class SourceRowsDataSource(TypedDict, total=False):
    """A dataset stored in rows."""

    rows: Required[Iterable[Dict[str, object]]]

    type: Literal["rows"]


Source: TypeAlias = Union[SourceUriDataSource, SourceRowsDataSource]
