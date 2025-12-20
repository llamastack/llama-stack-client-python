# Llama Stack Client Python API library


[![PyPI version](https://img.shields.io/pypi/v/llama_stack_client.svg)](https://pypi.org/project/llama_stack_client/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/llama-stack-client)](https://pypi.org/project/llama-stack-client/)
[![Discord](https://img.shields.io/discord/1257833999603335178)](https://discord.gg/llama-stack)

The Llama Stack Client Python library provides convenient access to the Llama Stack Client REST API from any Python 3.12+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is generated with [Stainless](https://www.stainlessapi.com/).

## Documentation

For starting up a Llama Stack server, please checkout our [Quickstart guide to start a Llama Stack server](https://llama-stack.readthedocs.io/en/latest/getting_started/index.html)

The REST API documentation can be found on [llama-stack API Reference](https://llama-stack.readthedocs.io/en/latest/references/api_reference/index.html). The full API of this library can be found in [api.md](api.md).

You can find more example apps with client SDKs to talk with the Llama Stack server in our [llama-stack-apps](https://github.com/meta-llama/llama-stack-apps/tree/main) repo.

## Installation

```sh
pip install llama-stack-client
```

## Usage

The full API of this library can be found in [api.md](api.md). You may find basic client examples in our [llama-stack-apps](https://github.com/meta-llama/llama-stack-apps/tree/main) repo.

```python
from llama_stack_client import LlamaStackClient

client = LlamaStackClient()

models = client.models.list()
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/) to add `LLAMA_STACK_CLIENT_API_KEY="My API Key"` to your `.env` file so that your API Key is not stored in source control.

After installing the `llama-stack-client` package, you can also use the [`llama-stack-client` CLI](https://github.com/meta-llama/llama-stack/tree/main/llama-stack-client) to interact with the Llama Stack server.
```bash
llama-stack-client inference chat-completion --message "hello, what model are you"
```

```python
OpenAIChatCompletion(
    id="AmivnS0iMv-mmEE4_A0DK1T",
    choices=[
        OpenAIChatCompletionChoice(
            finish_reason="stop",
            index=0,
            message=OpenAIChatCompletionChoiceMessageOpenAIAssistantMessageParam(
                role="assistant",
                content="Hello! I am an AI designed by Meta AI, and my model is a type of recurrent neural network (RNN) called a transformer. My specific architecture is based on the BERT (Bidirectional Encoder Representations from Transformers) model, which is a pre-trained language model that has been fine-tuned for a variety of natural language processing tasks.\n\nHere are some key details about my model:\n\n* **Model type:** Transformer-based language model\n* **Architecture:** BERT (Bidirectional Encoder Representations from Transformers)\n* **Training data:** A massive corpus of text data, including but not limited to:\n\t+ Web pages\n\t+ Books\n\t+ Articles\n\t+ Forums\n\t+ Social media platforms\n* **Parameters:** My model has approximately 1.5 billion parameters, which allows me to understand and generate human-like language.\n* **Capabilities:** I can perform a wide range of tasks, including but not limited to:\n\t+ Answering questions\n\t+ Generating text\n\t+ Translating languages\n\t+ Summarizing content\n\t+ Offering suggestions and ideas\n\nI'm constantly learning and improving, so please bear with me if I make any mistakes or don't quite understand what you're asking. How can I assist you today?",
                name=None,
                tool_calls=None,
                function_call=None,
            ),
            logprobs=OpenAIChatCompletionChoiceLogprobs(content=None, refusal=None),
        )
    ],
    created=1749825661,
    model="Llama-3.3-70B-Instruct",
    object="chat.completion",
    system_fingerprint=None,
    usage={
        "completion_tokens": 258,
        "prompt_tokens": 16,
        "total_tokens": 274,
        "completion_tokens_details": None,
        "prompt_tokens_details": None,
    },
    service_tier=None,
)
```

## Async usage

Simply import `AsyncLlamaStackClient` instead of `LlamaStackClient` and use `await` with each API call:

```python
import asyncio
from llama_stack_client import AsyncLlamaStackClient

client = AsyncLlamaStackClient(
    # defaults to "production".
    environment="sandbox",
)


async def main() -> None:
    models = await client.models.list()


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install --pre llama_stack_client[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import asyncio
from llama_stack_client import DefaultAioHttpClient
from llama_stack_client import AsyncLlamaStackClient


async def main() -> None:
    async with AsyncLlamaStackClient(
        http_client=DefaultAioHttpClient(),
    ) as client:
        models = await client.models.list()


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Pagination

List methods in the Llama Stack Client API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
from llama_stack_client import LlamaStackClient

client = LlamaStackClient()

all_responses = []
# Automatically fetches more pages as needed.
for response in client.responses.list():
    # Do something with response here
    all_responses.append(response)
print(all_responses)
```

Or, asynchronously:

```python
import asyncio
from llama_stack_client import AsyncLlamaStackClient

client = AsyncLlamaStackClient()


async def main() -> None:
    all_responses = []
    # Iterate through items across all pages, issuing requests as needed.
    async for response in client.responses.list():
        all_responses.append(response)
    print(all_responses)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await client.responses.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await client.responses.list()

print(f"next page cursor: {first_page.last_id}")  # => "next page cursor: ..."
for response in first_page.data:
    print(response.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from llama_stack_client import LlamaStackClient

client = LlamaStackClient()

client.toolgroups.register(
    provider_id="provider_id",
    toolgroup_id="toolgroup_id",
    mcp_endpoint={"uri": "uri"},
)
```

## File uploads

Request parameters that correspond to file uploads can be passed as `bytes`, or a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from llama_stack_client import LlamaStackClient

client = LlamaStackClient()

client.files.create(
    file=Path("/path/to/file"),
    purpose="assistants",
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `llama_stack_client.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `llama_stack_client.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `llama_stack_client.APIError`.

```python
import llama_stack_client
from llama_stack_client import LlamaStackClient

client = LlamaStackClient()

try:
    client.chat.completions.create(
        messages=[
            {
                "content": "string",
                "role": "user",
            }
        ],
        model="model",
    )
except llama_stack_client.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except llama_stack_client.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except llama_stack_client.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from llama_stack_client import LlamaStackClient

# Configure the default for all requests:
client = LlamaStackClient(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "content": "string",
            "role": "user",
        }
    ],
    model="model",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from llama_stack_client import LlamaStackClient

# Configure the default for all requests:
client = LlamaStackClient(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = LlamaStackClient(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "content": "string",
            "role": "user",
        }
    ],
    model="model",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `LLAMA_STACK_LOG` to `debug`.

```shell
$ export LLAMA_STACK_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from llama_stack_client import LlamaStackClient

client = LlamaStackClient()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "content": "string",
        "role": "user",
    }],
    model="model",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion.id)
```

These methods return an [`APIResponse`](https://github.com/meta-llama/llama-stack-python/tree/main/src/llama_stack_client/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/meta-llama/llama-stack-python/tree/main/src/llama_stack_client/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            "content": "string",
            "role": "user",
        }
    ],
    model="model",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) will be respected when making this
request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
from llama_stack_client import LlamaStackClient, DefaultHttpxClient

client = LlamaStackClient(
    # Or use the `LLAMA_STACK_CLIENT_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/meta-llama/llama-stack-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import llama_stack_client
print(llama_stack_client.__version__)
```

## Requirements

Python 3.12 or higher.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
