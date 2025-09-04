from langchain.agents import AgentExecutor
from .agent import get_agent_and_tools
from typing import Dict, Any


class AgentExecutorWrapper:
    def __init__(self):
        self._agent_executor = None

    def _create_executor(self) -> AgentExecutor:
        """Create the agent executor."""
        if self._agent_executor is None:
            agent, tools = get_agent_and_tools()
            self._agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        return self._agent_executor

    def invoke(self, query: str) -> Dict[str, Any]:
        """Execute a query using the agent."""
        try:
            executor = self._create_executor()
            result = executor.invoke({"input": query})
            return result
        except Exception as e:
            return {"output": f"Error processing query: {str(e)}", "error": True}

    async def ainvoke(self, query: str) -> Dict[str, Any]:
        """Async execute a query using the agent."""
        try:
            executor = self._create_executor()
            result = await executor.ainvoke({"input": query})
            return result
        except Exception as e:
            return {"output": f"Error processing query: {str(e)}", "error": True}


def get_agent_executor() -> AgentExecutorWrapper:
    """Factory function to get agent executor."""
    return AgentExecutorWrapper()
