from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from .base import BaseTool
from ..config import settings


class ArxivTool(BaseTool):
    def __init__(self):
        self._tool = None

    def initialize(self) -> ArxivQueryRun:
        """Initialize Arxiv tool with API wrapper."""
        if self._tool is None:
            arxiv_wrapper = ArxivAPIWrapper(
                top_k_results=settings.arxiv_top_k_results,
                doc_content_chars_max=settings.arxiv_doc_content_chars_max,
            )
            self._tool = ArxivQueryRun(arxiv_wrapper=arxiv_wrapper)
        return self._tool

    def get_tool(self) -> ArxivQueryRun:
        """Return the Arxiv tool."""
        return self.initialize()


def get_arxiv_tool() -> ArxivQueryRun:
    """Factory function to get Arxiv tool."""
    return ArxivTool().get_tool()
