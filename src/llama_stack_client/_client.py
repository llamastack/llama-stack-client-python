# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
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
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
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
        chat,
        alpha,
        files,
        models,
        routes,
        safety,
        batches,
        inspect,
        prompts,
        shields,
        providers,
        responses,
        vector_io,
        embeddings,
        completions,
        moderations,
        conversations,
        vector_stores,
    )
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.routes import RoutesResource, AsyncRoutesResource
    from .resources.safety import SafetyResource, AsyncSafetyResource
    from .resources.batches import BatchesResource, AsyncBatchesResource
    from .resources.inspect import InspectResource, AsyncInspectResource
    from .resources.shields import ShieldsResource, AsyncShieldsResource
    from .resources.chat.chat import ChatResource, AsyncChatResource
    from .resources.providers import ProvidersResource, AsyncProvidersResource
    from .resources.vector_io import VectorIoResource, AsyncVectorIoResource
    from .resources.embeddings import EmbeddingsResource, AsyncEmbeddingsResource
    from .resources.alpha.alpha import AlphaResource, AsyncAlphaResource
    from .resources.completions import CompletionsResource, AsyncCompletionsResource
    from .resources.moderations import ModerationsResource, AsyncModerationsResource
    from .resources.models.models import ModelsResource, AsyncModelsResource
    from .resources.prompts.prompts import PromptsResource, AsyncPromptsResource
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

        custom_headers_env = os.environ.get("LLAMA_STACK_CLIENT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

    @cached_property
    def responses(self) -> ResponsesResource:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
        from .resources.responses import ResponsesResource

        return ResponsesResource(self)

    @cached_property
    def prompts(self) -> PromptsResource:
        """Protocol for prompt management operations."""
        from .resources.prompts import PromptsResource

        return PromptsResource(self)

    @cached_property
    def conversations(self) -> ConversationsResource:
        """Protocol for conversation management operations."""
        from .resources.conversations import ConversationsResource

        return ConversationsResource(self)

    @cached_property
    def inspect(self) -> InspectResource:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.inspect import InspectResource

        return InspectResource(self)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        from .resources.embeddings import EmbeddingsResource

        return EmbeddingsResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def completions(self) -> CompletionsResource:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
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
        """
        Providers API for inspecting, listing, and modifying providers and their configurations.
        """
        from .resources.providers import ProvidersResource

        return ProvidersResource(self)

    @cached_property
    def routes(self) -> RoutesResource:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.routes import RoutesResource

        return RoutesResource(self)

    @cached_property
    def moderations(self) -> ModerationsResource:
        """OpenAI-compatible Moderations API."""
        from .resources.moderations import ModerationsResource

        return ModerationsResource(self)

    @cached_property
    def safety(self) -> SafetyResource:
        """OpenAI-compatible Moderations API."""
        from .resources.safety import SafetyResource

        return SafetyResource(self)

    @cached_property
    def shields(self) -> ShieldsResource:
        from .resources.shields import ShieldsResource

        return ShieldsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        """
        This API is used to upload documents that can be used with other Llama Stack APIs.
        """
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def batches(self) -> BatchesResource:
        """
        The API is designed to allow use of openai client libraries for seamless integration.

        This API provides the following extensions:
         - idempotent batch creation

        Note: This API is currently under active development and may undergo changes.
        """
        from .resources.batches import BatchesResource

        return BatchesResource(self)

    @cached_property
    def alpha(self) -> AlphaResource:
        from .resources.alpha import AlphaResource

        return AlphaResource(self)

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

        custom_headers_env = os.environ.get("LLAMA_STACK_CLIENT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

    @cached_property
    def responses(self) -> AsyncResponsesResource:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
        from .resources.responses import AsyncResponsesResource

        return AsyncResponsesResource(self)

    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        """Protocol for prompt management operations."""
        from .resources.prompts import AsyncPromptsResource

        return AsyncPromptsResource(self)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        """Protocol for conversation management operations."""
        from .resources.conversations import AsyncConversationsResource

        return AsyncConversationsResource(self)

    @cached_property
    def inspect(self) -> AsyncInspectResource:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.inspect import AsyncInspectResource

        return AsyncInspectResource(self)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        from .resources.embeddings import AsyncEmbeddingsResource

        return AsyncEmbeddingsResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
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
        """
        Providers API for inspecting, listing, and modifying providers and their configurations.
        """
        from .resources.providers import AsyncProvidersResource

        return AsyncProvidersResource(self)

    @cached_property
    def routes(self) -> AsyncRoutesResource:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.routes import AsyncRoutesResource

        return AsyncRoutesResource(self)

    @cached_property
    def moderations(self) -> AsyncModerationsResource:
        """OpenAI-compatible Moderations API."""
        from .resources.moderations import AsyncModerationsResource

        return AsyncModerationsResource(self)

    @cached_property
    def safety(self) -> AsyncSafetyResource:
        """OpenAI-compatible Moderations API."""
        from .resources.safety import AsyncSafetyResource

        return AsyncSafetyResource(self)

    @cached_property
    def shields(self) -> AsyncShieldsResource:
        from .resources.shields import AsyncShieldsResource

        return AsyncShieldsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        """
        This API is used to upload documents that can be used with other Llama Stack APIs.
        """
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def batches(self) -> AsyncBatchesResource:
        """
        The API is designed to allow use of openai client libraries for seamless integration.

        This API provides the following extensions:
         - idempotent batch creation

        Note: This API is currently under active development and may undergo changes.
        """
        from .resources.batches import AsyncBatchesResource

        return AsyncBatchesResource(self)

    @cached_property
    def alpha(self) -> AsyncAlphaResource:
        from .resources.alpha import AsyncAlphaResource

        return AsyncAlphaResource(self)

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
    def responses(self) -> responses.ResponsesResourceWithRawResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
        from .resources.responses import ResponsesResourceWithRawResponse

        return ResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithRawResponse:
        """Protocol for prompt management operations."""
        from .resources.prompts import PromptsResourceWithRawResponse

        return PromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithRawResponse:
        """Protocol for conversation management operations."""
        from .resources.conversations import ConversationsResourceWithRawResponse

        return ConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.InspectResourceWithRawResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.inspect import InspectResourceWithRawResponse

        return InspectResourceWithRawResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithRawResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        from .resources.embeddings import EmbeddingsResourceWithRawResponse

        return EmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithRawResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
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
        """
        Providers API for inspecting, listing, and modifying providers and their configurations.
        """
        from .resources.providers import ProvidersResourceWithRawResponse

        return ProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.RoutesResourceWithRawResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.routes import RoutesResourceWithRawResponse

        return RoutesResourceWithRawResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.ModerationsResourceWithRawResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.moderations import ModerationsResourceWithRawResponse

        return ModerationsResourceWithRawResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.SafetyResourceWithRawResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.safety import SafetyResourceWithRawResponse

        return SafetyResourceWithRawResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.ShieldsResourceWithRawResponse:
        from .resources.shields import ShieldsResourceWithRawResponse

        return ShieldsResourceWithRawResponse(self._client.shields)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        """
        This API is used to upload documents that can be used with other Llama Stack APIs.
        """
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.BatchesResourceWithRawResponse:
        """
        The API is designed to allow use of openai client libraries for seamless integration.

        This API provides the following extensions:
         - idempotent batch creation

        Note: This API is currently under active development and may undergo changes.
        """
        from .resources.batches import BatchesResourceWithRawResponse

        return BatchesResourceWithRawResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AlphaResourceWithRawResponse:
        from .resources.alpha import AlphaResourceWithRawResponse

        return AlphaResourceWithRawResponse(self._client.alpha)


class AsyncLlamaStackClientWithRawResponse:
    _client: AsyncLlamaStackClient

    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self._client = client

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithRawResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
        from .resources.responses import AsyncResponsesResourceWithRawResponse

        return AsyncResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithRawResponse:
        """Protocol for prompt management operations."""
        from .resources.prompts import AsyncPromptsResourceWithRawResponse

        return AsyncPromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithRawResponse:
        """Protocol for conversation management operations."""
        from .resources.conversations import AsyncConversationsResourceWithRawResponse

        return AsyncConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.AsyncInspectResourceWithRawResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.inspect import AsyncInspectResourceWithRawResponse

        return AsyncInspectResourceWithRawResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithRawResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        from .resources.embeddings import AsyncEmbeddingsResourceWithRawResponse

        return AsyncEmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithRawResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
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
        """
        Providers API for inspecting, listing, and modifying providers and their configurations.
        """
        from .resources.providers import AsyncProvidersResourceWithRawResponse

        return AsyncProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.AsyncRoutesResourceWithRawResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.routes import AsyncRoutesResourceWithRawResponse

        return AsyncRoutesResourceWithRawResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.AsyncModerationsResourceWithRawResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.moderations import AsyncModerationsResourceWithRawResponse

        return AsyncModerationsResourceWithRawResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.AsyncSafetyResourceWithRawResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.safety import AsyncSafetyResourceWithRawResponse

        return AsyncSafetyResourceWithRawResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.AsyncShieldsResourceWithRawResponse:
        from .resources.shields import AsyncShieldsResourceWithRawResponse

        return AsyncShieldsResourceWithRawResponse(self._client.shields)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        """
        This API is used to upload documents that can be used with other Llama Stack APIs.
        """
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.AsyncBatchesResourceWithRawResponse:
        """
        The API is designed to allow use of openai client libraries for seamless integration.

        This API provides the following extensions:
         - idempotent batch creation

        Note: This API is currently under active development and may undergo changes.
        """
        from .resources.batches import AsyncBatchesResourceWithRawResponse

        return AsyncBatchesResourceWithRawResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AsyncAlphaResourceWithRawResponse:
        from .resources.alpha import AsyncAlphaResourceWithRawResponse

        return AsyncAlphaResourceWithRawResponse(self._client.alpha)


class LlamaStackClientWithStreamedResponse:
    _client: LlamaStackClient

    def __init__(self, client: LlamaStackClient) -> None:
        self._client = client

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithStreamingResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
        from .resources.responses import ResponsesResourceWithStreamingResponse

        return ResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithStreamingResponse:
        """Protocol for prompt management operations."""
        from .resources.prompts import PromptsResourceWithStreamingResponse

        return PromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithStreamingResponse:
        """Protocol for conversation management operations."""
        from .resources.conversations import ConversationsResourceWithStreamingResponse

        return ConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.InspectResourceWithStreamingResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.inspect import InspectResourceWithStreamingResponse

        return InspectResourceWithStreamingResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithStreamingResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        from .resources.embeddings import EmbeddingsResourceWithStreamingResponse

        return EmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithStreamingResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
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
        """
        Providers API for inspecting, listing, and modifying providers and their configurations.
        """
        from .resources.providers import ProvidersResourceWithStreamingResponse

        return ProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.RoutesResourceWithStreamingResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.routes import RoutesResourceWithStreamingResponse

        return RoutesResourceWithStreamingResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.ModerationsResourceWithStreamingResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.moderations import ModerationsResourceWithStreamingResponse

        return ModerationsResourceWithStreamingResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.SafetyResourceWithStreamingResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.safety import SafetyResourceWithStreamingResponse

        return SafetyResourceWithStreamingResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.ShieldsResourceWithStreamingResponse:
        from .resources.shields import ShieldsResourceWithStreamingResponse

        return ShieldsResourceWithStreamingResponse(self._client.shields)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        """
        This API is used to upload documents that can be used with other Llama Stack APIs.
        """
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.BatchesResourceWithStreamingResponse:
        """
        The API is designed to allow use of openai client libraries for seamless integration.

        This API provides the following extensions:
         - idempotent batch creation

        Note: This API is currently under active development and may undergo changes.
        """
        from .resources.batches import BatchesResourceWithStreamingResponse

        return BatchesResourceWithStreamingResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AlphaResourceWithStreamingResponse:
        from .resources.alpha import AlphaResourceWithStreamingResponse

        return AlphaResourceWithStreamingResponse(self._client.alpha)


class AsyncLlamaStackClientWithStreamedResponse:
    _client: AsyncLlamaStackClient

    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self._client = client

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithStreamingResponse:
        """
        OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
        """
        from .resources.responses import AsyncResponsesResourceWithStreamingResponse

        return AsyncResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithStreamingResponse:
        """Protocol for prompt management operations."""
        from .resources.prompts import AsyncPromptsResourceWithStreamingResponse

        return AsyncPromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithStreamingResponse:
        """Protocol for conversation management operations."""
        from .resources.conversations import AsyncConversationsResourceWithStreamingResponse

        return AsyncConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def inspect(self) -> inspect.AsyncInspectResourceWithStreamingResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.inspect import AsyncInspectResourceWithStreamingResponse

        return AsyncInspectResourceWithStreamingResponse(self._client.inspect)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithStreamingResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
        from .resources.embeddings import AsyncEmbeddingsResourceWithStreamingResponse

        return AsyncEmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithStreamingResponse:
        """
        Llama Stack Inference API for generating completions, chat completions, and embeddings.

        This API provides the raw interface to the underlying models. Three kinds of models are supported:
        - LLM models: these models generate "raw" and "chat" (conversational) completions.
        - Embedding models: these models generate embeddings to be used for semantic search.
        - Rerank models: these models reorder the documents based on their relevance to a query.
        """
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
        """
        Providers API for inspecting, listing, and modifying providers and their configurations.
        """
        from .resources.providers import AsyncProvidersResourceWithStreamingResponse

        return AsyncProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def routes(self) -> routes.AsyncRoutesResourceWithStreamingResponse:
        """
        APIs for inspecting the Llama Stack service, including health status, available API routes with methods and implementing providers.
        """
        from .resources.routes import AsyncRoutesResourceWithStreamingResponse

        return AsyncRoutesResourceWithStreamingResponse(self._client.routes)

    @cached_property
    def moderations(self) -> moderations.AsyncModerationsResourceWithStreamingResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.moderations import AsyncModerationsResourceWithStreamingResponse

        return AsyncModerationsResourceWithStreamingResponse(self._client.moderations)

    @cached_property
    def safety(self) -> safety.AsyncSafetyResourceWithStreamingResponse:
        """OpenAI-compatible Moderations API."""
        from .resources.safety import AsyncSafetyResourceWithStreamingResponse

        return AsyncSafetyResourceWithStreamingResponse(self._client.safety)

    @cached_property
    def shields(self) -> shields.AsyncShieldsResourceWithStreamingResponse:
        from .resources.shields import AsyncShieldsResourceWithStreamingResponse

        return AsyncShieldsResourceWithStreamingResponse(self._client.shields)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        """
        This API is used to upload documents that can be used with other Llama Stack APIs.
        """
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def batches(self) -> batches.AsyncBatchesResourceWithStreamingResponse:
        """
        The API is designed to allow use of openai client libraries for seamless integration.

        This API provides the following extensions:
         - idempotent batch creation

        Note: This API is currently under active development and may undergo changes.
        """
        from .resources.batches import AsyncBatchesResourceWithStreamingResponse

        return AsyncBatchesResourceWithStreamingResponse(self._client.batches)

    @cached_property
    def alpha(self) -> alpha.AsyncAlphaResourceWithStreamingResponse:
        from .resources.alpha import AsyncAlphaResourceWithStreamingResponse

        return AsyncAlphaResourceWithStreamingResponse(self._client.alpha)


Client = LlamaStackClient

AsyncClient = AsyncLlamaStackClient
