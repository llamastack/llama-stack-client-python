# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .scoring_function_list_response import ScoringFunctionListResponse

__all__ = ["ListScoringFunctionsResponse"]


class ListScoringFunctionsResponse(BaseModel):
    data: ScoringFunctionListResponse
