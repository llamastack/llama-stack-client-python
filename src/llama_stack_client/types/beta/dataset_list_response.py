# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "DatasetListResponse",
    "DatasetListResponseItem",
    "DatasetListResponseItemSource",
    "DatasetListResponseItemSourceUriDataSource",
    "DatasetListResponseItemSourceRowsDataSource",
]


class DatasetListResponseItemSourceUriDataSource(BaseModel):
    uri: str

    type: Optional[Literal["uri"]] = None


class DatasetListResponseItemSourceRowsDataSource(BaseModel):
    rows: List[Dict[str, object]]

    type: Optional[Literal["rows"]] = None


DatasetListResponseItemSource: TypeAlias = Annotated[
    Union[DatasetListResponseItemSourceUriDataSource, DatasetListResponseItemSourceRowsDataSource],
    PropertyInfo(discriminator="type"),
]


class DatasetListResponseItem(BaseModel):
    identifier: str
    """Unique identifier for this resource in llama stack"""

    provider_id: str
    """ID of the provider that owns this resource"""

    purpose: Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"]
    """Purpose of the dataset. Each purpose has a required input data schema."""

    source: DatasetListResponseItemSource
    """A dataset that can be obtained from a URI."""

    metadata: Optional[Dict[str, object]] = None
    """Any additional metadata for this dataset"""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["dataset"]] = None


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
