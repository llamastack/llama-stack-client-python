# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.response_format import ResponseFormat
from .shared_params.sampling_params import SamplingParams
from .shared_params.interleaved_content import InterleavedContent

__all__ = ["InferenceBatchCompletionParams", "Logprobs"]


class InferenceBatchCompletionParams(TypedDict, total=False):
    content_batch: Required[SequenceNotStr[InterleavedContent]]
    """The content to generate completions for."""

    model_id: Required[str]
    """The identifier of the model to use.

    The model must be registered with Llama Stack and available via the /models
    endpoint.
    """

    logprobs: Logprobs
    """
    (Optional) If specified, log probabilities for each token position will be
    returned.
    """

    response_format: ResponseFormat
    """(Optional) Grammar specification for guided (structured) decoding."""

    sampling_params: SamplingParams
    """(Optional) Parameters to control the sampling strategy."""


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""
