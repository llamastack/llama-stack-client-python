from enum import Enum

class MetricQueryTypeParam(Enum):
    """The type of metric query to perform.
    :cvar RANGE: Query metrics over a time range
    :cvar INSTANT: Query metrics at a specific point in time
    """

    RANGE = "range"
    INSTANT = "instant"
