from typing import List

from langchain.docstore.document import Document
from langchain_text_splitters import TokenTextSplitter

from src.qa_rag.request_models import ChunkingRequest


def split_documents(
    documents: List[Document], chunking: ChunkingRequest
) -> List[Document]:

    doc_splitter = TokenTextSplitter(
        chunk_size=chunking.size, chunk_overlap=chunking.overlap
    )

    splitted_documents = doc_splitter.split_documents(documents)

    return splitted_documents
