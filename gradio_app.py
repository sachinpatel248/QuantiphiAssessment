from typing import List, Tuple


from gradio import Number, Textbox, DataFrame, Button, Info
from gradio import Tab, Markdown, Examples, File, Column, Dropdown
from gradio import Row, Dropdown, Blocks, Label, Slider, HighlightedText


from config import *
from src.qa_rag.qa_rag_pipeline import qa_rag_pipe, extract_answer


heading = """<h1 style="text-align: center;">QnA RAG Pipeline</h1>"""

more_info = """<h3>Pdf file available at <a href="https://assets.openstax.org/oscms-prodcms/media/documents/ConceptsofBiology-WEB.pdf">URL</a>. By default it process first 2 chapter from page number 19 to 68 of pdf.</h3>
"""

parameter_values = """<h4>Current parameters (uneditable)</h4>"""


question_examples = [
    "How many American men were diagnosed with syphilis and in which year?"
]


def get_answer(question: str) -> str:
    answer = extract_answer(qa_rag_pipe, question)
    return answer


with Blocks(title="QnA RAG Pipeline") as demo:
    Markdown(heading)
    Markdown(more_info)

    text_box_question = Textbox(
        lines=2,
        label="Question",
        placeholder="Enter question",
        value=question_examples[0],
        show_label=True,
        show_copy_button=True,
        interactive=True,
    )

    # region Parameters

    Markdown(parameter_values)
    with Row():
        chapters = Textbox(
            lines=1,
            label="Chapters",
            value="Chapters 1 & 2",
            interactive=False,
        )

        start_idx = Number(18, label="Page start index", interactive=False)
        end_idx = Number(68, label="Page end index", interactive=False)

        size = Number(128, label="Token chunk size", interactive=False)
        overlap = Number(32, label="Token chunk overlap", interactive=False)

        embedding_model_name = Textbox(
            lines=1,
            label="Embedding model name",
            value=HUGGING_FACE_EMBEDDING_MODEL_ID.split("/")[1],
            interactive=False,
        )

        qa_llm = Textbox(
            lines=1,
            label="QA LLM",
            value=LLM_QA_MODEL_ID.split("/")[1],
            interactive=False,
        )

    # endregion

    button_submit = Button("Submit")

    text_box_answer = Textbox(
        lines=2,
        label="Answer",
        placeholder="",
        value="",
        show_label=True,
        show_copy_button=True,
    )

    button_submit.click(get_answer, text_box_question, text_box_answer)


demo.queue(max_size=2)

if __name__ == "__main__":
    demo.launch(server_name=HOST, server_port=GRADIO_PORT)
