"""Tests for generated OpenResponses types."""

import pytest
from pydantic import ValidationError


def test_types_module_importable():
    """Test that the types module can be imported."""
    from openresponses_types import types  # noqa: F401


def test_response_resource_creation():
    """Test that ResponseResource can be instantiated with valid data."""
    from openresponses_types.types import ResponseResource, TextField, TextResponseFormat

    response = ResponseResource(
        id="resp_123",
        object="response",
        created_at=1234567890,
        completed_at=1234567891,
        status="completed",
        incomplete_details=None,
        model="gpt-4",
        previous_response_id=None,
        instructions=None,
        output=[],
        error=None,
        tools=[],
        tool_choice="auto",
        truncation="auto",
        parallel_tool_calls=True,
        text=TextField(format=TextResponseFormat(type="text")),
        top_p=1.0,
        presence_penalty=0.0,
        frequency_penalty=0.0,
        top_logprobs=0,
        temperature=0.7,
        reasoning=None,
        usage=None,
        max_output_tokens=None,
        max_tool_calls=None,
        store=False,
        background=False,
        service_tier="default",
        metadata={},
        safety_identifier=None,
        prompt_cache_key=None,
    )

    assert response.id == "resp_123"
    assert response.model == "gpt-4"
    assert response.status == "completed"


def test_create_response_body():
    """Test that CreateResponseBody validates correctly."""
    from openresponses_types.types import CreateResponseBody

    body = CreateResponseBody(
        model="gpt-4",
        input="Hello, world!",
    )

    assert body.model == "gpt-4"
    # input is wrapped in an Input RootModel
    assert body.input.root == "Hello, world!"


def test_input_text_content_param():
    """Test InputTextContentParam validation."""
    from openresponses_types.types import InputTextContentParam

    content = InputTextContentParam(
        type="input_text",
        text="Hello!",
    )

    assert content.type == "input_text"
    assert content.text == "Hello!"


def test_user_message_item_param():
    """Test UserMessageItemParam validation."""
    from openresponses_types.types import InputTextContentParam, UserMessageItemParam

    message = UserMessageItemParam(
        type="message",
        role="user",
        content=[
            InputTextContentParam(
                type="input_text",
                text="Hello!",
            )
        ],
    )

    assert message.type == "message"
    assert message.role == "user"
    assert len(message.content) == 1


def test_function_tool_param():
    """Test FunctionToolParam validation."""
    from openresponses_types.types import FunctionToolParam

    tool = FunctionToolParam(
        type="function",
        name="get_weather",
        description="Get weather for a location",
        parameters={"type": "object", "properties": {}},
    )

    assert tool.type == "function"
    assert tool.name == "get_weather"


def test_reasoning_param():
    """Test ReasoningParam validation."""
    from openresponses_types.types import ReasoningParam

    reasoning = ReasoningParam(
        effort="medium",
    )

    assert reasoning.effort == "medium"


def test_streaming_event_types_exist():
    """Test that streaming event types are defined."""
    from openresponses_types.types import (
        ResponseCompletedStreamingEvent,
        ResponseCreatedStreamingEvent,
        ResponseFailedStreamingEvent,
        ResponseInProgressStreamingEvent,
        ResponseOutputTextDeltaStreamingEvent,
    )

    assert ResponseCreatedStreamingEvent is not None
    assert ResponseInProgressStreamingEvent is not None
    assert ResponseCompletedStreamingEvent is not None
    assert ResponseFailedStreamingEvent is not None
    assert ResponseOutputTextDeltaStreamingEvent is not None


def test_invalid_model_raises_validation_error():
    """Test that invalid data raises ValidationError."""
    from openresponses_types.types import InputTextContentParam

    with pytest.raises(ValidationError):
        InputTextContentParam(
            type="invalid_type",
            text="Hello!",
        )


def _minimal_response_resource_kwargs():
    """Return the required scalar fields for a ResponseResource, minus `output`."""
    from openresponses_types.types import TextField, TextResponseFormat

    return {
        "id": "resp_123",
        "object": "response",
        "created_at": 1234567890,
        "completed_at": 1234567891,
        "status": "completed",
        "incomplete_details": None,
        "model": "gpt-4",
        "previous_response_id": None,
        "instructions": None,
        "error": None,
        "tools": [],
        "tool_choice": "auto",
        "truncation": "auto",
        "parallel_tool_calls": True,
        "text": TextField(format=TextResponseFormat(type="text")),
        "top_p": 1.0,
        "presence_penalty": 0.0,
        "frequency_penalty": 0.0,
        "top_logprobs": 0,
        "temperature": 0.7,
        "reasoning": None,
        "usage": None,
        "max_output_tokens": None,
        "max_tool_calls": None,
        "store": False,
        "background": False,
        "service_tier": "default",
        "metadata": {},
        "safety_identifier": None,
        "prompt_cache_key": None,
    }


def test_response_resource_output_accepts_compaction_item():
    """A `compaction` output item validates as part of ResponseResource.output."""
    from openresponses_types.types import CompactionBody, ResponseResource

    response = ResponseResource.model_validate(
        {
            **_minimal_response_resource_kwargs(),
            "output": [
                {
                    "type": "compaction",
                    "id": "cmp_1",
                    "encrypted_content": "encrypted-blob",
                    "created_by": "resp_0",
                }
            ],
        }
    )

    assert len(response.output) == 1
    item = response.output[0]
    assert isinstance(item, CompactionBody)
    assert item.type == "compaction"
    assert item.id == "cmp_1"
    assert item.encrypted_content == "encrypted-blob"
    assert item.created_by == "resp_0"


def test_compaction_body_created_by_is_optional():
    """`created_by` is the only optional field on CompactionBody."""
    from openresponses_types.types import CompactionBody

    body = CompactionBody(type="compaction", id="cmp_1", encrypted_content="enc")

    assert body.created_by is None


def test_create_response_body_input_accepts_compaction_summary_item():
    """A `compaction` input item validates in CreateResponseBody.input."""
    from openresponses_types.types import CompactionSummaryItemParam, CreateResponseBody

    body = CreateResponseBody.model_validate(
        {
            "model": "gpt-4",
            "input": [{"type": "compaction", "id": "cmp_1", "encrypted_content": "enc"}],
        }
    )

    assert isinstance(body.input[0], CompactionSummaryItemParam)
    assert body.input[0].encrypted_content == "enc"
