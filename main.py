import uvicorn
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from config import *
from src.qa_rag.qa_rag_routes import router as QARouter


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/")
def health():
    message = {"message": "OK health", "datetie": datetime.now()}
    return message


app.include_router(QARouter)


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
