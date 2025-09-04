from pydantic import BaseModel, Field
from typing import Dict, Any, List


class QueryRequest(BaseModel):
    input: str = Field(..., description="The query to process", min_length=1)

    class Config:
        json_schema_extra = {"example": {"input": "What's the paper 1605.08386 about?"}}


class QueryResponse(BaseModel):
    output: str = Field(..., description="The response from the agent")
    intermediate_steps: List[Dict[str, Any]] = Field(
        default=[], description="Intermediate steps taken by the agent"
    )
    error: bool = Field(default=False, description="Whether an error occurred")

    class Config:
        json_schema_extra = {
            "example": {
                "output": "The paper 1605.08386 is about...",
                "intermediate_steps": [],
                "error": False,
            }
        }


class HealthResponse(BaseModel):
    status: str = Field(..., description="Health status of the service")
    tools_available: List[str] = Field(
        default=[], description="List of available tools"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "status": "healthy",
                "tools_available": ["Wikipedia", "Arxiv", "LangSmith Search"],
            }
        }


class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Error message")
    error_type: str = Field(default="Unknown", description="Type of error")

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "An error occurred while processing the request",
                "error_type": "ValidationError",
            }
        }
