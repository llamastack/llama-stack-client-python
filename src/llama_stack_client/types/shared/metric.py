# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Metric"]


class Metric(BaseModel):
    metric: str
    """The name of the metric"""

    value: float
    """The numeric value of the metric"""

    unit: Optional[str] = None
    """(Optional) The unit of measurement for the metric value"""
