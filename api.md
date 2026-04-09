# Shared Types

```python
from llama_stack_client.types import (
    HealthInfo,
    InterleavedContent,
    InterleavedContentItem,
    ListProvidersResponse,
    ListRoutesResponse,
    ParamType,
    ProviderInfo,
    RouteInfo,
    SafetyViolation,
    SamplingParams,
    SystemMessage,
    VersionInfo,
)
```

# Responses

Types:

```python
from llama_stack_client.types import (
    CompactedResponse,
    ResponseInput,
    ResponseMessage,
    ResponseObject,
    ResponseObjectStream,
    ResponseOutput,
    ResponseListResponse,
    ResponseDeleteResponse,
)
```

Methods:

- <code title="post /v1/responses">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">create</a>(\*\*<a href="src/llama_stack_client/types/response_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/response_object.py">ResponseObject</a></code>
- <code title="get /v1/responses/{response_id}">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">retrieve</a>(response_id) -> <a href="./src/llama_stack_client/types/response_object.py">ResponseObject</a></code>
- <code title="get /v1/responses">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">list</a>(\*\*<a href="src/llama_stack_client/types/response_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/response_list_response.py">SyncOpenAICursorPage[ResponseListResponse]</a></code>
- <code title="delete /v1/responses/{response_id}">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">delete</a>(response_id) -> <a href="./src/llama_stack_client/types/response_delete_response.py">ResponseDeleteResponse</a></code>
- <code title="post /v1/responses/compact">client.responses.<a href="./src/llama_stack_client/resources/responses/responses.py">compact</a>(\*\*<a href="src/llama_stack_client/types/response_compact_params.py">params</a>) -> <a href="./src/llama_stack_client/types/compacted_response.py">CompactedResponse</a></code>

## InputItems

Types:

```python
from llama_stack_client.types.responses import InputItemListResponse
```

Methods:

