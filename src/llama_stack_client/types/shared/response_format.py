# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ResponseFormat", "JsonSchemaResponseFormat", "GrammarResponseFormat"]


class JsonSchemaResponseFormat(BaseModel):
    json_schema: Dict[str, Union[bool, float, str, List[object], object, None]]
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model.
    """

    type: Literal["json_schema"]
    """Must be "json_schema" to identify this format type"""


class GrammarResponseFormat(BaseModel):
    bnf: Dict[str, Union[bool, float, str, List[object], object, None]]
    """The BNF grammar specification the response should conform to"""

    type: Literal["grammar"]
    """Must be "grammar" to identify this format type"""


ResponseFormat: TypeAlias = Annotated[
    Union[JsonSchemaResponseFormat, GrammarResponseFormat], PropertyInfo(discriminator="type")
]
