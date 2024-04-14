from langchain_community.embeddings import HuggingFaceEmbeddings

from config import *


def get_hf_embedder(hf_model_id: str) -> HuggingFaceEmbeddings:
    hf_embedder = HuggingFaceEmbeddings(model_name=hf_model_id)

    return hf_embedder
