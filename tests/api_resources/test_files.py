# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    File,
    FileUpload,
    FileListResponse,
    FileListInBucketResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        file = client.files.retrieve(
            key="key",
            bucket="bucket",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.files.with_raw_response.retrieve(
            key="key",
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.files.with_streaming_response.retrieve(
            key="key",
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            client.files.with_raw_response.retrieve(
                key="key",
                bucket="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.files.with_raw_response.retrieve(
                key="",
                bucket="bucket",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        file = client.files.list(
            bucket="bucket",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.files.with_raw_response.list(
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.files.with_streaming_response.list(
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        file = client.files.delete(
            key="key",
            bucket="bucket",
        )
        assert file is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        response = client.files.with_raw_response.delete(
            key="key",
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.files.with_streaming_response.delete(
            key="key",
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            client.files.with_raw_response.delete(
                key="key",
                bucket="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.files.with_raw_response.delete(
                key="",
                bucket="bucket",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_upload_session(self, client: LlamaStackClient) -> None:
        file = client.files.create_upload_session(
            bucket="bucket",
            key="key",
            mime_type="mime_type",
            size=0,
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_upload_session(self, client: LlamaStackClient) -> None:
        response = client.files.with_raw_response.create_upload_session(
            bucket="bucket",
            key="key",
            mime_type="mime_type",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_upload_session(self, client: LlamaStackClient) -> None:
        with client.files.with_streaming_response.create_upload_session(
            bucket="bucket",
            key="key",
            mime_type="mime_type",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUpload, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_in_bucket(self, client: LlamaStackClient) -> None:
        file = client.files.list_in_bucket(
            "bucket",
        )
        assert_matches_type(FileListInBucketResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_in_bucket(self, client: LlamaStackClient) -> None:
        response = client.files.with_raw_response.list_in_bucket(
            "bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListInBucketResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_in_bucket(self, client: LlamaStackClient) -> None:
        with client.files.with_streaming_response.list_in_bucket(
            "bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListInBucketResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_in_bucket(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            client.files.with_raw_response.list_in_bucket(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        file = await async_client.files.retrieve(
            key="key",
            bucket="bucket",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            key="key",
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            key="key",
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                key="key",
                bucket="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                key="",
                bucket="bucket",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        file = await async_client.files.list(
            bucket="bucket",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.files.with_raw_response.list(
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.files.with_streaming_response.list(
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        file = await async_client.files.delete(
            key="key",
            bucket="bucket",
        )
        assert file is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.files.with_raw_response.delete(
            key="key",
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.files.with_streaming_response.delete(
            key="key",
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            await async_client.files.with_raw_response.delete(
                key="key",
                bucket="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.files.with_raw_response.delete(
                key="",
                bucket="bucket",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_upload_session(self, async_client: AsyncLlamaStackClient) -> None:
        file = await async_client.files.create_upload_session(
            bucket="bucket",
            key="key",
            mime_type="mime_type",
            size=0,
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_upload_session(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.files.with_raw_response.create_upload_session(
            bucket="bucket",
            key="key",
            mime_type="mime_type",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_upload_session(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.files.with_streaming_response.create_upload_session(
            bucket="bucket",
            key="key",
            mime_type="mime_type",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUpload, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_in_bucket(self, async_client: AsyncLlamaStackClient) -> None:
        file = await async_client.files.list_in_bucket(
            "bucket",
        )
        assert_matches_type(FileListInBucketResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_in_bucket(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.files.with_raw_response.list_in_bucket(
            "bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListInBucketResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_in_bucket(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.files.with_streaming_response.list_in_bucket(
            "bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListInBucketResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_in_bucket(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            await async_client.files.with_raw_response.list_in_bucket(
                "",
            )
