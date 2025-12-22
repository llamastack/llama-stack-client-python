# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Prompt"]


class Prompt(BaseModel):
    """
    A prompt resource representing a stored OpenAI Compatible prompt template in Llama Stack.
    """

    prompt_id: str
    """Unique identifier in format 'pmpt\\__<48-digit-hash>'"""

    version: int
    """Version (integer starting at 1, incremented on save)"""

    is_default: Optional[bool] = None
    """Boolean indicating whether this version is the default version"""

    prompt: Optional[str] = None
    """The system prompt with variable placeholders"""

    variables: Optional[List[str]] = None
    """List of variable names that can be used in the prompt template"""
