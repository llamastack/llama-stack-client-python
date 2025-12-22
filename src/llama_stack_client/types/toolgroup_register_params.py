# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ToolgroupRegisterParams", "McpEndpoint"]


class ToolgroupRegisterParams(TypedDict, total=False):
    provider_id: Required[str]

    toolgroup_id: Required[str]

    args: Optional[Dict[str, object]]

    mcp_endpoint: Optional[McpEndpoint]
    """A URL reference to external content."""


class McpEndpoint(TypedDict, total=False):
    """A URL reference to external content."""

    uri: Required[str]
