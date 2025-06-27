# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import json

import os
from typing import Any, Union, Mapping
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
from ._version import __version__
from .resources import (
    files,
    tools,
    models,
    routes,
    safety,
    inspect,
    scoring,
    shields,
    datasets,
    inference,
    providers,
    telemetry,
    vector_io,
    benchmarks,
    embeddings,
    toolgroups,
    vector_dbs,
    completions,
    scoring_functions,
    synthetic_data_generation,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.chat import chat
from .resources.eval import eval
from .resources.agents import agents
from .resources.responses import responses
from .resources.tool_runtime import tool_runtime
from .resources.post_training import post_training
from .resources.vector_stores import vector_stores

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
    toolgroups: toolgroups.ToolgroupsResource
    tools: tools.ToolsResource
    tool_runtime: tool_runtime.ToolRuntimeResource
    responses: responses.ResponsesResource
    agents: agents.AgentsResource
    datasets: datasets.DatasetsResource
    eval: eval.EvalResource
    inspect: inspect.InspectResource
    inference: inference.InferenceResource
    embeddings: embeddings.EmbeddingsResource
    chat: chat.ChatResource
    completions: completions.CompletionsResource
    vector_io: vector_io.VectorIoResource
    vector_dbs: vector_dbs.VectorDBsResource
    vector_stores: vector_stores.VectorStoresResource
    models: models.ModelsResource
    post_training: post_training.PostTrainingResource
    providers: providers.ProvidersResource
    routes: routes.RoutesResource
    safety: safety.SafetyResource
    shields: shields.ShieldsResource
    synthetic_data_generation: synthetic_data_generation.SyntheticDataGenerationResource
    telemetry: telemetry.TelemetryResource
    scoring: scoring.ScoringResource
    scoring_functions: scoring_functions.ScoringFunctionsResource
    benchmarks: benchmarks.BenchmarksResource
    files: files.FilesResource
    with_raw_response: LlamaStackClientWithRawResponse
    with_streaming_response: LlamaStackClientWithStreamedResponse

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

        This automatically infers the `api_key` argument from the `LLAMA_STACK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_STACK_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_BASE_URL")
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

        self.toolgroups = toolgroups.ToolgroupsResource(self)
        self.tools = tools.ToolsResource(self)
        self.tool_runtime = tool_runtime.ToolRuntimeResource(self)
        self.responses = responses.ResponsesResource(self)
        self.agents = agents.AgentsResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.eval = eval.EvalResource(self)
        self.inspect = inspect.InspectResource(self)
        self.inference = inference.InferenceResource(self)
        self.embeddings = embeddings.EmbeddingsResource(self)
        self.chat = chat.ChatResource(self)
        self.completions = completions.CompletionsResource(self)
        self.vector_io = vector_io.VectorIoResource(self)
        self.vector_dbs = vector_dbs.VectorDBsResource(self)
        self.vector_stores = vector_stores.VectorStoresResource(self)
        self.models = models.ModelsResource(self)
        self.post_training = post_training.PostTrainingResource(self)
        self.providers = providers.ProvidersResource(self)
        self.routes = routes.RoutesResource(self)
        self.safety = safety.SafetyResource(self)
        self.shields = shields.ShieldsResource(self)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResource(self)
        self.telemetry = telemetry.TelemetryResource(self)
        self.scoring = scoring.ScoringResource(self)
        self.scoring_functions = scoring_functions.ScoringFunctionsResource(self)
        self.benchmarks = benchmarks.BenchmarksResource(self)
        self.files = files.FilesResource(self)
        self.with_raw_response = LlamaStackClientWithRawResponse(self)
        self.with_streaming_response = LlamaStackClientWithStreamedResponse(self)

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
    toolgroups: toolgroups.AsyncToolgroupsResource
    tools: tools.AsyncToolsResource
    tool_runtime: tool_runtime.AsyncToolRuntimeResource
    responses: responses.AsyncResponsesResource
    agents: agents.AsyncAgentsResource
    datasets: datasets.AsyncDatasetsResource
    eval: eval.AsyncEvalResource
    inspect: inspect.AsyncInspectResource
    inference: inference.AsyncInferenceResource
    embeddings: embeddings.AsyncEmbeddingsResource
    chat: chat.AsyncChatResource
    completions: completions.AsyncCompletionsResource
    vector_io: vector_io.AsyncVectorIoResource
    vector_dbs: vector_dbs.AsyncVectorDBsResource
    vector_stores: vector_stores.AsyncVectorStoresResource
    models: models.AsyncModelsResource
    post_training: post_training.AsyncPostTrainingResource
    providers: providers.AsyncProvidersResource
    routes: routes.AsyncRoutesResource
    safety: safety.AsyncSafetyResource
    shields: shields.AsyncShieldsResource
    synthetic_data_generation: synthetic_data_generation.AsyncSyntheticDataGenerationResource
    telemetry: telemetry.AsyncTelemetryResource
    scoring: scoring.AsyncScoringResource
    scoring_functions: scoring_functions.AsyncScoringFunctionsResource
    benchmarks: benchmarks.AsyncBenchmarksResource
    files: files.AsyncFilesResource
    with_raw_response: AsyncLlamaStackClientWithRawResponse
    with_streaming_response: AsyncLlamaStackClientWithStreamedResponse

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

        This automatically infers the `api_key` argument from the `LLAMA_STACK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_STACK_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_BASE_URL")
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

        self.toolgroups = toolgroups.AsyncToolgroupsResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.tool_runtime = tool_runtime.AsyncToolRuntimeResource(self)
        self.responses = responses.AsyncResponsesResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.eval = eval.AsyncEvalResource(self)
        self.inspect = inspect.AsyncInspectResource(self)
        self.inference = inference.AsyncInferenceResource(self)
        self.embeddings = embeddings.AsyncEmbeddingsResource(self)
        self.chat = chat.AsyncChatResource(self)
        self.completions = completions.AsyncCompletionsResource(self)
        self.vector_io = vector_io.AsyncVectorIoResource(self)
        self.vector_dbs = vector_dbs.AsyncVectorDBsResource(self)
        self.vector_stores = vector_stores.AsyncVectorStoresResource(self)
        self.models = models.AsyncModelsResource(self)
        self.post_training = post_training.AsyncPostTrainingResource(self)
        self.providers = providers.AsyncProvidersResource(self)
        self.routes = routes.AsyncRoutesResource(self)
        self.safety = safety.AsyncSafetyResource(self)
        self.shields = shields.AsyncShieldsResource(self)
        self.synthetic_data_generation = synthetic_data_generation.AsyncSyntheticDataGenerationResource(self)
        self.telemetry = telemetry.AsyncTelemetryResource(self)
        self.scoring = scoring.AsyncScoringResource(self)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResource(self)
        self.benchmarks = benchmarks.AsyncBenchmarksResource(self)
        self.files = files.AsyncFilesResource(self)
        self.with_raw_response = AsyncLlamaStackClientWithRawResponse(self)
        self.with_streaming_response = AsyncLlamaStackClientWithStreamedResponse(self)

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
    def __init__(self, client: LlamaStackClient) -> None:
        self.toolgroups = toolgroups.ToolgroupsResourceWithRawResponse(client.toolgroups)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.tool_runtime = tool_runtime.ToolRuntimeResourceWithRawResponse(client.tool_runtime)
        self.responses = responses.ResponsesResourceWithRawResponse(client.responses)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.eval = eval.EvalResourceWithRawResponse(client.eval)
        self.inspect = inspect.InspectResourceWithRawResponse(client.inspect)
        self.inference = inference.InferenceResourceWithRawResponse(client.inference)
        self.embeddings = embeddings.EmbeddingsResourceWithRawResponse(client.embeddings)
        self.chat = chat.ChatResourceWithRawResponse(client.chat)
        self.completions = completions.CompletionsResourceWithRawResponse(client.completions)
        self.vector_io = vector_io.VectorIoResourceWithRawResponse(client.vector_io)
        self.vector_dbs = vector_dbs.VectorDBsResourceWithRawResponse(client.vector_dbs)
        self.vector_stores = vector_stores.VectorStoresResourceWithRawResponse(client.vector_stores)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.post_training = post_training.PostTrainingResourceWithRawResponse(client.post_training)
        self.providers = providers.ProvidersResourceWithRawResponse(client.providers)
        self.routes = routes.RoutesResourceWithRawResponse(client.routes)
        self.safety = safety.SafetyResourceWithRawResponse(client.safety)
        self.shields = shields.ShieldsResourceWithRawResponse(client.shields)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.telemetry = telemetry.TelemetryResourceWithRawResponse(client.telemetry)
        self.scoring = scoring.ScoringResourceWithRawResponse(client.scoring)
        self.scoring_functions = scoring_functions.ScoringFunctionsResourceWithRawResponse(client.scoring_functions)
        self.benchmarks = benchmarks.BenchmarksResourceWithRawResponse(client.benchmarks)
        self.files = files.FilesResourceWithRawResponse(client.files)


class AsyncLlamaStackClientWithRawResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.toolgroups = toolgroups.AsyncToolgroupsResourceWithRawResponse(client.toolgroups)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.tool_runtime = tool_runtime.AsyncToolRuntimeResourceWithRawResponse(client.tool_runtime)
        self.responses = responses.AsyncResponsesResourceWithRawResponse(client.responses)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.eval = eval.AsyncEvalResourceWithRawResponse(client.eval)
        self.inspect = inspect.AsyncInspectResourceWithRawResponse(client.inspect)
        self.inference = inference.AsyncInferenceResourceWithRawResponse(client.inference)
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithRawResponse(client.embeddings)
        self.chat = chat.AsyncChatResourceWithRawResponse(client.chat)
        self.completions = completions.AsyncCompletionsResourceWithRawResponse(client.completions)
        self.vector_io = vector_io.AsyncVectorIoResourceWithRawResponse(client.vector_io)
        self.vector_dbs = vector_dbs.AsyncVectorDBsResourceWithRawResponse(client.vector_dbs)
        self.vector_stores = vector_stores.AsyncVectorStoresResourceWithRawResponse(client.vector_stores)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.post_training = post_training.AsyncPostTrainingResourceWithRawResponse(client.post_training)
        self.providers = providers.AsyncProvidersResourceWithRawResponse(client.providers)
        self.routes = routes.AsyncRoutesResourceWithRawResponse(client.routes)
        self.safety = safety.AsyncSafetyResourceWithRawResponse(client.safety)
        self.shields = shields.AsyncShieldsResourceWithRawResponse(client.shields)
        self.synthetic_data_generation = synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.telemetry = telemetry.AsyncTelemetryResourceWithRawResponse(client.telemetry)
        self.scoring = scoring.AsyncScoringResourceWithRawResponse(client.scoring)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResourceWithRawResponse(
            client.scoring_functions
        )
        self.benchmarks = benchmarks.AsyncBenchmarksResourceWithRawResponse(client.benchmarks)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)


