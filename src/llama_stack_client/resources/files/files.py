# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import file_list_params, file_create_upload_session_params
from .session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.file import File
from ..._base_client import make_request_options
from ...types.file_upload import FileUpload
from ...types.file_list_response import FileListResponse
from ...types.file_list_in_bucket_response import FileListInBucketResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def session(self) -> SessionResource:
        return SessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        key: str,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> File:
        """
        Get a file info identified by a bucket and key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            f"/v1/files/{bucket}/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def list(
        self,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        List all buckets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"bucket": bucket}, file_list_params.FileListParams),
            ),
            cast_to=FileListResponse,
        )

    def delete(
        self,
        key: str,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a file identified by a bucket and key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/files/{bucket}/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_upload_session(
        self,
        *,
        bucket: str,
        key: str,
        mime_type: str,
        size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileUpload:
        """
        Create a new upload session for a file identified by a bucket and key.

        Args:
          bucket: Bucket under which the file is stored (valid chars: a-zA-Z0-9\\__-)

          key: Key under which the file is stored (valid chars: a-zA-Z0-9\\__-/.)

          mime_type: MIME type of the file

          size: File size in bytes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "key": key,
                    "mime_type": mime_type,
                    "size": size,
                },
                file_create_upload_session_params.FileCreateUploadSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUpload,
        )

    def list_in_bucket(
        self,
        bucket: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListInBucketResponse:
        """
        List all files in a bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        return self._get(
            f"/v1/files/{bucket}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileListInBucketResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def session(self) -> AsyncSessionResource:
        return AsyncSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        key: str,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> File:
        """
        Get a file info identified by a bucket and key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            f"/v1/files/{bucket}/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def list(
        self,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        List all buckets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"bucket": bucket}, file_list_params.FileListParams),
            ),
            cast_to=FileListResponse,
        )

    async def delete(
        self,
        key: str,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a file identified by a bucket and key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/files/{bucket}/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_upload_session(
        self,
        *,
        bucket: str,
        key: str,
        mime_type: str,
        size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileUpload:
        """
        Create a new upload session for a file identified by a bucket and key.

        Args:
          bucket: Bucket under which the file is stored (valid chars: a-zA-Z0-9\\__-)

          key: Key under which the file is stored (valid chars: a-zA-Z0-9\\__-/.)

          mime_type: MIME type of the file

          size: File size in bytes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "key": key,
                    "mime_type": mime_type,
                    "size": size,
                },
                file_create_upload_session_params.FileCreateUploadSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUpload,
        )

    async def list_in_bucket(
        self,
        bucket: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListInBucketResponse:
        """
        List all files in a bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        return await self._get(
            f"/v1/files/{bucket}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileListInBucketResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_raw_response_wrapper(
            files.retrieve,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.create_upload_session = to_raw_response_wrapper(
            files.create_upload_session,
        )
        self.list_in_bucket = to_raw_response_wrapper(
            files.list_in_bucket,
        )

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._files.session)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_raw_response_wrapper(
            files.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.create_upload_session = async_to_raw_response_wrapper(
            files.create_upload_session,
        )
        self.list_in_bucket = async_to_raw_response_wrapper(
            files.list_in_bucket,
        )

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._files.session)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_streamed_response_wrapper(
            files.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.create_upload_session = to_streamed_response_wrapper(
            files.create_upload_session,
        )
        self.list_in_bucket = to_streamed_response_wrapper(
            files.list_in_bucket,
        )

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._files.session)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_streamed_response_wrapper(
            files.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.create_upload_session = async_to_streamed_response_wrapper(
            files.create_upload_session,
        )
        self.list_in_bucket = async_to_streamed_response_wrapper(
            files.list_in_bucket,
        )

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._files.session)
