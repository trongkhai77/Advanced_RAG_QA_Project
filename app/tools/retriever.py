from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain.tools.retriever import create_retriever_tool
from .base import BaseTool
from ..config import settings


class RetrieverTool(BaseTool):
    def __init__(self):
        self._tool = None
        self._vectordb = None

    def _create_vector_store(self) -> FAISS:
        """Create and return FAISS vector store."""
        if self._vectordb is None:
            loader = WebBaseLoader(settings.langsmith_url)
            docs = loader.load()

            documents = RecursiveCharacterTextSplitter(
                chunk_size=settings.chunk_size, chunk_overlap=settings.chunk_overlap
            ).split_documents(docs)

            embeddings = CohereEmbeddings(
                model=settings.embedding_model, cohere_api_key=settings.cohere_api_key
            )

            self._vectordb = FAISS.from_documents(documents, embeddings)

        return self._vectordb

    def initialize(self):
        """Initialize retriever tool with vector store."""
        if self._tool is None:
            vectordb = self._create_vector_store()
            retriever = vectordb.as_retriever()

            self._tool = create_retriever_tool(
                retriever,
                "langsmith_search",
                "Search for information about Langsmith. For any questions about LangSmith, you must use this tool",
            )

        return self._tool

    def get_tool(self):
        """Return the retriever tool."""
        return self.initialize()


def get_retriever_tool():
    """Factory function to get retriever tool."""
    return RetrieverTool().get_tool()
