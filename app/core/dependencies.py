from fastapi import Depends
from ..services.query_service import QueryService, get_query_service
from ..config import settings


def get_settings():
    """Dependency to get application settings."""
    return settings


def get_query_service_dependency() -> QueryService:
    """Dependency to get query service instance."""
    return get_query_service()


# Dependency aliases for better organization
Settings = Depends(get_settings)
QueryServiceDep = Depends(get_query_service_dependency)
