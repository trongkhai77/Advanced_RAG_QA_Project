from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

"""## API wrapper
- this is basically use to query answer from wikipedia
"""

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

wiki.name

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import cohere
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
os.environ["COHERE_API_KEY"] = api_key

loader = WebBaseLoader("https://docs.smith.langchain.com/")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)

vectordb = FAISS.from_documents(
    documents, CohereEmbeddings(model="embed-multilingual-v3.0", cohere_api_key=api_key)
)
# Tạo retriever
retriever = vectordb.as_retriever()

from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about Langsmith. For any questions about LangSmith, you must use this tool",
)

retriever_tool.name

"""## Arxiv Tool"""

from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun

arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(arxiv_wrapper=arxiv_wrapper)
arxiv.name

"""## Combine All Tools"""

tools = [wiki, arxiv, retriever_tool]

tools

"""## Agents
- The core idea of agents is to use a language model to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.
[Learn more](https://python.langchain.com/v0.1/docs/modules/agents/)
"""
from langchain_cohere import ChatCohere

llm = ChatCohere(model="command-r-plus", temperature=0, cohere_api_key=api_key)

from langchain import hub

prompt = hub.pull("hwchase17/openai-functions-agent")
prompt.messages

from langchain.agents import create_openai_tools_agent

agent = create_openai_tools_agent(llm, tools, prompt)

"""## Agent Executor"""

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor

response = agent_executor.invoke({"input": "What's the paper 1605.08386 about?"})

print(response)