- <code title="get /v1/responses/{response_id}/input_items">client.responses.input_items.<a href="./src/llama_stack_client/resources/responses/input_items.py">list</a>(response_id, \*\*<a href="src/llama_stack_client/types/responses/input_item_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/responses/input_item_list_response.py">InputItemListResponse</a></code>

# Prompts

Types:

```python
from llama_stack_client.types import ListPromptsResponse, Prompt, PromptListResponse
```

Methods:

- <code title="post /v1/prompts">client.prompts.<a href="./src/llama_stack_client/resources/prompts/prompts.py">create</a>(\*\*<a href="src/llama_stack_client/types/prompt_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompts/{prompt_id}">client.prompts.<a href="./src/llama_stack_client/resources/prompts/prompts.py">retrieve</a>(prompt_id, \*\*<a href="src/llama_stack_client/types/prompt_retrieve_params.py">params</a>) -> <a href="./src/llama_stack_client/types/prompt.py">Prompt</a></code>
- <code title="put /v1/prompts/{prompt_id}">client.prompts.<a href="./src/llama_stack_client/resources/prompts/prompts.py">update</a>(prompt_id, \*\*<a href="src/llama_stack_client/types/prompt_update_params.py">params</a>) -> <a href="./src/llama_stack_client/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompts">client.prompts.<a href="./src/llama_stack_client/resources/prompts/prompts.py">list</a>() -> <a href="./src/llama_stack_client/types/prompt_list_response.py">PromptListResponse</a></code>
- <code title="delete /v1/prompts/{prompt_id}">client.prompts.<a href="./src/llama_stack_client/resources/prompts/prompts.py">delete</a>(prompt_id) -> None</code>
- <code title="put /v1/prompts/{prompt_id}/set-default-version">client.prompts.<a href="./src/llama_stack_client/resources/prompts/prompts.py">set_default_version</a>(prompt_id, \*\*<a href="src/llama_stack_client/types/prompt_set_default_version_params.py">params</a>) -> <a href="./src/llama_stack_client/types/prompt.py">Prompt</a></code>

## Versions

Methods:

- <code title="get /v1/prompts/{prompt_id}/versions">client.prompts.versions.<a href="./src/llama_stack_client/resources/prompts/versions.py">list</a>(prompt_id) -> <a href="./src/llama_stack_client/types/prompt_list_response.py">PromptListResponse</a></code>

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
    ItemDeleteResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="post /v1/conversations/{conversation_id}/items">client.conversations.items.<a href="./src/llama_stack_client/resources/conversations/items.py">create</a>(conversation_id, \*\*<a href="src/llama_stack_client/types/conversations/item_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/conversations/item_create_response.py">ItemCreateResponse</a></code>
- <code title="get /v1/conversations/{conversation_id}/items">client.conversations.items.<a href="./src/llama_stack_client/resources/conversations/items.py">list</a>(conversation_id, \*\*<a href="src/llama_stack_client/types/conversations/item_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/conversations/item_list_response.py">SyncOpenAICursorPage[ItemListResponse]</a></code>
- <code title="delete /v1/conversations/{conversation_id}/items/{item_id}">client.conversations.items.<a href="./src/llama_stack_client/resources/conversations/items.py">delete</a>(item_id, \*, conversation_id) -> <a href="./src/llama_stack_client/types/conversations/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="get /v1/conversations/{conversation_id}/items/{item_id}">client.conversations.items.<a href="./src/llama_stack_client/resources/conversations/items.py">get</a>(item_id, \*, conversation_id) -> <a href="./src/llama_stack_client/types/conversations/item_get_response.py">ItemGetResponse</a></code>

# Inspect

Methods:

- <code title="get /v1/health">client.inspect.<a href="./src/llama_stack_client/resources/inspect.py">health</a>() -> <a href="./src/llama_stack_client/types/shared/health_info.py">HealthInfo</a></code>
- <code title="get /v1/version">client.inspect.<a href="./src/llama_stack_client/resources/inspect.py">version</a>() -> <a href="./src/llama_stack_client/types/shared/version_info.py">VersionInfo</a></code>

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
- <code title="get /v1/chat/completions">client.chat.completions.<a href="./src/llama_stack_client/resources/chat/completions.py">list</a>(\*\*<a href="src/llama_stack_client/types/chat/completion_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/chat/completion_list_response.py">CompletionListResponse</a></code>

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
- <code title="get /v1/vector_stores/{vector_store_id}/files/{file_id}/content">client.vector_stores.files.<a href="./src/llama_stack_client/resources/vector_stores/files.py">content</a>(file_id, \*, vector_store_id, \*\*<a href="src/llama_stack_client/types/vector_stores/file_content_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_stores/file_content_response.py">FileContentResponse</a></code>

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
from llama_stack_client.types import ListModelsResponse, Model, ModelRetrieveResponse
```

Methods:

- <code title="get /v1/models/{model_id}">client.models.<a href="./src/llama_stack_client/resources/models/models.py">retrieve</a>(model_id) -> <a href="./src/llama_stack_client/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="get /v1/models">client.models.<a href="./src/llama_stack_client/resources/models/models.py">list</a>() -> <a href="./src/llama_stack_client/types/list_models_response.py">ListModelsResponse</a></code>

## OpenAI

Methods:

- <code title="get /v1/models">client.models.openai.<a href="./src/llama_stack_client/resources/models/openai.py">list</a>() -> <a href="./src/llama_stack_client/types/list_models_response.py">ListModelsResponse</a></code>

# Providers

Types:

```python
from llama_stack_client.types import ProviderListResponse
```

Methods:

- <code title="get /v1/providers/{provider_id}">client.providers.<a href="./src/llama_stack_client/resources/providers.py">retrieve</a>(provider_id) -> <a href="./src/llama_stack_client/types/shared/provider_info.py">ProviderInfo</a></code>
- <code title="get /v1/providers">client.providers.<a href="./src/llama_stack_client/resources/providers.py">list</a>() -> <a href="./src/llama_stack_client/types/provider_list_response.py">ProviderListResponse</a></code>

# Routes

Types:

```python
from llama_stack_client.types import RouteListResponse
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

# Files

Types:

```python
from llama_stack_client.types import (
    DeleteFileResponse,
    File,
    ListFilesResponse,
    FileContentResponse,
)
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/llama_stack_client/resources/files.py">create</a>(\*\*<a href="src/llama_stack_client/types/file_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/file.py">File</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/llama_stack_client/resources/files.py">retrieve</a>(file_id) -> <a href="./src/llama_stack_client/types/file.py">File</a></code>
- <code title="get /v1/files">client.files.<a href="./src/llama_stack_client/resources/files.py">list</a>(\*\*<a href="src/llama_stack_client/types/file_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/file.py">SyncOpenAICursorPage[File]</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/llama_stack_client/resources/files.py">delete</a>(file_id) -> <a href="./src/llama_stack_client/types/delete_file_response.py">DeleteFileResponse</a></code>
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/llama_stack_client/resources/files.py">content</a>(file_id) -> str</code>

# Batches

Types:

```python
from llama_stack_client.types import (
    BatchCreateResponse,
    BatchRetrieveResponse,
    BatchListResponse,
    BatchCancelResponse,
)
```

Methods:

- <code title="post /v1/batches">client.batches.<a href="./src/llama_stack_client/resources/batches.py">create</a>(\*\*<a href="src/llama_stack_client/types/batch_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="get /v1/batches/{batch_id}">client.batches.<a href="./src/llama_stack_client/resources/batches.py">retrieve</a>(batch_id) -> <a href="./src/llama_stack_client/types/batch_retrieve_response.py">BatchRetrieveResponse</a></code>
- <code title="get /v1/batches">client.batches.<a href="./src/llama_stack_client/resources/batches.py">list</a>(\*\*<a href="src/llama_stack_client/types/batch_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/batch_list_response.py">SyncOpenAICursorPage[BatchListResponse]</a></code>
- <code title="post /v1/batches/{batch_id}/cancel">client.batches.<a href="./src/llama_stack_client/resources/batches.py">cancel</a>(batch_id) -> <a href="./src/llama_stack_client/types/batch_cancel_response.py">BatchCancelResponse</a></code>

# Alpha

## Admin

Methods:

- <code title="get /v1alpha/admin/health">client.alpha.admin.<a href="./src/llama_stack_client/resources/alpha/admin.py">health</a>() -> <a href="./src/llama_stack_client/types/shared/health_info.py">HealthInfo</a></code>
- <code title="get /v1alpha/admin/providers/{provider_id}">client.alpha.admin.<a href="./src/llama_stack_client/resources/alpha/admin.py">inspect_provider</a>(provider_id) -> <a href="./src/llama_stack_client/types/shared/provider_info.py">ProviderInfo</a></code>
- <code title="get /v1alpha/admin/providers">client.alpha.admin.<a href="./src/llama_stack_client/resources/alpha/admin.py">list_providers</a>() -> <a href="./src/llama_stack_client/types/provider_list_response.py">ProviderListResponse</a></code>
- <code title="get /v1alpha/admin/inspect/routes">client.alpha.admin.<a href="./src/llama_stack_client/resources/alpha/admin.py">list_routes</a>(\*\*<a href="src/llama_stack_client/types/alpha/admin_list_routes_params.py">params</a>) -> <a href="./src/llama_stack_client/types/route_list_response.py">RouteListResponse</a></code>
- <code title="get /v1alpha/admin/version">client.alpha.admin.<a href="./src/llama_stack_client/resources/alpha/admin.py">version</a>() -> <a href="./src/llama_stack_client/types/shared/version_info.py">VersionInfo</a></code>

## Inference

Types:

```python
from llama_stack_client.types.alpha import InferenceRerankResponse
```

Methods:

- <code title="post /v1alpha/inference/rerank">client.alpha.inference.<a href="./src/llama_stack_client/resources/alpha/inference.py">rerank</a>(\*\*<a href="src/llama_stack_client/types/alpha/inference_rerank_params.py">params</a>) -> <a href="./src/llama_stack_client/types/alpha/inference_rerank_response.py">InferenceRerankResponse</a></code>
