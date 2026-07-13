from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from App.rag import ask

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Question(BaseModel):
    question: str

@app.post("/chat")
def chatbot(data: Question):

    answer = ask(data.question)

    return {
        "answer": answer
    }