"""Pydantic request class to be used while maing api request.
Reused in place of parameters for all internal function call of QA Pipeline"""

from uuid import uuid4
from pydantic import BaseModel

from config import *


class PDFRequest(BaseModel):
    file_path: str
    page_start_idx: int
    page_end_idx: int


class ChunkingRequest(BaseModel):
    size: int = 128
    overlap: int = 32


class EmbeddingRequest(BaseModel):
    hf_model_id: str = HUGGING_FACE_EMBEDDING_MODEL_ID


class VectorRetriverRequest(BaseModel):
    collection_name: str = VECTOR_DEFAULT_COLLECTION_NAME


class QaLLMRequest(BaseModel):
    hf_model_id: str = LLM_QA_MODEL_ID
    max_new_tokens: int = 100


class QaRagPipelineRequest(BaseModel):
    pdf: PDFRequest
    chunking: ChunkingRequest
    hf_embedder: EmbeddingRequest
    vector_retriver: VectorRetriverRequest
    qa_llm: QaLLMRequest


class QaRagQueryRequest(BaseModel):
    collection_name: str = VECTOR_DEFAULT_COLLECTION_NAME
    question: str
    answer: str = None
