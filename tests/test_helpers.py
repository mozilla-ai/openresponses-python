"""Tests for OpenResponses helper types and functions."""

from unittest.mock import MagicMock


def test_helpers_module_importable():
    """Test that the helpers module can be imported."""
    from openresponses_types import helpers  # noqa: F401


def test_response_alias():
    """Test that Response is an alias for ResponseResource."""
    from openresponses_types.helpers import Response
    from openresponses_types.types import ResponseResource

    assert Response is ResponseResource


def test_response_stream_event_union():
    """Test that ResponseStreamEvent is a union of streaming event types."""
    from openresponses_types.helpers import ResponseStreamEvent

    assert ResponseStreamEvent is not None


def test_mcp_tool_creation():
    """Test MCPTool model creation."""
    from openresponses_types.helpers import MCPTool, MCPToolApproval

    tool = MCPTool(
        server_label="test-server",
        server_url="https://example.com/mcp",
        allowed_tools=["tool1", "tool2"],
        require_approval=MCPToolApproval.ALWAYS,
    )

    assert tool.type == "mcp"
    assert tool.server_label == "test-server"
    assert tool.server_url == "https://example.com/mcp"
    assert tool.allowed_tools == ["tool1", "tool2"]
    assert tool.require_approval == MCPToolApproval.ALWAYS


def test_mcp_tool_with_headers():
    """Test MCPTool with custom headers."""
    from openresponses_types.helpers import MCPTool

    tool = MCPTool(
        server_label="auth-server",
        server_url="https://example.com/mcp",
        headers={"Authorization": "Bearer token123"},
    )

    assert tool.headers == {"Authorization": "Bearer token123"}


def test_mcp_tool_default_approval():
    """Test MCPTool default approval mode."""
    from openresponses_types.helpers import MCPTool, MCPToolApproval

    tool = MCPTool(
        server_label="test",
        server_url="https://example.com",
    )

    assert tool.require_approval == MCPToolApproval.NEVER


def test_reasoning_effort_enum():
    """Test ReasoningEffort enum values."""
    from openresponses_types.helpers import ReasoningEffort

    assert ReasoningEffort.NONE == "none"
    assert ReasoningEffort.LOW == "low"
    assert ReasoningEffort.MEDIUM == "medium"
    assert ReasoningEffort.HIGH == "high"
    assert ReasoningEffort.XHIGH == "xhigh"


def test_item_status_enum():
    """Test ItemStatus enum values."""
    from openresponses_types.helpers import ItemStatus

    assert ItemStatus.IN_PROGRESS == "in_progress"
    assert ItemStatus.COMPLETED == "completed"
    assert ItemStatus.FAILED == "failed"
    assert ItemStatus.INCOMPLETE == "incomplete"


def test_open_responses_stream_event_type_enum():
    """Test OpenResponsesStreamEventType enum values."""
    from openresponses_types.helpers import OpenResponsesStreamEventType

    assert OpenResponsesStreamEventType.RESPONSE_CREATED == "response.created"
    assert OpenResponsesStreamEventType.RESPONSE_COMPLETED == "response.completed"
    assert OpenResponsesStreamEventType.OUTPUT_TEXT_DELTA == "response.output_text.delta"


def test_responses_params():
    """Test ResponsesParams model creation."""
    from openresponses_types.helpers import ResponsesParams

    params = ResponsesParams(
        model="gpt-4",
        input="Hello!",
        temperature=0.7,
        max_output_tokens=1000,
    )

    assert params.model == "gpt-4"
    assert params.input == "Hello!"
    assert params.temperature == 0.7
    assert params.max_output_tokens == 1000


def test_responses_params_with_tools():
    """Test ResponsesParams with tools."""
    from openresponses_types.helpers import MCPTool, ResponsesParams

    mcp_tool = MCPTool(
        server_label="test",
        server_url="https://example.com",
    )

    params = ResponsesParams(
        model="gpt-4",
        input="Hello!",
        tools=[mcp_tool],
    )

    assert params.tools is not None
    assert len(params.tools) == 1


def test_get_output_text_with_text_content():
    """Test get_output_text extracts text from response."""
    from openresponses_types.helpers import Response, get_output_text

    mock_content = MagicMock()
    mock_content.type = "output_text"
    mock_content.text = "Hello, world!"

    mock_message = MagicMock()
    mock_message.type = "message"
    mock_message.content = [mock_content]

    mock_response = MagicMock(spec=Response)
    mock_response.output = [mock_message]

    result = get_output_text(mock_response)
    assert result == "Hello, world!"


def test_get_output_text_concatenates_multiple():
    """Test get_output_text concatenates multiple text blocks."""
    from openresponses_types.helpers import Response, get_output_text

    mock_content1 = MagicMock()
    mock_content1.type = "output_text"
    mock_content1.text = "Hello, "

    mock_content2 = MagicMock()
    mock_content2.type = "output_text"
    mock_content2.text = "world!"

    mock_message = MagicMock()
    mock_message.type = "message"
    mock_message.content = [mock_content1, mock_content2]

    mock_response = MagicMock(spec=Response)
    mock_response.output = [mock_message]

    result = get_output_text(mock_response)
    assert result == "Hello, world!"


def test_get_output_text_empty_response():
    """Test get_output_text with empty response."""
    from openresponses_types.helpers import Response, get_output_text

    mock_response = MagicMock(spec=Response)
    mock_response.output = []

    result = get_output_text(mock_response)
    assert result == ""


def test_get_output_text_ignores_non_text():
    """Test get_output_text ignores non-text content."""
    from openresponses_types.helpers import Response, get_output_text

    mock_text_content = MagicMock()
    mock_text_content.type = "output_text"
    mock_text_content.text = "Text content"

    mock_image_content = MagicMock()
    mock_image_content.type = "image"

    mock_message = MagicMock()
    mock_message.type = "message"
    mock_message.content = [mock_image_content, mock_text_content]

    mock_response = MagicMock(spec=Response)
    mock_response.output = [mock_message]

    result = get_output_text(mock_response)
    assert result == "Text content"


def test_backward_compatible_aliases():
    """Test backward-compatible type aliases exist."""
    from openresponses_types.helpers import (
        FunctionTool,
        GeneratedReasoningEffort,
        OpenResponsesReasoningConfig,
        OpenResponsesReasoningItem,
        OpenResponsesRequestBody,
        OpenResponsesResponse,
        ReasoningDeltaEvent,
        ReasoningSummaryDeltaEvent,
    )

    assert OpenResponsesReasoningConfig is not None
    assert OpenResponsesReasoningItem is not None
    assert FunctionTool is not None
    assert ReasoningDeltaEvent is not None
    assert ReasoningSummaryDeltaEvent is not None
    assert OpenResponsesResponse is not None
    assert OpenResponsesRequestBody is not None
    assert GeneratedReasoningEffort is not None
