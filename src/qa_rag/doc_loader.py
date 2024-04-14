from typing import List

import fitz
from langchain.docstore.document import Document

from src.qa_rag.utils import Validators
from src.qa_rag.request_models import PDFRequest


def read_page_text(page) -> str:
    """Extract text from page block as they appers. Returns cleaned formated page text"""

    page_text = ""
    # Sorts page block as they appear to human eyes. Extracts only text i.e. present 4th index in block tuple

    blocks = page.get_text_blocks(sort=True)
    for block in blocks:
        page_text = page_text + "\n" + block[4].replace("\n", " ")

    return page_text


def pdf_to_langchain_docs(pdf_request: PDFRequest) -> List[Document]:
    """Extracts & format text from pdf pages. Returns list of Langchain document"""

    documents = []
    Validators.validate_file_path(pdf_request.file_path)
    pdf_doc = fitz.open(pdf_request.file_path)

    Validators.validate_page_idxs(
        pdf_request.page_start_idx, pdf_request.page_end_idx, pdf_doc.page_count
    )

    for page_idx, page in enumerate(pdf_doc):
        if pdf_request.page_start_idx <= page_idx <= pdf_request.page_end_idx:
            page_text = read_page_text(page)
            page_meta = {"page_number": page_idx + 1}
            lang_chain_doc = Document(page_content=page_text, metadata=page_meta)

            documents.append(lang_chain_doc)

    return documents
