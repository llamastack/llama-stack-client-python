# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import json
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        beta,
        chat,
        alpha,
        files,
        tools,
        models,
        routes,
        safety,
        batches,
        inspect,
        prompts,
        scoring,
        shields,
        providers,
        responses,
        vector_io,
        embeddings,
        toolgroups,
        completions,
        moderations,
        tool_runtime,
        conversations,
        vector_stores,
        scoring_functions,
    )
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.tools import ToolsResource, AsyncToolsResource
    from .resources.routes import RoutesResource, AsyncRoutesResource
    from .resources.safety import SafetyResource, AsyncSafetyResource
    from .resources.batches import BatchesResource, AsyncBatchesResource
    from .resources.inspect import InspectResource, AsyncInspectResource
    from .resources.scoring import ScoringResource, AsyncScoringResource
    from .resources.shields import ShieldsResource, AsyncShieldsResource
    from .resources.beta.beta import BetaResource, AsyncBetaResource
    from .resources.chat.chat import ChatResource, AsyncChatResource
    from .resources.providers import ProvidersResource, AsyncProvidersResource
    from .resources.vector_io import VectorIoResource, AsyncVectorIoResource
    from .resources.embeddings import EmbeddingsResource, AsyncEmbeddingsResource
    from .resources.toolgroups import ToolgroupsResource, AsyncToolgroupsResource
    from .resources.alpha.alpha import AlphaResource, AsyncAlphaResource
    from .resources.completions import CompletionsResource, AsyncCompletionsResource
    from .resources.moderations import ModerationsResource, AsyncModerationsResource
    from .resources.tool_runtime import ToolRuntimeResource, AsyncToolRuntimeResource
    from .resources.models.models import ModelsResource, AsyncModelsResource
    from .resources.prompts.prompts import PromptsResource, AsyncPromptsResource
    from .resources.scoring_functions import ScoringFunctionsResource, AsyncScoringFunctionsResource
    from .resources.responses.responses import ResponsesResource, AsyncResponsesResource
    from .resources.conversations.conversations import ConversationsResource, AsyncConversationsResource
    from .resources.vector_stores.vector_stores import VectorStoresResource, AsyncVectorStoresResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LlamaStackClient",
    "AsyncLlamaStackClient",
    "Client",
    "AsyncClient",
]


