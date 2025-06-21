# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import File, FileUpload

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        session = client.files.session.retrieve(
            "upload_id",
        )
        assert_matches_type(FileUpload, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.files.session.with_raw_response.retrieve(
            "upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(FileUpload, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.files.session.with_streaming_response.retrieve(
            "upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(FileUpload, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.files.session.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload_content(self, client: LlamaStackClient) -> None:
        session = client.files.session.upload_content(
            upload_id="upload_id",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[File], session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload_content(self, client: LlamaStackClient) -> None:
        response = client.files.session.with_raw_response.upload_content(
            upload_id="upload_id",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Optional[File], session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload_content(self, client: LlamaStackClient) -> None:
        with client.files.session.with_streaming_response.upload_content(
            upload_id="upload_id",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Optional[File], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_upload_content(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.files.session.with_raw_response.upload_content(
                upload_id="",
                body=b"raw file contents",
            )


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.files.session.retrieve(
            "upload_id",
        )
        assert_matches_type(FileUpload, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.files.session.with_raw_response.retrieve(
            "upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(FileUpload, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.files.session.with_streaming_response.retrieve(
            "upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(FileUpload, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.files.session.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload_content(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.files.session.upload_content(
            upload_id="upload_id",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[File], session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload_content(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.files.session.with_raw_response.upload_content(
            upload_id="upload_id",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Optional[File], session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload_content(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.files.session.with_streaming_response.upload_content(
            upload_id="upload_id",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Optional[File], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_upload_content(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.files.session.with_raw_response.upload_content(
                upload_id="",
                body=b"raw file contents",
            )
