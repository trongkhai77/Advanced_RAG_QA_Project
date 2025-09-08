from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging
import uvicorn

from .api.routes import router
from .config import settings
from .core.exceptions import (
    AgentError,
    agent_error_handler,
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup event handler."""
    logger.info("Starting Advanced RAG QA Project...")
    logger.info(f"LangSmith URL: {settings.langsmith_url}")
    logger.info(f"Cohere Model: {settings.cohere_model}")
    logger.info("Application started successfully!")

    yield

    """Shutdown event handler."""
    logger.info("Shutting down Advanced RAG QA Project...")


# Create FastAPI app
app = FastAPI(
    title="Advanced RAG QA Project",
    description="A FastAPI application for RAG-based question answering using multiple tools",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
app.add_exception_handler(AgentError, agent_error_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Include API routes
app.include_router(router, prefix="/api/v1", tags=["RAG Agent"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to the Advanced RAG QA Project",
        "docs_url": "/docs",
        "health_url": "/api/v1/health",
        "query_url": "/api/v1/query",
    }


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host="0.0.0.0", port=8000, reload=True, log_level="info"
    )
