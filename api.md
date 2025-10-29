# Shared Types

```python
from llama_stack_client.types import (
    CompletionMessage,
    Document,
    InterleavedContent,
    InterleavedContentItem,
    Message,
    ParamType,
    QueryConfig,
    QueryResult,
    SafetyViolation,
    ScoringResult,
    SystemMessage,
    ToolCall,
    ToolResponseMessage,
    UserMessage,
)
```

# Toolgroups

Types:

```python
from llama_stack_client.types import ListToolGroupsResponse, ToolGroup, ToolgroupListResponse
```

Methods:

- <code title="get /v1/toolgroups">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">list</a>() -> <a href="./src/llama_stack_client/types/toolgroup_list_response.py">ToolgroupListResponse</a></code>
- <code title="get /v1/toolgroups/{toolgroup_id}">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">get</a>(toolgroup_id) -> <a href="./src/llama_stack_client/types/tool_group.py">ToolGroup</a></code>
- <code title="post /v1/toolgroups">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">register</a>(\*\*<a href="src/llama_stack_client/types/toolgroup_register_params.py">params</a>) -> None</code>
- <code title="delete /v1/toolgroups/{toolgroup_id}">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">unregister</a>(toolgroup_id) -> None</code>

# Tools

Types:

```python
from llama_stack_client.types import ToolListResponse
```

Methods:

