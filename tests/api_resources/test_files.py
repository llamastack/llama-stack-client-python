# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ogx_client import OgxClient, AsyncOgxClient
from tests.utils import assert_matches_type
from ogx_client.types import File, DeleteFileResponse
from ogx_client.pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OgxClient) -> None:
        file = client.files.create(
            file=b"Example data",
            purpose="assistants",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OgxClient) -> None:
        file = client.files.create(
            file=b"Example data",
            purpose="assistants",
            expires_after={
                "anchor": "created_at",
                "seconds": 3600,
            },
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OgxClient) -> None:
        response = client.files.with_raw_response.create(
            file=b"Example data",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OgxClient) -> None:
        with client.files.with_streaming_response.create(
            file=b"Example data",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: OgxClient) -> None:
        file = client.files.retrieve(
            "file_id",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OgxClient) -> None:
        response = client.files.with_raw_response.retrieve(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OgxClient) -> None:
        with client.files.with_streaming_response.retrieve(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: OgxClient) -> None:
        file = client.files.list()
        assert_matches_type(SyncOpenAICursorPage[File], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OgxClient) -> None:
        file = client.files.list(
            after="after",
            limit=0,
            order="asc",
            purpose="assistants",
        )
        assert_matches_type(SyncOpenAICursorPage[File], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OgxClient) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncOpenAICursorPage[File], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OgxClient) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncOpenAICursorPage[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: OgxClient) -> None:
        file = client.files.delete(
            "file_id",
        )
        assert_matches_type(DeleteFileResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OgxClient) -> None:
        response = client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(DeleteFileResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OgxClient) -> None:
        with client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(DeleteFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_content(self, client: OgxClient) -> None:
        file = client.files.content(
            "file_id",
        )
        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_raw_response_content(self, client: OgxClient) -> None:
        response = client.files.with_raw_response.content(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_streaming_response_content(self, client: OgxClient) -> None:
        with client.files.with_streaming_response.content(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_content(self, client: OgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.content(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOgxClient) -> None:
        file = await async_client.files.create(
            file=b"Example data",
            purpose="assistants",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOgxClient) -> None:
        file = await async_client.files.create(
            file=b"Example data",
            purpose="assistants",
            expires_after={
                "anchor": "created_at",
                "seconds": 3600,
            },
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.files.with_raw_response.create(
            file=b"Example data",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOgxClient) -> None:
        async with async_client.files.with_streaming_response.create(
            file=b"Example data",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOgxClient) -> None:
        file = await async_client.files.retrieve(
            "file_id",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOgxClient) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOgxClient) -> None:
        file = await async_client.files.list()
        assert_matches_type(AsyncOpenAICursorPage[File], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOgxClient) -> None:
        file = await async_client.files.list(
            after="after",
            limit=0,
            order="asc",
            purpose="assistants",
        )
        assert_matches_type(AsyncOpenAICursorPage[File], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncOpenAICursorPage[File], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOgxClient) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncOpenAICursorPage[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOgxClient) -> None:
        file = await async_client.files.delete(
            "file_id",
        )
        assert_matches_type(DeleteFileResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(DeleteFileResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOgxClient) -> None:
        async with async_client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(DeleteFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_content(self, async_client: AsyncOgxClient) -> None:
        file = await async_client.files.content(
            "file_id",
        )
        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_raw_response_content(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.files.with_raw_response.content(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_streaming_response_content(self, async_client: AsyncOgxClient) -> None:
        async with async_client.files.with_streaming_response.content(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_content(self, async_client: AsyncOgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.content(
                "",
            )
