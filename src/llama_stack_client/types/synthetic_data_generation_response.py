# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["SyntheticDataGenerationResponse"]


class SyntheticDataGenerationResponse(BaseModel):
    synthetic_data: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """List of generated synthetic data samples that passed the filtering criteria"""

    statistics: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None
    """
    (Optional) Statistical information about the generation process and filtering
    results
    """
