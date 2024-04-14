import os
from os import getenv, makedirs
from os.path import join, dirname, abspath, basename
from posixpath import splitext

import dotenv


env_dir = "env_var_files"
env_file_name = ".env.local"
env_file_path = join(env_dir, env_file_name)

if not os.path.exists(env_file_path):
    raise Exception("Valid .env file path does not exists")

dotenv.load_dotenv(env_file_path)


# API specifics
PORT = int(getenv("PORT"))
HOST = str(getenv("HOST"))

GRADIO_PORT = int(getenv("GRADIO_PORT"))

STATIC_DIR = getenv("STATIC_DIR", "static")
DOWNLOADED_MODEL_DIR = join(os.getcwd(), "downloaded_models")

makedirs(STATIC_DIR, exist_ok=True)
makedirs(DOWNLOADED_MODEL_DIR, exist_ok=True)


# Authentication
API_KEY = getenv("API_KEY")
API_KEY_NAME = getenv("API_KEY_NAME")


# Models
LLM_QA_MODEL_ID = getenv("LLM_QA_MODEL_ID")
HUGGING_FACE_EMBEDDING_MODEL_ID = getenv("HUGGING_FACE_EMBEDDING_MODEL_ID")

# Vector Collection Name
VECTOR_DEFAULT_COLLECTION_NAME = "Biology-Collection"
