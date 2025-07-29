from pydantic import BaseModel
from typing import List

class Document(BaseModel):
    documents: str
    questions: List[str]

class Answer(BaseModel):
    answers: List[str]