- <code title="get /v1/tools">client.tools.<a href="./src/llama_stack_client/resources/tools.py">list</a>(\*\*<a href="src/llama_stack_client/types/tool_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="get /v1/tools/{tool_name}">client.tools.<a href="./src/llama_stack_client/resources/tools.py">get</a>(tool_name) -> <a href="./src/llama_stack_client/types/tool_def.py">ToolDef</a></code>

# ToolRuntime

Types:

```python
from llama_stack_client.types import ToolDef, ToolInvocationResult, ToolRuntimeListToolsResponse
```

Methods:

- <code title="post /v1/tool-runtime/invoke">client.tool_runtime.<a href="./src/llama_stack_client/resources/tool_runtime/tool_runtime.py">invoke_tool</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime_invoke_tool_params.py">params</a>) -> <a href="./src/llama_stack_client/types/tool_invocation_result.py">ToolInvocationResult</a></code>
- <code title="get /v1/tool-runtime/list-tools">client.tool_runtime.<a href="./src/llama_stack_client/resources/tool_runtime/tool_runtime.py">list_tools</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime_list_tools_params.py">params</a>) -> <a href="./src/llama_stack_client/types/tool_runtime_list_tools_response.py">ToolRuntimeListToolsResponse</a></code>

## RagTool

Methods:

- <code title="post /v1/tool-runtime/rag-tool/insert">client.tool_runtime.rag_tool.<a href="./src/llama_stack_client/resources/tool_runtime/rag_tool.py">insert</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime/rag_tool_insert_params.py">params</a>) -> None</code>
- <code title="post /v1/tool-runtime/rag-tool/query">client.tool_runtime.rag_tool.<a href="./src/llama_stack_client/resources/tool_runtime/rag_tool.py">query</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime/rag_tool_query_params.py">params</a>) -> <a href="./src/llama_stack_client/types/shared/query_result.py">QueryResult</a></code>

# Responses

Types:

```python
from llama_stack_client.types import (
    ResponseObject,
    ResponseObjectStream,
    ResponseListResponse,
    ResponseDeleteResponse,
)
```

Methods:

- <code title="post /v1/responses">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">create</a>(\*\*<a href="src/llama_stack_client/types/response_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/response_object.py">ResponseObject</a></code>
- <code title="get /v1/responses/{response_id}">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">retrieve</a>(response_id) -> <a href="./src/llama_stack_client/types/response_object.py">ResponseObject</a></code>
- <code title="get /v1/responses">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">list</a>(\*\*<a href="src/llama_stack_client/types/response_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/response_list_response.py">SyncOpenAICursorPage[ResponseListResponse]</a></code>
- <code title="delete /v1/responses/{response_id}">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">delete</a>(response_id) -> <a href="./src/llama_stack_client/types/response_delete_response.py">ResponseDeleteResponse</a></code>

## InputItems

Types:

```python
from llama_stack_client.types.responses import InputItemListResponse
```

Methods:

- <code title="get /v1/responses/{response_id}/input_items">client.responses.input_items.<a href="./src/llama_stack_client/resources/responses/input_items.py">list</a>(response_id, \*\*<a href="src/llama_stack_client/types/responses/input_item_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/responses/input_item_list_response.py">InputItemListResponse</a></code>

# Conversations

Types:

```python
from llama_stack_client.types import ConversationObject, ConversationDeleteResponse
```

Methods:

- <code title="post /v1/conversations">client.conversations.<a href="./src/llama_stack_client/resources/conversations/conversations.py">create</a>(\*\*<a href="src/llama_stack_client/types/conversation_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/conversation_object.py">ConversationObject</a></code>
- <code title="get /v1/conversations/{conversation_id}">client.conversations.<a href="./src/llama_stack_client/resources/conversations/conversations.py">retrieve</a>(conversation_id) -> <a href="./src/llama_stack_client/types/conversation_object.py">ConversationObject</a></code>
- <code title="post /v1/conversations/{conversation_id}">client.conversations.<a href="./src/llama_stack_client/resources/conversations/conversations.py">update</a>(conversation_id, \*\*<a href="src/llama_stack_client/types/conversation_update_params.py">params</a>) -> <a href="./src/llama_stack_client/types/conversation_object.py">ConversationObject</a></code>
- <code title="delete /v1/conversations/{conversation_id}">client.conversations.<a href="./src/llama_stack_client/resources/conversations/conversations.py">delete</a>(conversation_id) -> <a href="./src/llama_stack_client/types/conversation_delete_response.py">ConversationDeleteResponse</a></code>

## Items

Types:

```python
from llama_stack_client.types.conversations import (
    ItemCreateResponse,
    ItemListResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="post /v1/conversations/{conversation_id}/items">client.conversations.items.<a href="./src/llama_stack_client/resources/conversations/items.py">create</a>(conversation_id, \*\*<a href="src/llama_stack_client/types/conversations/item_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/conversations/item_create_response.py">ItemCreateResponse</a></code>
- <code title="get /v1/conversations/{conversation_id}/items">client.conversations.items.<a href="./src/llama_stack_client/resources/conversations/items.py">list</a>(conversation_id, \*\*<a href="src/llama_stack_client/types/conversations/item_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/conversations/item_list_response.py">SyncOpenAICursorPage[ItemListResponse]</a></code>
- <code title="get /v1/conversations/{conversation_id}/items/{item_id}">client.conversations.items.<a href="./src/llama_stack_client/resources/conversations/items.py">get</a>(item_id, \*, conversation_id) -> <a href="./src/llama_stack_client/types/conversations/item_get_response.py">ItemGetResponse</a></code>

# Inspect

Types:

```python
from llama_stack_client.types import HealthInfo, ProviderInfo, RouteInfo, VersionInfo
```

Methods:

- <code title="get /v1/health">client.inspect.<a href="./src/llama_stack_client/resources/inspect.py">health</a>() -> <a href="./src/llama_stack_client/types/health_info.py">HealthInfo</a></code>
- <code title="get /v1/version">client.inspect.<a href="./src/llama_stack_client/resources/inspect.py">version</a>() -> <a href="./src/llama_stack_client/types/version_info.py">VersionInfo</a></code>

# Embeddings

Types:

```python
from llama_stack_client.types import CreateEmbeddingsResponse
```

Methods:

- <code title="post /v1/embeddings">client.embeddings.<a href="./src/llama_stack_client/resources/embeddings.py">create</a>(\*\*<a href="src/llama_stack_client/types/embedding_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/create_embeddings_response.py">CreateEmbeddingsResponse</a></code>

# Chat

Types:

```python
from llama_stack_client.types import ChatCompletionChunk
```

## Completions

Types:

```python
from llama_stack_client.types.chat import (
    CompletionCreateResponse,
    CompletionRetrieveResponse,
    CompletionListResponse,
)
```

Methods:

- <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/llama_stack_client/resources/chat/completions.py">create</a>(\*\*<a href="src/llama_stack_client/types/chat/completion_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>
- <code title="get /v1/chat/completions/{completion_id}">client.chat.completions.<a href="./src/llama_stack_client/resources/chat/completions.py">retrieve</a>(completion_id) -> <a href="./src/llama_stack_client/types/chat/completion_retrieve_response.py">CompletionRetrieveResponse</a></code>
- <code title="get /v1/chat/completions">client.chat.completions.<a href="./src/llama_stack_client/resources/chat/completions.py">list</a>(\*\*<a href="src/llama_stack_client/types/chat/completion_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/chat/completion_list_response.py">SyncOpenAICursorPage[CompletionListResponse]</a></code>

# Completions

Types:

```python
from llama_stack_client.types import CompletionCreateResponse
```

Methods:

- <code title="post /v1/completions">client.completions.<a href="./src/llama_stack_client/resources/completions.py">create</a>(\*\*<a href="src/llama_stack_client/types/completion_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/completion_create_response.py">CompletionCreateResponse</a></code>

# VectorIo

Types:

```python
from llama_stack_client.types import QueryChunksResponse
```

Methods:

- <code title="post /v1/vector-io/insert">client.vector_io.<a href="./src/llama_stack_client/resources/vector_io.py">insert</a>(\*\*<a href="src/llama_stack_client/types/vector_io_insert_params.py">params</a>) -> None</code>
- <code title="post /v1/vector-io/query">client.vector_io.<a href="./src/llama_stack_client/resources/vector_io.py">query</a>(\*\*<a href="src/llama_stack_client/types/vector_io_query_params.py">params</a>) -> <a href="./src/llama_stack_client/types/query_chunks_response.py">QueryChunksResponse</a></code>

# VectorStores

Types:

```python
from llama_stack_client.types import (
    ListVectorStoresResponse,
    VectorStore,
    VectorStoreDeleteResponse,
    VectorStoreSearchResponse,
)
```

Methods:

- <code title="post /v1/vector_stores">client.vector_stores.<a href="./src/llama_stack_client/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/llama_stack_client/types/vector_store_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/llama_stack_client/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/llama_stack_client/types/vector_store.py">VectorStore</a></code>
- <code title="post /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/llama_stack_client/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_store_update_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores">client.vector_stores.<a href="./src/llama_stack_client/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/llama_stack_client/types/vector_store_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_store.py">SyncOpenAICursorPage[VectorStore]</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/llama_stack_client/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/llama_stack_client/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>
- <code title="post /v1/vector_stores/{vector_store_id}/search">client.vector_stores.<a href="./src/llama_stack_client/resources/vector_stores/vector_stores.py">search</a>(vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_store_search_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_store_search_response.py">VectorStoreSearchResponse</a></code>

## Files

Types:

```python
from llama_stack_client.types.vector_stores import (
    VectorStoreFile,
    FileDeleteResponse,
    FileContentResponse,
)
```

Methods:

- <code title="post /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/llama_stack_client/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/llama_stack_client/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="post /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/llama_stack_client/resources/vector_stores/files.py">update</a>(file_id, \*, vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_stores/file_update_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/llama_stack_client/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file.py">SyncOpenAICursorPage[VectorStoreFile]</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/llama_stack_client/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/llama_stack_client/types/vector_stores/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files/{file_id}/content">client.vector_stores.files.<a href="./src/llama_stack_client/resources/vector_stores/files.py">content</a>(file_id, \*, vector_store_id) -> <a href="./src/llama_stack_client/types/vector_stores/file_content_response.py">FileContentResponse</a></code>

## FileBatches

Types:

```python
from llama_stack_client.types.vector_stores import (
    ListVectorStoreFilesInBatchResponse,
    VectorStoreFileBatches,
)
```

Methods:

- <code title="post /v1/vector_stores/{vector_store_id}/file_batches">client.vector_stores.file_batches.<a href="./src/llama_stack_client/resources/vector_stores/file_batches.py">create</a>(vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_stores/file_batch_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file_batches.py">VectorStoreFileBatches</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/file_batches/{batch_id}">client.vector_stores.file_batches.<a href="./src/llama_stack_client/resources/vector_stores/file_batches.py">retrieve</a>(batch_id, \*, vector_store_id) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file_batches.py">VectorStoreFileBatches</a></code>
- <code title="post /v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel">client.vector_stores.file_batches.<a href="./src/llama_stack_client/resources/vector_stores/file_batches.py">cancel</a>(batch_id, \*, vector_store_id) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file_batches.py">VectorStoreFileBatches</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/files">client.vector_stores.file_batches.<a href="./src/llama_stack_client/resources/vector_stores/file_batches.py">list_files</a>(batch_id, \*, vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_stores/file_batch_list_files_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_stores/vector_store_file.py">SyncOpenAICursorPage[VectorStoreFile]</a></code>

# Models

Types:

```python
from llama_stack_client.types import ListModelsResponse, Model, ModelListResponse
```

Methods:

- <code title="get /v1/models/{model_id}">client.models.<a href="./src/llama_stack_client/resources/models/models.py">retrieve</a>(model_id) -> <a href="./src/llama_stack_client/types/model.py">Model</a></code>
- <code title="get /v1/models">client.models.<a href="./src/llama_stack_client/resources/models/models.py">list</a>() -> <a href="./src/llama_stack_client/types/model_list_response.py">ModelListResponse</a></code>
- <code title="post /v1/models">client.models.<a href="./src/llama_stack_client/resources/models/models.py">register</a>(\*\*<a href="src/llama_stack_client/types/model_register_params.py">params</a>) -> <a href="./src/llama_stack_client/types/model.py">Model</a></code>
- <code title="delete /v1/models/{model_id}">client.models.<a href="./src/llama_stack_client/resources/models/models.py">unregister</a>(model_id) -> None</code>

## OpenAI

Methods:

- <code title="get /v1/models">client.models.openai.<a href="./src/llama_stack_client/resources/models/openai.py">list</a>() -> <a href="./src/llama_stack_client/types/model_list_response.py">ModelListResponse</a></code>

# Providers

Types:

```python
from llama_stack_client.types import ListProvidersResponse, ProviderListResponse
```

Methods:

- <code title="get /v1/providers/{provider_id}">client.providers.<a href="./src/llama_stack_client/resources/providers.py">retrieve</a>(provider_id) -> <a href="./src/llama_stack_client/types/provider_info.py">ProviderInfo</a></code>
- <code title="get /v1/providers">client.providers.<a href="./src/llama_stack_client/resources/providers.py">list</a>() -> <a href="./src/llama_stack_client/types/provider_list_response.py">ProviderListResponse</a></code>

# Routes

Types:

```python
from llama_stack_client.types import ListRoutesResponse, RouteListResponse
```

Methods:

- <code title="get /v1/inspect/routes">client.routes.<a href="./src/llama_stack_client/resources/routes.py">list</a>(\*\*<a href="src/llama_stack_client/types/route_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/route_list_response.py">RouteListResponse</a></code>

# Moderations

Types:

```python
from llama_stack_client.types import CreateResponse
```

Methods:

- <code title="post /v1/moderations">client.moderations.<a href="./src/llama_stack_client/resources/moderations.py">create</a>(\*\*<a href="src/llama_stack_client/types/moderation_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/create_response.py">CreateResponse</a></code>

# Safety

Types:

```python
from llama_stack_client.types import RunShieldResponse
```

Methods:

- <code title="post /v1/safety/run-shield">client.safety.<a href="./src/llama_stack_client/resources/safety.py">run_shield</a>(\*\*<a href="src/llama_stack_client/types/safety_run_shield_params.py">params</a>) -> <a href="./src/llama_stack_client/types/run_shield_response.py">RunShieldResponse</a></code>

# Shields

Types:

```python
from llama_stack_client.types import ListShieldsResponse, Shield, ShieldListResponse
```

Methods:

- <code title="get /v1/shields/{identifier}">client.shields.<a href="./src/llama_stack_client/resources/shields.py">retrieve</a>(identifier) -> <a href="./src/llama_stack_client/types/shield.py">Shield</a></code>
- <code title="get /v1/shields">client.shields.<a href="./src/llama_stack_client/resources/shields.py">list</a>() -> <a href="./src/llama_stack_client/types/shield_list_response.py">ShieldListResponse</a></code>
- <code title="delete /v1/shields/{identifier}">client.shields.<a href="./src/llama_stack_client/resources/shields.py">delete</a>(identifier) -> None</code>
- <code title="post /v1/shields">client.shields.<a href="./src/llama_stack_client/resources/shields.py">register</a>(\*\*<a href="src/llama_stack_client/types/shield_register_params.py">params</a>) -> <a href="./src/llama_stack_client/types/shield.py">Shield</a></code>

# SyntheticDataGeneration

Types:

```python
from llama_stack_client.types import SyntheticDataGenerationResponse
```

Methods:

- <code title="post /v1/synthetic-data-generation/generate">client.synthetic_data_generation.<a href="./src/llama_stack_client/resources/synthetic_data_generation.py">generate</a>(\*\*<a href="src/llama_stack_client/types/synthetic_data_generation_generate_params.py">params</a>) -> <a href="./src/llama_stack_client/types/synthetic_data_generation_response.py">SyntheticDataGenerationResponse</a></code>

# Scoring

Types:

```python
from llama_stack_client.types import ScoringScoreResponse, ScoringScoreBatchResponse
```

Methods:

- <code title="post /v1/scoring/score">client.scoring.<a href="./src/llama_stack_client/resources/scoring.py">score</a>(\*\*<a href="src/llama_stack_client/types/scoring_score_params.py">params</a>) -> <a href="./src/llama_stack_client/types/scoring_score_response.py">ScoringScoreResponse</a></code>
- <code title="post /v1/scoring/score-batch">client.scoring.<a href="./src/llama_stack_client/resources/scoring.py">score_batch</a>(\*\*<a href="src/llama_stack_client/types/scoring_score_batch_params.py">params</a>) -> <a href="./src/llama_stack_client/types/scoring_score_batch_response.py">ScoringScoreBatchResponse</a></code>

# ScoringFunctions

Types:

```python
from llama_stack_client.types import (
    ListScoringFunctionsResponse,
    ScoringFn,
    ScoringFnParams,
    ScoringFunctionListResponse,
)
```

Methods:

- <code title="get /v1/scoring-functions/{scoring_fn_id}">client.scoring_functions.<a href="./src/llama_stack_client/resources/scoring_functions.py">retrieve</a>(scoring_fn_id) -> <a href="./src/llama_stack_client/types/scoring_fn.py">ScoringFn</a></code>
- <code title="get /v1/scoring-functions">client.scoring_functions.<a href="./src/llama_stack_client/resources/scoring_functions.py">list</a>() -> <a href="./src/llama_stack_client/types/scoring_function_list_response.py">ScoringFunctionListResponse</a></code>
- <code title="post /v1/scoring-functions">client.scoring_functions.<a href="./src/llama_stack_client/resources/scoring_functions.py">register</a>(\*\*<a href="src/llama_stack_client/types/scoring_function_register_params.py">params</a>) -> None</code>

# Files

Types:

```python
from llama_stack_client.types import DeleteFileResponse, File, ListFilesResponse
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/llama_stack_client/resources/files.py">create</a>(\*\*<a href="src/llama_stack_client/types/file_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/file.py">File</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/llama_stack_client/resources/files.py">retrieve</a>(file_id) -> <a href="./src/llama_stack_client/types/file.py">File</a></code>
- <code title="get /v1/files">client.files.<a href="./src/llama_stack_client/resources/files.py">list</a>(\*\*<a href="src/llama_stack_client/types/file_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/file.py">SyncOpenAICursorPage[File]</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/llama_stack_client/resources/files.py">delete</a>(file_id) -> <a href="./src/llama_stack_client/types/delete_file_response.py">DeleteFileResponse</a></code>
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/llama_stack_client/resources/files.py">content</a>(file_id) -> object</code>
