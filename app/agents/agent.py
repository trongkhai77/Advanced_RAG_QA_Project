from langchain_cohere import ChatCohere
from langchain import hub
from langchain.agents import create_openai_tools_agent
from ..config import settings
from ..tools.wikipedia import get_wikipedia_tool
from ..tools.arxiv import get_arxiv_tool
from ..tools.retriever import get_retriever_tool


class Agent:
    def __init__(self):
        self._agent = None
        self._tools = None
        self._llm = None
        self._prompt = None

    def _get_llm(self) -> ChatCohere:
        """Get the LLM instance."""
        if self._llm is None:
            self._llm = ChatCohere(
                model=settings.cohere_model,
                temperature=settings.cohere_temperature,
                cohere_api_key=settings.cohere_api_key,
            )
        return self._llm

    def _get_tools(self) -> list:
        """Get all available tools."""
        if self._tools is None:
            self._tools = [get_wikipedia_tool(), get_arxiv_tool(), get_retriever_tool()]
        return self._tools

    def _get_prompt(self):
        """Get the agent prompt."""
        if self._prompt is None:
            self._prompt = hub.pull("hwchase17/openai-functions-agent")
        return self._prompt

    def create_agent(self):
        """Create and return the agent."""
        if self._agent is None:
            llm = self._get_llm()
            tools = self._get_tools()
            prompt = self._get_prompt()

            self._agent = create_openai_tools_agent(llm, tools, prompt)

        return self._agent

    def get_tools(self) -> list:
        """Get the tools list."""
        return self._get_tools()


def get_agent_and_tools():
    """Factory function to get agent and tools."""
    agent_instance = Agent()
    agent = agent_instance.create_agent()
    tools = agent_instance.get_tools()
    return agent, tools
