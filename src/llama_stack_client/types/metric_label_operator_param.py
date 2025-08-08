from enum import Enum

class MetricLabelOperator(Enum):
    """Operators for matching metric labels.
    :cvar EQUALS: Label value must equal the specified value
    :cvar NOT_EQUALS: Label value must not equal the specified value
    :cvar REGEX_MATCH: Label value must match the specified regular expression
    :cvar REGEX_NOT_MATCH: Label value must not match the specified regular expression
    """

    EQUALS = "="
    NOT_EQUALS = "!="
    REGEX_MATCH = "=~"
    REGEX_NOT_MATCH = "!~"
