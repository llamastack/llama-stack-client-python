# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.interleaved_content_item import InterleavedContentItem

__all__ = ["InferenceEmbeddingsParams"]


class InferenceEmbeddingsParams(TypedDict, total=False):
    contents: Required[Union[SequenceNotStr[str], Iterable[InterleavedContentItem]]]
    """List of contents to generate embeddings for.

    Each content can be a string or an InterleavedContentItem (and hence can be
    multimodal). The behavior depends on the model and provider. Some models may
    only support text.
    """

    model_id: Required[str]
    """The identifier of the model to use.

    The model must be an embedding model registered with Llama Stack and available
    via the /models endpoint.
    """

    output_dimension: int
    """(Optional) Output dimensionality for the embeddings.

    Only supported by Matryoshka models.
    """

    task_type: Literal["query", "document"]
    """
    (Optional) How is the embedding being used? This is only supported by asymmetric
    embedding models.
    """

    text_truncation: Literal["none", "start", "end"]
    """
    (Optional) Config for how to truncate text for embedding when text is longer
    than the model's max sequence length.
    """
