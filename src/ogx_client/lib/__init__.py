# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

__all__ = ["get_oauth_token_for_mcp_server"]


def __getattr__(name):
    if name == "get_oauth_token_for_mcp_server":
        from .tools.mcp_oauth import get_oauth_token_for_mcp_server

        return get_oauth_token_for_mcp_server
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
