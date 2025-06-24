from fastapi import APIRouter, HTTPException, Body
from app.services.quiz_generator import generate_quiz_from_text
from app.schemas.quiz import Quiz
from app.schemas.chat import (
    ChatMessage, 
    ChatResponse, 
)
from app.services.chat_service import ChatService


router = APIRouter()
chat_service = ChatService()  # <-- instantiate the service

@router.post("/chat/", response_model=ChatResponse)
async def chat_with_ai(
    message: ChatMessage,
):
    """Chat endpoint with conversation memory """
    response_text = await chat_service.get_chat_response(  # <-- use the instance
        message.content,
    )
    
    return ChatResponse(response=response_text)

@router.post("/generate-quiz/", response_model=Quiz)
async def generate_quiz(text: str = Body(..., media_type="text/plain")):
    """
    Receives raw text and generates a quiz based on its content.
    """
    if not text or not text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    quiz = await generate_quiz_from_text(text)  # <-- add await here

    if not quiz:
        raise HTTPException(status_code=500, detail="Failed to generate quiz.")

    return quiz
