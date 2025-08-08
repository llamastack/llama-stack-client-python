from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypedDict

from .metric_label_operator_param import MetricLabelOperator

__all__ = ["MetricLabelMatcherParam"]

class MetricLabelMatcherParam(TypedDict, total=False):
    """A matcher for filtering metrics by label values.
    :param name: The name of the label to match
    :param value: The value to match against
    :param operator: The comparison operator to use for matching
    """

    name: str
    value: str
    operator: MetricLabelOperator = MetricLabelOperator.EQUALS
