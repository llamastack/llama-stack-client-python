# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VectorDBRegisterParams"]


class VectorDBRegisterParams(TypedDict, total=False):
    embedding_model: Required[str]
    """The embedding model to use."""

    vector_db_id: Required[str]
    """The identifier of the vector database to register."""

    embedding_dimension: int
    """The dimension of the embedding model."""

    provider_id: str
    """The identifier of the provider."""

    provider_vector_db_id: str
    """The identifier of the vector database in the provider."""

    vector_db_name: str
    """The name of the vector database."""
