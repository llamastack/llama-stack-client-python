# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .query_condition_param import QueryConditionParam

__all__ = ["TelemetrySaveSpansToDatasetParams"]


class TelemetrySaveSpansToDatasetParams(TypedDict, total=False):
    attribute_filters: Required[Iterable[QueryConditionParam]]
    """The attribute filters to apply to the spans."""

    attributes_to_save: Required[SequenceNotStr[str]]
    """The attributes to save to the dataset."""

    dataset_id: Required[str]
    """The ID of the dataset to save the spans to."""

    max_depth: int
    """The maximum depth of the tree."""
