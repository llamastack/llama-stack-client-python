# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import json
import uuid
from typing import List, Optional, Union

from llama_stack_client.types.shared.completion_message import CompletionMessage
from llama_stack_client.types.shared.tool_call import ToolCall

from pydantic import BaseModel, ValidationError

from ..tool_parser import ToolParser


class Param(BaseModel):
    name: str
    value: Union[str, int, float, bool]


class Action(BaseModel):
    tool_name: str
    tool_params: List[Param]


class ReActOutput(BaseModel):
    thought: str
    action: Optional[Action]
    answer: Optional[str]


class ReActToolParser(ToolParser):
    def get_tool_calls(self, output_message: CompletionMessage) -> List[ToolCall]:
        tool_calls = []
        response_text = str(output_message.content)
        try:
            react_output = ReActOutput.model_validate_json(response_text)
        except ValidationError as e:
            print(f"Error parsing action: {e}")
            return tool_calls

        if react_output.answer:
            return tool_calls

        if react_output.action:
            tool_name = react_output.action.tool_name
            tool_params = react_output.action.tool_params
            params = {param.name: param.value for param in tool_params}
            if tool_name and tool_params:
                call_id = str(uuid.uuid4())
                tool_calls = [
                    ToolCall(
                        call_id=call_id,
                        tool_name=tool_name,
                        arguments=params,
                        arguments_json=json.dumps(params),
                    )
                ]

        return tool_calls
