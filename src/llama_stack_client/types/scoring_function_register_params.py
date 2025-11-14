# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScoringFunctionRegisterParams"]


class ScoringFunctionRegisterParams(TypedDict, total=False):
    description: Required[object]

    return_type: Required[object]

    scoring_fn_id: Required[object]

    params: object

    provider_id: object

    provider_scoring_fn_id: object
