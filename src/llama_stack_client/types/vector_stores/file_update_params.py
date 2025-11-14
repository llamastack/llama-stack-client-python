# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    vector_store_id: Required[str]

    attributes: Required[Dict[str, object]]
