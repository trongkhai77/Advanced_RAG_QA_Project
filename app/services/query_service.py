from typing import Dict, Any, List
from ..agents.executor import get_agent_executor
import logging

logger = logging.getLogger(__name__)


class QueryService:
    def __init__(self):
        self._agent_executor = None

    def _get_executor(self):
        """Get the agent executor instance."""
        if self._agent_executor is None:
            self._agent_executor = get_agent_executor()
        return self._agent_executor

    def process_query(self, query: str) -> Dict[str, Any]:
        """Process a query synchronously."""
        try:
            logger.info(f"Processing query: {query}")
            executor = self._get_executor()
            result = executor.invoke(query)

            response = {
                "output": result.get("output", ""),
                "intermediate_steps": result.get("intermediate_steps", []),
                "error": result.get("error", False),
            }

            logger.info(f"Query processed successfully")
            return response

        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return {
                "output": f"An error occurred while processing your query: {str(e)}",
                "intermediate_steps": [],
                "error": True,
            }

    async def process_query_async(self, query: str) -> Dict[str, Any]:
        """Process a query asynchronously."""
        try:
            logger.info(f"Processing async query: {query}")
            executor = self._get_executor()
            result = await executor.ainvoke(query)

            response = {
                "output": result.get("output", ""),
                "intermediate_steps": result.get("intermediate_steps", []),
                "error": result.get("error", False),
            }

            logger.info(f"Async query processed successfully")
            return response

        except Exception as e:
            logger.error(f"Error processing async query: {str(e)}")
            return {
                "output": f"An error occurred while processing your query: {str(e)}",
                "intermediate_steps": [],
                "error": True,
            }

    def get_available_tools(self) -> List[str]:
        """Get list of available tools."""
        try:
            from ..agents.agent import Agent

            agent_instance = Agent()
            tools = agent_instance.get_tools()
            return [tool.name for tool in tools]
        except Exception as e:
            logger.error(f"Error getting available tools: {str(e)}")
            return []


def get_query_service() -> QueryService:
    """Factory function to get query service."""
    return QueryService()
