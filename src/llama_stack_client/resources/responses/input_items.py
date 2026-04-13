# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.responses import input_item_list_params
from ...types.responses.input_item_list_response import InputItemListResponse

__all__ = ["InputItemsResource", "AsyncInputItemsResource"]


class InputItemsResource(SyncAPIResource):
    """
    OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
    """

    @cached_property
    def with_raw_response(self) -> InputItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return InputItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InputItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return InputItemsResourceWithStreamingResponse(self)

    def list(
        self,
        response_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Optional[Literal["asc", "desc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InputItemListResponse:
        """
        List input items.

        Args:
          response_id: The ID of the response to retrieve input items for.

          after: An item ID to list items after, used for pagination.

          before: An item ID to list items before, used for pagination.

          include: Additional fields to include in the response.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: The order to return the input items in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            path_template("/v1/responses/{response_id}/input_items", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "limit": limit,
                        "order": order,
                    },
                    input_item_list_params.InputItemListParams,
                ),
            ),
            cast_to=InputItemListResponse,
        )


class AsyncInputItemsResource(AsyncAPIResource):
    """
    OpenAI Responses API for agent orchestration with tool use, multi-turn conversations, and background processing.
    """

    @cached_property
    def with_raw_response(self) -> AsyncInputItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInputItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInputItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncInputItemsResourceWithStreamingResponse(self)

    async def list(
        self,
        response_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "web_search_call.action.sources",
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Optional[Literal["asc", "desc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InputItemListResponse:
        """
        List input items.

        Args:
          response_id: The ID of the response to retrieve input items for.

          after: An item ID to list items after, used for pagination.

          before: An item ID to list items before, used for pagination.

          include: Additional fields to include in the response.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: The order to return the input items in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            path_template("/v1/responses/{response_id}/input_items", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "limit": limit,
                        "order": order,
                    },
                    input_item_list_params.InputItemListParams,
                ),
            ),
            cast_to=InputItemListResponse,
        )


class InputItemsResourceWithRawResponse:
    def __init__(self, input_items: InputItemsResource) -> None:
        self._input_items = input_items

        self.list = to_raw_response_wrapper(
            input_items.list,
        )


class AsyncInputItemsResourceWithRawResponse:
    def __init__(self, input_items: AsyncInputItemsResource) -> None:
        self._input_items = input_items

        self.list = async_to_raw_response_wrapper(
            input_items.list,
        )


class InputItemsResourceWithStreamingResponse:
    def __init__(self, input_items: InputItemsResource) -> None:
        self._input_items = input_items

        self.list = to_streamed_response_wrapper(
            input_items.list,
        )


class AsyncInputItemsResourceWithStreamingResponse:
    def __init__(self, input_items: AsyncInputItemsResource) -> None:
        self._input_items = input_items

        self.list = async_to_streamed_response_wrapper(
            input_items.list,
        )
