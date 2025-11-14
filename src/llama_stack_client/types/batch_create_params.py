# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    completion_window: Required[Literal["24h"]]

    endpoint: Required[str]

    input_file_id: Required[str]

    idempotency_key: Optional[str]

    metadata: Optional[Dict[str, str]]
