__all__ = ["get_oauth_token_for_mcp_server"]


def __getattr__(name):
    if name == "get_oauth_token_for_mcp_server":
        from .tools.mcp_oauth import get_oauth_token_for_mcp_server

        return get_oauth_token_for_mcp_server
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
