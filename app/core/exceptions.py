from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger(__name__)


class AgentError(Exception):
    """Base exception for agent-related errors."""

    def __init__(self, message: str, error_type: str = "AgentError"):
        self.message = message
        self.error_type = error_type
        super().__init__(self.message)


class ToolInitializationError(AgentError):
    """Exception raised when tool initialization fails."""

    def __init__(self, tool_name: str, message: str):
        self.tool_name = tool_name
        super().__init__(
            f"Tool '{tool_name}' initialization failed: {message}",
            "ToolInitializationError",
        )


class QueryProcessingError(AgentError):
    """Exception raised when query processing fails."""

    def __init__(self, message: str):
        super().__init__(f"Query processing failed: {message}", "QueryProcessingError")


class ConfigurationError(AgentError):
    """Exception raised when configuration is invalid."""

    def __init__(self, message: str):
        super().__init__(f"Configuration error: {message}", "ConfigurationError")


async def agent_error_handler(request: Request, exc: AgentError):
    """Handle agent-specific errors."""
    logger.error(f"Agent error: {exc.error_type} - {exc.message}")
    return JSONResponse(
        status_code=500, content={"detail": exc.message, "error_type": exc.error_type}
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors."""
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error",
            "error_type": "ValidationError",
            "errors": exc.errors(),
        },
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Handle HTTP exceptions."""
    logger.error(f"HTTP error {exc.status_code}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "error_type": "HTTPError"},
    )


async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {type(exc).__name__} - {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected error occurred",
            "error_type": type(exc).__name__,
        },
    )
