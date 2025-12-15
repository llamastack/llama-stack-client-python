# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .dataset_list_response import DatasetListResponse

__all__ = ["ListDatasetsResponse"]


class ListDatasetsResponse(BaseModel):
    """Response from listing datasets."""

    data: DatasetListResponse
    """List of datasets"""
