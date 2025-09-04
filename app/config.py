from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    cohere_api_key: str
    langsmith_url: str = "https://docs.smith.langchain.com/"
    vector_store_path: Optional[str] = None

    # Wikipedia settings
    wikipedia_top_k_results: int = 1
    wikipedia_doc_content_chars_max: int = 200

    # Arxiv settings
    arxiv_top_k_results: int = 1
    arxiv_doc_content_chars_max: int = 200

    # Text splitter settings
    chunk_size: int = 1000
    chunk_overlap: int = 200

    # LLM settings
    cohere_model: str = "command-r-plus"
    cohere_temperature: float = 0

    # Embedding settings
    embedding_model: str = "embed-multilingual-v3.0"

    class Config:
        env_file = ".env"


settings = Settings()
