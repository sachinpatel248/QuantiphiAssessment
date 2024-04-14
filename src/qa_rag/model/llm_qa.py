import os
from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

from langchain_community.llms import HuggingFacePipeline

from src.qa_rag.utils import create_model_path
from src.qa_rag.request_models import QaLLMRequest


def get_qa_llm_pipe(lllm_qa_request: QaLLMRequest) -> HuggingFacePipeline:

    hf_qa_pipe = None
    llm_qa_model_id = lllm_qa_request.hf_model_id
    max_new_tokens = lllm_qa_request.max_new_tokens

    model_path = create_model_path(llm_qa_model_id)

    if os.path.exists(model_path):
        print(f"Loading HuggingFace LLM from local dir {model_path}")
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
    else:
        print(f"Downloading HuggingFace LLM")
        tokenizer = AutoTokenizer.from_pretrained(llm_qa_model_id)
        model = AutoModelForCausalLM.from_pretrained(llm_qa_model_id)

        print("Storing HuggingFace LLM to local dir")
        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)

    # Adjust other params as needed
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device_map="auto",
        max_new_tokens=max_new_tokens,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        return_full_text=False,
    )

    hf_qa_pipe = HuggingFacePipeline(pipeline=pipe)

    return hf_qa_pipe
