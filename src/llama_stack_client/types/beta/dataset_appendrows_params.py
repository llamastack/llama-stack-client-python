# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DatasetAppendrowsParams"]


class DatasetAppendrowsParams(TypedDict, total=False):
    body_dataset_id: Required[Annotated[str, PropertyInfo(alias="dataset_id")]]
    """The ID of the dataset to append the rows to."""

    rows: Required[Iterable[Dict[str, object]]]
    """The rows to append to the dataset."""
