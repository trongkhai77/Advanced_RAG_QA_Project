from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from .base import BaseTool
from ..config import settings


class WikipediaTool(BaseTool):
    def __init__(self):
        self._tool = None

    def initialize(self) -> WikipediaQueryRun:
        """Initialize Wikipedia tool with API wrapper."""
        if self._tool is None:
            api_wrapper = WikipediaAPIWrapper(
                top_k_results=settings.wikipedia_top_k_results,
                doc_content_chars_max=settings.wikipedia_doc_content_chars_max,
            )
            self._tool = WikipediaQueryRun(api_wrapper=api_wrapper)
        return self._tool

    def get_tool(self) -> WikipediaQueryRun:
        """Return the Wikipedia tool."""
        return self.initialize()


def get_wikipedia_tool() -> WikipediaQueryRun:
    """Factory function to get Wikipedia tool."""
    return WikipediaTool().get_tool()
