# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from pydantic import BaseModel, ValidationError
from typing import Dict, Any, Optional, List
from ..tool_parser import ToolParser
from llama_stack_client.types.shared.completion_message import CompletionMessage
from llama_stack_client.types.shared.tool_call import ToolCall

import uuid


class Action(BaseModel):
    tool_name: str
    tool_params: Dict[str, Any]


class ReflexionOutput(BaseModel):
    thought: str
    reflection: Optional[str] = None
    action: Optional[Action] = None
    answer: Optional[str] = None


class ReflexionToolParser(ToolParser):
    def get_tool_calls(self, output_message: CompletionMessage) -> List[ToolCall]:
        tool_calls = []
        response_text = str(output_message.content)
        try:
            reflexion_output = ReflexionOutput.model_validate_json(response_text)
        except ValidationError as e:
            print(f"Error parsing reflexion output: {e}")
            return tool_calls

        if reflexion_output.answer:
            return tool_calls

        if reflexion_output.action:
            tool_name = reflexion_output.action.tool_name
            tool_params = reflexion_output.action.tool_params
            if tool_name and tool_params:
                call_id = str(uuid.uuid4())
                tool_calls = [ToolCall(call_id=call_id, tool_name=tool_name, arguments=tool_params)]

        return tool_calls