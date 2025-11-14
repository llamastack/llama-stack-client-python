# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetRegisterParams"]


class DatasetRegisterParams(TypedDict, total=False):
    purpose: Required[object]

    source: Required[object]

    dataset_id: object

    metadata: object
