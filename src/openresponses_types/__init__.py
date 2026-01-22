"""OpenResponses Types - Python SDK for OpenResponses specification.

This package provides Pydantic models for the OpenResponses API specification,
enabling type-safe interaction with OpenResponses-compatible LLM providers.

Example usage:
    from openresponses_types import Response, ResponseStreamEvent, get_output_text

    # Type hints for responses
    response: Response = ...
    text = get_output_text(response)

    # Type hints for streaming events
    event: ResponseStreamEvent = ...
"""

__version__ = "0.1.0"
__spec_hash__ = "915047617fddd639c691fe1e00d5ba6917b7187d7abc62adf074fd7c823bad7f"

# Re-export all types from generated module
# Note: These imports will fail until types.py is generated
try:
    from openresponses_types.helpers import (
        FunctionTool,
        GeneratedReasoningEffort,
        ItemStatus,
        MCPTool,
        MCPToolApproval,
        OpenResponsesReasoningConfig,
        OpenResponsesReasoningItem,
        OpenResponsesRequestBody,
        OpenResponsesResponse,
        OpenResponsesStreamEventType,
        ReasoningDeltaEvent,
        ReasoningEffort,
        ReasoningSummaryDeltaEvent,
        Response,
        ResponseInputParam,
        ResponsesParams,
        ResponseStreamEvent,
        get_output_text,
    )
    from openresponses_types.types import (
        AssistantMessageItemParam,
        CreateResponseBody,
        DeveloperMessageItemParam,
        FunctionCall,
        FunctionCallItemParam,
        FunctionCallOutput,
        FunctionCallOutputItemParam,
        FunctionToolParam,
        Input,
        InputFileContentParam,
        InputImageContentParamAutoParam,
        InputTextContentParam,
        ItemReferenceParam,
        Message,
        ReasoningBody,
        ReasoningEffortEnum,
        ReasoningItemParam,
        ReasoningParam,
        ReasoningSummaryContentParam,
        ResponseCompletedStreamingEvent,
        ResponseContentPartAddedStreamingEvent,
        ResponseContentPartDoneStreamingEvent,
        ResponseCreatedStreamingEvent,
        ResponseFailedStreamingEvent,
        ResponseFunctionCallArgumentsDeltaStreamingEvent,
        ResponseFunctionCallArgumentsDoneStreamingEvent,
        ResponseIncompleteStreamingEvent,
        ResponseInProgressStreamingEvent,
        ResponseOutputItemAddedStreamingEvent,
        ResponseOutputItemDoneStreamingEvent,
        ResponseOutputTextAnnotationAddedStreamingEvent,
        ResponseOutputTextDeltaStreamingEvent,
        ResponseOutputTextDoneStreamingEvent,
        ResponseQueuedStreamingEvent,
        ResponseReasoningDeltaStreamingEvent,
        ResponseReasoningDoneStreamingEvent,
        ResponseReasoningSummaryDeltaStreamingEvent,
        ResponseReasoningSummaryDoneStreamingEvent,
        ResponseReasoningSummaryPartAddedStreamingEvent,
        ResponseReasoningSummaryPartDoneStreamingEvent,
        ResponseRefusalDeltaStreamingEvent,
        ResponseRefusalDoneStreamingEvent,
        ResponseResource,
        SystemMessageItemParam,
        UserMessageItemParam,
    )

    __all__ = [
        # Version info
        "__version__",
        "__spec_hash__",
        # Main types
        "Response",
        "ResponseResource",
        "CreateResponseBody",
        "ResponseStreamEvent",
        "ResponseInputParam",
        # Message types
        "Message",
        "UserMessageItemParam",
        "SystemMessageItemParam",
        "DeveloperMessageItemParam",
        "AssistantMessageItemParam",
        # Content types
        "InputTextContentParam",
        "InputImageContentParamAutoParam",
        "InputFileContentParam",
        "Input",
        # Function/tool types
        "FunctionCall",
        "FunctionCallOutput",
        "FunctionCallItemParam",
        "FunctionCallOutputItemParam",
        "FunctionToolParam",
        "FunctionTool",
        # Reasoning types
        "ReasoningBody",
        "ReasoningParam",
        "ReasoningItemParam",
        "ReasoningEffort",
        "ReasoningEffortEnum",
        "ReasoningSummaryContentParam",
        # Item types
        "ItemReferenceParam",
        "ItemStatus",
        # Streaming event types
        "ResponseCreatedStreamingEvent",
        "ResponseQueuedStreamingEvent",
        "ResponseInProgressStreamingEvent",
        "ResponseCompletedStreamingEvent",
        "ResponseFailedStreamingEvent",
        "ResponseIncompleteStreamingEvent",
        "ResponseOutputItemAddedStreamingEvent",
        "ResponseOutputItemDoneStreamingEvent",
        "ResponseContentPartAddedStreamingEvent",
        "ResponseContentPartDoneStreamingEvent",
        "ResponseOutputTextDeltaStreamingEvent",
        "ResponseOutputTextDoneStreamingEvent",
        "ResponseRefusalDeltaStreamingEvent",
        "ResponseRefusalDoneStreamingEvent",
        "ResponseFunctionCallArgumentsDeltaStreamingEvent",
        "ResponseFunctionCallArgumentsDoneStreamingEvent",
        "ResponseReasoningSummaryPartAddedStreamingEvent",
        "ResponseReasoningSummaryPartDoneStreamingEvent",
        "ResponseReasoningSummaryDeltaStreamingEvent",
        "ResponseReasoningSummaryDoneStreamingEvent",
        "ResponseReasoningDeltaStreamingEvent",
        "ResponseReasoningDoneStreamingEvent",
        "ResponseOutputTextAnnotationAddedStreamingEvent",
        # MCP types
        "MCPTool",
        "MCPToolApproval",
        # Utility types
        "ResponsesParams",
        "OpenResponsesStreamEventType",
        # Backward-compatible aliases
        "OpenResponsesReasoningConfig",
        "OpenResponsesReasoningItem",
        "OpenResponsesResponse",
        "OpenResponsesRequestBody",
        "GeneratedReasoningEffort",
        "ReasoningDeltaEvent",
        "ReasoningSummaryDeltaEvent",
        # Helper functions
        "get_output_text",
    ]
except ImportError:
    # types.py not yet generated - this is expected during initial setup
    __all__ = ["__version__", "__spec_hash__"]
