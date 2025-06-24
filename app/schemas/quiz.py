from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    question_text: str
    options: List[str]
    correct_answer: str

class Quiz(BaseModel):
    title: str
    questions: List[Question]

class QuizTextInput(BaseModel):
    text: str

