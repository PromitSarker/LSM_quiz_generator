import os
import logging
import httpx
from dotenv import load_dotenv
from app.core.config import settings  # this is now the instance
from typing import List, Dict
from collections import defaultdict

load_dotenv()

logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self):
        self.api_key = settings.GROQ_API_KEY
        self.base_url = settings.GROQ_API_URL
        self.model = settings.LLM_MODEL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.conversations = defaultdict(list)
        self.max_history = 50

    async def get_chat_response(self, user_message: str, user_id: str = "default") -> str:
        try:
            # Get conversation history for this user
            conversation = self.conversations[user_id]

            # System prompt: instruct the LLM to always reply in the same language as the user message
            system_prompt = (
                "You are a helpful assistant. Always reply in the same language as the user's message." \
                " Be helpful. You are an expert in various subjects, Specially in OSHA related fields but not limited to " \
                "If the user change the language mid conversation, do change the language as well."\
                "safety, health, and compliance. Provide accurate and concise answers. " \
                "Be precise, do not over explain. " 
            )

            messages = [
                {"role": "system", "content": system_prompt}
            ]
            messages.extend(conversation)
            current_message = {
                "role": "user",
                "content": user_message
            }
            messages.append(current_message)

            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": 0.4,
                "max_tokens": 300,
                "top_p": 1
            }

            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    self.base_url,
                    headers=self.headers,
                    json=payload
                )

            if response.status_code != 200:
                logger.error(f"Groq API error: {response.text}")
                return f"Sorry, I encountered an error: {response.text}"

            data = response.json()
            assistant_message = data["choices"][0]["message"]["content"]

            # Store the conversation
            self.conversations[user_id].append(current_message)
            self.conversations[user_id].append({
                "role": "assistant",
                "content": assistant_message
            })

            # Keep only the last N messages
            if len(self.conversations[user_id]) > self.max_history:
                self.conversations[user_id] = self.conversations[user_id][-self.max_history:]

            return assistant_message

        except Exception as e:
            logger.error(f"ChatService error: {str(e)}")
            return f"Sorry, I encountered an error: {str(e)}"

    def clear_history(self, user_id: str = "default") -> None:
        """Clear conversation history for a specific user"""
        if user_id in self.conversations:
            self.conversations[user_id].clear()
            logger.info(f"Cleared conversation history for user {user_id}")

    def get_history(self, user_id: str = "default") -> List[Dict[str, str]]:
        """Get conversation history for a specific user"""
        return self.conversations.get(user_id, [])