class LlamaStackClientWithStreamedResponse:
    def __init__(self, client: LlamaStackClient) -> None:
        self.toolgroups = toolgroups.ToolgroupsResourceWithStreamingResponse(client.toolgroups)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.tool_runtime = tool_runtime.ToolRuntimeResourceWithStreamingResponse(client.tool_runtime)
        self.responses = responses.ResponsesResourceWithStreamingResponse(client.responses)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.eval = eval.EvalResourceWithStreamingResponse(client.eval)
        self.inspect = inspect.InspectResourceWithStreamingResponse(client.inspect)
        self.inference = inference.InferenceResourceWithStreamingResponse(client.inference)
        self.embeddings = embeddings.EmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.chat = chat.ChatResourceWithStreamingResponse(client.chat)
        self.completions = completions.CompletionsResourceWithStreamingResponse(client.completions)
        self.vector_io = vector_io.VectorIoResourceWithStreamingResponse(client.vector_io)
        self.vector_dbs = vector_dbs.VectorDBsResourceWithStreamingResponse(client.vector_dbs)
        self.vector_stores = vector_stores.VectorStoresResourceWithStreamingResponse(client.vector_stores)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.post_training = post_training.PostTrainingResourceWithStreamingResponse(client.post_training)
        self.providers = providers.ProvidersResourceWithStreamingResponse(client.providers)
        self.routes = routes.RoutesResourceWithStreamingResponse(client.routes)
        self.safety = safety.SafetyResourceWithStreamingResponse(client.safety)
        self.shields = shields.ShieldsResourceWithStreamingResponse(client.shields)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResourceWithStreamingResponse(
            client.synthetic_data_generation
        )
        self.telemetry = telemetry.TelemetryResourceWithStreamingResponse(client.telemetry)
        self.scoring = scoring.ScoringResourceWithStreamingResponse(client.scoring)
        self.scoring_functions = scoring_functions.ScoringFunctionsResourceWithStreamingResponse(
            client.scoring_functions
        )
        self.benchmarks = benchmarks.BenchmarksResourceWithStreamingResponse(client.benchmarks)
        self.files = files.FilesResourceWithStreamingResponse(client.files)


class AsyncLlamaStackClientWithStreamedResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.toolgroups = toolgroups.AsyncToolgroupsResourceWithStreamingResponse(client.toolgroups)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.tool_runtime = tool_runtime.AsyncToolRuntimeResourceWithStreamingResponse(client.tool_runtime)
        self.responses = responses.AsyncResponsesResourceWithStreamingResponse(client.responses)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.eval = eval.AsyncEvalResourceWithStreamingResponse(client.eval)
        self.inspect = inspect.AsyncInspectResourceWithStreamingResponse(client.inspect)
        self.inference = inference.AsyncInferenceResourceWithStreamingResponse(client.inference)
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.chat = chat.AsyncChatResourceWithStreamingResponse(client.chat)
        self.completions = completions.AsyncCompletionsResourceWithStreamingResponse(client.completions)
        self.vector_io = vector_io.AsyncVectorIoResourceWithStreamingResponse(client.vector_io)
        self.vector_dbs = vector_dbs.AsyncVectorDBsResourceWithStreamingResponse(client.vector_dbs)
        self.vector_stores = vector_stores.AsyncVectorStoresResourceWithStreamingResponse(client.vector_stores)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.post_training = post_training.AsyncPostTrainingResourceWithStreamingResponse(client.post_training)
        self.providers = providers.AsyncProvidersResourceWithStreamingResponse(client.providers)
        self.routes = routes.AsyncRoutesResourceWithStreamingResponse(client.routes)
        self.safety = safety.AsyncSafetyResourceWithStreamingResponse(client.safety)
        self.shields = shields.AsyncShieldsResourceWithStreamingResponse(client.shields)
        self.synthetic_data_generation = (
            synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithStreamingResponse(
                client.synthetic_data_generation
            )
        )
        self.telemetry = telemetry.AsyncTelemetryResourceWithStreamingResponse(client.telemetry)
        self.scoring = scoring.AsyncScoringResourceWithStreamingResponse(client.scoring)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResourceWithStreamingResponse(
            client.scoring_functions
        )
        self.benchmarks = benchmarks.AsyncBenchmarksResourceWithStreamingResponse(client.benchmarks)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)


Client = LlamaStackClient

AsyncClient = AsyncLlamaStackClient
