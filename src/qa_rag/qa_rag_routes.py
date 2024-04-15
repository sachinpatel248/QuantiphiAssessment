from fastapi import APIRouter, Depends

from src.auth.api_key_auth import validate_user_using_api_key

from src.qa_rag.request_models import QaRagQueryRequest
from src.qa_rag.qa_rag_pipeline import qa_rag_pipe, extract_answer


router = APIRouter()


@router.post("/question", response_model=QaRagQueryRequest)
def question(
    request: QaRagQueryRequest,
    # is_user_authenticated: bool = Depends(validate_user_using_api_key)
):
    # Un comment above line to enable auth via api-key
    request.answer = extract_answer(qa_rag_pipe, request.question)

    return request
