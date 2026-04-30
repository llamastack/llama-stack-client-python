# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BatchCreateResponse",
    "Errors",
    "ErrorsData",
    "RequestCounts",
    "Usage",
    "UsageInputTokensDetails",
    "UsageOutputTokensDetails",
]


class ErrorsData(BaseModel):
    code: Optional[str] = None

    line: Optional[int] = None

    message: Optional[str] = None

    param: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Errors(BaseModel):
    data: Optional[List[ErrorsData]] = None

    object: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]


class RequestCounts(BaseModel):
    """The request counts for different statuses within the batch."""

    completed: int

    failed: int

    total: int

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class UsageInputTokensDetails(BaseModel):
    """A detailed breakdown of the input tokens."""

    cached_tokens: int

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class UsageOutputTokensDetails(BaseModel):
    """A detailed breakdown of the output tokens."""

    reasoning_tokens: int

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Usage(BaseModel):
    """
    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.
    """

    input_tokens: int

    input_tokens_details: UsageInputTokensDetails
    """A detailed breakdown of the input tokens."""

    output_tokens: int

    output_tokens_details: UsageOutputTokensDetails
    """A detailed breakdown of the output tokens."""

    total_tokens: int

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class BatchCreateResponse(BaseModel):
    id: str

    completion_window: str

    created_at: int

    endpoint: str

    input_file_id: str

    object: Literal["batch"]

    status: Literal[
        "validating", "failed", "in_progress", "finalizing", "completed", "expired", "cancelling", "cancelled"
    ]

    cancelled_at: Optional[int] = None

    cancelling_at: Optional[int] = None

    completed_at: Optional[int] = None

    error_file_id: Optional[str] = None

    errors: Optional[Errors] = None

    expired_at: Optional[int] = None

    expires_at: Optional[int] = None

    failed_at: Optional[int] = None

    finalizing_at: Optional[int] = None

    in_progress_at: Optional[int] = None

    metadata: Optional[Dict[str, str]] = None

    model: Optional[str] = None

    output_file_id: Optional[str] = None

    request_counts: Optional[RequestCounts] = None
    """The request counts for different statuses within the batch."""

    usage: Optional[Usage] = None
    """
    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on batches
    created after September 7, 2025.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]
