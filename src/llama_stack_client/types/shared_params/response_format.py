# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ResponseFormat", "JsonSchemaResponseFormat", "GrammarResponseFormat"]


class JsonSchemaResponseFormat(TypedDict, total=False):
    json_schema: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model.
    """

    type: Required[Literal["json_schema"]]
    """Must be "json_schema" to identify this format type"""


class GrammarResponseFormat(TypedDict, total=False):
    bnf: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The BNF grammar specification the response should conform to"""

    type: Required[Literal["grammar"]]
    """Must be "grammar" to identify this format type"""


ResponseFormat: TypeAlias = Union[JsonSchemaResponseFormat, GrammarResponseFormat]
