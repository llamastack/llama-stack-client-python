# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["QueryGeneratorConfig", "DefaultRagQueryGeneratorConfig", "LlmragQueryGeneratorConfig"]


class DefaultRagQueryGeneratorConfig(BaseModel):
    separator: str
    """String separator used to join query terms"""

    type: Literal["default"]
    """Type of query generator, always 'default'"""


class LlmragQueryGeneratorConfig(BaseModel):
    model: str
    """Name of the language model to use for query generation"""

    template: str
    """Template string for formatting the query generation prompt"""

    type: Literal["llm"]
    """Type of query generator, always 'llm'"""


QueryGeneratorConfig: TypeAlias = Annotated[
    Union[DefaultRagQueryGeneratorConfig, LlmragQueryGeneratorConfig], PropertyInfo(discriminator="type")
]