class LlamaStackClient(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
        provider_data: Mapping[str, Any] | None = None,
    ) -> None:
        """Construct a new synchronous LlamaStackClient client instance.

        This automatically infers the `api_key` argument from the `LLAMA_STACK_CLIENT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_STACK_CLIENT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://any-hosted-llama-stack.com"

        custom_headers = default_headers or {}
        custom_headers["X-LlamaStack-Client-Version"] = __version__
        if provider_data is not None:
            custom_headers["X-LlamaStack-Provider-Data"] = json.dumps(provider_data)

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=custom_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def toolgroups(self) -> ToolgroupsResource:
        from .resources.toolgroups import ToolgroupsResource

        return ToolgroupsResource(self)

    @cached_property
    def tools(self) -> ToolsResource:
        from .resources.tools import ToolsResource

        return ToolsResource(self)

    @cached_property
    def tool_runtime(self) -> ToolRuntimeResource:
        from .resources.tool_runtime import ToolRuntimeResource

        return ToolRuntimeResource(self)

    @cached_property
    def responses(self) -> ResponsesResource:
        from .resources.responses import ResponsesResource

        return ResponsesResource(self)

    @cached_property
    def prompts(self) -> PromptsResource:
        from .resources.prompts import PromptsResource

        return PromptsResource(self)

    @cached_property
    def conversations(self) -> ConversationsResource:
        from .resources.conversations import ConversationsResource

        return ConversationsResource(self)

    @cached_property
    def inspect(self) -> InspectResource:
        from .resources.inspect import InspectResource

        return InspectResource(self)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        from .resources.embeddings import EmbeddingsResource

        return EmbeddingsResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def completions(self) -> CompletionsResource:
        from .resources.completions import CompletionsResource

        return CompletionsResource(self)

    @cached_property
    def vector_io(self) -> VectorIoResource:
        from .resources.vector_io import VectorIoResource

        return VectorIoResource(self)

    @cached_property
    def vector_stores(self) -> VectorStoresResource:
        from .resources.vector_stores import VectorStoresResource

        return VectorStoresResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def providers(self) -> ProvidersResource:
        from .resources.providers import ProvidersResource

        return ProvidersResource(self)

    @cached_property
    def routes(self) -> RoutesResource:
        from .resources.routes import RoutesResource

        return RoutesResource(self)

    @cached_property
    def moderations(self) -> ModerationsResource:
        from .resources.moderations import ModerationsResource

        return ModerationsResource(self)

    @cached_property
    def safety(self) -> SafetyResource:
        from .resources.safety import SafetyResource

        return SafetyResource(self)

    @cached_property
    def shields(self) -> ShieldsResource:
        from .resources.shields import ShieldsResource

        return ShieldsResource(self)

    @cached_property
    def scoring(self) -> ScoringResource:
        from .resources.scoring import ScoringResource

        return ScoringResource(self)

    @cached_property
    def scoring_functions(self) -> ScoringFunctionsResource:
        from .resources.scoring_functions import ScoringFunctionsResource

        return ScoringFunctionsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def batches(self) -> BatchesResource:
        from .resources.batches import BatchesResource

        return BatchesResource(self)

    @cached_property
    def alpha(self) -> AlphaResource:
        from .resources.alpha import AlphaResource

        return AlphaResource(self)

    @cached_property
    def beta(self) -> BetaResource:
        from .resources.beta import BetaResource

        return BetaResource(self)

    @cached_property
    def with_raw_response(self) -> LlamaStackClientWithRawResponse:
        return LlamaStackClientWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlamaStackClientWithStreamedResponse:
        return LlamaStackClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLlamaStackClient(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
        provider_data: Mapping[str, Any] | None = None,
    ) -> None:
        """Construct a new async AsyncLlamaStackClient client instance.

        This automatically infers the `api_key` argument from the `LLAMA_STACK_CLIENT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_STACK_CLIENT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://any-hosted-llama-stack.com"

        custom_headers = default_headers or {}
        custom_headers["X-LlamaStack-Client-Version"] = __version__
        if provider_data is not None:
            custom_headers["X-LlamaStack-Provider-Data"] = json.dumps(provider_data)

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=custom_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def toolgroups(self) -> AsyncToolgroupsResource:
        from .resources.toolgroups import AsyncToolgroupsResource

        return AsyncToolgroupsResource(self)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        from .resources.tools import AsyncToolsResource

        return AsyncToolsResource(self)

    @cached_property
    def tool_runtime(self) -> AsyncToolRuntimeResource:
        from .resources.tool_runtime import AsyncToolRuntimeResource

        return AsyncToolRuntimeResource(self)

    @cached_property
    def responses(self) -> AsyncResponsesResource:
        from .resources.responses import AsyncResponsesResource

        return AsyncResponsesResource(self)

    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        from .resources.prompts import AsyncPromptsResource

        return AsyncPromptsResource(self)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        from .resources.conversations import AsyncConversationsResource

        return AsyncConversationsResource(self)

    @cached_property
    def inspect(self) -> AsyncInspectResource:
        from .resources.inspect import AsyncInspectResource

        return AsyncInspectResource(self)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        from .resources.embeddings import AsyncEmbeddingsResource

        return AsyncEmbeddingsResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        from .resources.completions import AsyncCompletionsResource

        return AsyncCompletionsResource(self)

    @cached_property
    def vector_io(self) -> AsyncVectorIoResource:
        from .resources.vector_io import AsyncVectorIoResource

        return AsyncVectorIoResource(self)

    @cached_property
    def vector_stores(self) -> AsyncVectorStoresResource:
        from .resources.vector_stores import AsyncVectorStoresResource

        return AsyncVectorStoresResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def providers(self) -> AsyncProvidersResource:
        from .resources.providers import AsyncProvidersResource

        return AsyncProvidersResource(self)

    @cached_property
    def routes(self) -> AsyncRoutesResource:
        from .resources.routes import AsyncRoutesResource

        return AsyncRoutesResource(self)

    @cached_property
    def moderations(self) -> AsyncModerationsResource:
        from .resources.moderations import AsyncModerationsResource

        return AsyncModerationsResource(self)

    @cached_property
    def safety(self) -> AsyncSafetyResource:
        from .resources.safety import AsyncSafetyResource

        return AsyncSafetyResource(self)

    @cached_property
    def shields(self) -> AsyncShieldsResource:
        from .resources.shields import AsyncShieldsResource

        return AsyncShieldsResource(self)

    @cached_property
    def scoring(self) -> AsyncScoringResource:
        from .resources.scoring import AsyncScoringResource

        return AsyncScoringResource(self)

    @cached_property
    def scoring_functions(self) -> AsyncScoringFunctionsResource:
        from .resources.scoring_functions import AsyncScoringFunctionsResource

        return AsyncScoringFunctionsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def batches(self) -> AsyncBatchesResource:
        from .resources.batches import AsyncBatchesResource

        return AsyncBatchesResource(self)

    @cached_property
    def alpha(self) -> AsyncAlphaResource:
        from .resources.alpha import AsyncAlphaResource

        return AsyncAlphaResource(self)

    @cached_property
    def beta(self) -> AsyncBetaResource:
        from .resources.beta import AsyncBetaResource

        return AsyncBetaResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLlamaStackClientWithRawResponse:
        return AsyncLlamaStackClientWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlamaStackClientWithStreamedResponse:
        return AsyncLlamaStackClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LlamaStackClientWithRawResponse:
    _client: LlamaStackClient

    def __init__(self, client: LlamaStackClient) -> None:
        self._client = client

    @cached_property
    def toolgroups(self) -> toolgroups.ToolgroupsResourceWithRawResponse:
        from .resources.toolgroups import ToolgroupsResourceWithRawResponse

        return ToolgroupsResourceWithRawResponse(self._client.toolgroups)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        from .resources.tools import ToolsResourceWithRawResponse

        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def tool_runtime(self) -> tool_runtime.ToolRuntimeResourceWithRawResponse:
        from .resources.tool_runtime import ToolRuntimeResourceWithRawResponse

        return ToolRuntimeResourceWithRawResponse(self._client.tool_runtime)

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithRawResponse:
        from .resources.responses import ResponsesResourceWithRawResponse

        return ResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithRawResponse:
        from .resources.prompts import PromptsResourceWithRawResponse

        return PromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithRawResponse:
        from .resources.conversations import ConversationsResourceWithRawResponse

        return ConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.InspectResourceWithRawResponse:
        from .resources.inspect import InspectResourceWithRawResponse

        return InspectResourceWithRawResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithRawResponse:
        from .resources.embeddings import EmbeddingsResourceWithRawResponse

        return EmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithRawResponse:
        from .resources.completions import CompletionsResourceWithRawResponse

        return CompletionsResourceWithRawResponse(self._client.completions)

    @cached_property
    def vector_io(self) -> vector_io.VectorIoResourceWithRawResponse:
        from .resources.vector_io import VectorIoResourceWithRawResponse

        return VectorIoResourceWithRawResponse(self._client.vector_io)

    @cached_property
    def vector_stores(self) -> vector_stores.VectorStoresResourceWithRawResponse:
        from .resources.vector_stores import VectorStoresResourceWithRawResponse

        return VectorStoresResourceWithRawResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def providers(self) -> providers.ProvidersResourceWithRawResponse:
        from .resources.providers import ProvidersResourceWithRawResponse

        return ProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.RoutesResourceWithRawResponse:
        from .resources.routes import RoutesResourceWithRawResponse

        return RoutesResourceWithRawResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.ModerationsResourceWithRawResponse:
        from .resources.moderations import ModerationsResourceWithRawResponse

        return ModerationsResourceWithRawResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.SafetyResourceWithRawResponse:
        from .resources.safety import SafetyResourceWithRawResponse

        return SafetyResourceWithRawResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.ShieldsResourceWithRawResponse:
        from .resources.shields import ShieldsResourceWithRawResponse

        return ShieldsResourceWithRawResponse(self._client.shields)

    @cached_property
    def scoring(self) -> scoring.ScoringResourceWithRawResponse:
        from .resources.scoring import ScoringResourceWithRawResponse

        return ScoringResourceWithRawResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.ScoringFunctionsResourceWithRawResponse:
        from .resources.scoring_functions import ScoringFunctionsResourceWithRawResponse

        return ScoringFunctionsResourceWithRawResponse(self._client.scoring_functions)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.BatchesResourceWithRawResponse:
        from .resources.batches import BatchesResourceWithRawResponse

        return BatchesResourceWithRawResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AlphaResourceWithRawResponse:
        from .resources.alpha import AlphaResourceWithRawResponse

        return AlphaResourceWithRawResponse(self._client.alpha)

    @cached_property
    def beta(self) -> beta.BetaResourceWithRawResponse:
        from .resources.beta import BetaResourceWithRawResponse

        return BetaResourceWithRawResponse(self._client.beta)


class AsyncLlamaStackClientWithRawResponse:
    _client: AsyncLlamaStackClient

    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self._client = client

    @cached_property
    def toolgroups(self) -> toolgroups.AsyncToolgroupsResourceWithRawResponse:
        from .resources.toolgroups import AsyncToolgroupsResourceWithRawResponse

        return AsyncToolgroupsResourceWithRawResponse(self._client.toolgroups)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        from .resources.tools import AsyncToolsResourceWithRawResponse

        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def tool_runtime(self) -> tool_runtime.AsyncToolRuntimeResourceWithRawResponse:
        from .resources.tool_runtime import AsyncToolRuntimeResourceWithRawResponse

        return AsyncToolRuntimeResourceWithRawResponse(self._client.tool_runtime)

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithRawResponse:
        from .resources.responses import AsyncResponsesResourceWithRawResponse

        return AsyncResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithRawResponse:
        from .resources.prompts import AsyncPromptsResourceWithRawResponse

        return AsyncPromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithRawResponse:
        from .resources.conversations import AsyncConversationsResourceWithRawResponse

        return AsyncConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.AsyncInspectResourceWithRawResponse:
        from .resources.inspect import AsyncInspectResourceWithRawResponse

        return AsyncInspectResourceWithRawResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithRawResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithRawResponse

        return AsyncEmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithRawResponse:
        from .resources.completions import AsyncCompletionsResourceWithRawResponse

        return AsyncCompletionsResourceWithRawResponse(self._client.completions)

    @cached_property
    def vector_io(self) -> vector_io.AsyncVectorIoResourceWithRawResponse:
        from .resources.vector_io import AsyncVectorIoResourceWithRawResponse

        return AsyncVectorIoResourceWithRawResponse(self._client.vector_io)

    @cached_property
    def vector_stores(self) -> vector_stores.AsyncVectorStoresResourceWithRawResponse:
        from .resources.vector_stores import AsyncVectorStoresResourceWithRawResponse

        return AsyncVectorStoresResourceWithRawResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def providers(self) -> providers.AsyncProvidersResourceWithRawResponse:
        from .resources.providers import AsyncProvidersResourceWithRawResponse

        return AsyncProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.AsyncRoutesResourceWithRawResponse:
        from .resources.routes import AsyncRoutesResourceWithRawResponse

        return AsyncRoutesResourceWithRawResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.AsyncModerationsResourceWithRawResponse:
        from .resources.moderations import AsyncModerationsResourceWithRawResponse

        return AsyncModerationsResourceWithRawResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.AsyncSafetyResourceWithRawResponse:
        from .resources.safety import AsyncSafetyResourceWithRawResponse

        return AsyncSafetyResourceWithRawResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.AsyncShieldsResourceWithRawResponse:
        from .resources.shields import AsyncShieldsResourceWithRawResponse

        return AsyncShieldsResourceWithRawResponse(self._client.shields)

    @cached_property
    def scoring(self) -> scoring.AsyncScoringResourceWithRawResponse:
        from .resources.scoring import AsyncScoringResourceWithRawResponse

        return AsyncScoringResourceWithRawResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.AsyncScoringFunctionsResourceWithRawResponse:
        from .resources.scoring_functions import AsyncScoringFunctionsResourceWithRawResponse

        return AsyncScoringFunctionsResourceWithRawResponse(self._client.scoring_functions)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.AsyncBatchesResourceWithRawResponse:
        from .resources.batches import AsyncBatchesResourceWithRawResponse

        return AsyncBatchesResourceWithRawResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AsyncAlphaResourceWithRawResponse:
        from .resources.alpha import AsyncAlphaResourceWithRawResponse

        return AsyncAlphaResourceWithRawResponse(self._client.alpha)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithRawResponse:
        from .resources.beta import AsyncBetaResourceWithRawResponse

        return AsyncBetaResourceWithRawResponse(self._client.beta)


class LlamaStackClientWithStreamedResponse:
    _client: LlamaStackClient

    def __init__(self, client: LlamaStackClient) -> None:
        self._client = client

    @cached_property
    def toolgroups(self) -> toolgroups.ToolgroupsResourceWithStreamingResponse:
        from .resources.toolgroups import ToolgroupsResourceWithStreamingResponse

        return ToolgroupsResourceWithStreamingResponse(self._client.toolgroups)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        from .resources.tools import ToolsResourceWithStreamingResponse

        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def tool_runtime(self) -> tool_runtime.ToolRuntimeResourceWithStreamingResponse:
        from .resources.tool_runtime import ToolRuntimeResourceWithStreamingResponse

        return ToolRuntimeResourceWithStreamingResponse(self._client.tool_runtime)

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithStreamingResponse:
        from .resources.responses import ResponsesResourceWithStreamingResponse

        return ResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithStreamingResponse:
        from .resources.prompts import PromptsResourceWithStreamingResponse

        return PromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithStreamingResponse:
        from .resources.conversations import ConversationsResourceWithStreamingResponse

        return ConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.InspectResourceWithStreamingResponse:
        from .resources.inspect import InspectResourceWithStreamingResponse

        return InspectResourceWithStreamingResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import EmbeddingsResourceWithStreamingResponse

        return EmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithStreamingResponse:
        from .resources.completions import CompletionsResourceWithStreamingResponse

        return CompletionsResourceWithStreamingResponse(self._client.completions)

    @cached_property
    def vector_io(self) -> vector_io.VectorIoResourceWithStreamingResponse:
        from .resources.vector_io import VectorIoResourceWithStreamingResponse

        return VectorIoResourceWithStreamingResponse(self._client.vector_io)

    @cached_property
    def vector_stores(self) -> vector_stores.VectorStoresResourceWithStreamingResponse:
        from .resources.vector_stores import VectorStoresResourceWithStreamingResponse

        return VectorStoresResourceWithStreamingResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def providers(self) -> providers.ProvidersResourceWithStreamingResponse:
        from .resources.providers import ProvidersResourceWithStreamingResponse

        return ProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.RoutesResourceWithStreamingResponse:
        from .resources.routes import RoutesResourceWithStreamingResponse

        return RoutesResourceWithStreamingResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.ModerationsResourceWithStreamingResponse:
        from .resources.moderations import ModerationsResourceWithStreamingResponse

        return ModerationsResourceWithStreamingResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.SafetyResourceWithStreamingResponse:
        from .resources.safety import SafetyResourceWithStreamingResponse

        return SafetyResourceWithStreamingResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.ShieldsResourceWithStreamingResponse:
        from .resources.shields import ShieldsResourceWithStreamingResponse

        return ShieldsResourceWithStreamingResponse(self._client.shields)

    @cached_property
    def scoring(self) -> scoring.ScoringResourceWithStreamingResponse:
        from .resources.scoring import ScoringResourceWithStreamingResponse

        return ScoringResourceWithStreamingResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.ScoringFunctionsResourceWithStreamingResponse:
        from .resources.scoring_functions import ScoringFunctionsResourceWithStreamingResponse

        return ScoringFunctionsResourceWithStreamingResponse(self._client.scoring_functions)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.BatchesResourceWithStreamingResponse:
        from .resources.batches import BatchesResourceWithStreamingResponse

        return BatchesResourceWithStreamingResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AlphaResourceWithStreamingResponse:
        from .resources.alpha import AlphaResourceWithStreamingResponse

        return AlphaResourceWithStreamingResponse(self._client.alpha)

    @cached_property
    def beta(self) -> beta.BetaResourceWithStreamingResponse:
        from .resources.beta import BetaResourceWithStreamingResponse

        return BetaResourceWithStreamingResponse(self._client.beta)


class AsyncLlamaStackClientWithStreamedResponse:
    _client: AsyncLlamaStackClient

    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self._client = client

    @cached_property
    def toolgroups(self) -> toolgroups.AsyncToolgroupsResourceWithStreamingResponse:
        from .resources.toolgroups import AsyncToolgroupsResourceWithStreamingResponse

        return AsyncToolgroupsResourceWithStreamingResponse(self._client.toolgroups)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        from .resources.tools import AsyncToolsResourceWithStreamingResponse

        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def tool_runtime(self) -> tool_runtime.AsyncToolRuntimeResourceWithStreamingResponse:
        from .resources.tool_runtime import AsyncToolRuntimeResourceWithStreamingResponse

        return AsyncToolRuntimeResourceWithStreamingResponse(self._client.tool_runtime)

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithStreamingResponse:
        from .resources.responses import AsyncResponsesResourceWithStreamingResponse

        return AsyncResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithStreamingResponse:
        from .resources.prompts import AsyncPromptsResourceWithStreamingResponse

        return AsyncPromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithStreamingResponse:
        from .resources.conversations import AsyncConversationsResourceWithStreamingResponse

        return AsyncConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.AsyncInspectResourceWithStreamingResponse:
        from .resources.inspect import AsyncInspectResourceWithStreamingResponse

        return AsyncInspectResourceWithStreamingResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithStreamingResponse

        return AsyncEmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithStreamingResponse:
        from .resources.completions import AsyncCompletionsResourceWithStreamingResponse

        return AsyncCompletionsResourceWithStreamingResponse(self._client.completions)

    @cached_property
    def vector_io(self) -> vector_io.AsyncVectorIoResourceWithStreamingResponse:
        from .resources.vector_io import AsyncVectorIoResourceWithStreamingResponse

        return AsyncVectorIoResourceWithStreamingResponse(self._client.vector_io)

    @cached_property
    def vector_stores(self) -> vector_stores.AsyncVectorStoresResourceWithStreamingResponse:
        from .resources.vector_stores import AsyncVectorStoresResourceWithStreamingResponse

        return AsyncVectorStoresResourceWithStreamingResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def providers(self) -> providers.AsyncProvidersResourceWithStreamingResponse:
        from .resources.providers import AsyncProvidersResourceWithStreamingResponse

        return AsyncProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.AsyncRoutesResourceWithStreamingResponse:
        from .resources.routes import AsyncRoutesResourceWithStreamingResponse

        return AsyncRoutesResourceWithStreamingResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.AsyncModerationsResourceWithStreamingResponse:
        from .resources.moderations import AsyncModerationsResourceWithStreamingResponse

        return AsyncModerationsResourceWithStreamingResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.AsyncSafetyResourceWithStreamingResponse:
        from .resources.safety import AsyncSafetyResourceWithStreamingResponse

        return AsyncSafetyResourceWithStreamingResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.AsyncShieldsResourceWithStreamingResponse:
        from .resources.shields import AsyncShieldsResourceWithStreamingResponse

        return AsyncShieldsResourceWithStreamingResponse(self._client.shields)

    @cached_property
    def scoring(self) -> scoring.AsyncScoringResourceWithStreamingResponse:
        from .resources.scoring import AsyncScoringResourceWithStreamingResponse

        return AsyncScoringResourceWithStreamingResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.AsyncScoringFunctionsResourceWithStreamingResponse:
        from .resources.scoring_functions import AsyncScoringFunctionsResourceWithStreamingResponse

        return AsyncScoringFunctionsResourceWithStreamingResponse(self._client.scoring_functions)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.AsyncBatchesResourceWithStreamingResponse:
        from .resources.batches import AsyncBatchesResourceWithStreamingResponse

        return AsyncBatchesResourceWithStreamingResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AsyncAlphaResourceWithStreamingResponse:
        from .resources.alpha import AsyncAlphaResourceWithStreamingResponse

        return AsyncAlphaResourceWithStreamingResponse(self._client.alpha)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithStreamingResponse:
        from .resources.beta import AsyncBetaResourceWithStreamingResponse

        return AsyncBetaResourceWithStreamingResponse(self._client.beta)


Client = LlamaStackClient

AsyncClient = AsyncLlamaStackClient
