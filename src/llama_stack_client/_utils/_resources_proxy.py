from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `llama_stack_client.resources` module.

    This is used so that we can lazily import `llama_stack_client.resources` only when
    needed *and* so that users can just import `llama_stack_client` and reference `llama_stack_client.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("llama_stack_client.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
