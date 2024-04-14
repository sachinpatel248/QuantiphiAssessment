from langchain.chains import RetrievalQA


from src.qa_rag.utils import pdf_file_path

from src.qa_rag.request_models import *

from src.qa_rag.doc_loader import pdf_to_langchain_docs
from src.qa_rag.doc_splitter import split_documents
from src.qa_rag.model.embedder import get_hf_embedder
from src.qa_rag.model.llm_qa import get_qa_llm_pipe
from src.qa_rag.retirver_vector_db import get_vector_retriver


def create_qa_rag_pipeline(qa_request: QaRagPipelineRequest):
    documents = pdf_to_langchain_docs(qa_request.pdf)
    splitted_documents = split_documents(documents, qa_request.chunking)
    hf_embedder = get_hf_embedder(qa_request.hf_embedder.hf_model_id)

    vector_retriver = get_vector_retriver(
        splitted_documents, hf_embedder, qa_request.vector_retriver.collection_name
    )

    hf_qa_pipe = get_qa_llm_pipe(qa_request.qa_llm)

    qa_rag_pipeline = RetrievalQA.from_chain_type(
        llm=hf_qa_pipe,
        chain_type="stuff",
        retriever=vector_retriver,
        verbose=True,
        return_source_documents=True,
    )

    return qa_rag_pipeline


def load_default_pipe():
    qa_rag_request = QaRagPipelineRequest(
        pdf=PDFRequest(file_path=pdf_file_path, page_start_idx=18, page_end_idx=68),
        chunking=ChunkingRequest(),
        hf_embedder=EmbeddingRequest(),
        vector_retriver=VectorRetriverRequest(),
        qa_llm=QaLLMRequest(),
    )

    qa_pipe = create_qa_rag_pipeline(qa_rag_request)

    return qa_pipe


def extract_answer(qa_pipe, question: str) -> QaRagQueryRequest:
    response = qa_pipe.invoke(question)
    answer = response["result"].strip()

    return answer


qa_rag_pipe = None
qa_rag_pipe = load_default_pipe()
