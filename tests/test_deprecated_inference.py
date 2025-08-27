import pytest
import warnings
import sys
from unittest import mock
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient


# Force all deprecation warnings to be shown, regardless of where they're emitted
warnings.filterwarnings("always", category=DeprecationWarning)


class TestDeprecatedInference:
    @pytest.fixture
    def client(self):
        client = LlamaStackClient(base_url="http://test", api_key="test_key")
        return client

    def test_direct_warning_capture_chat_completion(self, client):
        """Test deprecation warning using manual warning capture."""
        with mock.patch.object(client.inference, "_post") as mock_post:
            mock_post.return_value = {"id": "test_id", "choices": []}

            # Capture all warnings across all modules
            with warnings.catch_warnings(record=True) as recorded_warnings:
                # Ensure warnings are always shown
                warnings.simplefilter("always")

                # Call the deprecated method
                client.inference.chat_completion(messages=[{"role": "user", "content": "Hello"}], model_id="test_model")

                # Print warning details for debugging
                for w in recorded_warnings:
                    print(f"\nWarning category: {w.category}")
                    print(f"Warning message: {str(w.message)}")

                # Check for any DeprecationWarning with our message
                assert any(
                    issubclass(w.category, DeprecationWarning)
                    and "Use chat.completions.create instead" in str(w.message)
                    for w in recorded_warnings
                ), "No matching deprecation warnings were emitted"

    def test_completion_warning(self, client):
        """Test completion method emits deprecation warning."""
        with mock.patch.object(client.inference, "_post") as mock_post:
            mock_post.return_value = {"id": "test_id", "content": "test content"}

            # Capture all warnings across all modules
            with warnings.catch_warnings(record=True) as recorded_warnings:
                warnings.simplefilter("always")

                # Call the deprecated method
                client.inference.completion(content="Hello", model_id="test_model")

                # Check for any DeprecationWarning with our message
                assert any(
                    issubclass(w.category, DeprecationWarning) and "Use completions.create instead" in str(w.message)
                    for w in recorded_warnings
                ), "No matching deprecation warnings were emitted"

    def test_embeddings_warning(self, client):
        """Test embeddings method emits deprecation warning."""
        with mock.patch.object(client.inference, "_post") as mock_post:
            mock_post.return_value = {"data": [{"embedding": [0.1, 0.2]}]}

            # Capture all warnings across all modules
            with warnings.catch_warnings(record=True) as recorded_warnings:
                warnings.simplefilter("always")

                # Call the deprecated method
                client.inference.embeddings(contents=["Hello"], model_id="test_model")

                # Check for any DeprecationWarning with our message
                assert any(
                    issubclass(w.category, DeprecationWarning) and "Use embeddings.create instead" in str(w.message)
                    for w in recorded_warnings
                ), "No matching deprecation warnings were emitted"


class TestAsyncDeprecatedInference:
    @pytest.fixture
    def async_client(self):
        client = AsyncLlamaStackClient(base_url="http://test", api_key="test_key")
        return client

    @pytest.mark.asyncio
    async def test_async_chat_completion_warning(self, async_client):
        with mock.patch.object(async_client.inference, "_post", new_callable=mock.AsyncMock) as mock_post:
            mock_post.return_value = {"id": "test_id", "choices": []}

            # Capture all warnings across all modules
            with warnings.catch_warnings(record=True) as recorded_warnings:
                warnings.simplefilter("always")

                # Call the deprecated method
                await async_client.inference.chat_completion(
                    messages=[{"role": "user", "content": "Hello"}], model_id="test_model"
                )

                # Check for any DeprecationWarning with our message
                assert any(
                    issubclass(w.category, DeprecationWarning)
                    and "Use chat.completions.create instead" in str(w.message)
                    for w in recorded_warnings
                ), "No matching deprecation warnings were emitted"

    @pytest.mark.asyncio
    async def test_async_completion_warning(self, async_client):
        with mock.patch.object(async_client.inference, "_post", new_callable=mock.AsyncMock) as mock_post:
            mock_post.return_value = {"id": "test_id", "content": "test content"}

            # Capture all warnings across all modules
            with warnings.catch_warnings(record=True) as recorded_warnings:
                warnings.simplefilter("always")

                # Call the deprecated method
                await async_client.inference.completion(content="Hello", model_id="test_model")

                # Check for any DeprecationWarning with our message
                assert any(
                    issubclass(w.category, DeprecationWarning) and "Use completions.create instead" in str(w.message)
                    for w in recorded_warnings
                ), "No matching deprecation warnings were emitted"

    @pytest.mark.asyncio
    async def test_async_embeddings_warning(self, async_client):
        with mock.patch.object(async_client.inference, "_post", new_callable=mock.AsyncMock) as mock_post:
            mock_post.return_value = {"data": [{"embedding": [0.1, 0.2]}]}

            # Capture all warnings across all modules
            with warnings.catch_warnings(record=True) as recorded_warnings:
                warnings.simplefilter("always")

                # Call the deprecated method
                await async_client.inference.embeddings(contents=["Hello"], model_id="test_model")

                # Check for any DeprecationWarning with our message
                assert any(
                    issubclass(w.category, DeprecationWarning) and "Use embeddings.create instead" in str(w.message)
                    for w in recorded_warnings
                ), "No matching deprecation warnings were emitted"
