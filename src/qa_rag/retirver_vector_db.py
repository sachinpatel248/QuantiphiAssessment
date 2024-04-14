from typing import List

from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_vector_retriver(
    documents: List[Document],
    embedder: HuggingFaceEmbeddings,
    collection_name: str = "bio_vector_db",
):

    vector_store = Chroma.from_documents(
        documents=documents, embedding=embedder, collection_name=collection_name
    )

    vector_retriever = vector_store.as_retriever()

    return vector_retriever
