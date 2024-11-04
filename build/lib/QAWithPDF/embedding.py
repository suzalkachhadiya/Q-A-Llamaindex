from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import Settings, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import CustomException
from logger import logging

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("embeDDIng starteD")
        
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        Settings.llm = model
        Settings.embed_model = gemini_embed_model        

        logging.info("vectorstore starteD")
        index = VectorStoreIndex.from_documents(document,service_context=service_context)
        index.storage_context.persist()
        
        logging.info("query engine starteD")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise CustomException(e,sys)