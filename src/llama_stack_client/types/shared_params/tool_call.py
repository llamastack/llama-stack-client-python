# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ToolCall"]


class ToolCall(TypedDict, total=False):
    arguments: Required[
        Union[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    SequenceNotStr[Union[str, float, bool, None]],
                    Dict[str, Union[str, float, bool, None]],
                    None,
                ],
            ],
        ]
    ]

    call_id: Required[str]

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    arguments_json: str
