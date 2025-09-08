from fastapi import APIRouter, Depends, HTTPException, status
from ..models import QueryRequest, QueryResponse, HealthResponse, ErrorResponse
from ..services.query_service import get_query_service, QueryService
from .background_tasks_routes import background_tasks_router
import logging

logger = logging.getLogger(__name__)

router = APIRouter()
router.include_router(background_tasks_router)


@router.post(
    "/query",
    response_model=QueryResponse,
    responses={
        500: {"model": ErrorResponse, "description": "Internal server error"},
        422: {"model": ErrorResponse, "description": "Validation error"},
    },
    summary="Process a query",
    description="Process a natural language query using the RAG agent with multiple tools",
)
async def query(
    request: QueryRequest, service: QueryService = Depends(get_query_service)
) -> QueryResponse:
    """Process a query using the RAG agent."""
    try:
        result = await service.process_query_async(request.input)
        return QueryResponse(**result)
    except Exception as e:
        logger.error(f"Error in query endpoint: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your query: {str(e)}",
        )


@router.post(
    "/query/sync",
    response_model=QueryResponse,
    responses={
        500: {"model": ErrorResponse, "description": "Internal server error"},
        422: {"model": ErrorResponse, "description": "Validation error"},
    },
    summary="Process a query synchronously",
    description="Process a natural language query synchronously using the RAG agent",
)
def query_sync(
    request: QueryRequest, service: QueryService = Depends(get_query_service)
) -> QueryResponse:
    """Process a query synchronously using the RAG agent."""
    try:
        result = service.process_query(request.input)
        return QueryResponse(**result)
    except Exception as e:
        logger.error(f"Error in sync query endpoint: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your query: {str(e)}",
        )


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    description="Check the health status of the service and list available tools",
)
async def health_check(
    service: QueryService = Depends(get_query_service),
) -> HealthResponse:
    """Health check endpoint."""
    try:
        tools = service.get_available_tools()
        return HealthResponse(status="healthy", tools_available=tools)
    except Exception as e:
        logger.error(f"Error in health check: {str(e)}")
        return HealthResponse(status="unhealthy", tools_available=[])


@router.get(
    "/tools",
    response_model=dict,
    summary="List available tools",
    description="Get detailed information about available tools",
)
async def list_tools(service: QueryService = Depends(get_query_service)) -> dict:
    """List all available tools with descriptions."""
    try:
        tools = service.get_available_tools()
        return {
            "tools": [
                {
                    "name": "Wikipedia",
                    "description": "Search Wikipedia for information",
                    "active": "Wikipedia" in tools if tools else False,
                },
                {
                    "name": "Arxiv",
                    "description": "Search academic papers from Arxiv",
                    "active": "Arxiv" in tools if tools else False,
                },
                {
                    "name": "LangSmith Search",
                    "description": "Search LangSmith documentation",
                    "active": "langsmith_search" in tools if tools else False,
                },
            ],
            "total": len(tools) if tools else 0,
        }
    except Exception as e:
        logger.error(f"Error listing tools: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving tools information",
        )
