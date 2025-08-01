# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["QueryGeneratorConfig", "DefaultRagQueryGeneratorConfig", "LlmragQueryGeneratorConfig"]


class DefaultRagQueryGeneratorConfig(TypedDict, total=False):
    separator: Required[str]
    """String separator used to join query terms"""

    type: Required[Literal["default"]]
    """Type of query generator, always 'default'"""


class LlmragQueryGeneratorConfig(TypedDict, total=False):
    model: Required[str]
    """Name of the language model to use for query generation"""

    template: Required[str]
    """Template string for formatting the query generation prompt"""

    type: Required[Literal["llm"]]
    """Type of query generator, always 'llm'"""


QueryGeneratorConfig: TypeAlias = Union[DefaultRagQueryGeneratorConfig, LlmragQueryGeneratorConfig]
