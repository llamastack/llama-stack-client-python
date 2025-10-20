# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import operator
from typing import Any
from typing_extensions import override

from llama_stack_client._utils import LazyProxy


class RecursiveLazyProxy(LazyProxy[Any]):
    @override
    def __load__(self) -> Any:
        return self

    def __call__(self, *_args: Any, **_kwds: Any) -> Any:
        raise RuntimeError("This should never be called!")


def test_recursive_proxy() -> None:
    proxy = RecursiveLazyProxy()
    assert repr(proxy) == "RecursiveLazyProxy"
    assert str(proxy) == "RecursiveLazyProxy"
    assert dir(proxy) == []
    assert type(proxy).__name__ == "RecursiveLazyProxy"
    assert type(operator.attrgetter("name.foo.bar.baz")(proxy)).__name__ == "RecursiveLazyProxy"


def test_isinstance_does_not_error() -> None:
    class AlwaysErrorProxy(LazyProxy[Any]):
        @override
        def __load__(self) -> Any:
            raise RuntimeError("Mocking missing dependency")

    proxy = AlwaysErrorProxy()
    assert not isinstance(proxy, dict)
    assert isinstance(proxy, LazyProxy)
