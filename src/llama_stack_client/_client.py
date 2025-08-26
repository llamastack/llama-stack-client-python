# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import json
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
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
        chat,
        eval,
        files,
        tools,
        agents,
        models,
        routes,
        safety,
        inspect,
        scoring,
        shields,
        datasets,
        inference,
        providers,
        responses,
        telemetry,
        vector_io,
        benchmarks,
        embeddings,
        toolgroups,
        vector_dbs,
        completions,
        moderations,
        tool_runtime,
        post_training,
        vector_stores,
        scoring_functions,
        synthetic_data_generation,
    )
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.tools import ToolsResource, AsyncToolsResource
    from .resources.models import ModelsResource, AsyncModelsResource
    from .resources.routes import RoutesResource, AsyncRoutesResource
    from .resources.safety import SafetyResource, AsyncSafetyResource
    from .resources.inspect import InspectResource, AsyncInspectResource
    from .resources.scoring import ScoringResource, AsyncScoringResource
    from .resources.shields import ShieldsResource, AsyncShieldsResource
    from .resources.datasets import DatasetsResource, AsyncDatasetsResource
    from .resources.chat.chat import ChatResource, AsyncChatResource
    from .resources.eval.eval import EvalResource, AsyncEvalResource
    from .resources.inference import InferenceResource, AsyncInferenceResource
    from .resources.providers import ProvidersResource, AsyncProvidersResource
    from .resources.telemetry import TelemetryResource, AsyncTelemetryResource
    from .resources.vector_io import VectorIoResource, AsyncVectorIoResource
    from .resources.benchmarks import BenchmarksResource, AsyncBenchmarksResource
    from .resources.embeddings import EmbeddingsResource, AsyncEmbeddingsResource
    from .resources.toolgroups import ToolgroupsResource, AsyncToolgroupsResource
    from .resources.vector_dbs import VectorDBsResource, AsyncVectorDBsResource
    from .resources.completions import CompletionsResource, AsyncCompletionsResource
    from .resources.moderations import ModerationsResource, AsyncModerationsResource
    from .resources.agents.agents import AgentsResource, AsyncAgentsResource
    from .resources.scoring_functions import ScoringFunctionsResource, AsyncScoringFunctionsResource
    from .resources.responses.responses import ResponsesResource, AsyncResponsesResource
    from .resources.synthetic_data_generation import (
        SyntheticDataGenerationResource,
        AsyncSyntheticDataGenerationResource,
    )
    from .resources.tool_runtime.tool_runtime import ToolRuntimeResource, AsyncToolRuntimeResource
    from .resources.post_training.post_training import PostTrainingResource, AsyncPostTrainingResource
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
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def datasets(self) -> DatasetsResource:
        from .resources.datasets import DatasetsResource

        return DatasetsResource(self)

    @cached_property
    def eval(self) -> EvalResource:
        from .resources.eval import EvalResource

        return EvalResource(self)

    @cached_property
    def inspect(self) -> InspectResource:
        from .resources.inspect import InspectResource

        return InspectResource(self)

    @cached_property
    def inference(self) -> InferenceResource:
        from .resources.inference import InferenceResource

        return InferenceResource(self)

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
    def vector_dbs(self) -> VectorDBsResource:
        from .resources.vector_dbs import VectorDBsResource

        return VectorDBsResource(self)

    @cached_property
    def vector_stores(self) -> VectorStoresResource:
        from .resources.vector_stores import VectorStoresResource

        return VectorStoresResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def post_training(self) -> PostTrainingResource:
        from .resources.post_training import PostTrainingResource

        return PostTrainingResource(self)

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
    def synthetic_data_generation(self) -> SyntheticDataGenerationResource:
        from .resources.synthetic_data_generation import SyntheticDataGenerationResource

        return SyntheticDataGenerationResource(self)

    @cached_property
    def telemetry(self) -> TelemetryResource:
        from .resources.telemetry import TelemetryResource

        return TelemetryResource(self)

    @cached_property
    def scoring(self) -> ScoringResource:
        from .resources.scoring import ScoringResource

        return ScoringResource(self)

    @cached_property
    def scoring_functions(self) -> ScoringFunctionsResource:
        from .resources.scoring_functions import ScoringFunctionsResource

        return ScoringFunctionsResource(self)

    @cached_property
    def benchmarks(self) -> BenchmarksResource:
        from .resources.benchmarks import BenchmarksResource

        return BenchmarksResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        from .resources.datasets import AsyncDatasetsResource

        return AsyncDatasetsResource(self)

    @cached_property
    def eval(self) -> AsyncEvalResource:
        from .resources.eval import AsyncEvalResource

        return AsyncEvalResource(self)

    @cached_property
    def inspect(self) -> AsyncInspectResource:
        from .resources.inspect import AsyncInspectResource

        return AsyncInspectResource(self)

    @cached_property
    def inference(self) -> AsyncInferenceResource:
        from .resources.inference import AsyncInferenceResource

        return AsyncInferenceResource(self)

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
    def vector_dbs(self) -> AsyncVectorDBsResource:
        from .resources.vector_dbs import AsyncVectorDBsResource

        return AsyncVectorDBsResource(self)

    @cached_property
    def vector_stores(self) -> AsyncVectorStoresResource:
        from .resources.vector_stores import AsyncVectorStoresResource

        return AsyncVectorStoresResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def post_training(self) -> AsyncPostTrainingResource:
        from .resources.post_training import AsyncPostTrainingResource

        return AsyncPostTrainingResource(self)

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
    def synthetic_data_generation(self) -> AsyncSyntheticDataGenerationResource:
        from .resources.synthetic_data_generation import AsyncSyntheticDataGenerationResource

        return AsyncSyntheticDataGenerationResource(self)

    @cached_property
    def telemetry(self) -> AsyncTelemetryResource:
        from .resources.telemetry import AsyncTelemetryResource

        return AsyncTelemetryResource(self)

    @cached_property
    def scoring(self) -> AsyncScoringResource:
        from .resources.scoring import AsyncScoringResource

        return AsyncScoringResource(self)

    @cached_property
    def scoring_functions(self) -> AsyncScoringFunctionsResource:
        from .resources.scoring_functions import AsyncScoringFunctionsResource

        return AsyncScoringFunctionsResource(self)

    @cached_property
    def benchmarks(self) -> AsyncBenchmarksResource:
        from .resources.benchmarks import AsyncBenchmarksResource

        return AsyncBenchmarksResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithRawResponse:
        from .resources.datasets import DatasetsResourceWithRawResponse

        return DatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def eval(self) -> eval.EvalResourceWithRawResponse:
        from .resources.eval import EvalResourceWithRawResponse

        return EvalResourceWithRawResponse(self._client.eval)

    @cached_property
    def inspect(self) -> inspect.InspectResourceWithRawResponse:
        from .resources.inspect import InspectResourceWithRawResponse

        return InspectResourceWithRawResponse(self._client.inspect)

    @cached_property
    def inference(self) -> inference.InferenceResourceWithRawResponse:
        from .resources.inference import InferenceResourceWithRawResponse

        return InferenceResourceWithRawResponse(self._client.inference)

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
    def vector_dbs(self) -> vector_dbs.VectorDBsResourceWithRawResponse:
        from .resources.vector_dbs import VectorDBsResourceWithRawResponse

        return VectorDBsResourceWithRawResponse(self._client.vector_dbs)

    @cached_property
    def vector_stores(self) -> vector_stores.VectorStoresResourceWithRawResponse:
        from .resources.vector_stores import VectorStoresResourceWithRawResponse

        return VectorStoresResourceWithRawResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def post_training(self) -> post_training.PostTrainingResourceWithRawResponse:
        from .resources.post_training import PostTrainingResourceWithRawResponse

        return PostTrainingResourceWithRawResponse(self._client.post_training)

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
    def synthetic_data_generation(self) -> synthetic_data_generation.SyntheticDataGenerationResourceWithRawResponse:
        from .resources.synthetic_data_generation import SyntheticDataGenerationResourceWithRawResponse

        return SyntheticDataGenerationResourceWithRawResponse(self._client.synthetic_data_generation)

    @cached_property
    def telemetry(self) -> telemetry.TelemetryResourceWithRawResponse:
        from .resources.telemetry import TelemetryResourceWithRawResponse

        return TelemetryResourceWithRawResponse(self._client.telemetry)

    @cached_property
    def scoring(self) -> scoring.ScoringResourceWithRawResponse:
        from .resources.scoring import ScoringResourceWithRawResponse

        return ScoringResourceWithRawResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.ScoringFunctionsResourceWithRawResponse:
        from .resources.scoring_functions import ScoringFunctionsResourceWithRawResponse

        return ScoringFunctionsResourceWithRawResponse(self._client.scoring_functions)

    @cached_property
    def benchmarks(self) -> benchmarks.BenchmarksResourceWithRawResponse:
        from .resources.benchmarks import BenchmarksResourceWithRawResponse

        return BenchmarksResourceWithRawResponse(self._client.benchmarks)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)


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
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithRawResponse:
        from .resources.datasets import AsyncDatasetsResourceWithRawResponse

        return AsyncDatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def eval(self) -> eval.AsyncEvalResourceWithRawResponse:
        from .resources.eval import AsyncEvalResourceWithRawResponse

        return AsyncEvalResourceWithRawResponse(self._client.eval)

    @cached_property
    def inspect(self) -> inspect.AsyncInspectResourceWithRawResponse:
        from .resources.inspect import AsyncInspectResourceWithRawResponse

        return AsyncInspectResourceWithRawResponse(self._client.inspect)

    @cached_property
    def inference(self) -> inference.AsyncInferenceResourceWithRawResponse:
        from .resources.inference import AsyncInferenceResourceWithRawResponse

        return AsyncInferenceResourceWithRawResponse(self._client.inference)

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
    def vector_dbs(self) -> vector_dbs.AsyncVectorDBsResourceWithRawResponse:
        from .resources.vector_dbs import AsyncVectorDBsResourceWithRawResponse

        return AsyncVectorDBsResourceWithRawResponse(self._client.vector_dbs)

    @cached_property
    def vector_stores(self) -> vector_stores.AsyncVectorStoresResourceWithRawResponse:
        from .resources.vector_stores import AsyncVectorStoresResourceWithRawResponse

        return AsyncVectorStoresResourceWithRawResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def post_training(self) -> post_training.AsyncPostTrainingResourceWithRawResponse:
        from .resources.post_training import AsyncPostTrainingResourceWithRawResponse

        return AsyncPostTrainingResourceWithRawResponse(self._client.post_training)

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
    def synthetic_data_generation(
        self,
    ) -> synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithRawResponse:
        from .resources.synthetic_data_generation import AsyncSyntheticDataGenerationResourceWithRawResponse

        return AsyncSyntheticDataGenerationResourceWithRawResponse(self._client.synthetic_data_generation)

    @cached_property
    def telemetry(self) -> telemetry.AsyncTelemetryResourceWithRawResponse:
        from .resources.telemetry import AsyncTelemetryResourceWithRawResponse

        return AsyncTelemetryResourceWithRawResponse(self._client.telemetry)

    @cached_property
    def scoring(self) -> scoring.AsyncScoringResourceWithRawResponse:
        from .resources.scoring import AsyncScoringResourceWithRawResponse

        return AsyncScoringResourceWithRawResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.AsyncScoringFunctionsResourceWithRawResponse:
        from .resources.scoring_functions import AsyncScoringFunctionsResourceWithRawResponse

        return AsyncScoringFunctionsResourceWithRawResponse(self._client.scoring_functions)

    @cached_property
    def benchmarks(self) -> benchmarks.AsyncBenchmarksResourceWithRawResponse:
        from .resources.benchmarks import AsyncBenchmarksResourceWithRawResponse

        return AsyncBenchmarksResourceWithRawResponse(self._client.benchmarks)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)


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
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithStreamingResponse:
        from .resources.datasets import DatasetsResourceWithStreamingResponse

        return DatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def eval(self) -> eval.EvalResourceWithStreamingResponse:
        from .resources.eval import EvalResourceWithStreamingResponse

        return EvalResourceWithStreamingResponse(self._client.eval)

    @cached_property
    def inspect(self) -> inspect.InspectResourceWithStreamingResponse:
        from .resources.inspect import InspectResourceWithStreamingResponse

        return InspectResourceWithStreamingResponse(self._client.inspect)

    @cached_property
    def inference(self) -> inference.InferenceResourceWithStreamingResponse:
        from .resources.inference import InferenceResourceWithStreamingResponse

        return InferenceResourceWithStreamingResponse(self._client.inference)

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
    def vector_dbs(self) -> vector_dbs.VectorDBsResourceWithStreamingResponse:
        from .resources.vector_dbs import VectorDBsResourceWithStreamingResponse

        return VectorDBsResourceWithStreamingResponse(self._client.vector_dbs)

    @cached_property
    def vector_stores(self) -> vector_stores.VectorStoresResourceWithStreamingResponse:
        from .resources.vector_stores import VectorStoresResourceWithStreamingResponse

        return VectorStoresResourceWithStreamingResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def post_training(self) -> post_training.PostTrainingResourceWithStreamingResponse:
        from .resources.post_training import PostTrainingResourceWithStreamingResponse

        return PostTrainingResourceWithStreamingResponse(self._client.post_training)

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
    def synthetic_data_generation(
        self,
    ) -> synthetic_data_generation.SyntheticDataGenerationResourceWithStreamingResponse:
        from .resources.synthetic_data_generation import SyntheticDataGenerationResourceWithStreamingResponse

        return SyntheticDataGenerationResourceWithStreamingResponse(self._client.synthetic_data_generation)

    @cached_property
    def telemetry(self) -> telemetry.TelemetryResourceWithStreamingResponse:
        from .resources.telemetry import TelemetryResourceWithStreamingResponse

        return TelemetryResourceWithStreamingResponse(self._client.telemetry)

    @cached_property
    def scoring(self) -> scoring.ScoringResourceWithStreamingResponse:
        from .resources.scoring import ScoringResourceWithStreamingResponse

        return ScoringResourceWithStreamingResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.ScoringFunctionsResourceWithStreamingResponse:
        from .resources.scoring_functions import ScoringFunctionsResourceWithStreamingResponse

        return ScoringFunctionsResourceWithStreamingResponse(self._client.scoring_functions)

    @cached_property
    def benchmarks(self) -> benchmarks.BenchmarksResourceWithStreamingResponse:
        from .resources.benchmarks import BenchmarksResourceWithStreamingResponse

        return BenchmarksResourceWithStreamingResponse(self._client.benchmarks)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)


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
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithStreamingResponse:
        from .resources.datasets import AsyncDatasetsResourceWithStreamingResponse

        return AsyncDatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def eval(self) -> eval.AsyncEvalResourceWithStreamingResponse:
        from .resources.eval import AsyncEvalResourceWithStreamingResponse

        return AsyncEvalResourceWithStreamingResponse(self._client.eval)

    @cached_property
    def inspect(self) -> inspect.AsyncInspectResourceWithStreamingResponse:
        from .resources.inspect import AsyncInspectResourceWithStreamingResponse

        return AsyncInspectResourceWithStreamingResponse(self._client.inspect)

    @cached_property
    def inference(self) -> inference.AsyncInferenceResourceWithStreamingResponse:
        from .resources.inference import AsyncInferenceResourceWithStreamingResponse

        return AsyncInferenceResourceWithStreamingResponse(self._client.inference)

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
    def vector_dbs(self) -> vector_dbs.AsyncVectorDBsResourceWithStreamingResponse:
        from .resources.vector_dbs import AsyncVectorDBsResourceWithStreamingResponse

        return AsyncVectorDBsResourceWithStreamingResponse(self._client.vector_dbs)

    @cached_property
    def vector_stores(self) -> vector_stores.AsyncVectorStoresResourceWithStreamingResponse:
        from .resources.vector_stores import AsyncVectorStoresResourceWithStreamingResponse

        return AsyncVectorStoresResourceWithStreamingResponse(self._client.vector_stores)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def post_training(self) -> post_training.AsyncPostTrainingResourceWithStreamingResponse:
        from .resources.post_training import AsyncPostTrainingResourceWithStreamingResponse

        return AsyncPostTrainingResourceWithStreamingResponse(self._client.post_training)

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
    def synthetic_data_generation(
        self,
    ) -> synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithStreamingResponse:
        from .resources.synthetic_data_generation import AsyncSyntheticDataGenerationResourceWithStreamingResponse

        return AsyncSyntheticDataGenerationResourceWithStreamingResponse(self._client.synthetic_data_generation)

    @cached_property
    def telemetry(self) -> telemetry.AsyncTelemetryResourceWithStreamingResponse:
        from .resources.telemetry import AsyncTelemetryResourceWithStreamingResponse

        return AsyncTelemetryResourceWithStreamingResponse(self._client.telemetry)

    @cached_property
    def scoring(self) -> scoring.AsyncScoringResourceWithStreamingResponse:
        from .resources.scoring import AsyncScoringResourceWithStreamingResponse

        return AsyncScoringResourceWithStreamingResponse(self._client.scoring)

    @cached_property
    def scoring_functions(self) -> scoring_functions.AsyncScoringFunctionsResourceWithStreamingResponse:
        from .resources.scoring_functions import AsyncScoringFunctionsResourceWithStreamingResponse

        return AsyncScoringFunctionsResourceWithStreamingResponse(self._client.scoring_functions)

    @cached_property
    def benchmarks(self) -> benchmarks.AsyncBenchmarksResourceWithStreamingResponse:
        from .resources.benchmarks import AsyncBenchmarksResourceWithStreamingResponse

        return AsyncBenchmarksResourceWithStreamingResponse(self._client.benchmarks)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)


Client = LlamaStackClient

AsyncClient = AsyncLlamaStackClient
