# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    Prompt,
    PromptListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.create(
            prompt="prompt",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.create(
            prompt="prompt",
            variables=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.prompts.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.prompts.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.retrieve(
            prompt_id="prompt_id",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.retrieve(
            prompt_id="prompt_id",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.prompts.with_raw_response.retrieve(
            prompt_id="prompt_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.prompts.with_streaming_response.retrieve(
            prompt_id="prompt_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.retrieve(
                prompt_id="",
            )

    @parametrize
    def test_method_update(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
            set_as_default=True,
            variables=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LlamaStackClient) -> None:
        response = client.prompts.with_raw_response.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LlamaStackClient) -> None:
        with client.prompts.with_streaming_response.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.update(
                prompt_id="",
                prompt="prompt",
                version=0,
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.delete(
            "prompt_id",
        )
        assert prompt is None

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        response = client.prompts.with_raw_response.delete(
            "prompt_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert prompt is None

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.prompts.with_streaming_response.delete(
            "prompt_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert prompt is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_set_default_version(self, client: LlamaStackClient) -> None:
        prompt = client.prompts.set_default_version(
            prompt_id="prompt_id",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_set_default_version(self, client: LlamaStackClient) -> None:
        response = client.prompts.with_raw_response.set_default_version(
            prompt_id="prompt_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_set_default_version(self, client: LlamaStackClient) -> None:
        with client.prompts.with_streaming_response.set_default_version(
            prompt_id="prompt_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_default_version(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.set_default_version(
                prompt_id="",
                version=0,
            )


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.create(
            prompt="prompt",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.create(
            prompt="prompt",
            variables=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.prompts.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.prompts.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.retrieve(
            prompt_id="prompt_id",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.retrieve(
            prompt_id="prompt_id",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.prompts.with_raw_response.retrieve(
            prompt_id="prompt_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.prompts.with_streaming_response.retrieve(
            prompt_id="prompt_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.retrieve(
                prompt_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
            set_as_default=True,
            variables=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.prompts.with_raw_response.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.prompts.with_streaming_response.update(
            prompt_id="prompt_id",
            prompt="prompt",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.update(
                prompt_id="",
                prompt="prompt",
                version=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.delete(
            "prompt_id",
        )
        assert prompt is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.prompts.with_raw_response.delete(
            "prompt_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert prompt is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.prompts.with_streaming_response.delete(
            "prompt_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert prompt is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_set_default_version(self, async_client: AsyncLlamaStackClient) -> None:
        prompt = await async_client.prompts.set_default_version(
            prompt_id="prompt_id",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_set_default_version(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.prompts.with_raw_response.set_default_version(
            prompt_id="prompt_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_set_default_version(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.prompts.with_streaming_response.set_default_version(
            prompt_id="prompt_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_default_version(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.set_default_version(
                prompt_id="",
                version=0,
            )
