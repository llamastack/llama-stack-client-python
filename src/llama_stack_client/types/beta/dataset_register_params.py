# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DatasetRegisterParams", "Source", "SourceUriDataSource", "SourceRowsDataSource"]


class DatasetRegisterParams(TypedDict, total=False):
    purpose: Required[Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"]]
    """The purpose of the dataset.

    One of: - "post-training/messages": The dataset contains a messages column with
    list of messages for post-training. { "messages": [ {"role": "user", "content":
    "Hello, world!"}, {"role": "assistant", "content": "Hello, world!"}, ] } -
    "eval/question-answer": The dataset contains a question column and an answer
    column for evaluation. { "question": "What is the capital of France?", "answer":
    "Paris" } - "eval/messages-answer": The dataset contains a messages column with
    list of messages and an answer column for evaluation. { "messages": [ {"role":
    "user", "content": "Hello, my name is John Doe."}, {"role": "assistant",
    "content": "Hello, John Doe. How can I help you today?"}, {"role": "user",
    "content": "What's my name?"}, ], "answer": "John Doe" }
    """

    source: Required[Source]
    """The data source of the dataset.

    Ensure that the data source schema is compatible with the purpose of the
    dataset. Examples: - { "type": "uri", "uri":
    "https://mywebsite.com/mydata.jsonl" } - { "type": "uri", "uri":
    "lsfs://mydata.jsonl" } - { "type": "uri", "uri":
    "data:csv;base64,{base64_content}" } - { "type": "uri", "uri":
    "huggingface://llamastack/simpleqa?split=train" } - { "type": "rows", "rows": [
    { "messages": [ {"role": "user", "content": "Hello, world!"}, {"role":
    "assistant", "content": "Hello, world!"}, ] } ] }
    """

    dataset_id: str
    """The ID of the dataset. If not provided, an ID will be generated."""

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The metadata for the dataset. - E.g. {"description": "My dataset"}."""


class SourceUriDataSource(TypedDict, total=False):
    type: Required[Literal["uri"]]

    uri: Required[str]
    """The dataset can be obtained from a URI.

    E.g. - "https://mywebsite.com/mydata.jsonl" - "lsfs://mydata.jsonl" -
    "data:csv;base64,{base64_content}"
    """


class SourceRowsDataSource(TypedDict, total=False):
    rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]
    """The dataset is stored in rows.

    E.g. - [ {"messages": [{"role": "user", "content": "Hello, world!"}, {"role":
    "assistant", "content": "Hello, world!"}]} ]
    """

    type: Required[Literal["rows"]]


Source: TypeAlias = Union[SourceUriDataSource, SourceRowsDataSource]
