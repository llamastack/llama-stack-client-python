# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Generic, TypeVar

from ._models import GenericModel

__all__ = ["DataWrapper"]

_T = TypeVar("_T")


class DataWrapper(GenericModel, Generic[_T]):
    data: _T

    @staticmethod
    def _unwrapper(obj: "DataWrapper[_T]") -> _T:
        return obj.data
