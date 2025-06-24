from pydantic import BaseModel
from typing import List

# Chat and Speech-related schemas
class ChatMessage(BaseModel):
    content: str

class ChatResponse(BaseModel):
    response: str