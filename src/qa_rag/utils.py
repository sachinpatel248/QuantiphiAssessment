import os
import requests

from config import DOWNLOADED_MODEL_DIR, STATIC_DIR


def create_model_path(model_id: str) -> str:
    os.makedirs(DOWNLOADED_MODEL_DIR, exist_ok=True)
    model_id = model_id.replace("-", "_").replace("/", "__")
    file_path = os.path.join(DOWNLOADED_MODEL_DIR, model_id)
    return file_path


def create_file_path(file_name: str) -> str:
    os.makedirs(STATIC_DIR, exist_ok=True)
    file_path = os.path.join(STATIC_DIR, file_name)
    return file_path


def download_file(url: str, file_name: str) -> str:
    file_path = create_file_path(file_name)
    if not os.path.exists(file_path):
        print("Downloading file from url")
        response = requests.get(url)
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Downloaded file at {file_path}")

    return file_path


class Validators:
    @classmethod
    def validate_file_path(cls, file_path: str):
        if not isinstance(file_path, str):
            raise ValueError("File path is not str type")

        if not os.path.exists(file_path):
            raise ValueError("Not a valid file path")

    @classmethod
    def validate_page_idxs(
        cls, page_start_idx: int, page_end_idx: int, total_page_count: int
    ):
        if not isinstance(page_start_idx, int):
            raise ValueError("page_start_idx not int type")
        if not isinstance(page_end_idx, int):
            raise ValueError("page_end_idx not int type")
        if not isinstance(total_page_count, int):
            raise ValueError("total_page_count not int type")

        if not (0 <= page_start_idx < total_page_count):
            raise ValueError("Page start index must be between 0 and total page count.")

        if not (page_start_idx <= page_end_idx < total_page_count):
            raise ValueError(
                "Page end index must be between page start index and total page count."
            )


# Downloading file by default if not exists in static dir

pdf_file_name = "ConceptsofBiology-WEB.pdf"
pdf_url = "https://assets.openstax.org/oscms-prodcms/media/documents/ConceptsofBiology-WEB.pdf"

pdf_file_path = download_file(pdf_url, pdf_file_name)
