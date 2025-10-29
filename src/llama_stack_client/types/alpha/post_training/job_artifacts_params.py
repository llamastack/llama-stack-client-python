# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JobArtifactsParams"]


class JobArtifactsParams(TypedDict, total=False):
    job_uuid: Required[str]
    """The UUID of the job to get the artifacts of."""
